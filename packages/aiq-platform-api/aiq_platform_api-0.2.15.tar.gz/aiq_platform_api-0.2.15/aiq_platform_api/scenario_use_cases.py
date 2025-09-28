# Example use cases for Scenario endpoints
import os
import sys
from enum import Enum
from typing import Optional, Dict, Any

from aiq_platform_api.common_utils import (
    AttackIQRestClient,
    AttackIQLogger,
    ScenarioUtils,
)
from aiq_platform_api.env import ATTACKIQ_API_TOKEN, ATTACKIQ_PLATFORM_URL

logger = AttackIQLogger.get_logger(__name__)


def list_scenarios(
    client: AttackIQRestClient,
    limit: Optional[int] = 10,
    filter_params: Optional[Dict[str, Any]] = None,
) -> int:
    """Lists scenarios with optional filtering."""
    filter_params = filter_params or {}
    logger.info(f"Listing up to {limit} scenarios with params: {filter_params}")
    count = 0
    try:
        for scenario in ScenarioUtils.list_scenarios(client, params=filter_params, limit=limit):
            count += 1
            logger.info(f"Scenario {count}: ID={scenario.get('id')}, Name={scenario.get('name')}")
        logger.info(f"Total scenarios listed: {count}")
    except Exception as e:
        logger.error(f"Failed to list scenarios: {e}")
    return count


def save_scenario_copy(
    client: AttackIQRestClient,
    scenario_id: str,
    new_name: str,
    model_json: Optional[Dict[str, Any]] = None,
    fork_template: bool = True,
) -> Optional[Dict[str, Any]]:
    """Creates a copy of an existing scenario with potentially updated model data.

    Args:
        client: The API client to use
        scenario_id: ID of the scenario to copy
        new_name: Name for the new scenario
        model_json: Optional modified model JSON for the new scenario
        fork_template: Whether to create a new scenario template (True) or reuse the existing one (False)

    Returns:
        The newly created scenario data if successful, None otherwise
    """
    logger.info(f"Creating a copy of scenario {scenario_id} with name '{new_name}'")
    try:
        copy_data = {
            "name": new_name,
            "fork_template": fork_template,
        }
        if model_json:
            copy_data["model_json"] = model_json

        new_scenario = ScenarioUtils.save_copy(client, scenario_id, copy_data)
        if new_scenario:
            logger.info(f"Successfully created scenario copy with ID: {new_scenario.get('id')}")
            return new_scenario
        else:
            logger.error("Failed to create scenario copy")
    except Exception as e:
        logger.error(f"Error creating scenario copy: {e}")
    return None


def delete_scenario_use_case(client: AttackIQRestClient, scenario_id: str):
    """Deletes a specific scenario by its ID."""
    logger.info(f"--- Attempting to delete scenario: {scenario_id} ---")
    try:
        success = ScenarioUtils.delete_scenario(client, scenario_id)
        if success:
            logger.info(f"Successfully initiated deletion of scenario: {scenario_id}")
        else:
            logger.error(f"Failed to initiate deletion of scenario: {scenario_id}")
    except Exception as e:
        logger.error(f"Error deleting scenario {scenario_id}: {e}")


def test_list_scenarios(client: AttackIQRestClient, search_term: Optional[str] = None):
    """Test listing scenarios with optional search."""
    logger.info("--- Testing Scenario Listing ---")
    filter_params = {"search": search_term} if search_term else {}
    list_scenarios(client, limit=5, filter_params=filter_params)


def test_list_mimikatz_scenarios(client: AttackIQRestClient):
    """Test listing scenarios containing 'Mimikatz'."""
    logger.info("--- Testing Scenario Listing with Mimikatz filter ---")
    test_list_scenarios(client, "Mimikatz")


def test_copy_scenario(client: AttackIQRestClient, scenario_id: Optional[str] = None):
    """Test copying a scenario without deletion."""
    logger.info("--- Testing Scenario Copy ---")

    if not scenario_id:
        scenario_id = os.environ.get("ATTACKIQ_SCENARIO_ID", "5417db5e-569f-4660-86ae-9ea7b73452c5")

    scenario = ScenarioUtils.get_scenario(client, scenario_id)
    if not scenario:
        logger.error(f"Scenario {scenario_id} not found")
        return None

    old_name = scenario.get("name")
    old_model_json = scenario.get("model_json")
    if old_model_json:
        old_model_json["domain"] = "example.com"

    # Add timestamp to make name unique
    import time

    timestamp = int(time.time())
    new_scenario_name = f"aiq_platform_api created {old_name} - {timestamp}"
    new_scenario = save_scenario_copy(
        client,
        scenario_id=scenario_id,
        new_name=new_scenario_name,
        model_json=old_model_json,
    )

    if new_scenario:
        logger.info(f"New scenario created: {new_scenario.get('name')} ({new_scenario.get('id')})")
        return new_scenario.get("id")
    return None


def test_delete_scenario(client: AttackIQRestClient, scenario_id: str):
    """Test deleting a specific scenario."""
    logger.info("--- Testing Scenario Deletion ---")
    if not scenario_id:
        logger.warning("No scenario ID provided for deletion")
        return
    delete_scenario_use_case(client, scenario_id)


def test_copy_and_delete(client: AttackIQRestClient, scenario_id: Optional[str] = None):
    """Test the full workflow: copy a scenario and then delete the copy."""
    logger.info("--- Testing Scenario Copy and Delete Workflow ---")

    if not scenario_id:
        scenario_id = os.environ.get("ATTACKIQ_SCENARIO_ID", "5417db5e-569f-4660-86ae-9ea7b73452c5")

    new_scenario_id = test_copy_scenario(client, scenario_id)
    if new_scenario_id:
        logger.info(f"--- Proceeding to delete the created scenario: {new_scenario_id} ---")
        test_delete_scenario(client, new_scenario_id)
    else:
        logger.warning("Could not get ID of newly created scenario, skipping deletion.")


def test_all(client: AttackIQRestClient):
    """Run all scenario tests."""
    # Test listing without filter
    test_list_scenarios(client)

    # Test listing with filter
    test_list_mimikatz_scenarios(client)

    # Test copy and delete workflow
    scenario_id = os.environ.get("ATTACKIQ_SCENARIO_ID")
    if scenario_id:
        test_copy_and_delete(client, scenario_id)
    else:
        logger.warning("ATTACKIQ_SCENARIO_ID not set. Skipping copy/delete tests.")


def run_test(choice: "TestChoice", client: AttackIQRestClient, scenario_id: Optional[str] = None):
    """Run the selected test."""
    test_functions = {
        TestChoice.LIST_ALL: lambda: test_list_scenarios(client),
        TestChoice.LIST_MIMIKATZ: lambda: test_list_mimikatz_scenarios(client),
        TestChoice.COPY_SCENARIO: lambda: test_copy_scenario(client, scenario_id),
        TestChoice.DELETE_SCENARIO: lambda: (
            test_delete_scenario(client, scenario_id)
            if scenario_id
            else logger.error("Scenario ID required for delete test")
        ),
        TestChoice.COPY_AND_DELETE: lambda: test_copy_and_delete(client, scenario_id),
        TestChoice.ALL: lambda: test_all(client),
    }

    test_func = test_functions.get(choice)
    if test_func:
        test_func()
    else:
        logger.error(f"Unknown test choice: {choice}")


if __name__ == "__main__":
    if not ATTACKIQ_PLATFORM_URL or not ATTACKIQ_API_TOKEN:
        logger.error("Missing ATTACKIQ_PLATFORM_URL or ATTACKIQ_API_TOKEN")
        sys.exit(1)

    class TestChoice(Enum):
        LIST_ALL = "list_all"
        LIST_MIMIKATZ = "list_mimikatz"
        COPY_SCENARIO = "copy_scenario"
        DELETE_SCENARIO = "delete_scenario"
        COPY_AND_DELETE = "copy_and_delete"
        ALL = "all"

    client = AttackIQRestClient(ATTACKIQ_PLATFORM_URL, ATTACKIQ_API_TOKEN)
    scenario_id = os.environ.get("ATTACKIQ_SCENARIO_ID", "5417db5e-569f-4660-86ae-9ea7b73452c5")

    # Change this to test different functionalities
    choice = TestChoice.LIST_ALL
    # choice = TestChoice.LIST_MIMIKATZ
    # choice = TestChoice.COPY_SCENARIO
    # choice = TestChoice.DELETE_SCENARIO
    # choice = TestChoice.COPY_AND_DELETE
    # choice = TestChoice.ALL

    run_test(choice, client, scenario_id)
