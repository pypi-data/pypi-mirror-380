# get_jira_issue.py

import logging

from custom_python_logger import get_logger
from python_jira_plus.jira_plus import JiraPlus

ISSUE_KEY = 'SCRUM-1'


def main() -> None:
    logger = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        extra={'user': 'test_user'}
    )

    jira_plus = JiraPlus()
    issue = jira_plus.get_issue_by_key(key=ISSUE_KEY)
    logger.debug(f'issue: {issue}')


if __name__ == '__main__':
    main()
