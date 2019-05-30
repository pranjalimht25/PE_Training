#!/bin/bash
echo Enter 2 integers
read -r a  b
let sum=$a+$b
let diff=$a-$b
let prod=$a*$b
let quot=$a/$b
echo Sum is $sum
echo Diff is $diff
echo Product is $prod
echo Quotient is $quot

