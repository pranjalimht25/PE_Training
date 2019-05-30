def binarySearch(aList,l,r, x):
  if r >= l: 
    mid = l + (r - l)/2
    if aList[mid] == x:
        return mid
    elif aList[mid] > x:
        return binarySearch(aList, l, mid-1, x)
    else:
        return binarySearch(aList, mid + 1, r, x)
  else: 
        return -1
 
def main():
 a_list = input("Enter List of elements").split()
 r = len(a_list)
 a_list.sort()
 x = int(input("Enter Element to be searched"))
 idx = binarySearch(a_list,0,r-1,x)
 if idx != -1: 
    print ("Element is present at index % d" % idx )
 else:
    raise Exception ("Element is not found!")

main()