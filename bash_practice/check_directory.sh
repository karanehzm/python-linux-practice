#!/bin/bash

dir_path="$1"
if [ -z "$dir_path" ];then
echo "Error: No directory provided"
exit 1
fi

if [ -d "$dir_path" ];then
echo "Directory provided: $dir_path"
else
echo "Directory doesnt exist"
exit 1

fi







