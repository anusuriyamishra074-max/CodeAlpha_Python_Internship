import os
import shutil

source = "Photos"
destination = "JPG_Files"

if not os.path.exists(source):
    os.mkdir(source)

if not os.path.exists(destination):
    os.mkdir(destination)

count = 0

for file in os.listdir(source):

    if file.lower().endswith(".jpg"):

        old_path = os.path.join(source, file)
        new_path = os.path.join(destination, file)

        shutil.move(old_path, new_path)

        print(file, "moved successfully!")
        count += 1

if count == 0:
    print("No JPG files found!")

print("Task completed!")