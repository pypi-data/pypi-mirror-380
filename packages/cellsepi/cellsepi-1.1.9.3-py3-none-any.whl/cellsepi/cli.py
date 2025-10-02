import os
import shutil
import subprocess
import sys
import platform

def build():
    """
    Build cellsepi with flet build platform -v
    """
    #goto cellsepi folder
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    #check which system is used
    system = platform.system().lower()
    if system == "windows":
        target = "web"
        """
        #check if VS2022 is installed correctly to build flet on windows
        if shutil.which("cl") is None:
            print("Flet build failed: cl is not installed, please make sure you installed VS2022 and PATH is set correctly!")
            sys.exit(1)
        if shutil.which("cmake") is None:
            print("Flet build failed: cmake not found. Please make sure VS2022 is installed with the CMake component, and PATH is set correctly!")
            sys.exit(1)
        """
    elif system == "darwin":
        target = "macos"
    elif system == "linux":
        target = "linux"
    else:
        print("Flet build failed: unknown system")
        sys.exit(1)

    #try to build cellsepi
    try:
        subprocess.check_call([sys.executable, "-m", "flet.cli", "build", target, "-v"])
    except subprocess.CalledProcessError as e:
        print(f"Flet build failed: {e}")
        sys.exit(1)
