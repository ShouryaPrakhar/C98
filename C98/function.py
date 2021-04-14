# Made a custom function countwords from file, it counts words written in a file
def countWordsFromFile():
    # we made file name as input 
    fileName = input("Enter the file name:")
    # We made a variable Number of words
    numberOfWords = 0
    # We made file to open file and read it
    file = open(fileName,"r")
    # We made a loop line spliting and to see the number of words
    for line in file:
        words = line.split()
        # Used predefined function len to get length of the list 
        numberOfWords = numberOfWords + len(words)
    # We printed the string with variable 
    print("Number of words:")
    print(numberOfWords)

# We called the custom function we made
countWordsFromFile()