#!/bin/bash
echo Enter three sides of triangle
read -r x y z
if   [ $x -eq $y ] && [ $x -eq $z ]
 then echo "It's an Equilateral Triangle"
elif [ $x -eq $y ] || [ $y -eq $z ] || [ $x -eq $z ]        
 then echo "It's an Isosceles Triangle"
else
  echo "It's a Scalene Triangle"
fi
