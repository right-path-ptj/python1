inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for i, inStr in enumerate(inList, 1):
    print("%d: %s" % (i, inStr), end="")

inFp.close()
