import re 
import logging 
 
#Creating a Log File, to store logs during the program 
logging.basicConfig(filename='PasswordValidationLog.log',level=logging.DEBUG) 
 
#Validate : Logic Implementation for Password Validation 
def validate (pwd): 
 x=0 
 x = len(pwd) 
# Regex uses Lookahead (?=.*) to look for the presence of required characters in whole string  
 pattern = '^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])([a-zA-Z0-9#$@]+)$'     
#Check for the given Constraints and Update Log file accordingly 
 if (x >=6 and x <= 12): 
   match = re.search(pattern,pwd) 
   if (match): 
    print (" Valid") 
    logging.info(" Password is Valid") 
   else: 
       print ("Not Valid") 
       logging.warning(" Password is Not Valid") 
 else: 
   print ('Not Valid') 
   logging.warning(" Password is Not Valid") 

 
#Main function to take Input and Control flow of the program by calling Validate function 
def main(): 
 pwd = input("Enter password for Validation : ")  
 logging.info(" Password entered by user is:%s" %pwd) 
 validate(pwd) 
 
main() 
 
 