from tkinter import *

## 전역 변수 선언 부분 ##
fnameList = [
    "1.gif", "2.gif", "3.gif", "4.gif", "5.gif",
    "6.gif", "7.gif", "8.gif", "9.gif"
]
num = 0

## 함수 선언 부분 ##
def updateImage():
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.config(text=fnameList[num])  # 파일명 갱신

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    updateImage()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    updateImage()

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)
nameLabel = Label(window, text=fnameList[0])  # 파일명 표시 라벨

photo = PhotoImage(file=fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=200, y=10)
nameLabel.place(x=320, y=15)  # 버튼 사이 위치
btnNext.place(x=440, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
