from datetime import datetime

import random

def middle(a, b):
    if (debug):
      print ("middle: Entering function middle(" , a , ", " , b , ")")
    if(b > a):
        c = round(a+((b-a)/2))
        if (debug):
          print ("middle: Exiting function middle(" , a , ", " , b , ") = ", c)
        return c
    elif(b < a):
        c = b+((a-b)/2)
        if (debug):
          print ("middle: Exiting function middle(" , a , ", " , b , ") = ", c)
        return c
    else:
        if (debug):
          print ("middle: Exiting function middle(" , a , ", " , b , ") = ", b)
        return b

def midRandom(a, b):
    if (debug):
      print ("midRandom: Entering function middle(" , a , ", " , b , ")")
    if(b > a):
        if(a + 1 == b):
            c = b
        else:
            c = random.randint(a+1, b-1)
        if (debug):
          print ("midRandom: Exiting function middle(" , a , ", " , b , ") = ", c)
        return c
    elif(b < a):
        if(b+1 == a):
            c = a
        else:
            c = random.randint(b+1, a-1)
        if (debug):
          print ("midRandom: Exiting function middle(" , a , ", " , b , ") = ", c)
        return c
    else:
        if (debug):
          print ("midRandom: Exiting function middle(" , a , ", " , b , ") = ", b)
        return b


def findClosestLowerGuess(list):
    if (debug):
          print ("findClosestLowerGuess: Entering function findClosestLowerGuess(" , list , ")")
    length = len(list)
    lastguess = list[length-1]
    nexthighestguess = list[0]
    i = 0
    while (nexthighestguess > lastguess):
        nexthighestguess = list[i]
        if(i < length):
            i = i+1
        else:
            if (debug):
              print ("findClosestLowerGuess: Exiting with an error in findClosestLowerGuess( " , list, ")")
            return -1
    for x in list:
        if(x < lastguess):
            if(x > nexthighestguess):
                nexthighestguess = x
    if (debug):
          print ("findClosestLowerGuess: Exiting function findClosestLowerGuess(", list, ") = ", nexthighestguess)
    return nexthighestguess

def findClosestHigherGuess(list):
    if (debug):
          print ("findClosestHigherGuess: Entering function findClosestHigherGuess(" , list , ")")
    length = len(list)
    lastguess = list[length-1]
    nextlowestguess = list[0]
    i = 0
    while (nextlowestguess < lastguess):
        nextlowestguess = list[i]
        if(i < length):
            i = i+1
        else:
            if (debug):
                print ("findClosestHigherGuess: Exiting with an error in findClosestHigherGuess( " , list, ")")
            return -1
    for x in list:
        if(x > lastguess):
            if(x < nextlowestguess):
                nextlowestguess = x
    if (debug):
          print ("findClosestHigherGuess: Exiting function findClosestHigherGuess(", list ,") =", nextlowestguess)
    return nextlowestguess

def max(list):
    if (debug):
          print ("max: Entering function max(" , list , ")")
    num = list[0]
    for x in list:
        if(x > num):
            num = x
    return num

def min(list):
    if (debug):
          print ("min: Entering function min(" , list , ")")
    num = list[0]
    for x in list:
        if(x < num):
            num = x
    if (debug):
          print ("min: Exiting function min(" , list , ") = ", num)
    return num

def guessTheNumberBinary(answer, space):
    i = 0
    guessList = []
    guessList.append(middle(0, space))
    if (debug):
          print ("guessTheNumberBinary: Before while True Loop with i = ", i)
    if(answer == guessList[i]):
        return i+1
    elif(answer > guessList[i]):
        i = i+1
        guessList.append(middle(guessList[i-1], space))
    elif(answer < guessList[i]):
        i = i+1
        guessList.append(middle(0, guessList[i-1]))
    while i < space:
        if (debug):
            print ("guessTheNumberBinary: Entering while loop with i = ", i, ", guessList = ", guessList)
        if(answer == guessList[i]):
            return i+1
        elif(answer > guessList[i]):
            if(guessList[i] == max(guessList)):
                guessList.append(middle(guessList[i], space))
                i = i+1
            else:
                guessList.append(middle(guessList[i], findClosestHigherGuess(guessList)))
                i = i+1
        elif(answer < guessList[i]):
            if(guessList[i] == min(guessList)):
                guessList.append(middle(0, guessList[i]))
                i = i+1
            else:
                guessList.append(middle(findClosestLowerGuess(guessList), guessList[i]))
                i = i+1

# def guessTheNumberBinaryOrRandom(answer, space):
    



def guessTheNumberRandom(answer, space):
    i = 0
    guessList = []
    guessList.append(midRandom(0, space))
    if (debug):
          print ("guessTheNumberRandom: Before while True Loop with i = ", i)
    if(answer == guessList[i]):
        return i+1
    elif(answer > guessList[i]):
        i = i+1
        guessList.append(midRandom(guessList[i-1], space))
    elif(answer < guessList[i]):
        i = i+1
        guessList.append(midRandom(0, guessList[i-1]))
    while i < space:
        if (debug):
            print ("guessTheNumberRandom: Entering while loop with i = ", i, ", guessList = ", guessList)
        if(answer == guessList[i]):
            return i+1
        elif(answer > guessList[i]):
            if(guessList[i] == max(guessList)):
                guessList.append(midRandom(guessList[i], space))
                i = i+1
            else:
                guessList.append(midRandom(guessList[i], findClosestHigherGuess(guessList)))
                i = i+1
        elif(answer < guessList[i]):
            if(guessList[i] == min(guessList)):
                guessList.append(midRandom(0, guessList[i]))
                i = i+1
            else:
                guessList.append(midRandom(findClosestLowerGuess(guessList), guessList[i]))
                i = i+1

def guessTheNumberTrulyRandomWithList(answer, space):
    i = 1
    guessList = []
    randGuess = random.randint(1, space)    
    if (debug):
        print ("guessTheNumberTrulyRandomWithList: Before while Loop with answer = ", answer)
    while (randGuess != answer):
        randGuess = random.randint(1, space)
        if (debug):
            print ("guessTheNumberTrulyRandomWithList: In while True Loop with guess = ", randGuess) 
            print("contains: called ", i, " times with list size ", len(guessList))
        if (contains(guessList, randGuess)):
            continue
        else:
            guessList.append(randGuess)
            i = i+1
    return i
   
def guessTheNumberSequential(answer, space):
    i = 1
    if (debug):
      print ("guessTheNumberSequential: Before while True Loop with i = ", i)
    while (i != answer):
        i = i+1
    return i

def guessTheNumberTrulyRandom(answer, space):
    i = 1
    randGuess = random.randint(1, space)    
    if (debug):
      print ("guessTheNumberTrulyRandom: Before while True Loop with i = ", i)
    while (randGuess != answer):
        randGuess = random.randint(1, space)
        i = i+1
    return i


def spaceLoopRandom(space):
    #print ("spaceLoopRandom: Entering function spaceLoop with space = " , space)
    numOfGuesses = []
    i = 1
    while (i < space+1):
        #print ("spaceLoopRandom: Space " , space, " Iteration ", i)
        numberOfGuesses = guessTheNumberRandom(i, space)
        numOfGuesses.append(numberOfGuesses)
        i = i+1
    return numOfGuesses

def spaceLoopTrulyRandomWithList(space):
    #print ("spaceLoopTrulyRandomWithList: Entering function spaceLoop with space = " , space)
    numOfGuesses = []
    i = 1
    while (i < space+1):
        if(debug):
            print ("spaceLoopTrulyRandomWithList: Space " , space, " Iteration ", i)
        numberOfGuesses = guessTheNumberTrulyRandomWithList(i, space)
        numOfGuesses.append(numberOfGuesses)
        i = i+1
    return numOfGuesses

def spaceLoopBinary(space):
    #print ("spaceLoopBinary: Entering function spaceLoop with space = " , space)
    numOfGuesses = []
    i = 1
    while (i < space+1):
        #print ("spaceLoopBinary: Space " , space, " Iteration ", i)
        numberOfGuesses = guessTheNumberRandom(i, space)
        numOfGuesses.append(numberOfGuesses)
        i = i+1
    return numOfGuesses

def spaceLoopTrulyRandom(space):
    #print ("spaceLoopTrulyRandom: Entering function spaceLoop with space = " , space)
    numOfGuesses = []
    i = 1
    while (i < space+1):
        #print ("spaceLoopTrulyRandom: Space " , space, " Iteration ", i)
        numberOfGuesses = guessTheNumberTrulyRandom(i, space)
        numOfGuesses.append(numberOfGuesses)
        i = i+1
    return numOfGuesses

def spaceLoopSequential(space):
    #print ("spaceLoopSequential: Entering function spaceLoop with space = " , space)
    numOfGuesses = []
    i = 1
    while (i < space+1):
        #print ("spaceLoopSequential: Space " , space, " Iteration ", i)
        numberOfGuesses = guessTheNumberSequential(i, space)
        numOfGuesses.append(numberOfGuesses)
        i = i+1
    return numOfGuesses


def contains(list, element):
    if (debug):
        print ("contains: In function with list = ", list, " and element = ", element)
    for x in list:
        if(x == element):
            return True
    return False

def addList(list):
  sum = 0
  length = len(list)
  i = 0
  while i < length:
    sum = sum + list[i]
    i = i + 1
  return sum

def averageList(list):
  avg = addList(list) / len(list)
  return avg


debug = False
space = 1000
i = 1
print("GuessGame.py starting loop with max space = ", space)
print("Algorithm, space, average guess count, time to compute")
while (i < space + 1):
    # Compute the Binary Search First
    start = datetime.now()
    guesses = spaceLoopBinary(i)
    avgBinary = averageList(guesses)
    end = datetime.now()
    timeBinary = end - start
    # Now we have avgBinary and timeBinary
    print("Binary, ", i, ",", avgBinary, ",", timeBinary)

    # Compute the Random Search Next
    start = datetime.now()
    guesses = spaceLoopRandom(i)
    avgRandom = averageList(guesses)
    end = datetime.now()
    timeRandom = end - start
    # Now we have avgRandom and timeRandom
    print("Random/Smart, ", i, ",", avgRandom, ",", timeRandom)

    # Compute the Sequential Search Next
    if(i<1000001):
        start = datetime.now()
        guesses = spaceLoopSequential(i)
        avgSequential = averageList(guesses)
        end = datetime.now()
        timeSequential = end - start
    # Now we have avgSequential and timeSequential
        print("Sequential/Linear, ", i, ",", avgSequential, ",", timeSequential)

    if(i < 10001):
        # Compute the TrulyRandom Search next
        start = datetime.now()
        guesses = spaceLoopTrulyRandom(i)
        avgTrulyRandom = averageList(guesses)
        end = datetime.now()
        timeTrulyRandom = end - start
        # Now we have avgTrulyRandom and timeTrulyRandom
        print("Random/Simple, ", i, ",", avgTrulyRandom, ",", timeTrulyRandom)

        # Compute the TrulyRandomWithMemory Search Last
        start = datetime.now()
        guesses = spaceLoopTrulyRandomWithList(i)
        avgTrulyRandomWithList = averageList(guesses)
        end = datetime.now()
        timeTrulyRandomWithList = end - start
        # Now we have avgTrulyRandom and timeTrulyRandomWithList
        print("Random/SimpleWithList, ", i, ",", avgTrulyRandomWithList, ",", timeTrulyRandomWithList)

    i = i * 10