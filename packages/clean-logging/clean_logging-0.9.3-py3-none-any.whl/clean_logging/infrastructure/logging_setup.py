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
    """فیلتر داینامیک برای حذف پیام‌های حاوی الگوهای مشخص."""

    def __init__(self, patterns_to_suppress: List[str], logger_name: Optional[str] = None):
        super().__init__()
        self.patterns = patterns_to_suppress or []
        self.logger_name = logger_name

    def filter(self, record):
        message = record.getMessage()
        return not any(pattern in message for pattern in self.patterns)


class QueueLogHandler(logging.Handler):
    """هندلر سفارشی برای ارسال لاگ‌ها به صف و ذخیره در ریپازیتوری."""

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
    تنظیم سیستم لاگینگ مرکزی با coloredlogs، فیلترها، و ذخیره در ریپازیتوری.
    """

    if log_repository is None:
        raise ValueError("Log repository must be provided for logging setup.")

    if config_dict is None:
        raise ValueError("config_dict cannot be empty")

    cfg = config_dict
    level_name = str(cfg.get("level", "DEBUG")).upper()
    root_level = getattr(logging, level_name, logging.DEBUG)

    root_logger = logging.getLogger()
    root_logger.setLevel(root_level)

    # نصب coloredlogs برای root logger
    if cfg.get("enable_coloredlogs", enable_coloredlogs_default):
        coloredlogs.install(
            level=level_name,
            logger=root_logger,
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

    # --- ایجاد QueueLogHandler (برای ذخیره در فایل) ---
    queue_handler = QueueLogHandler(log_repository)
    handler_level_name = str(cfg.get("queue_handler_level", level_name)).upper()
    queue_handler.setLevel(getattr(logging, handler_level_name, root_level))
    root_logger.addHandler(queue_handler)

    # --- فیلترهای اضافه روی root ---
    if extra_filters:
        for flt in extra_filters:
            root_logger.addFilter(flt)

    # --- فیلترهای داینامیک بر اساس config ---
    filters_config = cfg.get("filters", {})
    dynamic_filters: Dict[str, DynamicPatternFilter] = {}
    if isinstance(filters_config, dict):
        for logger_name, patterns in filters_config.items():
            if isinstance(patterns, list) and patterns:
                dynamic_filters[logger_name] = DynamicPatternFilter(patterns, logger_name)

    # --- لاگرهای رایج (werkzeug, flask, socketio...) ---
    common_loggers = ["werkzeug", "socketio", "engineio", "flask"]
    for logger_name in common_loggers:
        specific_logger = logging.getLogger(logger_name)
        specific_logger.propagate = False  # جلوگیری از دوبل شدن
        specific_logger.setLevel(root_level)

        # اضافه کردن QueueLogHandler برای ثبت در فایل
        if not any(isinstance(h, QueueLogHandler) for h in specific_logger.handlers):
            specific_logger.addHandler(queue_handler)

        # اضافه کردن ConsoleHandler برای چاپ در ترمینال
        if not any(isinstance(h, logging.StreamHandler) for h in specific_logger.handlers):
            console_handler = logging.StreamHandler()
            console_handler.setLevel(root_level)
            console_handler.setFormatter(logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s",
                "%Y-%m-%d %H:%M:%S"
            ))
            specific_logger.addHandler(console_handler)

        # افزودن فیلترهای خاص این لاگر به خودش و تمام هندلرهایش
        if logger_name in dynamic_filters:
            flt = dynamic_filters[logger_name]
            if not any(isinstance(f, DynamicPatternFilter) and f.logger_name == logger_name for f in specific_logger.filters):
                specific_logger.addFilter(flt)
            for h in specific_logger.handlers:
                if not any(isinstance(f, DynamicPatternFilter) and f.logger_name == logger_name for f in h.filters):
                    h.addFilter(flt)

    # --- suppress loggers ---
    suppress_cfg = suppress_loggers_override if suppress_loggers_override is not None else cfg.get("suppress_loggers", {})
    if isinstance(suppress_cfg, dict):
        for name, lvl in suppress_cfg.items():
            logging.getLogger(name).setLevel(getattr(logging, str(lvl).upper(), logging.WARNING))
    elif isinstance(suppress_cfg, list):
        for name in suppress_cfg:
            logging.getLogger(name).setLevel(logging.WARNING)

    # --- هندلرهای اضافه ---
    if extra_handlers:
        for h in extra_handlers:
            if h is queue_handler:
                continue
            root_logger.addHandler(h)

    # --- شروع پردازش کیو ---
    log_repository.start_queue_processor()

    return {"queue_handler": queue_handler}
