import time
import random
import sys

fake_files = [
    "C:/Windows/System32/important.dll",
    "C:/Windows/Temp/secret_recipe.txt",
    "C:/Users/User/Documents/secret_plans.txt",
    "C:/Users/User/AppData/Roaming/doom_saver.bat",
    "C:/Program Files/SuspiciousApp/sus.exe",
    "C:/Program Files/Common Files/UnicornDriver.sys",
    "D:/Games/AncientGame/savefile.corrupt",
    "C:/Windows/Fonts/comic_sans_neue.ttf",
    "/usr/bin/ultimate_hack_tool.sh",
    "/usr/local/bin/self_destruct.sh",
    "/etc/passwd",
    "/etc/whywouldyouputthishere.conf",
    "/var/log/cat_pictures.log",
    "/tmp/hidden_gem.tmp",
    "/opt/secret_folder/forbidden_knowledge.pdf",
    "/home/user/DefinitelyNotMalware.py",
    "/home/user/.config/quantum_settings.yaml",
    "/dev/null",
    "/mnt/usb/totallylegit.iso",
    "A:/floppy_disk/nostalgia.exe",
    "Z:/network_drive/aliensighting.jpg",
    "C:/Windows/System32/404notfound.sys",
    "C:/super_secret/never_gonna_give_you_up.mp3",
    "/private/var/root/evilplan.docx",
    "/Users/Shared/README_DO_NOT_DELETE.txt",
    "/Applications/Clippy.app",
    "C:/Windows/WinSxS/backup_of_backup_of_backup.zip"
]

funny_messages = [
    "Reticulating splines...",
    "Counting backwards from infinity...",
    "Calculating the meaning of life...",
    "Unpacking memes...",
    "Reversing the polarity of the neutron flow...",
    "Consulting the magic 8-ball...",
    "Compiling with 100% more sarcasm...",
    "Replacing all your files with cat pictures...",
    "Mining Bitcoin (just kidding)...",
    "Optimizing useless code...",
    "Pretending to be busy...",
    "Downloading RAM...",
    "Upgrading your sense of humor...",
    "Fixing the flux capacitor...",
    "Summoning rubber ducks for debugging...",
    "Debugging the debugger...",
    "Translating binary to emoji...",
    "Herding electrons...",
    "Faking progress bar...",
    "Launching the launch sequence...",
    "Turning it off and on again...",
    "Stealing cookies (not the browser kind)...",
    "Encrypting all vowels...",
    "Reinstalling clippy...",
    "Feeding the hamsters that power your CPU...",
    "Befriending firewalls...",
    "Writing poetry in assembly language...",
    "Searching for lost socks...",
    "Negotiating with procrastination daemons...",
    "Asking the AI overlords for permission...",
    "Unlocking secret achievements...",
    "Redirecting to the mainframe...",
    "Just a flesh wound!",
    "404: Joke not found.",
    "Performing quantum entanglement...",
    "Rebooting the space-time continuum...",
    "Making coffee break mandatory...",
    "Running with scissors (dangerous!)",
    "Blinking rapidly to simulate activity...",
    "Tuning the banjo for the next step...",
    "Pretending to care...",
    "Making up more funny messages...",
    "Simulating a blue screen of happiness..."
]


def fake_progress_bar(total, prefix='Progress', length=40):
    for i in range(total + 1):
        percent = int(100 * i / total)
        bar = '#' * int(length * i / total)
        space = ' ' * (length - len(bar))
        sys.stdout.write(f"\r{prefix}: [{bar}{space}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def main():
    print("Welcome to the Totally Legit Installer v1.0")
    time.sleep(1)
    print("Starting installation...\n")
    time.sleep(1)

    for _ in range(25):
        fake_file = random.choice(fake_files)
        message = random.choice(funny_messages)
        print(f"Processing {fake_file}...")
        time.sleep(random.uniform(0.2, 0.7))
        print(message)
        fake_progress_bar(random.randint(5, 20), prefix="Updating")
        print()

    print("Installation complete! (Or is it?) 😏")
    print("Thank you for trusting us with your imaginary files.")


if __name__ == "__main__":
    main()