#!/bin/bash

file="states"
IFS=$'\n'

for state in `cat $file`
do
	echo $state
done

IFS=$':'
file='state2'
for file in `cat $file`
do
	echo $file
done

file='state2'
IFS=$'\n':;

while IFS= read -r line
do
	echo $line	
done < $file

if [ -d $HOME ]
then
	echo "files in directory $HOME are "
	
	for file in $HOME/*
	do
		echo $file
	done
fi

count=0

while (( $count < 10 ))
do
	echo $count
	(( count++ ))
done

