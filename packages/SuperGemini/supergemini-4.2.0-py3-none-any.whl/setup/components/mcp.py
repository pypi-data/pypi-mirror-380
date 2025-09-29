"""
MCP component for MCP server configuration via .gemini.json
"""

import json
import shutil
import time
import sys
import subprocess
import os
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path

# Platform-specific file locking imports
try:
    if sys.platform == "win32":
        import msvcrt
        LOCKING_AVAILABLE = "windows"
    else:
        import fcntl
        LOCKING_AVAILABLE = "unix"
except ImportError:
    LOCKING_AVAILABLE = None

from ..core.base import Component
from ..utils.ui import display_info, display_warning


class MCPComponent(Component):
    """MCP servers configuration component"""
    
    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize MCP component"""
        super().__init__(install_dir)
        
        # Define MCP servers available for configuration
        self.mcp_servers = {
            "context7": {
                "name": "context7",
                "description": "Official library documentation and code examples",
                "config_file": "context7.json",
                "npm_package": "@upstash/context7-mcp@latest",
                "requires_api_key": False
            },
            "sequential": {
                "name": "sequential-thinking", 
                "description": "Multi-step problem solving and systematic analysis",
                "config_file": "sequential.json",
                "npm_package": "@modelcontextprotocol/server-sequential-thinking",
                "requires_api_key": False
            },
            "magic": {
                "name": "magic",
                "description": "Modern UI component generation and design systems",
                "config_file": "magic.json",
                "npm_package": "@21st-dev/magic",
                "requires_api_key": True,
                "api_key_env": "TWENTYFIRST_API_KEY"
            },
            "playwright": {
                "name": "playwright",
                "description": "Cross-browser E2E testing and automation",
                "config_file": "playwright.json",
                "npm_package": "@playwright/mcp@latest", 
                "requires_api_key": False
            },
            "serena": {
                "name": "serena",
                "description": "Semantic code analysis and intelligent editing",
                "config_file": "serena.json",
                "install_method": "uv",
                "uv_package": "git+https://github.com/oraios/serena",
                "requires_api_key": False
            },
            "morphllm": {
                "name": "morphllm-fast-apply",
                "description": "Fast Apply capability for context-aware code modifications",
                "config_file": "morphllm.json",
                "npm_package": "@morph-llm/morph-fast-apply",
                "requires_api_key": True,
                "api_key_env": "MORPH_API_KEY"
            },
            "superagent": {
                "name": "superagent",
                "description": "Agent orchestration server for Gemini and Codex workflows",
                "config_file": "superagent.json",
                "npm_package": "@superclaude-org/superagent",
                "requires_api_key": False
            },
        }
        
        # This will be set during installation - initialize as empty list
        self.selected_servers: List[str] = []
        
        # Store collected API keys for configuration
        self.collected_api_keys: Dict[str, str] = {}
    
    def _lock_file(self, file_handle, exclusive: bool = False):
        """Cross-platform file locking with error handling"""
        try:
            if LOCKING_AVAILABLE == "unix":
                lock_type = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
                fcntl.flock(file_handle.fileno(), lock_type)
            elif LOCKING_AVAILABLE == "windows":
                # Windows locking using msvcrt with retry logic
                if exclusive:
                    try:
                        msvcrt.locking(file_handle.fileno(), msvcrt.LK_NBLCK, 1)
                    except OSError:
                        # If non-blocking lock fails, fall back to no locking
                        self.logger.debug("File locking failed, proceeding without lock")
            # If no locking available, continue without locking
        except Exception as e:
            self.logger.debug(f"File locking error (non-critical): {e}")
    
    def _unlock_file(self, file_handle):
        """Cross-platform file unlocking with error handling"""
        try:
            if LOCKING_AVAILABLE == "unix":
                fcntl.flock(file_handle.fileno(), fcntl.LOCK_UN)
            elif LOCKING_AVAILABLE == "windows":
                msvcrt.locking(file_handle.fileno(), msvcrt.LK_UNLCK, 1)
            # If no locking available, continue without unlocking
        except Exception as e:
            self.logger.debug(f"File unlocking error (non-critical): {e}")
    
    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        from .. import __version__
        return {
            "name": "mcp",
            "version": __version__,
            "description": "MCP server configuration management via .gemini.json",
            "category": "integration"
        }
    
    def set_selected_servers(self, selected_servers: List[str]) -> None:
        """Set which MCP servers were selected for configuration"""
        self.selected_servers = selected_servers
        self.logger.debug(f"MCP servers to configure: {selected_servers}")
    
    def validate_prerequisites(self, installSubPath: Optional[Path] = None) -> Tuple[bool, List[str]]:
        """
        Check prerequisites for MCP component
        """
        errors = []
        
        # Check if config source directory exists
        source_dir = self._get_config_source_dir()
        if not source_dir or not source_dir.exists():
            errors.append(f"MCP config source directory not found: {source_dir}")
            return False, errors
        
        # Check if user's Gemini settings directory exists
        settings_path = self.install_dir / "settings.json"
        if not settings_path.parent.exists():
            errors.append(f"Gemini settings directory not found: {settings_path.parent}")
            errors.append("Please ensure Gemini is properly configured")
        elif not settings_path.exists():
            # Create empty settings.json if directory exists but file doesn't
            try:
                settings_path.write_text('{}')
                self.logger.debug(f"Created empty settings.json at {settings_path}")
            except Exception as e:
                errors.append(f"Could not create settings.json: {e}")
        
        return len(errors) == 0, errors
    
    def get_files_to_install(self) -> List[Tuple[Path, Path]]:
        """MCP component doesn't install files - it modifies .gemini.json"""
        return []
    
    def _get_config_source_dir(self) -> Optional[Path]:
        """Get source directory for MCP config files"""
        project_root = Path(__file__).parent.parent.parent
        config_dir = project_root / "SuperGemini" / "MCP" / "configs"
        
        if not config_dir.exists():
            return None
        
        return config_dir
    
    def _get_source_dir(self) -> Optional[Path]:
        """Override parent method - MCP component doesn't use traditional file installation"""
        return self._get_config_source_dir()
    
    def _load_gemini_config(self) -> Tuple[Optional[Dict], Path]:
        """Load user's Gemini configuration with file locking"""
        settings_path = self.install_dir / "settings.json"
        
        try:
            with open(settings_path, 'r') as f:
                # Apply shared lock for reading
                self._lock_file(f, exclusive=False)
                try:
                    config = json.load(f)
                    return config, settings_path
                finally:
                    self._unlock_file(f)
        except Exception as e:
            self.logger.error(f"Failed to load Gemini configuration: {e}")
            return None, settings_path
    
    def _save_gemini_config(self, config: Dict, config_path: Path) -> bool:
        """Save user's Gemini configuration with backup and improved error handling"""
        max_retries = 3
        retry_delay = 0.1
        
        for attempt in range(max_retries):
            try:
                # Create backup first (if file exists and is not empty)
                if config_path.exists() and config_path.stat().st_size > 2:
                    backup_path = config_path.with_suffix('.json.backup')
                    shutil.copy2(config_path, backup_path)
                    self.logger.debug(f"Created backup: {backup_path}")
                
                # Try simple write first (no locking for problematic cases)
                try:
                    with open(config_path, 'w') as f:
                        json.dump(config, f, indent=2)
                        f.flush()
                    
                    self.logger.debug("Updated Gemini configuration")
                    return True
                    
                except (OSError, IOError, PermissionError) as e:
                    if attempt < max_retries - 1:
                        self.logger.warning(f"Write attempt {attempt + 1} failed, retrying: {e}")
                        time.sleep(retry_delay * (2 ** attempt))
                        continue
                    else:
                        # Final attempt with file locking
                        self.logger.debug("Trying with file locking as last resort")
                        with open(config_path, 'w') as f:
                            self._lock_file(f, exclusive=True)
                            try:
                                json.dump(config, f, indent=2)
                                f.flush()
                            finally:
                                self._unlock_file(f)
                        
                        self.logger.debug("Updated Gemini configuration with locking")
                        return True
                
            except (OSError, IOError) as e:
                if attempt < max_retries - 1:
                    self.logger.warning(f"File lock attempt {attempt + 1} failed, retrying: {e}")
                    time.sleep(retry_delay * (2 ** attempt))  # Exponential backoff
                    continue
                else:
                    self.logger.error(f"Failed to save Gemini config after {max_retries} attempts: {e}")
                    return False
            except Exception as e:
                self.logger.error(f"Failed to save Gemini config: {e}")
                return False
        
        return False
    
    def _merge_mcp_server_config(self, existing_config: Dict, new_config: Dict, server_key: str) -> None:
        """Precisely merge MCP server config, preserving user customizations
        
        Args:
            existing_config: User's current mcpServers configuration
            new_config: New MCP server configuration to merge
            server_key: Server key for logging purposes
        """
        for server_name, server_def in new_config.items():
            if server_name in existing_config:
                # Server already exists - preserve user customizations
                existing_server = existing_config[server_name]
                
                # Only add missing keys, never overwrite existing ones
                for key, value in server_def.items():
                    if key not in existing_server:
                        existing_server[key] = value
                        self.logger.debug(f"Added missing key '{key}' to existing server '{server_name}'")
                    else:
                        self.logger.debug(f"Preserved user customization for '{server_name}.{key}'")
                
                # NEW: Apply environment variable references for API keys
                if "env" in existing_server and self.collected_api_keys:
                    for env_key, env_value in existing_server["env"].items():
                        if env_key in self.collected_api_keys and env_value == "":
                            # Update to use environment variable reference
                            existing_server["env"][env_key] = f"${{{env_key}}}"
                            self.logger.info(f"Configured {env_key} to use environment variable")
                
                self.logger.info(f"Updated existing MCP server '{server_name}' (preserved user customizations)")
            else:
                # New server - add complete configuration
                # Apply environment variable references if we have collected keys
                if "env" in server_def and self.collected_api_keys:
                    for env_key in server_def["env"]:
                        if env_key in self.collected_api_keys and server_def["env"][env_key] == "":
                            server_def["env"][env_key] = f"${{{env_key}}}"
                
                existing_config[server_name] = server_def
                self.logger.info(f"Added new MCP server '{server_name}' from {server_key}")
    
    def _load_mcp_server_config(self, server_key: str) -> Optional[Dict]:
        """Load MCP server configuration snippet"""
        if server_key not in self.mcp_servers:
            return None
        
        server_info = self.mcp_servers[server_key]
        config_file = server_info["config_file"]
        config_source_dir = self._get_config_source_dir()
        
        if not config_source_dir:
            return None
        
        config_path = config_source_dir / config_file
        
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load MCP config for {server_key}: {e}")
            return None
    
    def _install_mcp_server_package(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Install MCP server package (supports both npm and uv methods)"""
        install_method = server_info.get("install_method", "npm")
        
        if install_method == "uv":
            return self._install_uv_package(server_key, server_info)
        else:
            return self._install_npm_package(server_key, server_info)
    
    def _install_npm_package(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Install npm package for MCP server"""
        npm_package = server_info.get("npm_package")
        if not npm_package:
            self.logger.error(f"No npm package defined for {server_key}")
            return False
        
        try:
            self.logger.info(f"Installing npm package: {npm_package}")
            
            result = subprocess.run(
                ["npm", "install", "-g", npm_package],
                capture_output=True,
                text=True,
                timeout=180,
                shell=(sys.platform == "win32")
            )
            
            if result.returncode == 0:
                self.logger.info(f"Successfully installed: {npm_package}")
                return True
            else:
                self.logger.error(f"npm install failed for {npm_package}: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error(f"npm install timeout for {npm_package}")
            return False
        except Exception as e:
            self.logger.error(f"Installation error for {server_key}: {e}")
            return False
    
    def _install_uv_package(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Install uv package for Python-based MCP server (like Serena)"""
        uv_package = server_info.get("uv_package")
        if not uv_package:
            self.logger.error(f"No uv package defined for {server_key}")
            return False
        
        try:
            self.logger.info(f"Installing uv package: {uv_package}")
            
            # Install using uv tool install with correct package name (serena-agent)
            result = subprocess.run(
                ["uv", "tool", "install", "--from", uv_package, "serena-agent"],
                capture_output=True,
                text=True,
                timeout=300,
                shell=(sys.platform == "win32")
            )
            
            if result.returncode == 0:
                self.logger.info(f"Successfully installed: {uv_package}")
                return True
            else:
                self.logger.error(f"uv install failed for {uv_package}: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error(f"uv install timeout for {uv_package}")
            return False
        except Exception as e:
            self.logger.error(f"Installation error for {server_key}: {e}")
            return False
    
    def _verify_mcp_installation(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Verify installed MCP server package"""
        install_method = server_info.get("install_method", "npm")
        
        if install_method == "uv":
            return self._verify_uv_installation(server_key, server_info)
        else:
            return self._verify_npm_installation(server_key, server_info)
    
    def _verify_npm_installation(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Verify npm package installation"""
        npm_package = server_info.get("npm_package")
        if not npm_package:
            return False
        
        try:
            result = subprocess.run(
                ["npm", "list", "-g", npm_package.split('@')[0]],
                capture_output=True,
                text=True,
                timeout=30,
                shell=(sys.platform == "win32")
            )
            
            if result.returncode == 0:
                self.logger.info(f"Verified installation: {server_key}")
                return True
            else:
                self.logger.warning(f"Package verification failed: {npm_package}")
                return False
                
        except Exception as e:
            self.logger.error(f"Verification failed for {server_key}: {e}")
            return False
    
    def _verify_uv_installation(self, server_key: str, server_info: Dict[str, Any]) -> bool:
        """Verify uv package installation"""
        try:
            # Check if uv tool is installed
            result = subprocess.run(
                ["uv", "tool", "list"],
                capture_output=True,
                text=True,
                timeout=30,
                shell=(sys.platform == "win32")
            )
            
            if result.returncode == 0 and ("serena" in result.stdout or "serena-agent" in result.stdout):
                self.logger.info(f"Verified installation: {server_key}")
                return True
            else:
                self.logger.warning(f"uv tool verification failed for {server_key}")
                return False
                
        except Exception as e:
            self.logger.error(f"Verification failed for {server_key}: {e}")
            return False
    
    def _find_executable_with_fallbacks(self, executable: str) -> Optional[str]:
        """Find executable with fallback locations for common version managers and pipx environments"""
        which_path = shutil.which(executable)
        if which_path:
            return which_path

        search_dirs: List[Path] = [
            Path.home() / ".asdf" / "shims",
            Path.home() / ".nvm" / "current" / "bin",
            Path.home() / ".volta" / "bin",
            Path.home() / ".fnm" / "current" / "bin",
            Path.home() / ".local" / "bin",
            Path.home() / "bin",
            Path("/usr/local/bin"),
            Path("/usr/bin"),
            Path.home() / ".cargo" / "bin",
        ]

        if sys.platform == "darwin":
            search_dirs.append(Path("/opt/homebrew/bin"))

        if sys.platform == "win32":
            search_dirs.extend([
                Path("C:/Program Files/nodejs"),
                Path("C:/Program Files (x86)/nodejs"),
                Path.home() / "AppData" / "Local" / "uv" / "bin",
            ])

        nvm_versions_dir = Path.home() / ".nvm" / "versions" / "node"
        if nvm_versions_dir.exists():
            for version_dir in nvm_versions_dir.iterdir():
                bin_dir = version_dir / "bin"
                if bin_dir.is_dir():
                    search_dirs.append(bin_dir)

        unique_dirs: List[Path] = []
        seen_dirs = set()
        for directory in search_dirs:
            if directory not in seen_dirs:
                seen_dirs.add(directory)
                unique_dirs.append(directory)

        for directory in unique_dirs:
            candidates = [directory / executable]
            if sys.platform == "win32" and not executable.endswith(".exe"):
                candidates.append(directory / f"{executable}.exe")

            for path in candidates:
                if path.exists() and path.is_file():
                    self.logger.debug(f"Found {executable} at fallback location: {path}")
                    return str(path)

        return None
    
    def _get_expanded_env(self) -> Dict[str, str]:
        """Get environment with expanded PATH including common tool locations"""
        env = os.environ.copy()
        
        # Additional paths to check for tools
        additional_paths = [
            str(Path.home() / ".asdf" / "shims"),
            str(Path.home() / ".nvm" / "current" / "bin"),
            str(Path.home() / ".volta" / "bin"),
            str(Path.home() / ".fnm" / "current" / "bin"),
            str(Path.home() / ".local" / "bin"),
            str(Path.home() / "bin"),
            str(Path.home() / ".cargo" / "bin"),
            "/usr/local/bin",
            "/usr/bin",
        ]
        
        # macOS specific
        if sys.platform == "darwin":
            additional_paths.append("/opt/homebrew/bin")
        
        # Windows specific
        if sys.platform == "win32":
            additional_paths.extend([
                "C:\\Program Files\\nodejs",
                "C:\\Program Files (x86)\\nodejs",
                str(Path.home() / "AppData" / "Local" / "uv" / "bin"),
            ])

        nvm_versions_dir = Path.home() / ".nvm" / "versions" / "node"
        if nvm_versions_dir.exists():
            for version_dir in nvm_versions_dir.iterdir():
                bin_dir = version_dir / "bin"
                if bin_dir.is_dir():
                    additional_paths.append(str(bin_dir))
        
        # Only add paths that actually exist
        existing_paths = [p for p in additional_paths if Path(p).exists()]
        
        # Expand PATH
        current_path = env.get("PATH", "")
        expanded_path = os.pathsep.join([current_path] + existing_paths)
        env["PATH"] = expanded_path
        
        return env
    
    def _run_command_with_fallbacks(self, command: List[str], timeout: int = 10) -> Optional[subprocess.CompletedProcess]:
        """Run command with fallback executable detection and expanded PATH"""
        executable = command[0]
        
        # First try to find executable with fallbacks
        executable_path = self._find_executable_with_fallbacks(executable)
        
        if executable_path:
            # Replace the executable in command with full path
            command_with_path = [executable_path] + command[1:]
            try:
                # Try with full path first
                result = subprocess.run(command_with_path, capture_output=True, text=True, timeout=timeout)
                if result.returncode == 0:
                    return result
            except Exception:
                pass
        
        # Try with expanded environment
        try:
            env = self._get_expanded_env()
            result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, env=env)
            if result.returncode == 0:
                return result
        except Exception:
            pass
        
        # Final attempt with shell=True as fallback
        try:
            result = subprocess.run(" ".join(command), capture_output=True, text=True, timeout=timeout, shell=True)
            return result
        except Exception:
            return None

    def _validate_prerequisites(self) -> Tuple[bool, List[str]]:
        """Validate Gemini environment, npm and uv prerequisites with enhanced PATH detection"""
        errors = []
        
        # Check Node.js version (>=18 required for MCP) with enhanced detection
        result = self._run_command_with_fallbacks(["node", "--version"])
        if result and result.returncode == 0:
            version = result.stdout.strip().lstrip('v')
            try:
                major_version = int(version.split('.')[0])
                if major_version < 18:
                    errors.append(f"Node.js {version} found, but 18+ required for MCP")
                else:
                    self.logger.debug(f"Node.js {version} OK")
            except ValueError:
                errors.append(f"Could not parse Node.js version: {version}")
        else:
            # Try to provide helpful message for pipx users
            node_path = self._find_executable_with_fallbacks("node")
            if node_path:
                errors.append(f"Node.js found at {node_path} but couldn't execute properly")
            else:
                errors.append("Node.js not found - required for MCP server installation")
                if "pipx" in sys.executable or "/.local/pipx/" in sys.executable:
                    errors.append("Note: Running in pipx environment. Ensure Node.js is in system PATH")
        
        # Check npm availability with enhanced detection
        result = self._run_command_with_fallbacks(["npm", "--version"])
        if result and result.returncode == 0:
            self.logger.debug(f"npm {result.stdout.strip()} OK")
        else:
            npm_path = self._find_executable_with_fallbacks("npm")
            if npm_path:
                errors.append(f"npm found at {npm_path} but couldn't execute properly")
            else:
                errors.append("npm not found - required for MCP server installation")
        
        # Check uv availability (for Python-based MCP servers like Serena) with enhanced detection
        result = self._run_command_with_fallbacks(["uv", "--version"])
        if result and result.returncode == 0:
            self.logger.debug(f"uv {result.stdout.strip()} OK")
        else:
            uv_path = self._find_executable_with_fallbacks("uv")
            if uv_path:
                self.logger.warning(f"uv found at {uv_path} but couldn't execute - Python MCP servers (Serena) will be skipped")
            else:
                self.logger.warning("uv not found - Python MCP servers (Serena) will be skipped")
        
        return len(errors) == 0, errors
    
    def _install(self, config: Dict[str, Any]) -> bool:
        """Install MCP component: npm packages + Gemini configuration (v3 + v4 hybrid)"""
        self.logger.info("Installing MCP servers for Gemini...")
        
        # Get selected servers from config
        selected_servers = config.get("selected_mcp_servers", [])
        if not selected_servers:
            self.logger.info("No MCP servers selected - skipping MCP installation")
            self.set_selected_servers([])
            return self._post_install()
        
        self.set_selected_servers(selected_servers)
        
        # Log collected API keys information
        if hasattr(self, 'collected_api_keys') and self.collected_api_keys:
            self.logger.info(f"Using {len(self.collected_api_keys)} collected API keys for configuration")
        
        # Validate Node.js and npm prerequisites (NEW from v3)
        success, errors = self._validate_prerequisites()
        if not success:
            for error in errors:
                self.logger.error(error)
            return False
        
        # Validate basic prerequisites
        success, errors = self.validate_prerequisites()
        if not success:
            for error in errors:
                self.logger.error(error)
            return False
        
        # Phase 1: Install npm packages (NEW - v3 logic)
        installed_count = 0
        failed_servers = []
        
        for server_key in selected_servers:
            if server_key not in self.mcp_servers:
                self.logger.warning(f"Unknown MCP server: {server_key}")
                failed_servers.append(server_key)
                continue
            
            server_info = self.mcp_servers[server_key]
            
            # Step 1: Install actual npm package
            if not self._install_mcp_server_package(server_key, server_info):
                self.logger.error(f"Failed to install npm package for {server_key}")
                failed_servers.append(server_key)
                continue
            
            # Step 2: Verify installation
            if not self._verify_mcp_installation(server_key, server_info):
                self.logger.warning(f"Installation verification failed for {server_key}")
                # Continue anyway as package might still work
            
            installed_count += 1
            self.logger.info(f"Successfully installed MCP server: {server_info['name']}")
        
        if installed_count == 0:
            self.logger.error("No MCP servers were successfully installed")
            return False
        
        # Phase 2: Configure settings.json (v4 logic)
        gemini_config, config_path = self._load_gemini_config()
        if gemini_config is None:
            self.logger.error("Failed to load Gemini configuration for setup")
            return False
        
        # Ensure mcpServers and _disabledMcpServers sections exist
        if "mcpServers" not in gemini_config:
            gemini_config["mcpServers"] = {}
        if "_disabledMcpServers" not in gemini_config:
            gemini_config["_disabledMcpServers"] = {}
        
        # Configure only successfully installed servers
        configured_count = 0
        for server_key in selected_servers:
            if server_key in failed_servers:
                continue  # Skip failed installations
            
            server_info = self.mcp_servers[server_key]
            server_config = self._load_mcp_server_config(server_key)
            
            if server_config is None:
                self.logger.error(f"Failed to load configuration for {server_key}")
                continue
            
            # Handle API key requirements
            if server_info.get("requires_api_key", False):
                api_key_env = server_info.get("api_key_env")
                if api_key_env:
                    display_info(f"Server '{server_key}' requires API key: {api_key_env}")
                    display_info("You can set this environment variable later")
            
            # Always enable newly managed servers by default
            target_section = "mcpServers"

            # If the server was previously disabled, remove the stale entry
            if server_key in gemini_config.get("_disabledMcpServers", {}):
                try:
                    del gemini_config["_disabledMcpServers"][server_key]
                except KeyError:
                    pass

            # Merge server config into active section
            self._merge_mcp_server_config(gemini_config[target_section], server_config, server_key)
            configured_count += 1

            self.logger.debug(f"Server '{server_key}' installed as enabled")
        
        # Save updated configuration
        if configured_count > 0:
            success = self._save_gemini_config(gemini_config, config_path)
            if not success:
                self.logger.error("Failed to save Gemini configuration")
                return False
        
        # Report results
        if failed_servers:
            self.logger.warning(f"Failed to install: {', '.join(failed_servers)}")
        
        if configured_count > 0:
            self.logger.success(f"Successfully installed and configured {configured_count} MCP servers")
            return self._post_install()
        else:
            self.logger.error("No MCP servers were successfully configured")
            return False
    
    def _post_install(self) -> bool:
        """Post-installation tasks"""
        try:
            # Update metadata
            from .. import __version__
            metadata_mods = {
                "components": {
                    "mcp": {
                        "version": __version__,
                        "installed": True,
                        "servers_configured": len(self.selected_servers),
                        "configured_servers": self.selected_servers
                    }
                }
            }
            self.settings_manager.update_metadata(metadata_mods)
            self.logger.info("Updated metadata with MCP component registration")
            
            # Add component registration
            self.settings_manager.add_component_registration("mcp", {
                "version": __version__,
                "category": "integration",
                "servers_configured": len(self.selected_servers),
                "configured_servers": self.selected_servers
            })
            self.logger.info("Registered MCP component in metadata")
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False
    
    def uninstall(self) -> bool:
        """Uninstall MCP component by removing servers from .gemini.json"""
        try:
            self.logger.info("Removing MCP server configurations...")
            
            # Load Gemini configuration
            gemini_config, config_path = self._load_gemini_config()
            if gemini_config is None:
                self.logger.warning("Could not load Gemini configuration for cleanup")
                return True  # Not a failure if config doesn't exist
            
            if "mcpServers" not in gemini_config:
                self.logger.info("No MCP servers configured")
                return True
            
            # Only remove servers that were installed by SuperGemini
            removed_count = 0
            installed_servers = self._get_installed_servers()
            
            for server_name in installed_servers:
                if server_name in gemini_config["mcpServers"]:
                    # Check if this server was installed by SuperGemini by comparing with our configs
                    if self._is_supergemini_managed_server(gemini_config["mcpServers"][server_name], server_name):
                        del gemini_config["mcpServers"][server_name]
                        removed_count += 1
                        self.logger.debug(f"Removed SuperGemini-managed MCP server: {server_name}")
                    else:
                        self.logger.info(f"Preserved user-customized MCP server: {server_name}")
            
            # Save updated configuration
            if removed_count > 0:
                success = self._save_gemini_config(gemini_config, config_path)
                if not success:
                    self.logger.warning("Failed to save updated Gemini configuration")
            
            # Update settings.json
            try:
                if self.settings_manager.is_component_installed("mcp"):
                    self.settings_manager.remove_component_registration("mcp")
                    self.logger.info("Removed MCP component from settings.json")
            except Exception as e:
                self.logger.warning(f"Could not update settings.json: {e}")
            
            if removed_count > 0:
                self.logger.success(f"MCP component uninstalled ({removed_count} SuperGemini-managed servers removed)")
            else:
                self.logger.info("MCP component uninstalled (no SuperGemini-managed servers to remove)")
            return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during MCP uninstallation: {e}")
            return False
    
    def _get_installed_servers(self) -> List[str]:
        """Get list of servers that were installed by SuperGemini"""
        try:
            metadata = self.settings_manager.get_metadata_setting("components")
            if metadata and "mcp" in metadata:
                return metadata["mcp"].get("configured_servers", [])
        except Exception:
            pass
        return []
    
    def _is_supergemini_managed_server(self, server_config: Dict, server_name: str) -> bool:
        """Check if a server configuration matches SuperGemini's templates
        
        This helps determine if a server was installed by SuperGemini or manually
        configured by the user, allowing us to preserve user customizations.
        """
        # Find the server key that maps to this server name
        server_key = None
        for key, info in self.mcp_servers.items():
            if info["name"] == server_name:
                server_key = key
                break
        
        if not server_key:
            return False  # Unknown server, don't remove
        
        # Load our template config for comparison
        template_config = self._load_mcp_server_config(server_key)
        if not template_config or server_name not in template_config:
            return False
        
        template_server = template_config[server_name]
        
        # Check if the current config has the same structure as our template
        # If user has customized it, the structure might be different
        required_keys = {"command", "args"}
        
        # Check if all required keys exist and match our template
        for key in required_keys:
            if key not in server_config or key not in template_server:
                return False
            # For command and basic structure, they should match our template
            if key == "command" and server_config[key] != template_server[key]:
                return False
        
        return True
    
    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return ["core"]
    
    def get_size_estimate(self) -> int:
        """Get estimated size - minimal since we only modify config"""
        return 4096  # 4KB - just config modifications
