from bs4 import BeautifulSoup
from PIL import Image
from datetime import datetime
import datetime
import os
from dateutil import parser #pip install python-dateutil
from win32_setctime import setctime #pip install win32-setctime


folder_path = "your_activity_across_facebook"

# Get a list of all HTML files in the folder and its subdirectories that start with "message_"
html_files = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(folder_path)
    for file in files
    if file.lower().endswith(".html") and file.lower().startswith("message_")
]

print("HTML files starting with 'message_' in the folder and its subdirectories:")
for html_file in html_files:
    print(html_file)

    # Read HTML content from the file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all links with href containing "your_activity_across_facebook"
    links = soup.find_all('a', href=lambda x: x and 'your_activity_across_facebook' in x)

    for link in links:
        timestamp_div = link.find_next('div')
        while timestamp_div:
            
            timestamp_div = timestamp_div.find_next('div')
            try:
                d = parser.parse(timestamp_div.text)
                #print(d)
                if isinstance(d, datetime.date):
                    #print(f"Link: {link['href']}, Timestamp: {d}")
                    break
                   
            except:
                pass
        new_timestamp = d
        file_path = link['href']
        
        try:
            os.utime(file_path, times=(new_timestamp.timestamp(), new_timestamp.timestamp()))
            setctime(file_path, d.timestamp())
            print(f"Modification timestamp of {file_path} updated to {new_timestamp}")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error updating timestamp: {e}")
        

