inFp, outFp = None, None
inStr = ""

# 사용자로부터 파일명 입력받기
src = input("소스 파일명을 입력하세요 : ")
dst = input("타깃 파일명을 입력하세요 : ")

# 파일 열기
inFp = open(src, "r")
outFp = open(dst, "w")

# 파일 내용 읽고 쓰기
inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

# 파일 닫기
inFp.close()
outFp.close()

print(f"--- {src} 파일이 {dst} 파일로 복사되었음 ---")
