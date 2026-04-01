WordArray = [] # global array of string
NumberWords = 0 # global

def ReadWords(filenameP):
    global WordArray, NumberWords
    try:
        f = open(filenameP, "r")
        for line in f:
            WordArray.append(line.strip())
            NumberWords += 1
    except FileNotFoundError:
        print("File not found")
    NumberWords -= 1
    Play()


def Play():
    global WordArray, NumberWords
    print(WordArray[0], NumberWords)
    word = input("Enter a word: ")
    counter = 0
    while word != "no":
        flag = False
        for i in range(len(WordArray)):
            if word == WordArray[i]:
                counter += 1
                WordArray[i] = None
                flag = True
                break
        if flag:
            print("Answer")
        else:
            print("Not an answer")
        word = input("Enter a word: ")
    print(counter/(len(WordArray)-1)*100)
    for i in range(len(WordArray)):
        if WordArray[i] != None:
            print(WordArray[i])

# main program
level = input("easy, medium or hard? ")
if level == "easy":
    ReadWords("Easy.txt")
elif level == "medium":
    ReadWords("Medium.txt")
else:
    ReadWords("Hard.txt")