import pytest

from codemie_test_harness.tests.enums.integrations import DataBaseDialect
from codemie_test_harness.tests.enums.tools import DataManagementTool, Toolkit
from codemie_test_harness.tests.utils.env_resolver import EnvironmentResolver

ELASTIC_TOOL_TASK = {
    "index": "_all",
    "query": '{"query": {"prefix": {"_index": "codemie"}}}',
}

sql_tools_test_data = [
    (
        Toolkit.DATA_MANAGEMENT,
        DataManagementTool.SQL,
        DataBaseDialect.MY_SQL,
        {"sql_query": "SHOW TABLES"},
        [{"Tables_in_my_database": "products"}, {"Tables_in_my_database": "users"}],
    ),
    (
        Toolkit.DATA_MANAGEMENT,
        DataManagementTool.SQL,
        DataBaseDialect.POSTGRES,
        {
            "sql_query": "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        },
        [{"table_name": "users"}, {"table_name": "products"}],
    ),
    pytest.param(
        Toolkit.DATA_MANAGEMENT,
        DataManagementTool.SQL,
        DataBaseDialect.MS_SQL,
        {
            "sql_query": """SELECT table_name
                            FROM
                            information_schema.tables
                            WHERE
                            table_type = 'BASE TABLE'
                            AND
                            table_catalog = 'autotests'
                            AND
                            table_schema = 'dbo';
                            """
        },
        [{"table_name": "Users"}, {"table_name": "Products"}],
        marks=pytest.mark.skipif(
            not EnvironmentResolver.is_sandbox(),
            reason="MS SQL is only available in staging environments",
        ),
        id=DataBaseDialect.MS_SQL,
    ),
]
