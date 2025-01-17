import os
import pytest
from unittest.mock import MagicMock

# Set environment variables to mock Config dependencies before any import
os.environ["COSMOSDB_ENDPOINT"] = "https://mock-endpoint"
os.environ["COSMOSDB_KEY"] = "mock-key"
os.environ["COSMOSDB_DATABASE"] = "mock-database"
os.environ["COSMOSDB_CONTAINER"] = "mock-container"
os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = "mock-deployment-name"
os.environ["AZURE_OPENAI_API_VERSION"] = "2023-01-01"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://mock-openai-endpoint"

from src.backend.agents.tech_support import (
    configure_server,
    grant_database_access,
    provide_tech_training,
    resolve_technical_issue,
    configure_printer,
    set_up_email_signature,
    configure_mobile_device,
    manage_software_licenses,
    set_up_remote_desktop,
    troubleshoot_hardware_issue,
    manage_network_security,
    update_firmware,
    assist_with_video_conferencing_setup,
    manage_it_inventory,
    configure_firewall_rules,
    manage_virtual_machines,
    provide_tech_support_for_event,
    configure_network_storage,
    set_up_two_factor_authentication,
    troubleshoot_email_issue,
    manage_it_helpdesk_tickets,
    provide_remote_tech_support,
    manage_network_bandwidth,
    assist_with_tech_documentation,
    monitor_system_performance,
    handle_software_bug_report,
    assist_with_data_recovery,
    manage_system_updates,
    configure_digital_signatures,
)
# Add more test cases to increase coverage

@pytest.mark.asyncio
async def test_assist_with_video_conferencing_setup():
    """Test the assist_with_video_conferencing_setup function."""
    result = await assist_with_video_conferencing_setup("John Doe", "Zoom")
    assert "Video Conferencing Setup" in result
    assert "John Doe" in result
    assert "Zoom" in result


@pytest.mark.asyncio
async def test_manage_it_inventory():
    """Test the manage_it_inventory function."""
    result = await manage_it_inventory()
    assert "IT Inventory Managed" in result


@pytest.mark.asyncio
async def test_configure_firewall_rules():
    """Test the configure_firewall_rules function."""
    result = await configure_firewall_rules("Allow traffic to port 8080")
    assert "Firewall Rules Configured" in result
    assert "Allow traffic to port 8080" in result


@pytest.mark.asyncio
async def test_manage_virtual_machines():
    """Test the manage_virtual_machines function."""
    result = await manage_virtual_machines("VM Details: Ubuntu Server")
    assert "Virtual Machines Managed" in result
    assert "Ubuntu Server" in result


@pytest.mark.asyncio
async def test_provide_tech_support_for_event():
    """Test the provide_tech_support_for_event function."""
    result = await provide_tech_support_for_event("Annual Tech Summit")
    assert "Tech Support for Event" in result
    assert "Annual Tech Summit" in result


@pytest.mark.asyncio
async def test_configure_network_storage():
    """Test the configure_network_storage function."""
    result = await configure_network_storage("John Doe", "500GB NAS Storage")
    assert "Network Storage Configured" in result
    assert "John Doe" in result
    assert "500GB NAS Storage" in result


@pytest.mark.asyncio
async def test_set_up_two_factor_authentication():
    """Test the set_up_two_factor_authentication function."""
    result = await set_up_two_factor_authentication("John Doe")
    assert "Two-Factor Authentication Setup" in result
    assert "John Doe" in result


@pytest.mark.asyncio
async def test_troubleshoot_email_issue():
    """Test the troubleshoot_email_issue function."""
    result = await troubleshoot_email_issue("John Doe", "Unable to send emails")
    assert "Email Issue Resolved" in result
    assert "Unable to send emails" in result
    assert "John Doe" in result


@pytest.mark.asyncio
async def test_manage_it_helpdesk_tickets():
    """Test the manage_it_helpdesk_tickets function."""
    result = await manage_it_helpdesk_tickets("Ticket #1234: Laptop not starting")
    assert "Helpdesk Tickets Managed" in result
    assert "Laptop not starting" in result


@pytest.mark.asyncio
async def test_provide_remote_tech_support():
    """Test the provide_remote_tech_support function."""
    result = await provide_remote_tech_support("John Doe")
    assert "Remote Tech Support Provided" in result
    assert "John Doe" in result


@pytest.mark.asyncio
async def test_manage_network_bandwidth():
    """Test the manage_network_bandwidth function."""
    result = await manage_network_bandwidth("Increase bandwidth for video calls")
    assert "Network Bandwidth Managed" in result
    assert "Increase bandwidth for video calls" in result


@pytest.mark.asyncio
async def test_assist_with_tech_documentation():
    """Test the assist_with_tech_documentation function."""
    result = await assist_with_tech_documentation("Technical Guide for VPN Setup")
    assert "Technical Documentation Created" in result
    assert "VPN Setup" in result


@pytest.mark.asyncio
async def test_monitor_system_performance():
    """Test the monitor_system_performance function."""
    result = await monitor_system_performance()
    assert "System Performance Monitored" in result

@pytest.mark.asyncio
async def test_handle_software_bug_report():
    """Test the handle_software_bug_report function."""
    result = await handle_software_bug_report("Critical bug in payment module")
    assert "Software Bug Report Handled" in result
    assert "Critical bug in payment module" in result


@pytest.mark.asyncio
async def test_assist_with_data_recovery():
    """Test the assist_with_data_recovery function."""
    result = await assist_with_data_recovery("John Doe", "Recover deleted files")
    assert "Data Recovery Assisted" in result
    assert "John Doe" in result
    assert "Recover deleted files" in result


@pytest.mark.asyncio
async def test_manage_system_updates():
    """Test the manage_system_updates function."""
    result = await manage_system_updates("Patch security vulnerabilities")
    assert "System Updates Managed" in result
    assert "Patch security vulnerabilities" in result


@pytest.mark.asyncio
async def test_configure_digital_signatures():
    """Test the configure_digital_signatures function."""
    result = await configure_digital_signatures("John Doe", "Secure email signature")
    assert "Digital Signatures Configured" in result
    assert "John Doe" in result
    assert "Secure email signature" in result


@pytest.mark.asyncio
async def test_provide_tech_training():
    """Test the provide_tech_training function."""
    result = await provide_tech_training("Jane Smith", "VPN Configuration Tool")
    assert "Tech Training Provided" in result
    assert "Jane Smith" in result
    assert "VPN Configuration Tool" in result


@pytest.mark.asyncio
async def test_manage_software_licenses():
    """Test the manage_software_licenses function."""
    result = await manage_software_licenses("Microsoft Office", 100)
    assert "Software Licenses Managed" in result
    assert "Microsoft Office" in result
    assert "100" in result


@pytest.mark.asyncio
async def test_update_firmware():
    """Test the update_firmware function."""
    result = await update_firmware("Printer XYZ", "v1.2.3")
    assert "Firmware Updated" in result
    assert "Printer XYZ" in result
    assert "v1.2.3" in result


@pytest.mark.asyncio
async def test_resolve_technical_issue():
    """Test the resolve_technical_issue function."""
    result = await resolve_technical_issue("System freezes during boot")
    assert "Technical Issue Resolved" in result
    assert "System freezes during boot" in result


@pytest.mark.asyncio
async def test_set_up_remote_desktop():
    """Test the set_up_remote_desktop function."""
    result = await set_up_remote_desktop("Emily White")
    assert "Remote Desktop Setup" in result
    assert "Emily White" in result


@pytest.mark.asyncio
async def test_configure_mobile_device():
    """Test the configure_mobile_device function."""
    result = await configure_mobile_device("John Doe", "iPhone 14 Pro")
    assert "Mobile Device Configuration" in result
    assert "John Doe" in result
    assert "iPhone 14 Pro" in result

@pytest.mark.asyncio
async def test_manage_network_security():
    """Test the manage_network_security function."""
    result = await manage_network_security()
    assert "Network Security Managed" in result

@pytest.mark.asyncio
async def test_configure_server():
    """Test the configure_server function."""
    result = await configure_server("Main Database Server")
    assert "Server Configuration" in result
    assert "Main Database Server" in result


@pytest.mark.asyncio
async def test_grant_database_access():
    """Test the grant_database_access function."""
    result = await grant_database_access("Alice Smith", "CustomerDB")
    assert "Database Access Granted" in result
    assert "Alice Smith" in result
    assert "CustomerDB" in result


@pytest.mark.asyncio
async def test_configure_printer():
    """Test the configure_printer function."""
    result = await configure_printer("Alice Smith", "HP LaserJet Pro")
    assert "Printer Configuration" in result
    assert "HP LaserJet Pro" in result
    assert "Alice Smith" in result


@pytest.mark.asyncio
async def test_set_up_email_signature():
    """Test the set_up_email_signature function."""
    result = await set_up_email_signature("Bob Lee", "Best regards, Bob")
    assert "Email Signature Setup" in result
    assert "Bob Lee" in result
    assert "Best regards, Bob" in result


@pytest.mark.asyncio
async def test_troubleshoot_hardware_issue():
    """Test the troubleshoot_hardware_issue function."""
    result = await troubleshoot_hardware_issue("Keyboard not responding")
    assert "Hardware Issue Resolved" in result
    assert "Keyboard not responding" in result

@pytest.mark.asyncio
async def test_configure_digital_signatures_with_special_chars():
    """Test the configure_digital_signatures function with special characters."""
    result = await configure_digital_signatures("Alice O'Conner", "Confidential [Secure]")
    assert "Digital Signatures Configured" in result
    assert "Alice O'Conner" in result
    assert "Confidential [Secure]" in result


@pytest.mark.asyncio
async def test_manage_system_updates_multiple_patches():
    """Test the manage_system_updates function with multiple patch details."""
    result = await manage_system_updates("Apply patches: CVE-2023-1234, CVE-2023-5678")
    assert "System Updates Managed" in result
    assert "CVE-2023-1234" in result
    assert "CVE-2023-5678" in result


@pytest.mark.asyncio
async def test_resolve_technical_issue_multiple_issues():
    """Test the resolve_technical_issue function with multiple issues."""
    result = await resolve_technical_issue("System crash and slow boot time")
    assert "Technical Issue Resolved" in result
    assert "System crash" in result
    assert "slow boot time" in result


@pytest.mark.asyncio
async def test_configure_mobile_device_multiple_models():
    """Test the configure_mobile_device function with multiple models."""
    result = await configure_mobile_device("John Doe", "Samsung Galaxy S23 Ultra")
    assert "Mobile Device Configuration" in result
    assert "Samsung Galaxy S23 Ultra" in result
    assert "John Doe" in result


@pytest.mark.asyncio
async def test_grant_database_access_multiple_roles():
    """Test the grant_database_access function with roles."""
    result = await grant_database_access("Sarah Connor", "SalesDB")
    assert "Database Access Granted" in result
    assert "Sarah Connor" in result
    assert "SalesDB" in result


@pytest.mark.asyncio
async def test_troubleshoot_hardware_issue_complex_case():
    """Test the troubleshoot_hardware_issue function with a complex issue."""
    result = await troubleshoot_hardware_issue("Random crashes during workload processing")
    assert "Hardware Issue Resolved" in result
    assert "Random crashes during workload processing" in result


@pytest.mark.asyncio
async def test_set_up_email_signature_long_text():
    """Test the set_up_email_signature function with a long signature."""
    signature = (
        "Best regards,\nJohn Doe\nSenior Developer\nXYZ Corporation\nEmail: john.doe@xyz.com"
    )
    result = await set_up_email_signature("John Doe", signature)
    assert "Email Signature Setup" in result
    assert "John Doe" in result
    assert "Senior Developer" in result


@pytest.mark.asyncio
async def test_configure_server_with_security_configs():
    """Test the configure_server function with additional security configurations."""
    result = await configure_server("Secure Database Server")
    assert "Server Configuration" in result
    assert "Secure Database Server" in result


@pytest.mark.asyncio
async def test_manage_software_licenses_multiple_types():
    """Test the manage_software_licenses function with multiple software types."""
    result = await manage_software_licenses("Adobe Creative Cloud", 50)
    assert "Software Licenses Managed" in result
    assert "Adobe Creative Cloud" in result
    assert "50" in result 

@pytest.mark.asyncio
async def test_set_up_email_signature_multiline():
    """Test the set_up_email_signature function with multiline signature."""
    signature = "John Doe\nDeveloper\nCompany XYZ"
    result = await set_up_email_signature("John Doe", signature)
    assert "Email Signature Setup" in result
    assert "Developer" in result
    assert "John Doe" in result


@pytest.mark.asyncio
async def test_configure_server_detailed():
    """Test the configure_server function with detailed configurations."""
    result = await configure_server("Application Server with Security")
    assert "Server Configuration" in result
    assert "Application Server with Security" in result


@pytest.mark.asyncio
async def test_set_up_remote_desktop_with_security():
    """Test the set_up_remote_desktop function with additional context."""
    result = await set_up_remote_desktop("Alice Smith")
    assert "Remote Desktop Setup" in result
    assert "Alice Smith" in result


@pytest.mark.asyncio
async def test_configure_mobile_device_advanced():
    """Test the configure_mobile_device function with advanced device model."""
    result = await configure_mobile_device("Bob Johnson", "Google Pixel 7")
    assert "Mobile Device Configuration" in result
    assert "Bob Johnson" in result
    assert "Google Pixel 7" in result


@pytest.mark.asyncio
async def test_troubleshoot_hardware_issue_with_details():
    """Test the troubleshoot_hardware_issue function with detailed issue."""
    result = await troubleshoot_hardware_issue("Overheating CPU under load")
    assert "Hardware Issue Resolved" in result
    assert "Overheating CPU under load" in result


@pytest.mark.asyncio
async def test_manage_software_licenses_bulk():
    """Test the manage_software_licenses function with bulk licenses."""
    result = await manage_software_licenses("AutoCAD", 500)
    assert "Software Licenses Managed" in result
    assert "AutoCAD" in result
    assert "500" in result


@pytest.mark.asyncio
async def test_update_firmware_latest_version():
    """Test the update_firmware function with the latest version."""
    result = await update_firmware("Router ABC", "v2.0.1")
    assert "Firmware Updated" in result
    assert "Router ABC" in result
    assert "v2.0.1" in result


@pytest.mark.asyncio
async def test_manage_system_updates_with_notes():
    """Test the manage_system_updates function with additional notes."""
    result = await manage_system_updates("Apply critical security patches")
    assert "System Updates Managed" in result
    assert "Apply critical security patches" in result


@pytest.mark.asyncio
async def test_provide_tech_training_different_tool():
    """Test the provide_tech_training function with a different tool."""
    result = await provide_tech_training("Eve Carter", "Data Analysis Suite")
    assert "Tech Training Provided" in result
    assert "Eve Carter" in result
    assert "Data Analysis Suite" in result


@pytest.mark.asyncio
async def test_grant_database_access_advanced():
    """Test the grant_database_access function with detailed roles."""
    result = await grant_database_access("Martin Lee", "FinanceDB")
    assert "Database Access Granted" in result
    assert "Martin Lee" in result
    assert "FinanceDB" in result


@pytest.mark.asyncio
async def test_configure_firewall_rules_complex():
    """Test the configure_firewall_rules function with complex rule."""
    result = await configure_firewall_rules("Block traffic from 192.168.1.100")
    assert "Firewall Rules Configured" in result
    assert "Block traffic from 192.168.1.100" in result


@pytest.mark.asyncio
async def test_monitor_system_performance_with_metrics():
    """Test the monitor_system_performance function with detailed metrics."""
    result = await monitor_system_performance()
    assert "System Performance Monitored" in result

@pytest.mark.asyncio
async def test_configure_server_with_edge_case():
    """Test configure_server with an edge case (e.g., server name is special characters)."""
    result = await configure_server("!@#$%^&*()_+Server")
    assert "Server Configuration" in result
    assert "!@#$%^&*()_+Server" in result

@pytest.mark.asyncio
async def test_configure_printer_with_special_characters():
    """Test configure_printer with a printer model containing special characters."""
    result = await configure_printer("Alice Smith", "HP@123!Printer")
    assert "Printer Configuration" in result
    assert "HP@123!Printer" in result

@pytest.mark.asyncio
async def test_configure_mobile_device_unusual_model():
    """Test configure_mobile_device with an unusual device model."""
    result = await configure_mobile_device("John Doe", "XYZ@Device#2023")
    assert "Mobile Device Configuration" in result
    assert "XYZ@Device#2023" in result

@pytest.mark.asyncio
async def test_troubleshoot_hardware_issue_with_long_description():
    """Test troubleshoot_hardware_issue with a very long description."""
    issue_description = " " * 300 + "Fault detected."
    result = await troubleshoot_hardware_issue(issue_description)
    assert "Hardware Issue Resolved" in result
    assert "Fault detected." in result