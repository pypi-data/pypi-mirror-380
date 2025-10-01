"""CLI Integration Patterns for Communication Pillar.

IMPORTANT: This module provides integration patterns and examples only.
The communication pillar does NOT depend on the CLI pillar.

Applications that want CLI functionality should:
1. Import both communication and CLI pillars independently
2. Implement integration at the application level using patterns from this module

Example:
    from xlibrary.communication import CommManager
    from xlibrary.cli import CLIFramework  # Hypothetical CLI pillar
    from xlibrary.communication.cli.integration_pattern import CommunicationCLIIntegrationPattern

    # Application-level integration
    comm = CommManager()
    cli = CLIFramework()
    integration = CommunicationCLIIntegrationPattern(comm, cli)
    integration.register_email_commands()
"""

from .integration_pattern import CommunicationCLIIntegrationPattern, INTEGRATION_PATTERNS

__all__ = ["CommunicationCLIIntegrationPattern", "INTEGRATION_PATTERNS"]