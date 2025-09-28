import logging
import os
from typing import Optional
import colorlog
from hd_logging.SizeAndTimeLoggingHandler import SizeAndTimeLoggingHandler as STLH
import time

def setup_logger(
    logger_name: str,
    log_file_path: Optional[str] = None,
    log_level_console: Optional[int] = None,
    log_level_files: Optional[int] = None,
    use_otlp_format: bool = None,
    service_name: Optional[str] = None,
    environment: Optional[str] = None,
    service_version: Optional[str] = None
) -> logging.Logger:
    """
    Set up a standardized logger with colorized console output and size+time rotating file handler.
    - Prevents duplicate handlers.
    - Uses ISO 8601 timestamps.
    - Log levels and file path can be set via environment variables or function arguments.

    Args:
        logger_name (str): Name of the logger (use 'api_service' for main app).
        log_file_path (str, optional): Path to the log file. Defaults to 'hd_shared.log' if not specified.
        log_level_console (int, optional): Console log level. Defaults to LOG_LEVEL env or logging.INFO.
        log_level_files (int, optional): File log level. Defaults to LOG_LEVEL env or logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Environment/config defaults
    log_file_path = log_file_path or os.getenv("LOG_FILE", "logs/hd_logging.log")
    env_log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level_console = log_level_console or getattr(logging, env_log_level)
    log_level_files = log_level_files or getattr(logging, env_log_level)
    
    # OpenTelemetry format configuration
    if use_otlp_format is None:
        use_otlp_format = os.getenv("LOG_FILE_OTLP_FORMAT", "true").lower() == "true"
    
    service_name = service_name or os.getenv("SERVICE_NAME", "hd_logging")
    environment = environment or os.getenv("ENVIRONMENT", "development")
    service_version = service_version or os.getenv("SERVICE_VERSION", "1.0.0")

    logger = logging.getLogger(logger_name)
    logger.setLevel(min(log_level_console, log_level_files))  # Set to lowest for capturing all

    # Prevent duplicate handlers
    if getattr(logger, "_custom_handlers_set", False):
        return logger

    iso_time_format = "%Y-%m-%dT%H:%M:%S%z"
    # Set the converter for all Formatters to use UTC
    logging.Formatter.converter = time.gmtime
    # File formatter
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s - [Component: %(module)s, Function: %(funcName)s, Line: %(lineno)d]',
        datefmt=iso_time_format
    )

    # Colorized console formatter
    console_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s - [Component: %(module)s, Function: %(funcName)s, Line: %(lineno)d]",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        datefmt=iso_time_format
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level_console)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Ensure log directory exists if log_file_path is set
    if log_file_path:
        log_dir = os.path.dirname(log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
    # Size and time rotating file handler
    stime_handler = STLH(
        filename=log_file_path,
        when="midnight",
        interval=1,
        backupCount=7,
        maxBytes=20_000_000,
        use_otlp_format=use_otlp_format,
        service_name=service_name,
        environment=environment,
        service_version=service_version
    )
    stime_handler.setLevel(log_level_files)
    
    # Set formatter based on OTLP format preference
    if use_otlp_format:
        # OTLP formatter is already set in the handler
        pass
    else:
        stime_handler.setFormatter(file_formatter)
    
    logger.addHandler(stime_handler)

    # Mark as configured to prevent duplicate handlers
    logger._custom_handlers_set = True

    return logger 
