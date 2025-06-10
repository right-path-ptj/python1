inFp = None
inStr = ""

inFp = open("C:/Temp/data1.txt", "r")

lineNo = 1
for inStr in inFp:
    print("%d: %s" % (lineNo, inStr), end="")
    lineNo += 1

inFp.close()
