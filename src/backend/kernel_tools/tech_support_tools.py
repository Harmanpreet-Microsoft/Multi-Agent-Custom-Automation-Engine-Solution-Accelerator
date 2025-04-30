import inspect
from typing import Annotated, Callable, Dict

from semantic_kernel.functions import kernel_function

formatting_instructions = "Instructions: returning the output of this function call verbatim to the user in markdown. Then write AGENT SUMMARY: and then include a summary of what you did."


class TechSupportTools:
    # Define Tech Support tools (functions)
    @staticmethod
    @kernel_function(
        description="Send a welcome email to a new employee as part of onboarding."
    )
    async def send_welcome_email(employee_name: str, email_address: str) -> str:
        return (
            f"##### Welcome Email Sent\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Email Address:** {email_address}\n\n"
            f"A welcome email has been successfully sent to {employee_name} at {email_address}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Set up an Office 365 account for an employee.")
    async def set_up_office_365_account(employee_name: str, email_address: str) -> str:
        return (
            f"##### Office 365 Account Setup\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Email Address:** {email_address}\n\n"
            f"An Office 365 account has been successfully set up for {employee_name} at {email_address}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Configure a laptop for a new employee.")
    async def configure_laptop(employee_name: str, laptop_model: str) -> str:
        return (
            f"##### Laptop Configuration\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Laptop Model:** {laptop_model}\n\n"
            f"The laptop {laptop_model} has been successfully configured for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Reset the password for an employee.")
    async def reset_password(employee_name: str) -> str:
        return (
            f"##### Password Reset\n"
            f"**Employee Name:** {employee_name}\n\n"
            f"The password for {employee_name} has been successfully reset.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Set up VPN access for an employee.")
    async def setup_vpn_access(employee_name: str) -> str:
        return (
            f"##### VPN Access Setup\n"
            f"**Employee Name:** {employee_name}\n\n"
            f"VPN access has been successfully set up for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Assist in troubleshooting network issues reported.")
    async def troubleshoot_network_issue(issue_description: str) -> str:
        return (
            f"##### Network Issue Resolved\n"
            f"**Issue Description:** {issue_description}\n\n"
            f"The network issue described as '{issue_description}' has been successfully resolved.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Install software for an employee.")
    async def install_software(employee_name: str, software_name: str) -> str:
        return (
            f"##### Software Installation\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Software Name:** {software_name}\n\n"
            f"The software '{software_name}' has been successfully installed for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Update software for an employee.")
    async def update_software(employee_name: str, software_name: str) -> str:
        return (
            f"##### Software Update\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Software Name:** {software_name}\n\n"
            f"The software '{software_name}' has been successfully updated for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Manage data backup for an employee's device.")
    async def manage_data_backup(employee_name: str) -> str:
        return (
            f"##### Data Backup Managed\n"
            f"**Employee Name:** {employee_name}\n\n"
            f"Data backup has been successfully configured for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Handle a reported cybersecurity incident.")
    async def handle_cybersecurity_incident(incident_details: str) -> str:
        return (
            f"##### Cybersecurity Incident Handled\n"
            f"**Incident Details:** {incident_details}\n\n"
            f"The cybersecurity incident described as '{incident_details}' has been successfully handled.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(
        description="Assist procurement with technical specifications of equipment."
    )
    async def assist_procurement_with_tech_equipment(equipment_details: str) -> str:
        return (
            f"##### Technical Specifications Provided\n"
            f"**Equipment Details:** {equipment_details}\n\n"
            f"Technical specifications for the following equipment have been provided: {equipment_details}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Collaborate with CodeAgent for code deployment.")
    async def collaborate_with_code_deployment(project_name: str) -> str:
        return (
            f"##### Code Deployment Collaboration\n"
            f"**Project Name:** {project_name}\n\n"
            f"Collaboration on the deployment of project '{project_name}' has been successfully completed.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Provide technical support for a marketing campaign.")
    async def provide_tech_support_for_marketing(campaign_name: str) -> str:
        return (
            f"##### Tech Support for Marketing Campaign\n"
            f"**Campaign Name:** {campaign_name}\n\n"
            f"Technical support has been successfully provided for the marketing campaign '{campaign_name}'.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Provide tech support for a new product launch.")
    async def assist_product_launch(product_name: str) -> str:
        return (
            f"##### Tech Support for Product Launch\n"
            f"**Product Name:** {product_name}\n\n"
            f"Technical support has been successfully provided for the product launch of '{product_name}'.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Implement and manage an IT policy.")
    async def implement_it_policy(policy_name: str) -> str:
        return (
            f"##### IT Policy Implemented\n"
            f"**Policy Name:** {policy_name}\n\n"
            f"The IT policy '{policy_name}' has been successfully implemented.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Manage cloud services used by the company.")
    async def manage_cloud_service(service_name: str) -> str:
        return (
            f"##### Cloud Service Managed\n"
            f"**Service Name:** {service_name}\n\n"
            f"The cloud service '{service_name}' has been successfully managed.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Configure a server.")
    async def configure_server(server_name: str) -> str:
        return (
            f"##### Server Configuration\n"
            f"**Server Name:** {server_name}\n\n"
            f"The server '{server_name}' has been successfully configured.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Grant database access to an employee.")
    async def grant_database_access(employee_name: str, database_name: str) -> str:
        return (
            f"##### Database Access Granted\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Database Name:** {database_name}\n\n"
            f"Access to the database '{database_name}' has been successfully granted to {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Provide technical training on new tools.")
    async def provide_tech_training(employee_name: str, tool_name: str) -> str:
        return (
            f"##### Tech Training Provided\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Tool Name:** {tool_name}\n\n"
            f"Technical training on '{tool_name}' has been successfully provided to {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(
        description="Resolve general technical issues reported by employees."
    )
    async def resolve_technical_issue(issue_description: str) -> str:
        return (
            f"##### Technical Issue Resolved\n"
            f"**Issue Description:** {issue_description}\n\n"
            f"The technical issue described as '{issue_description}' has been successfully resolved.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Configure a printer for an employee.")
    async def configure_printer(employee_name: str, printer_model: str) -> str:
        return (
            f"##### Printer Configuration\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Printer Model:** {printer_model}\n\n"
            f"The printer '{printer_model}' has been successfully configured for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Set up an email signature for an employee.")
    async def set_up_email_signature(employee_name: str, signature: str) -> str:
        return (
            f"##### Email Signature Setup\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Signature:** {signature}\n\n"
            f"The email signature for {employee_name} has been successfully set up as '{signature}'.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Configure a mobile device for an employee.")
    async def configure_mobile_device(employee_name: str, device_model: str) -> str:
        return (
            f"##### Mobile Device Configuration\n"
            f"**Employee Name:** {employee_name}\n"
            f"**Device Model:** {device_model}\n\n"
            f"The mobile device '{device_model}' has been successfully configured for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Manage software licenses for a specific software.")
    async def manage_software_licenses(software_name: str, license_count: int) -> str:
        return (
            f"##### Software Licenses Managed\n"
            f"**Software Name:** {software_name}\n"
            f"**License Count:** {license_count}\n\n"
            f"{license_count} licenses for the software '{software_name}' have been successfully managed.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Set up remote desktop access for an employee.")
    async def set_up_remote_desktop(employee_name: str) -> str:
        return (
            f"##### Remote Desktop Setup\n"
            f"**Employee Name:** {employee_name}\n\n"
            f"Remote desktop access has been successfully set up for {employee_name}.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Assist in troubleshooting hardware issues reported.")
    async def troubleshoot_hardware_issue(issue_description: str) -> str:
        return (
            f"##### Hardware Issue Resolved\n"
            f"**Issue Description:** {issue_description}\n\n"
            f"The hardware issue described as '{issue_description}' has been successfully resolved.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    @kernel_function(description="Manage network security protocols.")
    async def manage_network_security() -> str:
        return (
            f"##### Network Security Managed\n\n"
            f"Network security protocols have been successfully managed.\n"
            f"{formatting_instructions}"
        )

    @staticmethod
    def get_all_kernel_functions() -> Dict[str, Callable]:
        """
        Returns a dictionary of all methods in this class that have the @kernel_function annotation.
        This function itself is not annotated with @kernel_function.

        Returns:
            Dict[str, Callable]: Dictionary with function names as keys and function objects as values
        """
        kernel_functions = {}

        # Get all class methods
        for name, method in inspect.getmembers(
            TechSupportTools, predicate=inspect.isfunction
        ):
            # Skip this method itself and any private/special methods
            if name.startswith("_") or name == "get_all_kernel_functions":
                continue

            # Check if the method has the kernel_function annotation
            # by looking at its __annotations__ attribute
            method_attrs = getattr(method, "__annotations__", {})
            if hasattr(method, "__kernel_function__") or "kernel_function" in str(
                method_attrs
            ):
                kernel_functions[name] = method

        return kernel_functions
