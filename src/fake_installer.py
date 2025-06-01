import time
import random
import sys
from data import fake_files, funny_messages

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