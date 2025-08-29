import subprocess
import platform
from pathlib import Path
from subprocess import run, CalledProcessError

""" Define the system functionalities for environment creation to be used within trezenv commands """

def run(cmd, cwd=None, capture_output=False):
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=False,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.STDOUT
    )
    return result.stdout.strip() if capture_output else None
    

def ensure_dir(env_path: Path):
    if not env_path.exists():
        print(f"Creating environment directory: {env_path}")
        env_path.mkdir(parents=True, exist_ok=True)

# Clone vcpkg to project environment path
def setup_environment_repo(repo_url: str, dest: Path):
    # If path is a valid directory skip recreating it
    if dest.is_dir():
        print(f"Vcpkg already exists: {dest}")
        return   
    # Create path if it doesn't exist and clone repo inside it
    ensure_dir(dest.parent)
    run(["git", "clone", repo_url, str(dest)])


# Bootstrap process for vcpkg

def bootstrap_vcpkg(vcpkg_root: Path):
    
    script = (vcpkg_root / "bootstrap-vcpkg.bat").resolve()

    print("Setting up vcpkg...")
    print(f"Script Path: {script}")
    print(f"Working Directory: {vcpkg_root}")

    try:
        run([str(script)])
    except CalledProcessError as e:
        print(f"Bootstrap failed with exit code {e.returncode}")
        print(f"Command: {e.cmd}")

def vcpkg_init_manifest_mode(vcpkg_root: Path, app_dir: Path):
    """
    Init manifest mode at specified directory. Most likely project root dir.
    """
    print("Manifest mode active")

    vcpkg_exe = vcpkg_root / "vcpkg.exe"
    cmd = [str(vcpkg_exe), "new", "--application"]

    # verbose try/except statement for debug purposes
    try:
        result = subprocess.run(cmd, cwd=app_dir, capture_output=True, text=True, check=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print(f"vcpkg executable not found at: {vcpkg_exe}")

def vcpkg_set_dependencies_path(vcpkg_root: Path, app_deps_path: Path):
    """
    Set the dependencies installation path. Early development state, might not work.
    """
    print(app_deps_path)
    

    cmd = [
        str(vcpkg_root / "vcpkg.exe"),
        "install",
        f"--x-install-root={str(app_deps_path)}"
    ]
    run(cmd)


def add_ports_from_file(vcpkg_path: Path, deps_file: Path):
    with deps_file.open("r") as f:
        ports = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if ports:
        cmd = [str(vcpkg_path / "vcpkg.exe"), "add", "port", *ports]
        run(cmd)


def vcpkg_install_dependencies(vcpkg_root: Path):
    """
    Install the requested vcpkg packages.
    
    """

    print("Installing dependencies…")
    cmd = [vcpkg_root / "vcpkg.exe", "install", "--recurse"]
   
    run(cmd)

def vcpkg_list_installed(vcpkg_root: Path):
    """
    Print the list of installed ports (for debugging).
    """

    print("Installed packages:")
    run([vcpkg_root / "vcpkg.exe", "list"], capture_output=True)


def integrate_vcpkg(vcpkg_root: Path):
    """
    Integrate install vcpkg. While its integrated system wide, 
    the project CMakeLists.txt defines that the scope of this toolchain is used only within this project.
    This behaviour is reliable and repeatable on windows systems. Not required in most cases and when manifest mode is on.
    """
    if platform.system() == "Windows":
        print("Finishing vcpkg setup for windows")
        run([vcpkg_root / "vcpkg.exe", "integrate", "install"])


if __name__ == "__main__":
    print("Environment Initialize script module")