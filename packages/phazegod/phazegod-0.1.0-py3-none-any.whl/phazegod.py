#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os
from pyfiglet import Figlet
from colorama import init, Fore, Style

init(autoreset=True)

VERSION = "0.1.0"
CREATOR = "Shaurya - Phazegod"
REPO = "https://github.com/a00137/phazegod"

def ascii_banner(text, colour=Fore.GREEN):
    f = Figlet(font='slant')
    return colour + f.renderText(text)

def show_main():
    print(ascii_banner("Phazegod"))
    print(Fore.GREEN + f"Creator: {CREATOR}")
    print(Fore.GREEN + f"GitHub Repo: {REPO}\n")
    print(Fore.BLUE + f"Version: {VERSION}\n")
    print(Style.BRIGHT + "Help:")
    print("  -zenpo\tInstall zenpo")
    print("  -help \tShow this help")
    print("  -refresh\tUpdate phazegod")

def refresh_package():
    try:
        pkg_dir = os.path.expanduser("~/phazegod")
        if not os.path.exists(pkg_dir):
            print(f"Cloning phazegod into {pkg_dir}...")
            subprocess.run(["git", "clone", REPO, pkg_dir], check=True)
        else:
            print(f"Refreshing Phazegod in {pkg_dir}...\n")
            subprocess.run(["git", "pull"], cwd=pkg_dir, check=True)

        subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], cwd=pkg_dir, check=True)
        print("\nPhazegod has been updated successfully!")
    except Exception as e:
        print(f"Failed to refresh Phazegod: {e}")

def install_zenpo():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "zenpo"], check=True)
    except Exception as e:
        print(f"Failed to install Zenpo: {e}")

def main():
    parser = argparse.ArgumentParser(prog="phazegod", add_help=False)
    parser.add_argument("-zenpo", action="store_true", help="Install zenpo")
    parser.add_argument("-refresh", action="store_true", help="Update phazegod to latest GitHub version")
    parser.add_argument("-help", action="store_true", help="Show help")
    args = parser.parse_args()

    if args.zenpo:
        install_zenpo()
    elif args.refresh:
        refresh_package()
    elif args.help:
        show_main()
    else:
        show_main()

if __name__ == "__main__":
    main()
