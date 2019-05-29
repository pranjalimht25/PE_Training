def last(n):
    return n[-1]  
 
def sort(tuples):
    return sorted(tuples, key=last)


ch='y'
aList = []
while ch =='y':
 print("Enter the tupple values")
 TuppleVar = tuple(int(x.strip()) for x in input().split(','))
 aList.append(TuppleVar)
 #sort(aList)
 aList.sort(key=lambda x: x[-1])
 print("Sorted Tupples are :")
 print(aList)
 ch = input("Enter 'y' to continue adding tupples")

