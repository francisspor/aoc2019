def setupPointers(currentIndex):
    global opcode, operand1, operand2, outputTarget
    opcode = currentIndex
    operand1 = currentIndex + 1
    operand2 = currentIndex + 2
    outputTarget = currentIndex + 3

puzzleInput = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0'
#puzzleInput = '1,9,10,3,2,3,11,0,99,30,40,50'
puzzleInput =  [int(x) for x in puzzleInput.split(",")]
print (puzzleInput)

#1202 it
puzzleInput[1] = 12
puzzleInput[2] = 2

currentIndex = 0

while True:
    setupPointers(currentIndex)

    # addition
    if puzzleInput[opcode] == 1:
        puzzleInput[puzzleInput[outputTarget]] = puzzleInput[puzzleInput[operand1]] + puzzleInput[puzzleInput[operand2]]
    #multiplication
    elif puzzleInput[opcode] == 2:
        puzzleInput[puzzleInput[outputTarget]] = puzzleInput[puzzleInput[operand1]] * puzzleInput[puzzleInput[operand2]]
    #stop
    elif puzzleInput[opcode] == 99:
        print("exit")
        break
        #stop
    
    print (puzzleInput)
    currentIndex += 4

print (puzzleInput[0])


puzzleInput = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0'
#puzzleInput = '1,9,10,3,2,3,11,0,99,30,40,50'
puzzleInput =  [int(x) for x in puzzleInput.split(",")]
print (puzzleInput)

for noun in range (0,99):
    for verb in range (0,99):

        currentIndex = 0
        thisRun = puzzleInput
        thisRun[1] = noun
        thisRun[2] = verb
            
        while True:
            setupPointers(currentIndex)

            # addition
            if thisRun[opcode] == 1:
                thisRun[thisRun[outputTarget]] = thisRun[thisRun[operand1]] + thisRun[thisRun[operand2]]
            #multiplication
            elif thisRun[opcode] == 2:
                thisRun[thisRun[outputTarget]] = thisRun[thisRun[operand1]] * thisRun[thisRun[operand2]]
            #stop
            elif thisRun[opcode] == 99:
                print("hi")
                break
                #stop
            
            print (thisRun)
            currentIndex += 4

        if (thisRun[0] == 19690720):
            print (noun)
            print (verb)
            break
            break
    