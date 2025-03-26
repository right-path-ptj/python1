select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: "))

if (select == 1):
    exp = input("*** 수식을 입력하세요: ")
    print(exp, "결과는", eval(exp), "입니다.")
    
else:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요: "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요: "))
    
    if (num1 > num2):
        num1, num2 = num2, num1
        
    print("%d+...+%d는 %d입니다." % (num1, num2, sum(range(num1, num2+1))) )
    
    