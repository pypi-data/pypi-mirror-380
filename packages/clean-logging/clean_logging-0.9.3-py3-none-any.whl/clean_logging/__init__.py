
def logging_setup(*args, **kwargs):
    from clean_logging.infrastructure.logging_setup import logging_setup
    return logging_setup(*args, **kwargs)

__all__ = ["logging_setup", "ILogRepository"]
#....test2