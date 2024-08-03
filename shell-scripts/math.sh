#!/bin/bash

var1=$[ 1 + 5]
var2=$[ $[$var1 / 3 ] + $var1]
echo $var1
echo $var2

# float point solution

variable=` bc << EOF
scale=4
a1 = ($var1 + $var2)
a2 = ($var1 - $var3)
a1 + a2
EOF`
