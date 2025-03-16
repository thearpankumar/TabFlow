import time
import pyautogui
import pyperclip

import subprocess
# Before starting, force-focus Chrome
  # Install wmctrl first

# Function to copy the URL of the current tab
def copy_tab_url():
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)  # Increased from 0.5s
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Increased from 0.5s
    return pyperclip.paste()

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)  # Increased from 0.5s

# Main function to extract all tab URLs
def extract_all_tab_urls(num_tabs):
    urls = []
    for _ in range(num_tabs):
        url = copy_tab_url()
        urls.append(url)
        switch_to_next_tab()
    return urls

# Save URLs to a file
def save_urls_to_file(urls, filename="tabs.txt"):
    with open(filename, 'w') as file:
        for url in urls:
            file.write(url + '\n')
    print(f"Saved {len(urls)} URLs to {filename}")

# Run the script
if __name__ == "__main__":
    try:
        input("Make sure Chrome is active. Press Enter to continue...")
        num_tabs = int(input("Enter number of open tabs: "))
        subprocess.run(['wmctrl', '-a', 'Chrome'])
        urls = extract_all_tab_urls(num_tabs)
        save_urls_to_file(urls)
    except KeyboardInterrupt:
        print("\nScript terminated by user.")