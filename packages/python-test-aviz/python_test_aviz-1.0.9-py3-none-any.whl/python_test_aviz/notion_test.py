import json
import logging
import os

from python_notion_plus import NotionClient

logger = logging.getLogger(__name__)


def main() -> None:
    notion_client = NotionClient(database_id=os.getenv("NOTION_DATABASE_ID"))

    metadata = notion_client.get_metadata()
    logger.info(f'notion_schema: {metadata}')

    notion_title = notion_client.get_database_title()
    logger.info(f'notion_title: {notion_title}')

    notion_properties = notion_client.get_database_properties()
    logger.info(f'notion_properties: {notion_properties}')

    total_results = notion_client.get_total_results()
    logger.info(f'total_results: {total_results}')

    notion_content = notion_client.get_database_content()
    logger.info(f'notion_content: {notion_content}')
    for page in notion_content:
        properties = notion_client.format_notion_page(page)
        formatted_data = json.dumps(properties, indent=4)

        logger.info(f'notion_page_properties: {formatted_data}')


if __name__ == '__main__':
    from custom_python_logger import get_logger

    _ = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        # extra={'user': 'test_user'}
    )

    main()
