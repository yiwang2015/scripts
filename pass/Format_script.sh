#!/bin/bash

if [ $# -lt 1 ];then
	echo -e "$0: file"
	exit
fi

file=$1
if [ ! -f $file ];then
	echo -e "$file not exist"
else
	sed -i "s/\s*$//g" $file
	echo -e "Done format $file"
fi

