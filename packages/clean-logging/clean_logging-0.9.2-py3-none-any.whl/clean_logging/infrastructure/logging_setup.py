import logging
import coloredlogs
import queue
import re
from typing import Any, Dict, List, Optional, Union
from clean_logging.core.interfaces.log_repository_interface import ILogRepository

log_queue = queue.Queue()


def remove_ansi_codes(text: str) -> str:
    """حذف کدهای ANSI (رنگ‌ها) از متن برای ذخیره‌سازی تمیز."""
    ansi_escape = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

class DynamicPatternFilter(logging.Filter):
    """
    فیلتری که پیام‌های حاوی هر یک از الگوهای داده‌شده را سرکوب می‌کند.
    """
    def __init__(self, patterns_to_suppress: List[str], logger_name: Optional[str] = None):
        super().__init__()
        self.patterns = patterns_to_suppress or []
        self.logger_name = logger_name  # فقط برای دیباگ/شناسایی

    def filter(self, record):
        message = record.getMessage()
        for pattern in self.patterns:
            if pattern in message:
                return False
        return True
    

class QueueLogHandler(logging.Handler):
    """هندلر سفارشی برای ارسال لاگ‌ها به یک صف و ذخیره در ریپازیتوری."""
    
    def __init__(self, log_repository: ILogRepository):
        super().__init__()
        self.log_repository = log_repository

    def emit(self, record):
        try:
            message = record.getMessage()
            clean_message = remove_ansi_codes(message)
            self.log_repository.log_queue.put({
                'level': record.levelname,
                'message': clean_message,
                'function_name': record.funcName,
                'filename': record.pathname,
                'lineno': record.lineno
            })
        except Exception as e:
            # چاپ خطا به stderr برای جلوگیری از حلقهٔ بی‌نهایت
            print(f"[QueueLogHandler] خطا در افزودن به کیو: {str(e)}")


def logging_setup(
    config_dict: Dict[str, Any],
    log_repository: ILogRepository,
    extra_filters: Optional[List[logging.Filter]] = None,
    extra_handlers: Optional[List[logging.Handler]] = None,
    suppress_loggers_override: Optional[Union[List[str], Dict[str, str]]] = None,
    enable_coloredlogs_default: bool = True,
) -> Dict[str, logging.Handler]:
    """
    تنظیم سیستم لاگینگ مرکزی با پشتیبانی از فیلتر، سرکوب لاگرها، و ذخیره‌سازی در ریپازیتوری.
    
    :param config_dict: دیکشنری کانفیگ لاگینگ (مستقیماً شامل level, suppress_loggers و ...)
    :param log_repository: ریپازیتوری برای ذخیره لاگ‌ها.
    :param extra_filters: فیلترهای سفارشی از caller.
    :param extra_handlers: هندلرهای اضافه (مثل FileHandler).
    :param suppress_loggers_override: لیست یا دیکشنری برای سرکوب لاگرهای خاص.
    :param enable_coloredlogs_default: فعال‌سازی coloredlogs در صورت عدم مشخص‌بودن در کانفیگ.
    :return: دیکشنری هندلرهای ایجادشده.
    """

    if log_repository is None:
        raise ValueError("Log repository must be provided for logging setup.")
    
    if config_dict is None:
        raise ValueError("config_dict can not be empty")

    cfg = config_dict 

    # سطح لاگ کلی
    level_name = str(cfg.get("level", "DEBUG")).upper()
    root_level = getattr(logging, level_name, logging.DEBUG)

    logger = logging.getLogger()
    logger.setLevel(root_level)

    # نصب coloredlogs (در صورت فعال بودن)
    if cfg.get("enable_coloredlogs", enable_coloredlogs_default):
        coloredlogs.install(
            level=level_name,
            logger=logger,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level_styles={
                'debug': {'color': 'green'},
                'info': {'color': 'blue'},
                'warning': {'color': 'yellow'},
                'error': {'color': 'red'},
                'critical': {'color': 'red', 'bold': True},
            },
            field_styles={
                'asctime': {'color': 'cyan'},
                'name': {'color': 'white'},
                'levelname': {'color': 'white', 'bold': True},
                'funcName': {'color': 'magenta'},
            }
        )

    # --- هندلر اصلی کیو (همیشه اضافه می‌شود) ---
    queue_handler = QueueLogHandler(log_repository)
    handler_level_name = str(cfg.get("queue_handler_level", level_name)).upper()
    queue_handler.setLevel(getattr(logging, handler_level_name, root_level))
    logger.addHandler(queue_handler)

    # --- اتصال خودکار به لاگرهای رایج (مثل werkzeug, socketio) ---
    # این کار باعث می‌شود لاگ‌های این ماژول‌ها هم وارد سیستم صف ما شوند
    common_loggers = ["werkzeug", "socketio", "engineio", "flask"]
    for logger_name in common_loggers:
        specific_logger = logging.getLogger(logger_name)
        # جلوگیری از اضافه‌شدن چندباره همان هندلر
        if not any(isinstance(h, QueueLogHandler) for h in specific_logger.handlers):
            specific_logger.addHandler(queue_handler)
            specific_logger.setLevel(root_level)
            specific_logger.propagate = True  # جلوگیری از چاپ در stderr

    # --- اضافه کردن هندلرهای اضافه از بیرون ---
    if extra_handlers:
        for h in extra_handlers:
            if h is queue_handler:
                continue
            logger.addHandler(h)

    # --- سرکوب یا تنظیم سطح لاگرهای خاص ---
    suppress_cfg = suppress_loggers_override if suppress_loggers_override is not None else cfg.get("suppress_loggers", {})

    if isinstance(suppress_cfg, dict):
        for name, lvl in suppress_cfg.items():
            lvl_name = str(lvl).upper()
            logging.getLogger(name).setLevel(getattr(logging, lvl_name, logging.WARNING))
    elif isinstance(suppress_cfg, list):
        for name in suppress_cfg:
            logging.getLogger(name).setLevel(logging.WARNING)
    else:
        default_suppress = cfg.get("default_suppress_list", ["urllib3", "charset_normalizer", "asyncio"])
        for name in default_suppress:
            logging.getLogger(name).setLevel(logging.WARNING)

    # --- اضافه کردن فیلترهای اضافه از بیرون ---
    if extra_filters:
        for flt in extra_filters:
            logger.addFilter(flt)

        # --- فیلترهای پویا بر اساس config_dict['filters'] ---
    filters_config = cfg.get("filters", {})
    if isinstance(filters_config, dict):
        for logger_name, patterns in filters_config.items():
            if not isinstance(patterns, list):
                continue  # اطمینان از اینکه لیست است
            if not patterns:
                continue  # اگر لیست خالی بود، نیازی به فیلتر نیست

            # ساخت فیلتر پویا
            dynamic_filter = DynamicPatternFilter(patterns_to_suppress=patterns, logger_name=logger_name)

            # دریافت لاگر هدف
            target_logger = logging.getLogger(logger_name)

            # جلوگیری از افزودن فیلتر تکراری (اختیاری ولی پیشنهادی)
            if not any(isinstance(f, DynamicPatternFilter) and getattr(f, 'logger_name', None) == logger_name 
                       for f in target_logger.filters):
                target_logger.addFilter(dynamic_filter)
    elif filters_config:  # اگر نوع دیگری بود (مثلاً لیست)، هشدار بده یا نادیده بگیر
        print("[WARNING] filters config must be a dict of {logger_name: [patterns]}")

    # --- شروع پردازش کیو در ریپازیتوری ---
    log_repository.start_queue_processor()

    return {"queue_handler": queue_handler}