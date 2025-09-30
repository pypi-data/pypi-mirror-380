"""
MCP Configuration Manager
========================

Manages MCP service configurations, preferring pipx installations
over local virtual environments for better isolation and management.

This module provides utilities to detect, configure, and validate
MCP service installations.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, Tuple

from ..core.logger import get_logger


class ConfigLocation(Enum):
    """Enumeration of Claude configuration file locations."""

    CLAUDE_JSON = Path.home() / ".claude.json"  # Primary Claude config
    CLAUDE_DESKTOP = (
        Path.home() / ".claude" / "claude_desktop_config.json"
    )  # Not used by Claude Code
    PROJECT_MCP = ".mcp.json"  # Project-level MCP config (deprecated)


class MCPConfigManager:
    """Manages MCP service configurations with pipx preference."""

    # Standard MCP services that should use pipx
    PIPX_SERVICES = {
        "mcp-vector-search",
        "mcp-browser",
        "mcp-ticketer",
        "kuzu-memory",
    }

    # Static known-good MCP service configurations
    # These are the correct, tested configurations that work reliably
    STATIC_MCP_CONFIGS = {
        "kuzu-memory": {
            "type": "stdio",
            "command": "kuzu-memory",  # Use direct binary, will be resolved to full path
            "args": ["mcp", "serve"]  # v1.1.0+ uses 'mcp serve' command
        },
        "mcp-ticketer": {
            "type": "stdio",
            "command": "mcp-ticketer",  # Use direct binary to preserve injected dependencies
            "args": ["mcp"]
        },
        "mcp-browser": {
            "type": "stdio",
            "command": "mcp-browser",  # Use direct binary
            "args": ["mcp"],
            "env": {"MCP_BROWSER_HOME": str(Path.home() / ".mcp-browser")}
        },
        "mcp-vector-search": {
            "type": "stdio",
            # Use pipx venv's Python directly for module execution
            "command": str(Path.home() / ".local" / "pipx" / "venvs" / "mcp-vector-search" / "bin" / "python"),
            "args": ["-m", "mcp_vector_search.mcp.server", "{project_root}"],
            "env": {}
        }
    }

    def __init__(self):
        """Initialize the MCP configuration manager."""
        self.logger = get_logger(__name__)
        self.pipx_base = Path.home() / ".local" / "pipx" / "venvs"
        self.project_root = Path.cwd()

        # Use the proper Claude config file location
        self.claude_config_path = ConfigLocation.CLAUDE_JSON.value

    def detect_service_path(self, service_name: str) -> Optional[str]:
        """
        Detect the best path for an MCP service.

        Priority order:
        1. For kuzu-memory: prefer v1.1.0+ with MCP support
        2. Pipx installation (preferred)
        3. System PATH (likely from pipx or homebrew)
        4. Local venv (fallback)

        Args:
            service_name: Name of the MCP service

        Returns:
            Path to the service executable or None if not found
        """
        # Special handling for kuzu-memory - prefer v1.1.0+ with MCP support
        if service_name == "kuzu-memory":
            candidates = []

            # Check pipx installation
            pipx_path = self._check_pipx_installation(service_name)
            if pipx_path:
                candidates.append(pipx_path)

            # Check system PATH (including homebrew)
            import shutil

            system_path = shutil.which(service_name)
            if system_path and system_path not in candidates:
                candidates.append(system_path)

            # Choose the best candidate (prefer v1.1.0+ with MCP support)
            for path in candidates:
                try:
                    result = subprocess.run(
                        [path, "--help"],
                        capture_output=True,
                        text=True,
                        timeout=5,
                        check=False,
                    )
                    # Check if this version has MCP support
                    if "claude" in result.stdout or "mcp" in result.stdout:
                        self.logger.debug(
                            f"Found kuzu-memory with MCP support at {path}"
                        )
                        return path
                except:
                    pass

            # If no MCP-capable version found, log warning but return None
            if candidates:
                self.logger.warning(
                    f"Found kuzu-memory at {candidates[0]} but it lacks MCP support. "
                    f"Upgrade to v1.1.0+ for MCP integration: pipx upgrade kuzu-memory"
                )
            return None  # Don't configure MCP for incompatible versions

        # Standard detection for other services
        # Check pipx installation first
        pipx_path = self._check_pipx_installation(service_name)
        if pipx_path:
            self.logger.debug(f"Found {service_name} via pipx: {pipx_path}")
            return pipx_path

        # Check system PATH
        system_path = self._check_system_path(service_name)
        if system_path:
            self.logger.debug(f"Found {service_name} in PATH: {system_path}")
            return system_path

        # Fallback to local venv
        local_path = self._check_local_venv(service_name)
        if local_path:
            self.logger.warning(
                f"Using local venv for {service_name} (consider installing via pipx)"
            )
            return local_path

        self.logger.debug(
            f"Service {service_name} not found - will auto-install when needed"
        )
        return None

    def _check_pipx_installation(self, service_name: str) -> Optional[str]:
        """Check if service is installed via pipx."""
        pipx_venv = self.pipx_base / service_name

        if not pipx_venv.exists():
            return None

        # Special handling for mcp-vector-search (needs Python interpreter)
        if service_name == "mcp-vector-search":
            python_bin = pipx_venv / "bin" / "python"
            if python_bin.exists() and python_bin.is_file():
                return str(python_bin)
        else:
            # Other services use direct binary
            service_bin = pipx_venv / "bin" / service_name
            if service_bin.exists() and service_bin.is_file():
                return str(service_bin)

        return None

    def _check_system_path(self, service_name: str) -> Optional[str]:
        """Check if service is available in system PATH."""
        try:
            result = subprocess.run(
                ["which", service_name],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                path = result.stdout.strip()
                # Verify it's from pipx
                if "/.local/bin/" in path or "/pipx/" in path:
                    return path
        except Exception as e:
            self.logger.debug(f"Error checking system PATH: {e}")

        return None

    def _check_local_venv(self, service_name: str) -> Optional[str]:
        """Check for local virtual environment installation (fallback)."""
        # Common local development paths
        possible_paths = [
            Path.home() / "Projects" / "managed" / service_name / ".venv" / "bin",
            self.project_root / ".venv" / "bin",
            self.project_root / "venv" / "bin",
        ]

        for base_path in possible_paths:
            if service_name == "mcp-vector-search":
                python_bin = base_path / "python"
                if python_bin.exists():
                    return str(python_bin)
            else:
                service_bin = base_path / service_name
                if service_bin.exists():
                    return str(service_bin)

        return None

    def test_service_command(self, service_name: str, config: Dict) -> bool:
        """
        Test if a service configuration actually works.

        Args:
            service_name: Name of the MCP service
            config: Service configuration to test

        Returns:
            True if service responds correctly, False otherwise
        """
        try:
            import shutil

            # Build command - handle pipx PATH issues
            command = config["command"]

            # If command is pipx and not found, try common paths
            if command == "pipx":
                pipx_path = shutil.which("pipx")
                if not pipx_path:
                    # Try common pipx locations
                    for possible_path in [
                        "/opt/homebrew/bin/pipx",
                        "/usr/local/bin/pipx",
                        str(Path.home() / ".local" / "bin" / "pipx"),
                    ]:
                        if Path(possible_path).exists():
                            command = possible_path
                            break
                else:
                    command = pipx_path

            cmd = [command]

            # Add test args (--help or --version)
            if "args" in config:
                # For MCP services, test with --help after the subcommand
                test_args = config["args"].copy()
                # Replace project root placeholder for testing
                test_args = [
                    arg.replace("{project_root}", str(self.project_root)) if "{project_root}" in arg else arg
                    for arg in test_args
                ]

                # Add --help at the end
                if service_name == "mcp-vector-search":
                    # For Python module invocation, just test if Python can import the module
                    cmd.extend(test_args[:2])  # Just python -m module_name
                    cmd.extend(["--help"])
                else:
                    cmd.extend(test_args)
                    cmd.append("--help")
            else:
                cmd.append("--help")

            # Run test command with timeout
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
                env=config.get("env", {})
            )

            # Check if command executed (exit code 0 or 1 for help)
            if result.returncode in [0, 1]:
                # Additional check for import errors in stderr
                if "ModuleNotFoundError" in result.stderr or "ImportError" in result.stderr:
                    self.logger.debug(f"Service {service_name} has import errors")
                    return False
                return True

        except subprocess.TimeoutExpired:
            # Timeout might mean the service started successfully and is waiting for input
            return True
        except Exception as e:
            self.logger.debug(f"Error testing {service_name}: {e}")

        return False

    def get_static_service_config(self, service_name: str, project_path: Optional[str] = None) -> Optional[Dict]:
        """
        Get the static, known-good configuration for an MCP service.

        Args:
            service_name: Name of the MCP service
            project_path: Optional project path to use (defaults to current project)

        Returns:
            Static service configuration dict or None if service not known
        """
        if service_name not in self.STATIC_MCP_CONFIGS:
            return None

        config = self.STATIC_MCP_CONFIGS[service_name].copy()
        import shutil

        # Resolve service binary commands to full paths
        if service_name in ["kuzu-memory", "mcp-ticketer", "mcp-browser"]:
            # Try to find the full path of the binary
            binary_name = config["command"]
            binary_path = shutil.which(binary_name)

            if not binary_path:
                # Try common installation locations
                possible_paths = [
                    f"/opt/homebrew/bin/{binary_name}",
                    f"/usr/local/bin/{binary_name}",
                    str(Path.home() / ".local" / "bin" / binary_name),
                ]
                for path in possible_paths:
                    if Path(path).exists():
                        binary_path = path
                        break

            if binary_path:
                config["command"] = binary_path
            # If still not found, keep the binary name and hope it's in PATH

        # Resolve pipx command to full path if needed
        elif config.get("command") == "pipx":
            pipx_path = shutil.which("pipx")
            if not pipx_path:
                # Try common pipx locations
                for possible_path in [
                    "/opt/homebrew/bin/pipx",
                    "/usr/local/bin/pipx",
                    str(Path.home() / ".local" / "bin" / "pipx"),
                ]:
                    if Path(possible_path).exists():
                        pipx_path = possible_path
                        break
            if pipx_path:
                config["command"] = pipx_path
            else:
                # Keep as "pipx" and hope it's in PATH when executed
                config["command"] = "pipx"

        # Handle user-specific paths for mcp-vector-search
        if service_name == "mcp-vector-search":
            # Get the correct pipx venv path for the current user
            home = Path.home()
            python_path = home / ".local" / "pipx" / "venvs" / "mcp-vector-search" / "bin" / "python"

            # Check if the Python interpreter exists, if not fallback to pipx run
            if python_path.exists():
                config["command"] = str(python_path)
            else:
                # Fallback to pipx run method
                import shutil
                pipx_path = shutil.which("pipx")
                if not pipx_path:
                    # Try common pipx locations
                    for possible_path in [
                        "/opt/homebrew/bin/pipx",
                        "/usr/local/bin/pipx",
                        str(Path.home() / ".local" / "bin" / "pipx"),
                    ]:
                        if Path(possible_path).exists():
                            pipx_path = possible_path
                            break
                config["command"] = pipx_path if pipx_path else "pipx"
                config["args"] = ["run", "--spec", "mcp-vector-search", "python"] + config["args"]

            # Use provided project path or current project
            project_root = project_path if project_path else str(self.project_root)
            config["args"] = [
                arg.replace("{project_root}", project_root) if "{project_root}" in arg else arg
                for arg in config["args"]
            ]

        return config

    def generate_service_config(self, service_name: str) -> Optional[Dict]:
        """
        Generate configuration for a specific MCP service.

        Prefers static configurations over detection. Falls back to detection
        only for unknown services.

        Args:
            service_name: Name of the MCP service

        Returns:
            Service configuration dict or None if service not found
        """
        # First try to get static configuration
        static_config = self.get_static_service_config(service_name)
        if static_config:
            # Validate that the static config actually works
            if self.test_service_command(service_name, static_config):
                self.logger.debug(f"Static config for {service_name} validated successfully")
                return static_config
            else:
                self.logger.warning(f"Static config for {service_name} failed validation, trying fallback")

        # Fall back to detection-based configuration for unknown services
        import shutil

        # Check for pipx run first (preferred for isolation)
        use_pipx_run = False
        use_uvx = False

        # Try pipx run test
        if shutil.which("pipx"):
            try:
                result = subprocess.run(
                    ["pipx", "run", service_name, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=False,
                )
                if result.returncode == 0 or "version" in result.stdout.lower():
                    use_pipx_run = True
                    self.logger.debug(f"Will use 'pipx run' for {service_name}")
            except:
                pass

        # Try uvx if pipx run not available
        if not use_pipx_run and shutil.which("uvx"):
            try:
                result = subprocess.run(
                    ["uvx", service_name, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=False,
                )
                if result.returncode == 0 or "version" in result.stdout.lower():
                    use_uvx = True
                    self.logger.debug(f"Will use 'uvx' for {service_name}")
            except:
                pass

        # If neither work, try to find direct path
        service_path = None
        if not use_pipx_run and not use_uvx:
            service_path = self.detect_service_path(service_name)
            if not service_path:
                return None

        # Build configuration
        config = {"type": "stdio"}

        # Service-specific configurations
        if service_name == "mcp-vector-search":
            if use_pipx_run:
                config["command"] = "pipx"
                config["args"] = [
                    "run",
                    "mcp-vector-search",
                    "-m",
                    "mcp_vector_search.mcp.server",
                    str(self.project_root),
                ]
            elif use_uvx:
                config["command"] = "uvx"
                config["args"] = [
                    "mcp-vector-search",
                    "-m",
                    "mcp_vector_search.mcp.server",
                    str(self.project_root),
                ]
            else:
                config["command"] = service_path
                config["args"] = [
                    "-m",
                    "mcp_vector_search.mcp.server",
                    str(self.project_root),
                ]
            config["env"] = {}

        elif service_name == "mcp-browser":
            if use_pipx_run:
                config["command"] = "pipx"
                config["args"] = ["run", "mcp-browser", "mcp"]
            elif use_uvx:
                config["command"] = "uvx"
                config["args"] = ["mcp-browser", "mcp"]
            else:
                config["command"] = service_path
                config["args"] = ["mcp"]
            config["env"] = {"MCP_BROWSER_HOME": str(Path.home() / ".mcp-browser")}

        elif service_name == "mcp-ticketer":
            if use_pipx_run:
                config["command"] = "pipx"
                config["args"] = ["run", "mcp-ticketer", "mcp"]
            elif use_uvx:
                config["command"] = "uvx"
                config["args"] = ["mcp-ticketer", "mcp"]
            else:
                config["command"] = service_path
                config["args"] = ["mcp"]

        elif service_name == "kuzu-memory":
            # Determine kuzu-memory command version
            kuzu_args = ["mcp", "serve"]  # Default to the standard v1.1.0+ format
            test_cmd = None

            if use_pipx_run:
                test_cmd = ["pipx", "run", "kuzu-memory", "--help"]
            elif use_uvx:
                test_cmd = ["uvx", "kuzu-memory", "--help"]
            elif service_path:
                test_cmd = [service_path, "--help"]

            if test_cmd:
                try:
                    result = subprocess.run(
                        test_cmd,
                        capture_output=True,
                        text=True,
                        timeout=10,
                        check=False,
                    )
                    # Check for MCP support in help output
                    help_output = result.stdout.lower() + result.stderr.lower()

                    # Standard version detection - look for "mcp serve" command (v1.1.0+)
                    # This is the correct format for kuzu-memory v1.1.0 and later
                    if "mcp serve" in help_output or ("mcp" in help_output and "serve" in help_output):
                        # Standard v1.1.0+ version with mcp serve command
                        kuzu_args = ["mcp", "serve"]
                    # Legacy version detection - only "serve" without "mcp"
                    elif "serve" in help_output and "mcp" not in help_output:
                        # Very old version that only has serve command
                        kuzu_args = ["serve"]
                    else:
                        # Default to the standard mcp serve format (v1.1.0+)
                        # Note: "claude mcp-server" format is deprecated and does not work
                        kuzu_args = ["mcp", "serve"]
                except Exception:
                    # Default to the standard mcp serve command on any error
                    kuzu_args = ["mcp", "serve"]

            if use_pipx_run:
                config["command"] = "pipx"
                config["args"] = ["run", "kuzu-memory"] + kuzu_args
            elif use_uvx:
                config["command"] = "uvx"
                config["args"] = ["kuzu-memory"] + kuzu_args
            else:
                config["command"] = service_path
                config["args"] = kuzu_args

        # Generic config for unknown services
        elif use_pipx_run:
            config["command"] = "pipx"
            config["args"] = ["run", service_name]
        elif use_uvx:
            config["command"] = "uvx"
            config["args"] = [service_name]
        else:
            config["command"] = service_path
            config["args"] = []

        return config

    def ensure_mcp_services_configured(self) -> Tuple[bool, str]:
        """
        Ensure MCP services are configured correctly in ~/.claude.json on startup.

        This method checks ALL projects in ~/.claude.json and ensures each has
        the correct, static MCP service configurations. It will:
        1. Add missing services
        2. Fix incorrect configurations
        3. Update all projects, not just the current one

        Returns:
            Tuple of (success, message)
        """
        updated = False
        fixed_services = []
        added_services = []

        # Load existing Claude config or create minimal structure
        claude_config = {}
        if self.claude_config_path.exists():
            try:
                with open(self.claude_config_path) as f:
                    claude_config = json.load(f)
            except Exception as e:
                self.logger.error(f"Error reading {self.claude_config_path}: {e}")
                return False, f"Failed to read Claude config: {e}"

        # Ensure projects structure exists
        if "projects" not in claude_config:
            claude_config["projects"] = {}
            updated = True

        # Fix any corrupted MCP service installations first
        fix_success, fix_message = self.fix_mcp_service_issues()
        if not fix_success:
            self.logger.warning(f"Some MCP services could not be fixed: {fix_message}")

        # Process ALL projects in the config, not just current one
        projects_to_update = list(claude_config.get("projects", {}).keys())

        # Also add the current project if not in list
        current_project_key = str(self.project_root)
        if current_project_key not in projects_to_update:
            projects_to_update.append(current_project_key)
            # Initialize new project structure
            claude_config["projects"][current_project_key] = {
                "allowedTools": [],
                "history": [],
                "mcpContextUris": [],
                "mcpServers": {},
                "enabledMcpjsonServers": [],
                "disabledMcpjsonServers": [],
                "hasTrustDialogAccepted": False,
                "projectOnboardingSeenCount": 0,
                "hasClaudeMdExternalIncludesApproved": False,
                "hasClaudeMdExternalIncludesWarningShown": False,
            }
            updated = True

        # Update each project's MCP configurations
        for project_key in projects_to_update:
            project_config = claude_config["projects"][project_key]

            # Ensure mcpServers section exists
            if "mcpServers" not in project_config:
                project_config["mcpServers"] = {}
                updated = True

            # Check and fix each service configuration
            for service_name in self.PIPX_SERVICES:
                # Get the correct static configuration with project-specific paths
                correct_config = self.get_static_service_config(service_name, project_key)

                if not correct_config:
                    self.logger.warning(f"No static config available for {service_name}")
                    continue

                # Check if service exists and has correct configuration
                existing_config = project_config["mcpServers"].get(service_name)

                # Determine if we need to update
                needs_update = False
                if not existing_config:
                    # Service is missing
                    needs_update = True
                    added_services.append(f"{service_name} in {Path(project_key).name}")
                else:
                    # Service exists, check if configuration is correct
                    # Compare command and args (the most critical parts)
                    if (existing_config.get("command") != correct_config.get("command") or
                        existing_config.get("args") != correct_config.get("args")):
                        needs_update = True
                        fixed_services.append(f"{service_name} in {Path(project_key).name}")

                # Update configuration if needed
                if needs_update:
                    project_config["mcpServers"][service_name] = correct_config
                    updated = True
                    self.logger.debug(
                        f"Updated MCP service config for {service_name} in project {Path(project_key).name}"
                    )

        # Write updated config if changes were made
        if updated:
            try:
                # Create backup if file exists and is large (> 100KB)
                if self.claude_config_path.exists():
                    file_size = self.claude_config_path.stat().st_size
                    if file_size > 100000:  # 100KB
                        backup_path = self.claude_config_path.with_suffix(
                            f".backup.{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
                        )
                        import shutil
                        shutil.copy2(self.claude_config_path, backup_path)
                        self.logger.debug(f"Created backup: {backup_path}")

                # Write updated config
                with open(self.claude_config_path, "w") as f:
                    json.dump(claude_config, f, indent=2)

                messages = []
                if added_services:
                    messages.append(f"Added MCP services: {', '.join(added_services[:3])}")
                if fixed_services:
                    messages.append(f"Fixed MCP services: {', '.join(fixed_services[:3])}")

                if messages:
                    return True, "; ".join(messages)
                return True, "All MCP services already configured correctly"
            except Exception as e:
                self.logger.error(f"Failed to write Claude config: {e}")
                return False, f"Failed to write configuration: {e}"

        return True, "All MCP services already configured correctly"

    def update_mcp_config(self, force_pipx: bool = True) -> Tuple[bool, str]:
        """
        Update the MCP configuration in ~/.claude.json.

        Args:
            force_pipx: If True, only use pipx installations

        Returns:
            Tuple of (success, message)
        """
        # This method now delegates to ensure_mcp_services_configured
        # since we're updating the Claude config directly
        return self.ensure_mcp_services_configured()

    def update_project_mcp_config(self, force_pipx: bool = True) -> Tuple[bool, str]:
        """
        Update the .mcp.json configuration file (legacy method).

        Args:
            force_pipx: If True, only use pipx installations

        Returns:
            Tuple of (success, message)
        """
        mcp_config_path = self.project_root / ConfigLocation.PROJECT_MCP.value

        # Load existing config if it exists
        existing_config = {}
        if mcp_config_path.exists():
            try:
                with open(mcp_config_path) as f:
                    existing_config = json.load(f)
            except Exception as e:
                self.logger.error(f"Error reading existing config: {e}")

        # Generate new configurations
        new_config = {"mcpServers": {}}
        missing_services = []

        for service_name in self.PIPX_SERVICES:
            config = self.generate_service_config(service_name)
            if config:
                new_config["mcpServers"][service_name] = config
            elif force_pipx:
                missing_services.append(service_name)
            # Keep existing config if not forcing pipx
            elif service_name in existing_config.get("mcpServers", {}):
                new_config["mcpServers"][service_name] = existing_config["mcpServers"][
                    service_name
                ]

        # Add any additional services from existing config
        for service_name, config in existing_config.get("mcpServers", {}).items():
            if service_name not in new_config["mcpServers"]:
                new_config["mcpServers"][service_name] = config

        # Write the updated configuration
        try:
            with open(mcp_config_path, "w") as f:
                json.dump(new_config, f, indent=2)

            if missing_services:
                message = f"Updated .mcp.json. Missing services (install via pipx): {', '.join(missing_services)}"
                return True, message
            return True, "Successfully updated .mcp.json with pipx paths"
        except Exception as e:
            return False, f"Failed to update .mcp.json: {e}"

    def validate_configuration(self) -> Dict[str, bool]:
        """
        Validate that all configured MCP services are accessible.

        Returns:
            Dict mapping service names to availability status
        """
        project_key = str(self.project_root)

        # Check Claude config
        if not self.claude_config_path.exists():
            # Also check legacy .mcp.json
            mcp_config_path = self.project_root / ConfigLocation.PROJECT_MCP.value
            if mcp_config_path.exists():
                try:
                    with open(mcp_config_path) as f:
                        config = json.load(f)
                        results = {}
                        for service_name, service_config in config.get(
                            "mcpServers", {}
                        ).items():
                            command_path = service_config.get("command", "")
                            results[service_name] = Path(command_path).exists()
                        return results
                except Exception:
                    pass
            return {}

        try:
            with open(self.claude_config_path) as f:
                claude_config = json.load(f)

            # Get project's MCP servers
            if "projects" in claude_config and project_key in claude_config["projects"]:
                mcp_servers = claude_config["projects"][project_key].get(
                    "mcpServers", {}
                )
                results = {}
                for service_name, service_config in mcp_servers.items():
                    command_path = service_config.get("command", "")
                    results[service_name] = Path(command_path).exists()
                return results
        except Exception as e:
            self.logger.error(f"Error reading config: {e}")

        return {}

    def install_missing_services(self) -> Tuple[bool, str]:
        """
        Install missing MCP services via pipx with verification and fallbacks.

        Returns:
            Tuple of (success, message)
        """
        missing = []
        for service_name in self.PIPX_SERVICES:
            if not self.detect_service_path(service_name):
                missing.append(service_name)

        if not missing:
            return True, "All MCP services are already installed"

        installed = []
        failed = []

        for service_name in missing:
            # Try pipx install first
            success, method = self._install_service_with_fallback(service_name)
            if success:
                installed.append(f"{service_name} ({method})")
                self.logger.info(f"Successfully installed {service_name} via {method}")
            else:
                failed.append(service_name)
                self.logger.error(f"Failed to install {service_name}")

        if failed:
            return False, f"Failed to install: {', '.join(failed)}"
        if installed:
            return True, f"Successfully installed: {', '.join(installed)}"
        return True, "No services needed installation"

    def _install_service_with_fallback(self, service_name: str) -> Tuple[bool, str]:
        """
        Install a service with multiple fallback methods.

        Returns:
            Tuple of (success, installation_method)
        """
        import shutil

        # Method 1: Try pipx install
        if shutil.which("pipx"):
            try:
                self.logger.debug(f"Attempting to install {service_name} via pipx...")
                result = subprocess.run(
                    ["pipx", "install", service_name],
                    capture_output=True,
                    text=True,
                    timeout=120,  # 2 minute timeout
                    check=False,
                )

                if result.returncode == 0:
                    # Verify installation worked
                    if self._verify_service_installed(service_name, "pipx"):
                        return True, "pipx"

                    self.logger.warning(
                        f"pipx install succeeded but verification failed for {service_name}"
                    )
                else:
                    self.logger.debug(f"pipx install failed: {result.stderr}")
            except subprocess.TimeoutExpired:
                self.logger.warning(f"pipx install timed out for {service_name}")
            except Exception as e:
                self.logger.debug(f"pipx install error: {e}")

        # Method 2: Try uvx (if available)
        if shutil.which("uvx"):
            try:
                self.logger.debug(f"Attempting to install {service_name} via uvx...")
                result = subprocess.run(
                    ["uvx", "install", service_name],
                    capture_output=True,
                    text=True,
                    timeout=120,
                    check=False,
                )

                if result.returncode == 0:
                    if self._verify_service_installed(service_name, "uvx"):
                        return True, "uvx"
            except Exception as e:
                self.logger.debug(f"uvx install error: {e}")

        # Method 3: Try pip install --user
        try:
            self.logger.debug(f"Attempting to install {service_name} via pip --user...")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--user", service_name],
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )

            if result.returncode == 0:
                if self._verify_service_installed(service_name, "pip"):
                    return True, "pip --user"

                self.logger.warning(
                    f"pip install succeeded but verification failed for {service_name}"
                )
        except Exception as e:
            self.logger.debug(f"pip install error: {e}")

        return False, "none"

    def _check_and_fix_mcp_ticketer_dependencies(self) -> bool:
        """Check and fix mcp-ticketer missing gql dependency.

        Note: This is a workaround for mcp-ticketer <= 0.1.8 which is missing
        the gql dependency in its package metadata. Future versions (> 0.1.8)
        should include 'gql[httpx]>=3.0.0' as a dependency, making this fix
        unnecessary. We keep this for backward compatibility with older versions.
        """
        try:
            # Test if gql is available in mcp-ticketer's environment
            test_result = subprocess.run(
                ["pipx", "run", "--spec", "mcp-ticketer", "python", "-c", "import gql"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )

            # If import fails, inject the dependency
            if test_result.returncode != 0:
                self.logger.info("🔧 mcp-ticketer missing gql dependency, fixing...")

                inject_result = subprocess.run(
                    ["pipx", "inject", "mcp-ticketer", "gql"],
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False,
                )

                if inject_result.returncode == 0:
                    self.logger.info("✅ Successfully injected gql dependency into mcp-ticketer")
                    return True
                else:
                    self.logger.warning(f"Failed to inject gql: {inject_result.stderr}")
                    return False

            return False

        except Exception as e:
            self.logger.debug(f"Could not check/fix mcp-ticketer dependencies: {e}")
            return False

    def fix_mcp_service_issues(self) -> Tuple[bool, str]:
        """
        Detect and fix corrupted MCP service installations.

        This method:
        1. Tests each MCP service for import/execution errors
        2. Automatically reinstalls corrupted services
        3. Fixes missing dependencies (like mcp-ticketer's gql)
        4. Validates fixes worked

        Returns:
            Tuple of (success, message)
        """
        self.logger.info("🔍 Checking MCP services for issues...")

        services_to_fix = []
        fixed_services = []
        failed_services = []

        # Check each service for issues
        for service_name in self.PIPX_SERVICES:
            issue_type = self._detect_service_issue(service_name)
            if issue_type:
                services_to_fix.append((service_name, issue_type))
                self.logger.debug(f"Found issue with {service_name}: {issue_type}")

        if not services_to_fix:
            return True, "All MCP services are functioning correctly"

        # Fix each problematic service
        for service_name, issue_type in services_to_fix:
            self.logger.info(f"🔧 Fixing {service_name}: {issue_type}")

            if issue_type == "not_installed":
                # Install the service
                success, method = self._install_service_with_fallback(service_name)
                if success:
                    fixed_services.append(f"{service_name} (installed via {method})")
                else:
                    failed_services.append(f"{service_name} (installation failed)")

            elif issue_type == "import_error":
                # Reinstall to fix corrupted installation
                self.logger.info(f"  Reinstalling {service_name} to fix import errors...")
                success = self._reinstall_service(service_name)
                if success:
                    # Special handling for mcp-ticketer - inject missing gql dependency
                    if service_name == "mcp-ticketer":
                        self._check_and_fix_mcp_ticketer_dependencies()
                    fixed_services.append(f"{service_name} (reinstalled)")
                else:
                    failed_services.append(f"{service_name} (reinstall failed)")

            elif issue_type == "missing_dependency":
                # Fix missing dependencies
                if service_name == "mcp-ticketer":
                    if self._check_and_fix_mcp_ticketer_dependencies():
                        fixed_services.append(f"{service_name} (dependency fixed)")
                    else:
                        failed_services.append(f"{service_name} (dependency fix failed)")
                else:
                    failed_services.append(f"{service_name} (unknown dependency issue)")

            elif issue_type == "path_issue":
                # Path issues are handled by config updates
                self.logger.info(f"  Path issue for {service_name} will be fixed by config update")
                fixed_services.append(f"{service_name} (config updated)")

        # Build result message
        messages = []
        if fixed_services:
            messages.append(f"✅ Fixed: {', '.join(fixed_services)}")
        if failed_services:
            messages.append(f"❌ Failed: {', '.join(failed_services)}")

        # Return success if at least some services were fixed
        success = len(fixed_services) > 0 or len(failed_services) == 0
        message = " | ".join(messages) if messages else "No services needed fixing"

        # Provide manual fix instructions if auto-fix failed
        if failed_services:
            message += "\n\n💡 Manual fix instructions:"
            for failed in failed_services:
                service = failed.split(" ")[0]
                message += f"\n  • {service}: pipx uninstall {service} && pipx install {service}"

        return success, message

    def _detect_service_issue(self, service_name: str) -> Optional[str]:
        """
        Detect what type of issue a service has.

        Returns:
            Issue type: 'not_installed', 'import_error', 'missing_dependency', 'path_issue', or None
        """
        import shutil

        # First check if pipx is available
        if not shutil.which("pipx"):
            return "not_installed"  # Can't use pipx services without pipx

        # Try to run the service with --help to detect issues
        try:
            # Test with pipx run
            result = subprocess.run(
                ["pipx", "run", service_name, "--help"],
                capture_output=True,
                text=True,
                timeout=10,
                check=False
            )

            # Check for specific error patterns
            stderr_lower = result.stderr.lower()
            stdout_lower = result.stdout.lower()
            combined_output = stderr_lower + stdout_lower

            # Not installed
            if "no apps associated" in combined_output or "not found" in combined_output:
                return "not_installed"

            # Import errors (like mcp-ticketer's corrupted state)
            if "modulenotfounderror" in combined_output or "importerror" in combined_output:
                # Check if it's specifically the gql dependency for mcp-ticketer
                if service_name == "mcp-ticketer" and "gql" in combined_output:
                    return "missing_dependency"
                return "import_error"

            # Path issues
            if "no such file or directory" in combined_output:
                return "path_issue"

            # If help text appears, service is working
            if "usage:" in combined_output or "help" in combined_output or result.returncode in [0, 1]:
                return None  # Service is working

            # Unknown issue
            if result.returncode not in [0, 1]:
                return "unknown_error"

        except subprocess.TimeoutExpired:
            # Timeout might mean service is actually working but waiting for input
            return None
        except Exception as e:
            self.logger.debug(f"Error detecting issue for {service_name}: {e}")
            return "unknown_error"

        return None

    def _reinstall_service(self, service_name: str) -> bool:
        """
        Reinstall a corrupted MCP service.

        Args:
            service_name: Name of the service to reinstall

        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.debug(f"Uninstalling {service_name}...")

            # First uninstall the corrupted version
            uninstall_result = subprocess.run(
                ["pipx", "uninstall", service_name],
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )

            # Don't check return code - uninstall might fail if partially corrupted
            self.logger.debug(f"Uninstall result: {uninstall_result.returncode}")

            # Now reinstall
            self.logger.debug(f"Installing fresh {service_name}...")
            install_result = subprocess.run(
                ["pipx", "install", service_name],
                capture_output=True,
                text=True,
                timeout=120,
                check=False
            )

            if install_result.returncode == 0:
                # Verify the reinstall worked
                issue = self._detect_service_issue(service_name)
                if issue is None:
                    self.logger.info(f"✅ Successfully reinstalled {service_name}")
                    return True
                else:
                    self.logger.warning(f"Reinstalled {service_name} but still has issue: {issue}")
                    return False
            else:
                self.logger.error(f"Failed to reinstall {service_name}: {install_result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Error reinstalling {service_name}: {e}")
            return False

    def _verify_service_installed(self, service_name: str, method: str) -> bool:
        """
        Verify that a service was successfully installed and is functional.

        Args:
            service_name: Name of the service
            method: Installation method used

        Returns:
            True if service is installed and functional
        """
        import time

        # Give the installation a moment to settle
        time.sleep(1)

        # Note: mcp-ticketer dependency fix is now handled once in ensure_mcp_services_configured()
        # to avoid running the same pipx inject command multiple times

        # Check if we can find the service
        service_path = self.detect_service_path(service_name)
        if not service_path:
            # Try pipx run as fallback for pipx installations
            if method == "pipx":
                try:
                    result = subprocess.run(
                        ["pipx", "run", service_name, "--version"],
                        capture_output=True,
                        text=True,
                        timeout=10,
                        check=False,
                    )
                    if result.returncode == 0 or "version" in result.stdout.lower():
                        self.logger.debug(f"{service_name} accessible via 'pipx run'")
                        return True
                except:
                    pass
            return False

        # Try to verify it works
        try:
            # Different services may need different verification
            test_commands = [
                [service_path, "--version"],
                [service_path, "--help"],
            ]

            for cmd in test_commands:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    check=False,
                )

                output = (result.stdout + result.stderr).lower()
                # Check for signs of success
                if result.returncode == 0:
                    return True
                # Some tools return non-zero but still work
                if any(
                    indicator in output
                    for indicator in ["version", "usage", "help", service_name.lower()]
                ):
                    # Make sure it's not an error message
                    if not any(
                        error in output
                        for error in ["error", "not found", "traceback", "no such"]
                    ):
                        return True
        except Exception as e:
            self.logger.debug(f"Verification error for {service_name}: {e}")

        return False

    def _get_fallback_config(self, service_name: str, project_path: str) -> Optional[Dict]:
        """
        Get a fallback configuration for a service if the primary config fails.

        Args:
            service_name: Name of the MCP service
            project_path: Project path to use

        Returns:
            Fallback configuration or None
        """
        # Special fallback for mcp-vector-search using pipx run
        if service_name == "mcp-vector-search":
            return {
                "type": "stdio",
                "command": "pipx",
                "args": ["run", "--spec", "mcp-vector-search", "python", "-m", "mcp_vector_search.mcp.server", project_path],
                "env": {}
            }

        # For other services, try pipx run
        return None
