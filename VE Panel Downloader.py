import requests
import re
import os
import sys

page_count = int(requests.get("https://api.deconreconstruction.com/pages/count?story.name=vast-error&published_at_null=false").content)#-227

size = page_count * 0.242149073023

print(f"Estimated Disk Space Required: {round(size)} MB")
os.system('pause')

def get_script_folder():
    # path of main .py or .exe when converted with pyinstaller
    if getattr(sys, 'frozen', False):
        script_path = os.path.dirname(sys.executable)
    else:
        script_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return script_path

dir_path = get_script_folder()
output_dir = dir_path + "\\downloaded panels"
DIRECTORY_NAME = "pages"

def download(n):
    if (os.path.isdir(DIRECTORY_NAME) == False):
        os.mkdir(DIRECTORY_NAME)
        print(f"Directory '{DIRECTORY_NAME}' created successfully.")
    for i in range(1, n+1):
        if os.path.isfile(f"pages\\{i}.html"):
            print(f"page {i} exists")
        else:
            print(f"downloading page {i}")
            with open(f"pages\\{i}.html", "w") as pagefile:
                pagefile.write(str(requests.get(f"https://www.deconreconstruction.com/vasterror/{i}").content))
                
download(page_count)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(1, page_count+1):
    # Read the content of the HTML file
    with open(f"pages\\{i}.html", 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Find all image URLs in the HTML content
    image_urls = re.findall(r'(https?://\S+?\.(?:jpg|png|gif|mp4|webp|swf))', html_content)

    # Download images
    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Create a file name based on the image URL
            file_name = os.path.join(output_dir, url.split('/')[-1])
            # Write the image content to the file
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"{file_name} successfully downloaded")
        else:
            print(f"Failed to download image from URL: {url}")

print(f"Panel downloading has complete, panels downloaded to {get_script_folder()}\\downloaded panels.")
os.system('pause')



