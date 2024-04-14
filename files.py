#with open("dataset_24465_4 (1).txt", "r") as f1, open("textfile2.txt", "w") as f2:
#    lines = f1.readlines()
#    for line in reversed(lines):
#        f2.write(line)

import os
import os.path
import shutil

'''
projdir = os.getcwd()
print(projdir)
downloads = 
os.chdir(downloads)
curr = os.getcwd()
print(curr)
lst = os.listdir()

target = "sample.zip"
backslash = r'/'
target = backslash + target
try:
    shutil.unpack_archive(curr+target, projdir)
except:
    print("Error")
print("sample.zip" in lst)

os.chdir(projdir)'''

from pathlib import Path

key = '.py'

key_dir_set = set()

for current_dir, dirs, files in os.walk("./main"):
    for file in files:
        if Path(file).suffix == key:
            key_dir_set.add(current_dir[2:].replace(r"\\", r"/"))
            break
print(key_dir_set)
key_dir_set = sorted(key_dir_set)
print(key_dir_set)

with open("output.txt", "w") as f:
    f.writelines('\n'.join(key_dir_set))