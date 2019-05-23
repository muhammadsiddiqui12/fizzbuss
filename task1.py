filename = input("Enter filename")
pages = input("Enter pages you want to copy(seperated by commas)")
pageslist = pages.split(",")
lineNumber = 0


def isLineInPage():
    for x in pageslist:
        lowerLimit = 1 + ((int(x) - 1) * 25)
        upperLimit = 25 + ((int(x) - 1) * 25)
        if lineNumber >= lowerLimit and lineNumber <= upperLimit:
            return True
