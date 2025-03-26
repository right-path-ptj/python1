myDigit = input("입력 진수 결정(16/10/8/2):")

myInput = input("값 입력: ")

if myDigit == "16":
    myInput = int(myInput, 16) 
    
elif myDigit == "10":
    myInput = int(myInput, 10)

elif myDigit == "8":
    myInput = int(myInput, 8)
    
elif myDigit == "2":
    myInput = int(myInput, 2)
    
else:
    print("16/10/8/2 숫자만 입력하세요")
    
print("16진수 ==> ", hex(myInput))
print("10진수 ==> ", myInput)
print("8진수 ==> ", oct(myInput))
print("2진수 ==> ", bin(myInput))
    
    


