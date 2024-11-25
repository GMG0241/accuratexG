#Code written by Gabriel Gullidge

from math import comb, prod
from itertools import combinations

MAX_TEAMS = 2

def loadFile():
    fileName = None
    data = {i:[] for i in range(MAX_TEAMS)}
    while fileName is None:
        fileName = input("Enter the file name to use\n")
        try:
            with open(fileName,"r") as f:
                for line in f.readlines():
                    team,value = line.split(",")
                    data[int(team)].append(float(value))
        except Exception as e:
            print("Cannot find file provided, or file is not structured correctly")
            fileName = None
    return data

def loadInput():
    xG = {}
    for i in range(MAX_TEAMS):
        numEntries = None
        while  numEntries is None or numEntries < 0:
            if numEntries is not None:
                print("Please select a response that is either 0 or greater")
            try:
                numEntries = int(input("Please enter how many entries you have for team %d\n" %(i+1)) )
            except Exception as e:
                print("Please select a response that is either 0 or greater")
        data = []
        for j in range(numEntries):
            entry = None
            while entry is None or entry > 1 or entry < 0 :
                if entry is not None:
                    print("Please select a number which is between 0 and 1 inclusive")
                try:
                    entry = float(input("Please enter xG entry %d for team %d\n" %(j+1,i+1)))
                except Exception as e:
                    print("Please select a number which is between 0 and 1 inclusive")
            data.append(entry)
        xG[i] = data
    return xG

def generateTable(teamData):
    SIZE = len(teamData)
    tablePDF = {}
    for x in range(SIZE,-1,-1):
        perms = combinations(teamData,x)
        calc = sum([prod(y) for y in perms]) #to be improved using matricies
        for i in range(x,SIZE):
            coef = comb(i+1,x)
            calc -= coef*tablePDF[i+1]
        tablePDF[x] = calc
    return tablePDF


print("Welcome to a better way to use xG")
userResponse = None
while userResponse not in range(1,3):
    if userResponse is not None:
        print("Please select a response that is either 1 or 2")
    try:
        userResponse = int(input("Please select how to load your data:\n1. From a file\n2. Manually enter all entries\n"))
    except Exception as e:
        print("Please select a response that is either 1 or 2")
if userResponse == 1:
    data = loadFile()
else:
    data = loadInput()

print("starting team 0")
tblTeam0 = generateTable(data[0])
print("Finished team 0")
print("starting team 1")
tblTeam1 = generateTable(data[1])
print("finished team 1")


