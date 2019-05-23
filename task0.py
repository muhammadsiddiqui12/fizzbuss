for x in range(100):
    currentNumber = x + 1
    printString = currentNumber
    if currentNumber % 5 == 0 and currentNumber % 3 == 0:
        printString = "FizzBuzz"
    elif currentNumber % 5 == 0:
        printString = "Buzz"
    elif currentNumber % 3 == 0:
        printString = "Fizz"

    print(printString)

