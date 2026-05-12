def ReadData():
    HighScores = []
    for i in range(7):
        HighScores.append(["", "", ""])
    try:
        f = open("HighScoreTable.txt", "r")
        counter1 = 0
        counter2 = 0
        for line in f:
            HighScores[counter1][counter2] = line.strip()
            counter2 += 1
            if counter2 > 2:
                counter1 += 1
                counter2 = 0
        f.close()
    except FileNotFoundError:
        print("File not found")
    return HighScores

def OutputHighScores(arr):
    for i in range(7):
        line = []
        for j in range(3):
            line.append(arr[i][j])
        outputLine = f"{line[0]} reached a level {line[1]} with a score of {line[2]}"
        print(outputLine)

def SortScores(HighScores):
    highScores = HighScores
    for i in range(7):
        for j in range(6-i):
            if int(highScores[j][1]) < int(highScores[j+1][1]):
                highScores[j], highScores[j+1] = highScores[j+1], highScores[j]
            if int(highScores[j][1]) == int(highScores[j+1][1]):
                if int(highScores[j][2]) < int(highScores[j+1][2]):
                    highScores[j], highScores[j+1] = highScores[j+1], highScores[j]
    return highScores


# main program
HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)