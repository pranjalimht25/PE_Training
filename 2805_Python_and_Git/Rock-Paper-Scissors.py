#Rock-Paper-Scissors
def play(ip1, ip2):
 winner=1
 if (ip1 == "Scissors" and ip2 =="Paper" ):  
    winner = 1
 elif (ip1 =="Rock" and ip2 =="Scissors"):
    winner = 1
 elif (ip1 =="Paper" and ip2 =="Rock"):
    winner = 1
 elif (ip2 == "Scissors" and ip1 =="Paper"):
    winner =2
 elif (ip2 == "Rock" and ip1 =="Scissors"):
    winner =2
 elif (ip2== "Paper" and ip1=="Rock"):
    winner =2
 else:
    winner=0
 return winner

ch='y'
while ch=='y':
 a = input("Play your choice - Player1: ")
 b = input("Play your choice - Player2: ") 
 win = play(a,b)
 if(win == 1):
	  print("Congratulations Player1 !!")
 elif(win ==2):
	  print("Congratulations Player2 !!")
 else:
 	 print("Its a Tie!")
 ch = input("To start a new game press 'y' else 'n'")

