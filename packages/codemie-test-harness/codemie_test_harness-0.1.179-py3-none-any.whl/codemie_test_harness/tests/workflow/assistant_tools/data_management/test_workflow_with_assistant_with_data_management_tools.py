import pytest
from codemie_sdk.models.integration import CredentialTypes

from codemie_test_harness.tests.enums.tools import DataManagementTool, Toolkit
from codemie_test_harness.tests.test_data.data_management_tools_test_data import (
    ELASTIC_TOOL_TASK,
    RESPONSE_FOR_ELASTIC,
    sql_tools_test_data,
    SQL_TOOL_CREATE_TABLE_TASK,
    SQL_TOOL_DELETE_TABLE_TASK,
    SQL_TOOL_INSERT_TABLE_TASK,
    SQL_TOOL_QUERY_TABLE_TASK,
    RESPONSE_FOR_SQL,
)
from codemie_test_harness.tests.utils.credentials_manager import CredentialsManager
from codemie_test_harness.tests.utils.env_resolver import EnvironmentResolver

pytestmark = pytest.mark.skipif(
    EnvironmentResolver.is_localhost(),
    reason="Skipping this tests on local environment",
)


@pytest.mark.workflow
@pytest.mark.workflow_with_assistant
@pytest.mark.elastic
@pytest.mark.regression
def test_workflow_with_assistant_with_elastic_tools(
    assistant,
    workflow_with_assistant,
    workflow_utils,
    integration_utils,
    similarity_check,
):
    """Test workflow execution with Elastic tools."""
    credential_values = CredentialsManager.elasticsearch_credentials()
    settings = integration_utils.create_integration(
        CredentialTypes.ELASTIC, credential_values
    )
    assistant = assistant(
        Toolkit.DATA_MANAGEMENT, DataManagementTool.ELASTIC, settings=settings
    )

    workflow_with_assistant = workflow_with_assistant(assistant, ELASTIC_TOOL_TASK)
    response = workflow_utils.execute_workflow(
        workflow_with_assistant.id, assistant.name
    )
    similarity_check.check_similarity(response, RESPONSE_FOR_ELASTIC)


@pytest.mark.workflow
@pytest.mark.workflow_with_assistant
@pytest.mark.sql
@pytest.mark.regression
@pytest.mark.parametrize(
    "db_dialect",
    sql_tools_test_data,
)
def test_workflow_with_assistant_with_sql_tools(
    assistant,
    workflow_with_assistant,
    workflow_utils,
    integration_utils,
    similarity_check,
    db_dialect,
):
    """Test workflow execution with SQL data management tools (various dialects)."""
    credential_values = CredentialsManager.sql_credentials(db_dialect)
    settings = integration_utils.create_integration(
        CredentialTypes.SQL, credential_values
    )

    assistant = assistant(
        Toolkit.DATA_MANAGEMENT, DataManagementTool.SQL, settings=settings
    )
    workflow_with_assistant = workflow_with_assistant(assistant, "Run")

    workflow_utils.execute_workflow(
        workflow_with_assistant.id, assistant.name, SQL_TOOL_CREATE_TABLE_TASK
    )
    workflow_utils.execute_workflow(
        workflow_with_assistant.id, assistant.name, SQL_TOOL_INSERT_TABLE_TASK
    )
    response = workflow_utils.execute_workflow(
        workflow_with_assistant.id, assistant.name, SQL_TOOL_QUERY_TABLE_TASK
    )
    workflow_utils.execute_workflow(
        workflow_with_assistant.id, assistant.name, SQL_TOOL_DELETE_TABLE_TASK
    )

    similarity_check.check_similarity(response, RESPONSE_FOR_SQL)
