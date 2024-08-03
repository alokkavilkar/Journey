#!/bin/bash

if date
then
	echo `date`
fi

var1='vagrant'
if grep $var1 /etc/passwd
then
	ls -al /home/$var1/.b*
fi

var1=10
var2=20
if [ $var1 -gt 5 ]
then
	echo $var1 is greater than 5
fi

var1="vagrant"

if [[ $var1 == "vagrant" ]]
then
	echo "user matched"
fi

var2=""
if [ -z $var2 ]
then
	echo "$var2 has length zero"
fi

if [ -e "$HOME" ]
then
	echo "its a directory"
fi

var1=10
var2=20
if (( $var2 > $var1 ))
then
	(( var2++ ))
	echo $var2
	echo $var1 is greater
fi


if ! (( $var2 > 22 )) 
then
	echo $var2 is not greated than 22
fi
