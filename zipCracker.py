import zipfile
import sys

try :
    fp = zipfile.ZipFile(sys.argv[1])        	#Associates ZipFile With fp
    wordlist = open(sys.argv[2],'r')         	#Associates Wordlist File With wordlist
except Exception :
    print("Usage : python zipCracker.py ZipFile WorlistFile")
    exit(-1)					#Exits Program

for line in wordlist :               		#Reading Passwords From Wordlist
    passwd = line.strip("\n")			#Strips newline Character From Password
    try:
        fp.extractall(pwd=bytes(passwd,'utf-8'))    	#Try Password, If Incorrect Password, Bad_Password Exception Will Raise
        print("Password Cracked!\t: "+passwd)	#Prints Password
        wordlist.close()
        exit(0)					#Exits Program, If Password Found
    except Exception :
        pass					#Pass The Control To Check For Next Password In The Wordlist
    
wordlist.close()
print("Password Not Found!")                    #If Wordlist Doesn't Contains The Correct Password
