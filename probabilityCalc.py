#Code written by Gabriel Gullidge

from math import comb
from numpy import poly

MAX_TEAMS = 2
TOP_N_RESULTS = 5

def ordinal(n): #code from https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like because I'm lazy :/
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def loadFile():
    fileName = None
    data = {i:[] for i in range(MAX_TEAMS)}
    while fileName is None:
        fileName = input("Enter the file name to use\n")
        try:
            with open(fileName,"r") as f:
                for line in f.readlines():
                    team,value = line.split(",")[:2] # solution currently doesn't use extra data provided by the file
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

    #generate polymonial coefficients, and then calculate the sum of roots
    polyCoeffs = poly(teamData)
    calcs = [polyCoeffs[i]/polyCoeffs[0]*(-1)**i for i in range(len(polyCoeffs))] #the 'ith' value represents the sum of the unique combinations of size i
    for x in range(SIZE,-1,-1):
        calc = calcs[x]
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

tblTeam0 = generateTable(data[0])
tblTeam1 = generateTable(data[1])
team0Name, team1Name,actualScoreline = input("Enter the name of team 0:\n"),input("Enter the name of team 1:\n"),[int(x) for x in input("Please enter the result of the match in the format NUM-NUM:\n").split("-")]
results = {}
for result0 in tblTeam0: #yes, I know I could have done this better
    for result1 in tblTeam1:
        results[str(result0)+"-"+str(result1)] = tblTeam0[result0]*tblTeam1[result1]

sortedResults = sorted(results,reverse=True,key=lambda x: results[x])
sortedResults = {sortedResult: results[sortedResult] for sortedResult in sortedResults}
print(sortedResults)
print("sanity check:",sum([results[x] for x in results])) #sanity check should equal 1
mostLikelyResults = list(sortedResults)[:TOP_N_RESULTS]
print("5 most likely results:",mostLikelyResults,"with probabilities:",[results[x] for x in mostLikelyResults])
team0WinProb, drawProb, team0LoseProb = 0,0,0
for result in results:
    team0, team1 = result.split("-")
    if int(team0) - int(team1) < 0:
        team0LoseProb += results[result]
    elif int(team0) - int(team1) == 0:
        drawProb += results[result]
    else:
        team0WinProb += results[result]
print("Result Outcome Probability (as a percentage), according to xG:")
print("Team 0 Win: %f\nDraw: %f\nTeam 0 Loss: %f" %(team0WinProb*100,drawProb*100,team0LoseProb*100))


#summary of stats
msg = '''%s %d - %d %s
Total xG: %.2f - %.2f
Top %d most likely results:
''' % (team0Name,actualScoreline[0],actualScoreline[1],team1Name,sum(data[0]),sum(data[1]),TOP_N_RESULTS)
for resultNum in range(1,TOP_N_RESULTS+1):
    msg += "%d. %s (%.2f%%)\n" %(resultNum,mostLikelyResults[resultNum-1],round(results[mostLikelyResults[resultNum-1]]*100,3))
msg += """Match Probability:
%s Win: %.2f%%, Draw: %.2f%%, %s Win: %.2f%%""" %(team0Name,round(team0WinProb*100,3),round(drawProb*100,3),team1Name,round(team0LoseProb*100,3))    
stringActualScoreline = str(actualScoreline[0])+"-"+str(actualScoreline[1])
if stringActualScoreline not in mostLikelyResults:
    msg += "\nThe result %s was the %s most likely result (%.2f%%)" %(stringActualScoreline,ordinal(list(sortedResults).index(stringActualScoreline)+1),round(results[stringActualScoreline]*100,3))
print(msg)