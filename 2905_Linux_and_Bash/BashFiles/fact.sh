#!/bin/bash
echo Enter a number
read x
fact=1
while [ $x -gt 1 ]
do
  fact=$((fact * x)) 
  let x--     
done

echo $fact

