"""
Check MCP external services installation and health.

WHY: Verify that MCP services (mcp-vector-search, mcp-browser, mcp-ticketer, kuzu-memory)
are properly installed and accessible for enhanced Claude Desktop capabilities.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from ..models import DiagnosticResult, DiagnosticStatus
from .base_check import BaseDiagnosticCheck


class MCPServicesCheck(BaseDiagnosticCheck):
    """Check MCP external services installation and health."""

    # Define MCP services to check
    MCP_SERVICES = {
        "mcp-vector-search": {
            "package": "mcp-vector-search",
            "command": ["mcp-vector-search", "--help"],
            "description": "Vector search for semantic code navigation",
            "check_health": True,
            "health_command": ["mcp-vector-search", "--version"],
        },
        "mcp-browser": {
            "package": "mcp-browser",
            "command": ["mcp-browser", "--help"],
            "description": "Browser automation and web interaction",
            "check_health": True,
            "health_command": ["mcp-browser", "--version"],
        },
        "mcp-ticketer": {
            "package": "mcp-ticketer",
            "command": ["mcp-ticketer", "--help"],
            "description": "Ticket and task management",
            "check_health": True,
            "health_command": ["mcp-ticketer", "--version"],
        },
        "kuzu-memory": {
            "package": "kuzu-memory",
            "command": ["kuzu-memory", "--help"],
            "description": "Graph-based memory system",
            "check_health": False,  # May not have version command
        },
    }

    @property
    def name(self) -> str:
        return "mcp_services_check"

    @property
    def category(self) -> str:
        return "MCP Services"

    def run(self) -> DiagnosticResult:
        """Run MCP services diagnostics."""
        try:
            details = {}
            sub_results = []
            services_status = {}

            # Check each MCP service
            for service_name, service_config in self.MCP_SERVICES.items():
                service_result = self._check_service(service_name, service_config)
                sub_results.append(service_result)
                services_status[service_name] = {
                    "status": service_result.status.value,
                    "installed": service_result.details.get("installed", False),
                    "accessible": service_result.details.get("accessible", False),
                    "version": service_result.details.get("version"),
                }

            # Check MCP gateway configuration for services
            gateway_result = self._check_gateway_configuration()
            sub_results.append(gateway_result)

            # Count service statuses
            installed_count = sum(1 for s in services_status.values() if s["installed"])
            accessible_count = sum(
                1 for s in services_status.values() if s["accessible"]
            )
            total_services = len(self.MCP_SERVICES)

            details["services"] = services_status
            details["installed_count"] = installed_count
            details["accessible_count"] = accessible_count
            details["total_services"] = total_services
            details["gateway_configured"] = gateway_result.status == DiagnosticStatus.OK

            # Determine overall status
            errors = [r for r in sub_results if r.status == DiagnosticStatus.ERROR]
            warnings = [r for r in sub_results if r.status == DiagnosticStatus.WARNING]

            if errors:
                status = DiagnosticStatus.ERROR
                message = f"Critical issues with {len(errors)} MCP service(s)"
            elif installed_count == 0:
                status = DiagnosticStatus.WARNING
                message = "No MCP services installed"
            elif accessible_count < installed_count:
                status = DiagnosticStatus.WARNING
                message = f"{installed_count}/{total_services} services installed, {accessible_count} accessible"
            elif installed_count < total_services:
                status = DiagnosticStatus.WARNING
                message = f"{installed_count}/{total_services} MCP services installed"
            else:
                status = DiagnosticStatus.OK
                message = f"All {total_services} MCP services installed and accessible"

            return DiagnosticResult(
                category=self.category,
                status=status,
                message=message,
                details=details,
                sub_results=sub_results if self.verbose else [],
            )

        except Exception as e:
            return DiagnosticResult(
                category=self.category,
                status=DiagnosticStatus.ERROR,
                message=f"MCP services check failed: {e!s}",
                details={"error": str(e)},
            )

    def _check_service(self, service_name: str, config: Dict) -> DiagnosticResult:
        """Check a specific MCP service."""
        details = {"service": service_name}

        # Check if installed via pipx
        pipx_installed, pipx_path = self._check_pipx_installation(config["package"])
        details["pipx_installed"] = pipx_installed
        if pipx_path:
            details["pipx_path"] = pipx_path

        # Check if accessible in PATH
        accessible, command_path = self._check_command_accessible(config["command"])
        details["accessible"] = accessible
        if command_path:
            details["command_path"] = command_path

        # Check for installation in various locations
        if not pipx_installed and not accessible:
            # Try common installation locations
            alt_installed, alt_path = self._check_alternative_installations(
                service_name
            )
            if alt_installed:
                details["alternative_installation"] = alt_path
                accessible = alt_installed

        details["installed"] = pipx_installed or accessible

        # Check service health/version if accessible
        if accessible and config.get("check_health"):
            version = self._get_service_version(
                config.get("health_command", config["command"])
            )
            if version:
                details["version"] = version

        # Determine status
        if not (pipx_installed or accessible):
            return DiagnosticResult(
                category=f"MCP Service: {service_name}",
                status=DiagnosticStatus.WARNING,
                message=f"Not installed: {config['description']}",
                details=details,
                fix_command=f"pipx install {config['package']}",
                fix_description=f"Install {service_name} for {config['description']}",
            )

        if pipx_installed and not accessible:
            return DiagnosticResult(
                category=f"MCP Service: {service_name}",
                status=DiagnosticStatus.WARNING,
                message="Installed via pipx but not in PATH",
                details=details,
                fix_command="pipx ensurepath",
                fix_description="Ensure pipx bin directory is in PATH",
            )

        return DiagnosticResult(
            category=f"MCP Service: {service_name}",
            status=DiagnosticStatus.OK,
            message="Installed and accessible",
            details=details,
        )

    def _check_pipx_installation(self, package_name: str) -> Tuple[bool, Optional[str]]:
        """Check if a package is installed via pipx."""
        try:
            result = subprocess.run(
                ["pipx", "list", "--json"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )

            if result.returncode == 0:
                try:
                    data = json.loads(result.stdout)
                    venvs = data.get("venvs", {})

                    if package_name in venvs:
                        venv_info = venvs[package_name]
                        # Get the main app path
                        apps = (
                            venv_info.get("metadata", {})
                            .get("main_package", {})
                            .get("apps", [])
                        )
                        if apps:
                            app_path = (
                                venv_info.get("metadata", {})
                                .get("main_package", {})
                                .get("app_paths", [])
                            )
                            if app_path:
                                return True, app_path[0]
                        return True, None
                except json.JSONDecodeError:
                    pass
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return False, None

    def _check_command_accessible(
        self, command: List[str]
    ) -> Tuple[bool, Optional[str]]:
        """Check if a command is accessible in PATH."""
        try:
            # Use 'which' on Unix-like systems
            result = subprocess.run(
                ["which", command[0]],
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )

            if result.returncode == 0:
                path = result.stdout.strip()
                return True, path
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        # Try direct execution
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )
            if (
                result.returncode == 0
                or "help" in result.stdout.lower()
                or "usage" in result.stdout.lower()
            ):
                return True, None
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return False, None

    def _check_alternative_installations(
        self, service_name: str
    ) -> Tuple[bool, Optional[str]]:
        """Check for alternative installation locations."""
        # Common installation paths
        paths_to_check = [
            Path.home() / ".local" / "bin" / service_name,
            Path("/usr/local/bin") / service_name,
            Path("/opt") / service_name / "bin" / service_name,
            Path.home() / ".npm" / "bin" / service_name,  # For npm-based services
            Path.home() / ".cargo" / "bin" / service_name,  # For Rust-based services
        ]

        for path in paths_to_check:
            if path.exists():
                return True, str(path)

        return False, None

    def _get_service_version(self, command: List[str]) -> Optional[str]:
        """Get version information for a service."""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=2,
                check=False,
            )

            if result.returncode == 0:
                output = result.stdout.strip()
                # Try to extract version from output
                lines = output.split("\n")
                for line in lines:
                    if "version" in line.lower() or "v" in line.lower():
                        return line.strip()
                # Return first line if no version line found
                if lines:
                    return lines[0].strip()
        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return None

    def _check_gateway_configuration(self) -> DiagnosticResult:
        """Check if MCP services are configured in the gateway."""
        try:
            # Check MCP config file
            config_dir = Path.home() / ".claude" / "mcp"
            config_file = config_dir / "config.json"

            if not config_file.exists():
                return DiagnosticResult(
                    category="MCP Gateway Configuration",
                    status=DiagnosticStatus.WARNING,
                    message="MCP configuration file not found",
                    details={"config_path": str(config_file), "exists": False},
                    fix_command="claude-mpm configure --mcp",
                    fix_description="Initialize MCP configuration",
                )

            with open(config_file) as f:
                config = json.load(f)

            # Check for external services configuration
            external_services = config.get("external_services", {})
            configured_services = []
            missing_services = []

            for service_name in self.MCP_SERVICES:
                if service_name in external_services:
                    configured_services.append(service_name)
                else:
                    # Also check if it's in the services list directly
                    services = config.get("services", [])
                    if any(s.get("name") == service_name for s in services):
                        configured_services.append(service_name)
                    else:
                        missing_services.append(service_name)

            details = {
                "config_path": str(config_file),
                "configured_services": configured_services,
                "missing_services": missing_services,
            }

            if not configured_services:
                return DiagnosticResult(
                    category="MCP Gateway Configuration",
                    status=DiagnosticStatus.WARNING,
                    message="No MCP services configured in gateway",
                    details=details,
                    fix_command="claude-mpm configure --mcp --add-services",
                    fix_description="Add MCP services to gateway configuration",
                )

            if missing_services:
                return DiagnosticResult(
                    category="MCP Gateway Configuration",
                    status=DiagnosticStatus.WARNING,
                    message=f"{len(configured_services)} services configured, {len(missing_services)} missing",
                    details=details,
                )

            return DiagnosticResult(
                category="MCP Gateway Configuration",
                status=DiagnosticStatus.OK,
                message=f"All {len(configured_services)} services configured",
                details=details,
            )

        except json.JSONDecodeError as e:
            return DiagnosticResult(
                category="MCP Gateway Configuration",
                status=DiagnosticStatus.ERROR,
                message="Invalid JSON in MCP configuration",
                details={"error": str(e)},
            )
        except Exception as e:
            return DiagnosticResult(
                category="MCP Gateway Configuration",
                status=DiagnosticStatus.WARNING,
                message=f"Could not check configuration: {e!s}",
                details={"error": str(e)},
            )
