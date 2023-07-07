import datetime
import os
import platform

# Get the current date and time
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# Get the operating system name
os_name = platform.system()

# Get the operating system version
os_version = platform.release()

# Formated data
data = f"date: {current_date}, time: {current_time}, os_name: {os_name}, os_version: {os_version}"
print(data)
# File name
file_path = "/app/info.txt"
print(os.getcwd())
# Open the file in write mode
with open(file_path, "w") as file:
    file.write(data)

# The path for listing items
path = '.'
 
# The list of items
files = os.listdir(path)

# Loop to print each filename separately
for filename in files:
    print(filename)