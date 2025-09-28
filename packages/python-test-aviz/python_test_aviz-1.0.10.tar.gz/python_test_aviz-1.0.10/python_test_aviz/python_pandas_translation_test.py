import logging

import pandas as pd
from python_pandas_translation import pandas_row

logger = logging.getLogger(__name__)


def main() -> None:
    sample_df = pd.DataFrame(
        {
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [30, 25, 35]
        }
    )

    logger.info(pandas_row.get_rows(sample_df, start=0, end=1))


if __name__ == '__main__':
    from custom_python_logger import get_logger

    _ = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        # extra={'user': 'test_user'}
    )

    main()
