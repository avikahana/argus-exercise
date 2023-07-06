# import datetime
# import platform

# # Get the current date and time
# current_date = datetime.datetime.now().strftime("%d-%m-%Y")
# current_time = datetime.datetime.now().strftime("%H:%M:%S")

# # Get the operating system name
# os_name = platform.system()

# # Get the operating system version
# os_version = platform.release()

# # Formated data
# data = f"date: {current_date}, time: {current_time}, os_name: {os_name}, os_version: {os_version}"
# print(data)
# # File name
# file_path = "info.txt"

# # Open the file in write mode
# with open(file_path, "w") as file:
#     file.write(data)


import platform
import subprocess

# Get operating system information
os_name = platform.system()
os_version = platform.version()

# Get current date and time
date_output = subprocess.check_output(["date"]).decode().strip()

# Print Current date & time
print("Current Date and Time:", date_output)

# Print OS name & version
print("Operating System:", os_name, "| OS Version:", platform.release())