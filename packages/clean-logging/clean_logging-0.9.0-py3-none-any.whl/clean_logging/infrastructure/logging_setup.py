import logging
import coloredlogs
import queue
import re
from typing import Any, Dict, List, Optional, Union
from clean_logging.core.interfaces.log_repository_interface import ILogRepository

log_queue = queue.Queue()


def remove_ansi_codes(text: str) -> str:
    ansi_escape = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


class QueueLogHandler(logging.Handler):
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
            # اینجا داخل پکیج صرفاً لاگ چاپ می‌کنیم تا از حلقهٔ بی‌نهایت جلوگیری شود
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
    :param config_dict: دیکشنری کانفیگ که شامل کلید "logging" است.
    :param log_repository: ریپازیتوری برای ذخیره لاگ‌ها.
    :param extra_filters: فیلترهایی که caller از بیرون می‌خواهد اضافه کند.
    :param extra_handlers: هندلرهایی که caller از بیرون می‌خواهد اضافه کند (مثلاً FileHandler).
    :param suppress_loggers_override: اگر پاس داده شود، اولویت روی آن است. می‌تواند
           لیست اسامی لاگرها (که سطحشان WARNING می‌شود) یا دیکشنری {name: level}.
    :param enable_coloredlogs_default: اگر کانفیگ چیزی نداشت، این مقدار پیش‌فرض استفاده می‌شود.
    :return: دیکشنری شامل هندلرهای ایجادشده (مثل queue_handler) برای استفادهٔ caller در صورت نیاز.
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

    # نصب coloredlogs با پیش‌فرض‌های پکیج (در صورت فعال بودن)
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
    # سطح هندلر را می‌توان از کانفیگ گرفت؛ اگر نبود از root_level استفاده کن
    handler_level_name = str(cfg.get("queue_handler_level", level_name)).upper()
    queue_handler.setLevel(getattr(logging, handler_level_name, root_level))
    logger.addHandler(queue_handler)

    # --- اضافه کردن هندلرهای اضافه از بیرون ---
    if extra_handlers:
        for h in extra_handlers:
            # جلوگیری از اضافه‌شدن دوبارهٔ همان هندلر
            if h is queue_handler:
                continue
            logger.addHandler(h)

    # --- سرکوب یا تنظیم سطح لاگرهای خاص ---
    # ابتدا از override ورودی تابع استفاده می‌کنیم (اگر پاس شده باشد)
    suppress_cfg = suppress_loggers_override if suppress_loggers_override is not None else cfg.get("suppress_loggers", {})

    # دو حالت ممکن: لیست یا دیکشنری
    if isinstance(suppress_cfg, dict):
        # مثال: {"urllib3": "WARNING", "socketio": "ERROR"}
        for name, lvl in suppress_cfg.items():
            lvl_name = str(lvl).upper()
            logging.getLogger(name).setLevel(getattr(logging, lvl_name, logging.WARNING))
    elif isinstance(suppress_cfg, list):
        # اگر لیست است، همه را به WARNING می‌بریم (رفتار قدیمی حفظ می‌شود)
        for name in suppress_cfg:
            logging.getLogger(name).setLevel(logging.WARNING)
    else:
        # اگر هیچ‌کدام وجود نداشت، می‌توان یک لیست پیش‌فرض تعریف کرد
        default_suppress = cfg.get("default_suppress_list", ["urllib3", "charset_normalizer", "asyncio"])
        for name in default_suppress:
            logging.getLogger(name).setLevel(logging.WARNING)

    # --- اضافه کردن فیلترهای اضافه از بیرون ---
    if extra_filters:
        for flt in extra_filters:
            logger.addFilter(flt)

    # اگر خواستید بر اساس کانفیگ فیلترهای داخلی هم اضافه کنید (اختیاری)
    for f in cfg.get("filters", []):
        if isinstance(f, dict) and f.get("type") == "static_file":
            # فقط اگر caller نخواست خودش فیلتر را اضافه کند
            # (فرض می‌کنیم اگر caller فیلتر داد، از آن استفاده می‌کند)
            class StaticFileFilter(logging.Filter):
                def filter(self, record):
                    if record.name == 'werkzeug' and ' /static/' in record.getMessage():
                        return False
                    return True
            logger.addFilter(StaticFileFilter())

    # --- شروع پردازش کیو در ریپازیتوری ---
    log_repository.start_queue_processor()

    # برگردوندن هندلرها برای دسترسی caller در صورت نیاز
    return {"queue_handler": queue_handler}
