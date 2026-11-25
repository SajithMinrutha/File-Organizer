from pathlib import Path

P = Path(".")

# list all sub directories
subdirectory_list = [directories for directories in P.iterdir() if directories.is_dir()]
for sub_directory in subdirectory_list:
    print(sub_directory)
