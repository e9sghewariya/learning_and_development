

#!/bin/bash
# - Task4: Size of directories - shell
#     1. Take a directory path as an input from user.
#     2. Find and display size of all subdirectories on this path.

read -p "Enter directory path: " dir
if [ -d "$dir" ]; then
    du -sh "$dir"/*
else
    echo "Invalid directory."
fi
