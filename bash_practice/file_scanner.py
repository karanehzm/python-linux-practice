
import sys 
from pathlib import Path
import datetime


len_cmlA = len(sys.argv)
if len_cmlA < 2:
    print("Please provide a directory path")
    sys.exit(1)


directory = Path(sys.argv[1])
print(f"Scanning directory: {directory}")

if not directory.is_dir():
    print("Invalid directory")
    sys.exit(1)


for files in directory.rglob("*.py"):
    info = files.stat()
    print(files, f"size of the file: {info.st_size}, last modification: {datetime.date.fromtimestamp(info.st_mtime)}")



