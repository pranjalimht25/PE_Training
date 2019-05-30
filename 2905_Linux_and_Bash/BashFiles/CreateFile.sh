#!/bin/bash
echo Enter the desired name for file :
read fileName
Fullname=$fileName\_file.txt
touch $Fullname
echo "I am present inside the new file" >> $Fullname 
cat fileName.txt
