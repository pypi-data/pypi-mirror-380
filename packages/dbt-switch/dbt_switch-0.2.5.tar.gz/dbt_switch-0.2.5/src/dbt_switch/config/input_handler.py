"""
Input handler for the dbt_switch.yml file. This includes all operations that
take input from the user which leads to some action on the dbt_switch.yml file.
"""

from dbt_switch.utils.logger import logger
from dbt_switch.config.file_handler import (
    add_config,
    update_project_host,
    update_project_id,
    delete_project_config,
    list_all_projects,
)
from dbt_switch.config.cloud_handler import switch_project


def add_user_config_input(command: str, project_name: str | None = None, host: str | None = None, project_id: int | None = None):
    """
    Add a new project host and project_id to the dbt_switch.yml file.
    Supports both interactive and non-interactive modes.
    
    Args:
        command: The command to add a new project host and project_id
        project_name: Project name (optional, for non-interactive mode)
        host: Project host URL (optional, for non-interactive mode)
        project_id: Project ID (optional, for non-interactive mode)
    """
    if command != "add":
        raise ValueError(f"Invalid command: {command}")

    # Non-interactive mode
    if project_name and host and project_id:
        if not project_name.strip():
            logger.error("Project name cannot be empty")
            return
        if not host.strip():
            logger.error("Project host cannot be empty")
            return
        
        try:
            add_config(project_name.strip(), host.strip(), project_id)
        except ValueError as e:
            logger.error(f"Invalid configuration: {e}")
        return
    
    # Partial arguments
    if project_name or host or project_id:
        logger.error("When using command-line arguments, all three are required: project_name, --host, and --project-id")
        logger.error("Use 'dbt-switch add --help' for more information.")
        logger.error("For interactive mode, run 'dbt-switch add' without any arguments.")
        return

    # Interactive mode
    project_name_input = input("Enter the project name: ").strip()
    if not project_name_input:
        logger.error("Project name cannot be empty")
        return

    project_host_input = input("Enter the project host: ").strip()
    project_id_input = input("Enter the project id: ").strip()

    try:
        project_id_int = int(project_id_input)
        add_config(project_name_input, project_host_input, project_id_int)

    except ValueError as e:
        if "invalid literal for int()" in str(e):
            logger.error(f"Invalid project ID '{project_id_input}': must be a number")
        else:
            raise


def update_user_config_input(arg: str):
    """
    Update a project host or project_id in the dbt_switch.yml file.
    Args:
        arg: The argument to update a project host or project_id
    """
    if arg not in ["host", "project_id"]:
        raise ValueError(f"Invalid argument: {arg}")

    project_name = input("Enter the project name: ").strip()
    if not project_name:
        logger.error("Project name cannot be empty")
        return

    if arg == "host":
        project_host = input("Enter the project host: ").strip()
        if not project_host:
            logger.error("Project host cannot be empty")
            return

        update_project_host(project_name, project_host)

    elif arg == "project_id":
        project_id_input = input("Enter the project id: ").strip()

        try:
            project_id = int(project_id_input)
            update_project_id(project_name, project_id)

        except ValueError as e:
            if "invalid literal for int()" in str(e):
                logger.error(
                    f"Invalid project ID '{project_id_input}': must be a number"
                )
            else:
                raise


def delete_user_config_input(command: str):
    """
    Delete a project entry from the dbt_switch.yml file.
    Args:
        command: The command to delete a project entry
    """
    if command != "delete":
        raise ValueError(f"Invalid command: {command}")

    project_name = input("Enter the project name: ").strip()
    if not project_name:
        logger.error("Project name cannot be empty")
        return

    delete_project_config(project_name)


def switch_user_config_input(project_name: str):
    """
    Switch to a project by updating dbt_cloud.yml with values from dbt_switch.yml.
    Args:
        project_name: The name of the project to switch to
    """
    if not project_name:
        logger.error("Project name cannot be empty")
        return

    try:
        switch_project(project_name)
    except Exception as e:
        logger.error(f"Failed to switch to project '{project_name}': {e}")
        raise


def list_projects():
    """
    Wrapper function to list all projects. This is done to fit the
    module architecture and to keep the import in file_handler.py consistent.
    """
    list_all_projects()
