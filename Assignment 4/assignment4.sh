#!/bin/bash
var1=4.5
var2=1.7
floating=$(echo "scale=3; $var1/$var2" | bc)
echo "Our floating variable is $floating and use the options to display the value to have 3 decimal places."
