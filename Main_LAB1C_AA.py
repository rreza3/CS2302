""" #Reza, Raul: I really like the header of the lab, I'll implement it myself for future labs
Alexis Aguirre
CS2302: Lab 1, Option C (Decrypting Passowrds)
Due on: 9/13/18
Lab goes over recursion applications in generating large amounts of password
combinations and then hashing to decrypt a given set of hashed passwords.
"""
import hashlib 
from pathlib import Path

usersFile = Path("C:/Users/aagui/Documents/UTEP 6th Semester/CS2302 Data Structures/Lab 1/1.3 Passwords/1.3 Passwords/password_file.txt")       # File path with slashes edited, may be different on different OS #Reza, Raul: Keep in mind it won't be compatible even in another computer, not just different OS
hashedRecords = []      # Will hold data from given passwords file
passwords = []      # Will hold decrypted passwords
minLength = 3
maxLength = 5


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def lookupPassword(numString):  # Method checks if current combination is a password in the records
    for h in range(len(hashedRecords)):
        if (hash_with_sha256(numString + hashedRecords[h][1]) == hashedRecords[h][2]):
            passwords.append(hashedRecords[h][0] + ' password is: ' + numString + hashedRecords[h][1])      # If found, appended to passwords list, and then record is deleted from hashedRecords so that we are not redundantly checking
            del hashedRecords[h]
            return


def recPermu(currString, strLength, possChar):      # Method generates combination by first getting to appropriate length, then cycling through possible combinations by changing one digit at a time
    if (strLength > 0):                             # Ex. 000, 001, 002, 002 .... 009, 010, 011 012 ..... 999
        for i in range(possChar):
            recPermu(currString + str(i), strLength - 1, possChar)
    elif (strLength == 0):
#        if (int(currString)%200000 == 0):  # Used to keep track of calls . #Reza, Raul: I like the way you tested your method here
#            print(currString)
        lookupPassword(currString)


def main():
    f = open(usersFile, 'r')    # Reading from file
    currLine = f.readline()
    while currLine != '':
        currLine = currLine.strip()     #Stripping newline characters to avoid errors when checking passwords, and then splitting seperating data in file
        lineElements = currLine.split(',')
        hashedRecords.append(lineElements)
        currLine = f.readline()
    
    for i in range(minLength, maxLength + 1):   # Method can be updated depenging on required lengths
        recPermu('', i, 10)

    for j in range(len(passwords)): # Outputs decrypted passwords
        print(passwords[j])

main()
