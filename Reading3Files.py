import threading


def LastLine(inputFileObj):
 inputFile = inputFileObj.readlines()
 print(inputFile[-1])



inputFileObj1 = open("inputFile1.txt","r")
inputFileObj2 = open("inputFile2.txt","r")
inputFileObj3 = open("inputFile3.txt","r")
t1 = threading.Thread(target=LastLine, args=(inputFileObj1,))
t2 = threading.Thread(target=LastLine, args=(inputFileObj2,))
t3 = threading.Thread(target=LastLine, args=(inputFileObj3,))
 
t1.start() 
t2.start() 
t3.start()
t1.join() 
t2.join()
t3.join() 
  
     