"""CLI Integration Pattern for Communication Pillar.

This module demonstrates how applications can integrate the communication pillar
with the CLI pillar while maintaining pillar independence.

IMPORTANT: The communication pillar does NOT depend on the CLI pillar.
Applications that want CLI functionality should import both pillars
independently and implement the integration at the application level.

Example Application Integration:
    # app.py - Application-level integration
    from xlibrary.communication import CommManager
    from xlibrary.cli import CLIFramework

    # Create independent pillar instances
    comm = CommManager()
    cli = CLIFramework()

    # Application-level integration
    def send_email_command(args):
        gmail = comm.gmail(credentials_path="credentials.json")
        return gmail.send_message(args.to, args.subject, args.body)

    cli.add_command("email-send", send_email_command)
"""

from typing import Dict, Any, Optional, Callable


class CommunicationCLIIntegrationPattern:
    """Pattern class showing how to integrate communication with CLI.

    This is a reference implementation that applications can adapt.
    It does NOT create dependencies between pillars.
    """

    def __init__(self, comm_manager, cli_framework):
        """Initialize with independent pillar instances.

        Args:
            comm_manager: Instance from communication pillar
            cli_framework: Instance from CLI pillar
        """
        self.comm = comm_manager
        self.cli = cli_framework

    def register_email_commands(self) -> None:
        """Example of registering email commands with CLI.

        Applications should implement similar patterns based on their needs.
        """
        # Example command registration (pseudo-code)
        # self.cli.add_command("email-send", self._email_send_handler)
        # self.cli.add_command("email-search", self._email_search_handler)
        pass

    def _email_send_handler(self, args) -> None:
        """Example email send handler."""
        # Application logic using communication pillar
        gmail = self.comm.gmail(credentials_path=args.credentials)
        return gmail.send_message(args.to, args.subject, args.body)

    def _email_search_handler(self, args) -> None:
        """Example email search handler."""
        from xlibrary.communication import EmailQuery

        gmail = self.comm.gmail(credentials_path=args.credentials)
        query = EmailQuery()

        if args.sender:
            query = query.from_sender(args.sender)
        if args.unread:
            query = query.is_unread()
        if args.limit:
            query = query.limit(args.limit)

        return gmail.search(query)


def create_integration_example():
    """Example showing proper pillar integration in applications.

    This function demonstrates the correct way to use multiple pillars
    together while maintaining their independence.
    """
    example_code = '''
# application.py - Proper pillar integration example

from xlibrary.communication import CommManager, EmailQuery
from xlibrary.cli import CLIFramework  # Hypothetical CLI pillar import

class EmailApplication:
    def __init__(self):
        # Create independent pillar instances
        self.comm = CommManager()
        self.cli = CLIFramework()

        # Register application-level integrations
        self._register_commands()

    def _register_commands(self):
        """Register email commands with CLI framework."""
        self.cli.add_command("send", self.send_email)
        self.cli.add_command("search", self.search_emails)

    def send_email(self, args):
        """Send email using communication pillar."""
        gmail = self.comm.gmail(credentials_path=args.credentials)
        return gmail.send_message(args.to, args.subject, args.body)

    def search_emails(self, args):
        """Search emails using communication pillar."""
        gmail = self.comm.gmail(credentials_path=args.credentials)
        query = EmailQuery().from_sender(args.sender).limit(args.limit)
        return gmail.search(query)

# Usage
app = EmailApplication()
app.cli.run()  # Runs CLI with integrated email commands
'''
    return example_code


# Integration patterns that applications can use
INTEGRATION_PATTERNS = {
    "command_registration": {
        "description": "Register communication commands with CLI pillar",
        "example": create_integration_example()
    },
    "progress_integration": {
        "description": "Use CLI progress bars with communication operations",
        "pattern": "Application imports both pillars and uses CLI progress with comm operations"
    },
    "interactive_menus": {
        "description": "Create CLI menus for communication operations",
        "pattern": "Application creates CLI menus that call communication pillar methods"
    }
}