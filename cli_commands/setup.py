import click
from pathlib import Path
from primals.systems import path_finder as pf;
from primals.scripts import environment_initialize as env_init


# Set Command
@click.command()
@click.option("--envpath", "-ep", help = "Declare a new path for the environment. " \
"Resets to default path when no args are provied.", default=pf.tze_env_path, required=False )
def set(envpath: Path) -> None:
    
    """Set parameters related to the trezenv environment. See options."""

    default_envpath = pf.tze_env_path
    pf.tze_env_path = envpath
    if(envpath):
        print(f"Environment path changed from {default_envpath} to {envpath}")


# Check Command
@click.command()
@click.option("--envpath", "-ep", is_flag=True, help = "Check the current path for the environment. ")
def check(envpath) -> None:
    
    """Check values related to the trezenv environment. See options."""
   
    if(envpath):
        envpath = pf.tze_env_path
        print(f"Path: {envpath}")
    else:
        pass

    

# Init Command
@click.command()
def init() -> None:
    """Initialize trezenv environment and setup portable vcpkg installation. 
    A "trezenv" file is required specifying deps root project folder """

    # Check trezenv file exists before proceeding
    pf.tze_root_project_path = pf.assert_tze_root() 
    pf.tze_vcpkg_path = pf.set_tze_vcpkg_path()
    
    print("Set Root Path Success")

    # Clone vcpkg repo
    env_init.setup_environment_repo(pf.tze_vcpkg_repo,   pf.tze_vcpkg_path)
    print("setup env Success")

    # Bootstrap vcpkg
    env_init.bootstrap_vcpkg(pf.tze_vcpkg_path)
    print("setup bootstrap Success")

    # Vcpkg App Init
    env_init.vcpkg_init_manifest_mode(pf.tze_vcpkg_path, pf.tze_root_project_path)
    print("manifest mode Success")

    # Vcpkg Dependencies Path Installation
    env_init.vcpkg_set_dependencies_path( pf.tze_vcpkg_path, pf.set_tze_project_deps_install_path())
    print("dependencies path set Success")

    # Fetch ports from trezenv file
    env_init.add_ports_from_file(pf.tze_vcpkg_path, pf.set_tze_project_file_path())
    print("add port from trezenv file Success")

    # Install deps from manifest
    env_init.vcpkg_install_dependencies(pf.tze_vcpkg_path)
    print("installed deps from manifest Success")

    # List installed deps from manifest
    env_init.vcpkg_list_installed(pf.tze_vcpkg_path)
   


if __name__ == "__main__":
    print("Env Setup module")