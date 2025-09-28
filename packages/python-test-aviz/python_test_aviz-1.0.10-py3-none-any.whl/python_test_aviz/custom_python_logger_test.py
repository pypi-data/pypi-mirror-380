import logging

from custom_python_logger import CustomLoggerAdapter

logger: CustomLoggerAdapter = CustomLoggerAdapter(logging.getLogger(__name__))


class LoggerTest:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

    def main(self) -> None:
        self.logger.info('Hello World')
        self.logger.debug('Hello World')


def main() -> None:
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.step("This is a step message.")
    logger.warning("This is a warning message.")

    try:
        _ = 1 / 0
    except ZeroDivisionError:
        logger.exception("This is an exception message.")

    logger.critical("This is a critical message.")

    logger_test = LoggerTest()
    logger_test.main()


if __name__ == '__main__':
    from custom_python_logger import get_logger

    _ = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        # extra={'user': 'test_user'}
    )

    main()
