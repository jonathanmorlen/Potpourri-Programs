import zipfile
import time
import sys
import os
import subprocess


source = sys.argv[1]
destination = sys.argv[2]
zipname = time.strftime("%m-%d-%Y", time.localtime()) + ".zip"

# Get the size of the folder to be zipped
print("\nInitializing\n")

size = 0
for root, dirs, files in os.walk(source):
    for filename in files:
        path = os.path.join(root, filename)
        size += os.path.getsize(path)

if size < 1024:
    print(f"Compressing {size} bytes\n")
elif size < (1024 * 1024):
    print(f"Compressing {size / 1024:.3f} KB\n")
elif size < (1024 * 1024 * 1024):
    print(f"Compressing {size / 1024 / 1024:.3f} MB\n")

# Add all items to zipped file
relroot = os.path.abspath(os.path.join(source, os.pardir))
z = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
current = 0
for root, dirs, files in os.walk(source):
    z.write(root, os.path.relpath(root, relroot))
    for file in files:
        filename = os.path.join(root, file)
        if os.path.isfile(filename):
            arcname = os.path.join(os.path.relpath(root, relroot), file)
            if size != 0:   # Don't print anything if the source folder is empty
                percent = 100 * current / size
                current += os.path.getsize(filename)
                string = f"\r{percent:>7.2f}% Compressing file: {file}"
                print(string + " " * (90 - len(string)), end="")
            z.write(filename, arcname)
complete = "\r 100.00% Compression complete"
print(complete + " " * (90 - len(complete)), end="")
z.close()

print(f"\n\nTransferring to {destination}\n")
command = f"move {zipname} \"{destination}\">NUL"
subprocess.call(command, shell=True)
print("Transfer complete\n")
