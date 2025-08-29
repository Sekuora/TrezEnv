from pathlib import Path

# Global Paths
tze_env_path = Path("externals")
tze_vcpkg_path = None  
tze_toolchain_file = Path(f"{tze_env_path}/scripts/buildsystems/vcpkg.cmake")
tze_vcpkg_repo = "https://github.com/microsoft/vcpkg.git"
tze_root_project_path = None
tze_project_deps_install_path = None
tze_project_file_path = None

def find_tze_root(start_path: Path = Path.cwd()) -> Path | None:
    current = start_path.resolve()
    while current != current.parent:
        if (current / "trezenv").is_file():
            return current
        current = current.parent
    return None

def assert_tze_root(start_path: Path = Path.cwd()) -> Path:
    root = find_tze_root(start_path)
    if root is None:
        raise RuntimeError(f"No 'trezenv' project found in {start_path} or its parents. Run init from root file.")
    return root

def set_tze_project_deps_install_path() -> Path:
    if (tze_root_project_path):
        tze_project_deps_path = Path(f"{tze_vcpkg_path}/installed")
        return tze_project_deps_path
    else:
        raise RuntimeError(f"No 'trezenv' project found. Run init from root file.")
    
def set_tze_project_file_path() -> Path:
    if (tze_root_project_path):
        tze_project_file_path = tze_root_project_path / "trezenv"
        return tze_project_file_path
    else:
        raise RuntimeError(f"No 'trezenv' project found. Run init from root file.")
    
def set_tze_vcpkg_path() -> Path:
    if (tze_root_project_path):
        tze_vcpkg_path = Path(f"{tze_root_project_path}/{tze_env_path}/vcpkg")
        return tze_vcpkg_path
    else:
        raise RuntimeError(f"No 'vcpkg' path found. Run init from root file.")


if __name__ == "__main__":
    print("Path globals module")