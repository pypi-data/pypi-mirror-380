#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path
import platform
import getpass
import time
from datetime import datetime
import plistlib
import shutil
import ctypes

# External
from colorama import init, Fore, Style

init(autoreset=True)

# --- Constants ---
LOG_FILE = (
    "/var/log/os_flip.log" if platform.system() == "Linux" 
    else os.path.join(os.environ['TEMP'], f"os_flip_{getpass.getuser()}.log") if platform.system() == "Windows"
    else f"/tmp/os_flip_{getpass.getuser()}.log"
)
USER_LOG_FILE = f"/tmp/os_flip_{getpass.getuser()}.log" if platform.system() in ("Linux", "Darwin") else None

# --- Logging ---
def log(message):
    path = LOG_FILE
    if platform.system() in ("Linux", "Darwin") and os.geteuid() != 0:
        path = USER_LOG_FILE
    
    try:
        with open(path, "a") as f:
            f.write(f"[{datetime.now()}] {message}\n")
    except PermissionError:
        print(f"{Fore.RED}⚠️ Cannot write to log at {path}. Logging disabled.")

# --- Print Helpers ---
def print_success(msg): print(f"{Fore.GREEN}✅ {msg}"); log(f"SUCCESS: {msg}")
def print_info(msg): print(f"{Fore.CYAN}ℹ️  {msg}"); log(f"INFO: {msg}")
def print_warning(msg): print(f"{Fore.YELLOW}⚠️  {msg}"); log(f"WARNING: {msg}")
def print_error(msg): print(f"{Fore.RED}❌ {msg}"); log(f"ERROR: {msg}")

# --- Banner ---
def print_banner():
    if platform.system() == "Windows":
        color = Fore.BLUE
        os_name = "Windows"
    elif platform.system() == "Darwin":
        color = Fore.MAGENTA
        os_name = "macOS"
    else:  # Linux
        color = Fore.RED
        os_name = "Linux"
    
    banner = rf"""{color}{Style.BRIGHT}
   ____   _____          ______ _      _____ _____ 
  / __ \ / ____|        |  ____| |    |_   _|  __ \
 | |  | | (___    ___   | |__  | |      | | | |__) |
 | |  | |\___ \         |  __| | |      | | |  ___/ 
 | |__| |____) |        | |    | |____ _| |_| |     
  \____/|_____/         |_|    |______|_____|_|   
    
{Style.RESET_ALL}
{Style.BRIGHT}         Welcome to OS FLIP 
                            By - AK({os_name})
{Style.RESET_ALL}
"""
    print(banner)
    log(f"Launched OS Flip ({os_name})")

# --- Launches a New Terminal ---
def launch_in_new_terminal():
    """Try to launch the script in the user's default terminal, or fall back to known list."""
    current_os = platform.system()
    script_path = os.path.abspath(__file__)
    
    if current_os == "Windows":
        subprocess.Popen(f'start cmd /k python "{script_path}" --no-terminal-launch', shell=True)
        sys.exit(0)
    elif current_os == "Darwin":
        subprocess.Popen([
            "osascript",
            "-e", f'tell app "Terminal" to do script "python3 \'{script_path}\' --no-terminal-launch"'
        ])
        sys.exit(0)
    elif current_os == "Linux":
        # 1. Define the executable and arguments for launching the script
        python_executable = sys.executable
        script_command = [python_executable, script_path, "--no-terminal-launch"]
        
        # 2. Check environment for user-defined default terminal ($TERMINAL)
        default_term_cmd = os.environ.get("TERMINAL")
        if default_term_cmd and shutil.which(default_term_cmd):
            print_info(f"Attempting to launch in default terminal: {default_term_cmd}")
            try:
                # Most default terminals will work with the simple -e or a specific command format
                # We'll use the safe, separate-argument format first.
                subprocess.Popen([default_term_cmd, "-e"] + script_command)
                sys.exit(0)
            except Exception as e:
                print_warning(f"Failed to launch with user's default terminal ({default_term_cmd}): {e}. Falling back...")
        
        # 3. Fallback to the comprehensive list (your original logic)
        terminals = [
            "ptyxis", "kitty", "ghostty", "alacritty", "wezterm", "foot", "st", "gnome-terminal", "konsole", 
            "xfce4-terminal", "mate-terminal", "tilix", "terminator", "lxterminal", 
            "deepin-terminal", "qterminal", "eterm", "mlterm", "urxvt", "xterm"
        ]

        for term in terminals:
            if shutil.which(term):
                try:
                    # Group 1: Terminals that typically require the command as a single, quoted shell string
                    if term in ("gnome-terminal", "konsole", "xfce4-terminal", "mate-terminal", "lxterminal", "deepin-terminal", "qterminal", "eterm", "mlterm"):
                        # We use sys.executable and quotes for shell compatibility
                        full_cmd_string = f'{python_executable} "{script_path}" --no-terminal-launch'
                        subprocess.Popen([term, "-e", full_cmd_string])
                    
                    # Group 2: Terminals that require the command and arguments as separate items
                    elif term in ("alacritty", "kitty", "foot", "wezterm", "ghostty", "st", "tilix", "terminator", "ptyxis", "urxvt", "xterm"):
                        # This is the safest way to pass the command for modern terminals
                        subprocess.Popen([term, "-e"] + script_command)
                    
                    else:
                        # Default fallback using separate items (safer approach)
                        subprocess.Popen([term, "-e"] + script_command)
                        
                    sys.exit(0)
                except Exception as e:
                    print_warning(f"Failed to launch with {term}: {e}")
        
        # 4. Final Fallback prompt
        print_warning("⚠️ No supported terminal emulator found.")
        fallback = input("Would you like to run this script in the current terminal instead? (y/N): ").strip().lower()
        if fallback == "y":
            # Just continue running in this terminal (no recursion!)
            return
        else:
            print_error("Please install a terminal emulator (e.g., kitty or gnome-terminal).")
            sys.exit(1)
            
# --- Privilege Checks ---
def is_windows_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def exit_if_not_admin():
    if platform.system() == "Linux":
        if os.geteuid() != 0:
            print_error("This script must be run as root. Use `sudo`.")
            sys.exit(1)
    elif platform.system() == "Darwin":
        try:
            subprocess.run(["sudo", "-v"], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print_error("This script must be run with sudo.")
            sys.exit(1)
    elif platform.system() == "Windows":
        if not is_windows_admin():
            print_error("This script must be run as Administrator.")
            sys.exit(1)

# --- Linux Specific Functions ---
def get_grub_update_cmd():
    if Path("/etc/arch-release").exists():
        print_info("Detected Arch Linux/derivative.")
        return "grub-mkconfig -o /boot/grub/grub.cfg"
    elif Path("/etc/debian_version").exists():
        print_info("Detected Debian/Ubuntu/derivative.")
        return "update-grub"
    elif Path("/etc/redhat-release").exists() or "fedora" in platform.platform().lower():
        print_info("Detected RedHat/Fedora/derivative.")
        return "grub2-mkconfig -o /boot/grub2/grub.cfg"
        
    print_error("Unsupported Linux distribution. Cannot determine GRUB update command.")
    sys.exit(1)

def update_grub():
    global GRUB_UPDATE_CMD
    try:
        subprocess.run(GRUB_UPDATE_CMD, shell=True, check=True)
        print_success("GRUB configuration updated.")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to update GRUB: {e}")
        return False

def backup_grub_config():
    timestamp = int(time.time())
    backup_path = f"/etc/default/grub.bak.{timestamp}"
    try:
        shutil.copy("/etc/default/grub", backup_path)
        print_info(f"Backed up GRUB config to {backup_path}")
        return True
    except Exception as e:
        print_error(f"Failed to backup GRUB config: {e}")
        return False

def ensure_os_prober_enabled():
    if not Path("/usr/bin/os-prober").exists():
        print_warning("os-prober not found. Some OSes may not be detected.")
        return False

    if not backup_grub_config():
        return False

    try:
        with open("/etc/default/grub", "r") as f:
            lines = f.readlines()
    except Exception as e:
        print_error(f"Failed to read /etc/default/grub: {e}")
        return False

    updated = False
    for i, line in enumerate(lines):
        if line.startswith("GRUB_DISABLE_OS_PROBER="):
            lines[i] = "GRUB_DISABLE_OS_PROBER=false\n"
            updated = True
            break

    if not updated:
        lines.append("\nGRUB_DISABLE_OS_PROBER=false\n")

    try:
        with open("/etc/default/grub", "w") as f:
            f.writelines(lines)
    except PermissionError as e:
        print_error(f"Failed to modify GRUB config: {e}")
        return False

    print_success("os-prober enabled in /etc/default/grub.")
    print_info("Updating GRUB entries (running os-prober)...")
    try:
        subprocess.run(["os-prober"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return update_grub()
    except subprocess.CalledProcessError as e:
        print_warning(f"Failed to run os-prober directly: {e}. Attempting GRUB update anyway.")
        return update_grub()
        
#Made By- https://github.com/AKris15

def get_linux_boot_entries():
    entries = []
    seen = set()

    grub_cfgs = [
        "/boot/grub/grub.cfg",
        "/boot/grub2/grub.cfg",
        "/boot/efi/EFI/fedora/grub.cfg"
    ]

    grub_path = next((p for p in grub_cfgs if Path(p).exists()), None)
    if grub_path:
        try:
            with open(grub_path, "r") as f:
                for line in f:
                    if line.strip().startswith("menuentry "):
                        # Extract exact title including quotes
                        parts = line.split("'")
                        if len(parts) > 1:
                            title = parts[1]
                        else:
                            parts = line.split('"')
                            if len(parts) > 1:
                                title = parts[1]
                            else:
                                continue # Skip lines that don't match expected format
                                
                        if title not in seen:
                            entries.append(title)
                            seen.add(title)
        except Exception as e:
            print_warning(f"Failed to read GRUB config at {grub_path}: {e}")
        
    bls_dir = Path("/boot/loader/entries")
    if bls_dir.exists():
        for entry in bls_dir.glob("*.conf"):
            try:
                with open(entry) as f:
                    for line in f:
                        if line.startswith("title"):
                            title = line.strip().split(" ", 1)[1]
                            if title not in seen:
                                entries.append(title)
                                seen.add(title)
                            break
            except Exception as e:
                print_warning(f"Failed to read BLS entry {entry}: {e}")


    if not entries:
        print_error("No boot entries found in standard locations.")
    return entries

def get_current_linux_default_os():
    try:
        with open("/etc/default/grub", "r") as f:
            for line in f:
                if line.startswith("GRUB_DEFAULT="):
                    return line.split("=", 1)[1].strip().strip('"')
    except Exception as e:
        print_warning(f"Could not read default GRUB entry: {e}")
        return None

def set_linux_default_os(entry_name):
    try:
        with open("/etc/default/grub", "r") as f:
            lines = f.readlines()
    except Exception as e:
        print_error(f"Failed to read /etc/default/grub: {e}")
        return False

    found = False
    for i, line in enumerate(lines):
        if line.startswith("GRUB_DEFAULT="):
            lines[i] = f'GRUB_DEFAULT="{entry_name}"\n'
            found = True
            break
    
    if not found:
        lines.append(f'\nGRUB_DEFAULT="{entry_name}"\n')

    try:
        with open("/etc/default/grub", "w") as f:
            f.writelines(lines)
    except PermissionError as e:
        print_error(f"Failed to write to /etc/default/grub: {e}")
        return False

    return update_grub()

# --- Windows Specific Functions ---
def get_windows_boot_entries():
    entries = []
    identifiers = []
    
    try:
        commands = [
            ["bcdedit", "/enum", "Firmware"],
            ["bcdedit", "/enum", "OSLOADER"],
            ["bcdedit"]
        ]
        
        for cmd in commands:
            if entries:
                break
                
            try:
                output = subprocess.check_output(cmd, text=True, stderr=subprocess.PIPE)
                
                current_identifier = None
                current_description = None
                
                for line in output.splitlines():
                    line = line.strip()
                    if line.startswith("identifier"):
                        current_identifier = line.split()[-1]
                    elif line.startswith("description"):
                        current_description = " ".join(line.split()[1:])
                        if current_identifier and current_description:
                            if current_description not in entries:
                                entries.append(current_description)
                                identifiers.append(current_identifier)
                            current_identifier = None
                            current_description = None
            except subprocess.CalledProcessError:
                continue
        
        return entries, identifiers
    
    except Exception as e:
        print_error(f"Failed to enumerate boot entries: {e}")
        return [], []

def get_current_windows_default_os():
    try:
        output = subprocess.check_output(["bcdedit"], text=True)
        for line in output.splitlines():
            if "default" in line.lower() and "identifier" in line.lower():
                return line.split()[-1]
        return None
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to get current default OS: {e}")
        return None

def set_windows_default_os(identifier):
    try:
        subprocess.run(["bcdedit", "/default", identifier], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to set default OS: {e}")
        return False

# --- macOS Specific Functions ---
def get_macos_boot_entries():
    entries = []
    identifiers = []
    
    try:
        # Get all bootable volumes as binary plist
        output = subprocess.check_output(["diskutil", "list", "-plist", "internal"])
        plist_data = plistlib.loads(output)
        
        current_boot_id = None
        try:
            current_boot_info = subprocess.check_output(["diskutil", "info", "/"], text=True)
            for line in current_boot_info.splitlines():
                if "Device Identifier:" in line:
                    current_boot_id = line.split(":")[1].strip()
                    break
        except:
            pass
        
        # Iterate over partitions to find bootable volumes
        for disk in plist_data.get("AllDisksAndPartitions", []):
            if disk.get("Content") == "Apple_APFS":
                for partition in disk.get("Partitions", []):
                    # Look for APFS Volumes
                    if partition.get("Content") in ("Apple_APFS_Volume", "Apple_Boot"): 
                        vol_name = partition.get("VolumeName", "Untitled")
                        vol_id = partition.get("DeviceIdentifier")
                        
                        if vol_id and vol_name and vol_id not in identifiers:
                            # Only include macOS volumes (skip recovery, preboot, etc. unless they are the current boot)
                            if vol_name.lower().startswith("macintosh hd") or vol_id == current_boot_id:
                                entries.append(f"macOS ({vol_name})")
                                identifiers.append(vol_id)
        
        # Check for Boot Camp
        try:
            bootcamp_output = subprocess.check_output(
                ["diskutil", "list", "BOOTCAMP"], 
                text=True,
                stderr=subprocess.DEVNULL
            )
            if "BOOTCAMP" in bootcamp_output and "BOOTCAMP" not in identifiers:
                entries.append("Windows (Boot Camp)")
                identifiers.append("BOOTCAMP") 
        except:
            pass
        
        return entries, identifiers
    
    except Exception as e:
        print_error(f"Failed to enumerate boot entries: {e}")
        return [], []

def get_current_macos_default_os():
    try:
        # Returns a descriptive path, e.g., "/System/Library/CoreServices/boot.efi" or "disk0s2"
        output = subprocess.check_output(["systemsetup", "-getstartupdisk"], text=True)
        return output.split(":")[1].strip() if ":" in output else None
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to get current default OS: {e}")
        return None

def set_macos_default_os(disk_identifier):
    try:
        if disk_identifier == "BOOTCAMP":
            # For Boot Camp, we bless the volume mount point
            subprocess.run(["sudo", "bless", "--mount", "/Volumes/BOOTCAMP", "--setBoot"], check=True)
        else:
            # Find the mount point for the device identifier
            mount_point = None
            try:
                disk_info = subprocess.check_output(["diskutil", "info", disk_identifier], text=True)
                for line in disk_info.splitlines():
                    if "Mount Point:" in line:
                        mount_point = line.split(":")[1].strip()
                        break
            except Exception as e:
                print_error(f"Failed to find mount point for {disk_identifier}: {e}")
                return False

            if mount_point:
                # Bless the mount point
                subprocess.run(["sudo", "bless", "--mount", mount_point, "--setBoot"], check=True)
            else:
                print_error(f"Could not determine mount point for identifier {disk_identifier}. Cannot bless.")
                return False
                
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to set default OS: {e}")
        return False

def reboot_macos():
    try:
        subprocess.run(["sudo", "shutdown", "-r", "now"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to reboot: {e}")
        return False

# --- Main Menu ---
def main():
    # Check if we should launch in new terminal
    if "--no-terminal-launch" not in sys.argv:
        launch_in_new_terminal()

    
    print_banner()
    
    try:
        current_os = platform.system()
        if current_os not in ("Linux", "Windows", "Darwin"):
            print_error("This script only runs on Linux, Windows, or macOS systems.")
            sys.exit(1)
            
        exit_if_not_admin()

        if current_os == "Linux":
            global GRUB_UPDATE_CMD
            GRUB_UPDATE_CMD = get_grub_update_cmd()
            if not ensure_os_prober_enabled():
                print_warning("Continuing with limited functionality")
            entries = get_linux_boot_entries()
            identifiers = None
            current_default = get_current_linux_default_os()
        elif current_os == "Windows":
            entries, identifiers = get_windows_boot_entries()
            current_default_id = get_current_windows_default_os()
            current_default = entries[identifiers.index(current_default_id)] if current_default_id and current_default_id in identifiers else "Unknown"
        else:  # macOS
            entries, identifiers = get_macos_boot_entries()
            current_default_display_name = get_current_macos_default_os()
            # Note: macOS default is complex. We use the display name for comparison.
            current_default = current_default_display_name

        if not entries:
            print_error("No boot entries found. Cannot continue.")
            return

        print(f"\n{Fore.CYAN}📜 Available Boot Entries:{Style.RESET_ALL}")
        if current_os == "Linux":
            for idx, entry in enumerate(entries):
                current_marker = " (Current Default)" if entry == current_default else ""
                print(f"  {idx + 1}. {entry}{current_marker}")
        else:  # Windows or macOS
            for idx, (entry, identifier) in enumerate(zip(entries, identifiers)):
                current_marker = ""
                if current_os == "Windows":
                    current_marker = " (Current Default)" if identifier == current_default_id else ""
                elif current_os == "Darwin":
                    # Check if the entry name is contained in the descriptive current default path
                    if identifier == "BOOTCAMP" and "BOOTCAMP" in current_default_display_name:
                        current_marker = " (Current Default)"
                    elif identifier != "BOOTCAMP" and identifier in current_default_display_name:
                        current_marker = " (Current Default)"

                print(f"  {idx + 1}. {entry}{current_marker}")

        print(f"""\n{Fore.CYAN}⚙️  Options:
  1. Set default boot OS
  2. Flip OS
  3. Exit{Style.RESET_ALL}""")

        try:
            option = int(input("\nChoose an option (1-3): ").strip())
            if option not in [1, 2, 3]:
                print_error("Invalid option.")
                return
            if option == 3:
                print_info("Exiting OS Flip.")
                sys.exit(0)
                return

            choice = int(input("Select OS number: ").strip()) - 1
            if choice < 0 or choice >= len(entries):
                print_error("Invalid OS selection.")
                return

            if current_os == "Linux":
                selected_os = entries[choice]
                print_info(f"Selected: {selected_os}")

                if option == 1:
                    print_info(f"Current default: {current_default}")
                    if set_linux_default_os(selected_os):
                        print_success(f"Default OS set to: {selected_os}")
                        reboot = input("🔁 Flip now? (y/N): ").strip().lower()
                        if reboot == "y":
                            subprocess.run(["reboot"])
                elif option == 2:
                    print_info(f"Flip into: {selected_os}")
                    grub_reboot_cmd = shutil.which("grub-reboot") or shutil.which("grub2-reboot")
                    
                    if not grub_reboot_cmd:
                        print_error("❌ Neither 'grub-reboot' nor 'grub2-reboot' found")
                        print_info("💡 Install with: e.g., sudo apt install grub2-common (Debian) or sudo pacman -S grub (Arch)")
                        return

                    try:
                        subprocess.run([grub_reboot_cmd, selected_os], check=True)
                        print_success("Temporary boot set. Rebooting...")
                        subprocess.run(["reboot"])
                    except subprocess.CalledProcessError as e:
                        print_error(f"Failed to set temporary boot: {e}")
                        
            elif current_os == "Windows":
                selected_os = entries[choice]
                selected_id = identifiers[choice]
                print_info(f"Selected: {selected_os}")

                if option == 1:
                    print_info(f"Current default: {current_default}")
                    if set_windows_default_os(selected_id):
                        print_success(f"Default OS set to: {selected_os}")
                        reboot = input("🔁 Flip now? (y/N): ").strip().lower()
                        if reboot == "y":
                            subprocess.run(["shutdown", "/r", "/t", "0"])
                elif option == 2:
                    print_info(f"Rebooting into: {selected_os}...")
                    if set_windows_default_os(selected_id):
                        subprocess.run(["shutdown", "/r", "/t", "0"])
            else:  # macOS
                selected_os = entries[choice]
                selected_id = identifiers[choice]
                print_info(f"Selected: {selected_os}")

                if option == 1:
                    print_info(f"Current default: {current_default_display_name}")
                    if set_macos_default_os(selected_id):
                        print_success(f"Default OS set to: {selected_os}")
                        reboot = input("🔁 Flip now? (y/N): ").strip().lower()
                        if reboot == "y":
                            reboot_macos()
                elif option == 2:
                    print_info(f"Rebooting into: {selected_os} (One-time and default boot are the same on macOS)...")
                    if set_macos_default_os(selected_id):
                        reboot_macos()

        except ValueError:
            print_error("Invalid input. Please enter a number.")

    except KeyboardInterrupt:
        print_warning("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
        log(f"CRITICAL ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()