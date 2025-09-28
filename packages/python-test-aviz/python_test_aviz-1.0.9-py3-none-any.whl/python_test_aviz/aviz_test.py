import logging

from custom_python_logger import get_logger


class AvizTest:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.name = "Aviz"

    def print_name(self) -> None:
        self.logger.info(f"Test name: {self.name}")


def main() -> None:
    _ = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        extra={'user': 'test_user'}
    )

    a = AvizTest()
    a.print_name()


if __name__ == '__main__':
    main()
