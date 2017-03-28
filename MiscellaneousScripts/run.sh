#!/bin/bash
#Script to perform multiple BNG runs
Folder=$1;
File=$2;
N=$3;
path=$4;
rm -r $Folder #Overwrite
mkdir $Folder 
cd $Folder
for i in $(seq 1 $N)
do
	mkdir "folder$i"
	cd "folder$i"
	cp "../../$File" "./$File"
	echo $i
	perl $path "$File" > "output$i"
	cd ..
done