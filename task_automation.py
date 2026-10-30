Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

... import os
... import shutil
... import re
... import requests
... 
... def automate_task():
... 
...     url = "https://example.com"
... 
...     try:
...         response = requests.get(url, timeout=10)
...         response.raise_for_status()
... 
...         # Extract webpage title using regex
...         match = re.search(
...             r"<title>(.*?)</title>",
...             response.text,
...             re.IGNORECASE | re.DOTALL
...         )
... 
...         if match:
...             title = match.group(1).strip()
...         else:
...             title = "Title not found"
... 
...         # Create folder using os
...         folder = "automation_output"
...         os.makedirs(folder, exist_ok=True)
... 
...         # Save title using file handling
...         file_path = os.path.join(folder, "title.txt")
... 
...         with open(file_path, "w", encoding="utf-8") as file:
...             file.write(title)
... 
...         # Create backup using shutil
...         shutil.copy(file_path, os.path.join(folder, "title_backup.txt"))
... 
...         print("Webpage Title:", title)
...         print("Title saved successfully!")
...         print("Backup created successfully!")
... 
...     except requests.RequestException as error:
...         print("Error:", error)
... 
... automate_task()
