import hashlib
import os
from typing import Optional, Any

from ..core.interfaces import EnvironmentExecutor, PackageManagerDetector
from ..executors.host_executor import HostExecutor


class PipDetector(PackageManagerDetector):
    """Detector for Python packages managed by pip."""

    NAME = "pip"

    def __init__(self, venv_path: Optional[str] = None, debug: bool = False):
        self.explicit_venv_path = venv_path
        self.debug = debug
        self._cached_venv_path: str | None = None
        self._venv_path_searched = False
        self._cached_pip_command: str | None = None

    def is_usable(self, executor: EnvironmentExecutor, working_dir: Optional[str] = None) -> bool:
        """Check if pip is usable in the environment."""
        _, _, exit_code = executor.execute_command("pip --version", working_dir)
        return exit_code == 0

    def get_dependencies(
        self, executor: EnvironmentExecutor, working_dir: Optional[str] = None, skip_hash_collection: bool = False
    ) -> dict[str, Any]:
        """Extract pip dependencies with versions from multiple locations.

        Uses 'pip list --format=freeze' for clean package==version format.
        Returns single location structure or nested structure for mixed locations.
        See docs/technical/detectors/pip_detector.md
        """
        # Collect dependencies from both venv and system locations
        venv_result = self._get_venv_dependencies(executor, working_dir, skip_hash_collection)
        system_result = self._get_system_dependencies(executor, working_dir, skip_hash_collection)

        # Determine output structure based on what was found
        if venv_result and system_result:
            # Mixed case - use new nested structure
            locations = {}

            # Add venv location
            venv_location_data = {"scope": "project", "dependencies": venv_result["dependencies"]}
            if "hash" in venv_result:
                venv_location_data["hash"] = venv_result["hash"]
            locations[venv_result["location"]] = venv_location_data

            # Add system location
            system_location_data = {"scope": "system", "dependencies": system_result["dependencies"]}
            if "hash" in system_result:
                system_location_data["hash"] = system_result["hash"]
            locations[system_result["location"]] = system_location_data

            return {"scope": "mixed", "locations": locations}
        elif venv_result:
            # Only venv - use single location structure
            return venv_result
        elif system_result:
            # Only system - use single location structure
            return system_result
        else:
            # No packages found - return empty result
            if working_dir:
                location = self._resolve_absolute_path(executor, working_dir)
                return {"scope": "project", "location": location, "dependencies": {}}
            else:
                return {"scope": "system", "location": "/usr/lib/python3/dist-packages", "dependencies": {}}

    def _get_venv_dependencies(
        self, executor: EnvironmentExecutor, working_dir: Optional[str] = None, skip_hash_collection: bool = False
    ) -> dict[str, Any] | None:
        """Get dependencies from virtual environment if it exists."""
        venv_path = self._find_venv_path(executor, working_dir)
        if not venv_path:
            return None

        venv_pip = f"{venv_path}/bin/pip"
        if not executor.path_exists(venv_pip):
            return None

        stdout, _, exit_code = executor.execute_command(f"{venv_pip} list --format=freeze", working_dir)
        if exit_code != 0:
            return None

        dependencies = {}
        for line in stdout.strip().split("\n"):
            if line and "==" in line:
                package_name, version = line.split("==", 1)
                package_name = package_name.strip()
                version = version.strip()
                dependencies[package_name] = {"version": version}

        if not dependencies:
            return None

        # Get venv location
        location_stdout, _, location_exit_code = executor.execute_command(f"{venv_pip} show pip", working_dir)
        location = "/usr/lib/python3/dist-packages"  # fallback
        if location_exit_code == 0:
            for line in location_stdout.split("\n"):
                if line.startswith("Location:"):
                    location = line.split(":", 1)[1].strip()
                    break

        result: dict[str, Any] = {"scope": "project", "location": location}
        if not skip_hash_collection:
            result["hash"] = self._generate_location_hash(executor, location)
        result["dependencies"] = dependencies
        return result

    def _get_system_dependencies(
        self, executor: EnvironmentExecutor, working_dir: Optional[str] = None, skip_hash_collection: bool = False
    ) -> dict[str, Any] | None:
        """Get dependencies from system pip installation."""
        # Check if we have a venv - we need to work around it to get system packages
        venv_path = self._find_venv_path(executor, working_dir)

        # Try different approaches to get system packages
        system_commands = [
            # Method 1: Deactivate any virtual env and use system python
            "unset VIRTUAL_ENV && unset PYTHONPATH && /usr/bin/python3 -m pip list --format=freeze 2>/dev/null || /usr/bin/pip3 list --format=freeze 2>/dev/null || pip list --format=freeze",
            # Method 2: Use system python directly
            "/usr/bin/python3 -m pip list --format=freeze",
            # Method 3: Use system pip directly
            "/usr/bin/pip3 list --format=freeze",
            # Method 4: Fallback to regular pip (might be system)
            "pip list --format=freeze",
        ]

        stdout = ""
        for cmd in system_commands:
            stdout, _, exit_code = executor.execute_command(cmd, working_dir)
            if exit_code == 0 and stdout.strip():
                break
        else:
            return None

        # Get system location
        location_commands = [
            "unset VIRTUAL_ENV && unset PYTHONPATH && /usr/bin/python3 -m pip show pip 2>/dev/null || /usr/bin/pip3 show pip 2>/dev/null || pip show pip",
            "/usr/bin/python3 -m pip show pip",
            "/usr/bin/pip3 show pip",
            "pip show pip",
        ]

        location = "/usr/lib/python3/dist-packages"  # fallback
        for cmd in location_commands:
            location_stdout, _, location_exit_code = executor.execute_command(cmd, working_dir)
            if location_exit_code == 0:
                for line in location_stdout.split("\n"):
                    if line.startswith("Location:"):
                        potential_location = line.split(":", 1)[1].strip()
                        # Only use if it looks like a system location
                        if self._is_system_location(potential_location):
                            location = potential_location
                            break
                break

        # If we have a venv and the location doesn't look like system, we might have gotten venv packages
        # In that case, we shouldn't return system dependencies
        if venv_path and not self._is_system_location(location):
            return None

        dependencies = {}
        for line in stdout.strip().split("\n"):
            if line and "==" in line:
                package_name, version = line.split("==", 1)
                package_name = package_name.strip()
                version = version.strip()
                dependencies[package_name] = {"version": version}

        if not dependencies:
            return None

        result: dict[str, Any] = {"scope": "system", "location": location}
        if not skip_hash_collection:
            result["hash"] = self._generate_location_hash(executor, location)
        result["dependencies"] = dependencies
        return result

    def _is_system_location(self, location: str) -> bool:
        """Check if a location path represents a system-wide installation."""
        return location.startswith(("/usr/lib", "/usr/local/lib"))

    def _get_pip_location(self, executor: EnvironmentExecutor, working_dir: Optional[str] = None) -> str:
        """Get the actual location path of the pip environment."""
        pip_command = self._get_pip_command(executor, working_dir)
        stdout, _, exit_code = executor.execute_command(f"{pip_command} show pip", working_dir)

        if exit_code == 0:
            for line in stdout.split("\n"):
                if line.startswith("Location:"):
                    location = line.split(":", 1)[1].strip()
                    return location

        # Fallback: return a default system location when pip location cannot be determined
        return "/usr/lib/python3/dist-packages"

    def _get_pip_command(self, executor: EnvironmentExecutor, working_dir: Optional[str] = None) -> str:
        """Get the appropriate pip command, activating venv if available."""
        if hasattr(self, "_cached_pip_command") and self._cached_pip_command:
            return self._cached_pip_command

        venv_path = self._find_venv_path(executor, working_dir)
        if venv_path:
            venv_pip = f"{venv_path}/bin/pip"
            if executor.path_exists(venv_pip):
                self._cached_pip_command = venv_pip
                return venv_pip

        self._cached_pip_command = "pip"
        return "pip"

    def _validate_venv_path(self, executor: EnvironmentExecutor, path: str) -> str | None:
        """Check if a path contains pyvenv.cfg and return the venv path if valid."""
        pyvenv_cfg_path = f"{path}/pyvenv.cfg"
        if executor.path_exists(pyvenv_cfg_path):
            self._cached_venv_path = path
            self._venv_path_searched = True
            return path
        return None

    def _find_venv_path(self, executor: EnvironmentExecutor, working_dir: Optional[str] = None) -> str | None:
        """Find virtual environment using priority-based search for pyvenv.cfg files."""
        # Return cached result if already searched
        if self._venv_path_searched:
            return self._cached_venv_path

        # 1. Explicit venv path (highest priority) - check immediately
        if self.explicit_venv_path:
            stdout, _, exit_code = executor.execute_command(f"echo {self.explicit_venv_path}")
            if exit_code == 0 and stdout.strip():
                venv_path = self._validate_venv_path(executor, stdout.strip())
                if venv_path:
                    self._cached_venv_path = venv_path
                    self._venv_path_searched = True
                    return venv_path

        # 2. VIRTUAL_ENV environment variable (Docker containers) - check immediately
        if not isinstance(executor, HostExecutor):
            stdout, _, exit_code = executor.execute_command("echo $VIRTUAL_ENV", working_dir)
            if exit_code == 0 and stdout.strip():
                venv_path = self._validate_venv_path(executor, stdout.strip())
                if venv_path:
                    self._cached_venv_path = venv_path
                    self._venv_path_searched = True
                    return venv_path

        # 3. Extract venv path from pip show pip location
        stdout, _, exit_code = executor.execute_command("pip show pip", working_dir)
        if exit_code == 0:
            for line in stdout.split("\n"):
                if line.startswith("Location:"):
                    pip_location = line.split(":", 1)[1].strip()
                    # Skip system locations
                    if not pip_location.startswith(("/usr/lib", "/usr/local/lib")) and "/lib/python" in pip_location:
                        venv_path = pip_location.split("/lib/python")[0]
                        # Trust this path since pip is installed there - just cache and return
                        self._cached_venv_path = venv_path
                        self._venv_path_searched = True
                        return venv_path
                    break

        # 4. Batch search for remaining venv locations
        # Collect all paths and use single find command for efficiency (fewer executor calls)
        search_paths = set()
        common_venv_names = ["venv", ".venv", "env", ".env", "virtualenv"]

        # Check working directory, if specified
        if working_dir:
            search_paths.add(working_dir)  # working_dir itself
            for venv_name in common_venv_names:
                search_paths.add(f"{working_dir}/{venv_name}")

        # Check current directory, if running in container environment
        if not isinstance(executor, HostExecutor):
            pwd_stdout, _, pwd_exit_code = executor.execute_command("pwd")
            if pwd_exit_code == 0 and pwd_stdout.strip():
                current_dir = pwd_stdout.strip()
                for venv_name in common_venv_names:
                    search_paths.add(f"{current_dir}/{venv_name}")

        # Check home directory subdirectories (always check)
        # Resolve home directory explicitly to avoid tilde expansion issues
        home_stdout, _, home_exit_code = executor.execute_command("echo $HOME")
        if home_exit_code == 0 and home_stdout.strip():
            home_dir = home_stdout.strip()
            for venv_name in common_venv_names:
                search_paths.add(f"{home_dir}/{venv_name}")

        # External venv locations (project-specific, only if working_dir specified)
        if working_dir:
            resolved_working_dir = self._resolve_absolute_path(executor, working_dir)
            project_name = os.path.basename(resolved_working_dir)

            # Use resolved home directory for external locations too
            if home_exit_code == 0 and home_stdout.strip():
                home_dir = home_stdout.strip()
                external_locations = [
                    f"{home_dir}/.virtualenvs/{project_name}",
                    f"{home_dir}/.local/share/virtualenvs/{project_name}",
                    f"{home_dir}/.cache/pypoetry/virtualenvs/{project_name}",
                    f"{home_dir}/.pyenv/versions/{project_name}",
                ]
                search_paths.update(external_locations)

        if search_paths:
            escaped_paths = [f"'{path}'" for path in search_paths]
            find_cmd = f"find {' '.join(escaped_paths)} -maxdepth 1 -name 'pyvenv.cfg' -type f 2>/dev/null | head -1"

            stdout, _, exit_code = executor.execute_command(find_cmd)
            if exit_code == 0 and stdout.strip():
                pyvenv_cfg_path = stdout.strip()
                venv_path = os.path.dirname(pyvenv_cfg_path)
                self._cached_venv_path = venv_path
                self._venv_path_searched = True
                return venv_path

        # Fallback: System-wide search (only in container environments)
        if not isinstance(executor, HostExecutor):
            if self.debug:
                print("pip_detector performing system-wide pyvenv.cfg search in container environment")

            stdout, _, exit_code = executor.execute_command(
                "find /opt /home -name 'pyvenv.cfg' -type f 2>/dev/null | head -1"
            )

            if exit_code == 0 and stdout.strip():
                pyvenv_cfg_path = stdout.strip()
                venv_path = os.path.dirname(pyvenv_cfg_path)
                if self.debug:
                    print(f"pip_detector found pyvenv.cfg at {pyvenv_cfg_path}, venv_path: {venv_path}")
                self._cached_venv_path = venv_path
                self._venv_path_searched = True
                return venv_path

        # No venv found
        if self.debug:
            print("pip_detector did not found any venv location!")
        self._cached_venv_path = None
        self._venv_path_searched = True
        return None

    def _resolve_absolute_path(self, executor: EnvironmentExecutor, path: str) -> str:
        """Resolve absolute path within the executor's context."""
        if path == ".":
            stdout, stderr, exit_code = executor.execute_command("pwd")
            if exit_code == 0 and stdout.strip():
                return stdout.strip()
            raise RuntimeError(f"Failed to resolve current directory in executor context: {stderr}")
        else:
            stdout, stderr, exit_code = executor.execute_command(f"cd '{path}' && pwd")
            if exit_code == 0 and stdout.strip():
                return stdout.strip()
            raise RuntimeError(f"Failed to resolve path '{path}' in executor context: {stderr}")

    def _generate_location_hash(self, executor: EnvironmentExecutor, location: str) -> str:
        """Generate a hash based on the contents of the location directory.

        Implements package manager location hashing as part of multi-tiered hash strategy.
        See docs/technical/detectors/pip_detector.md
        """
        # Use environment-independent sorting for consistent hashes across systems.
        # Two-tier sort strategy: primary by file size (numeric), secondary by path (lexicographic).
        # Include both regular files and symbolic links to capture complete directory state.
        # For symlinks, include the target path (%l) to make hash sensitive to link changes.
        # The -printf format ensures consistent "size path [target]" output regardless of system.
        # LC_COLLATE=C ensures byte-wise lexicographic sorting independent of system locale.
        stdout, _, exit_code = executor.execute_command(
            f"cd '{location}' && find . "
            "-name '__pycache__' -prune -o "
            "-name '__editable__*' -prune -o "
            "-name 'pip*' -prune -o "
            "-name 'setuptools*' -prune -o "
            "-name 'pkg_resources' -prune -o "
            "-name '*distutils*' -prune -o "
            "-path '*/pip/_vendor' -prune -o "
            "-not -name '*.pyc' "
            "-not -name '*.pyo' "
            "-not -name 'INSTALLER' "
            "-not -name 'RECORD' "
            "\\( -type f -o -type l \\) -printf '%s %p %l\\n' | LC_COLLATE=C sort -n -k1,1 -k2,2"
        )
        if exit_code == 0 and stdout.strip():
            content = stdout.strip()
            return hashlib.sha256(content.encode()).hexdigest()
        else:
            if self.debug:
                print(f"ERROR: pip_detector hash generation command failed with exit code {exit_code}")
                print(f"ERROR: command stdout: {stdout}")
                print(f"ERROR: location: {location}")
            return ""

    def is_os_package_manager(self) -> bool:
        """PIP is a language package manager, not an OS package manager."""
        return False
