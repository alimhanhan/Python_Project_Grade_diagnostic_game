import tkinter
import random
import os



# PyInstaller에 의해 임시폴더에서 실행될 경우 임시폴더로 접근하는 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 버튼 클릭 시 체크한 버튼의 개수를 확인하고 A+ 맞을 확률을 출력해주는 함수
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts += 1
    nekodo = int(100 * pts / 7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", f"<진단결과>\n당신이 A+을 맞을 확률은 {nekodo}%입니다\n {RESULT[pts]}")

    
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("A+ 확률 진단 게임")
    root.resizable(False, False)
    canvas = tkinter.Canvas(root, width=800, height=600)
    canvas.pack()
    img = resource_path("mina2.gif")
    gazou = tkinter.PhotoImage(file=img)
    canvas.create_image(400, 300, image=gazou)
    button = tkinter.Button(text="진단하기", font=("Times New Roman", 32),
                                bg="lightgreen", command=click_btn)
    button.place(x=400, y=480)
    text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
    text.place(x=320, y=30)

    # BooleanVal 객체용 리스트
    bvar = [None] * 7
    # 체크 버튼용 리스트
    cbtn = [None] * 7
    # 체크 버튼 질문 정의
    ITEM = [
        "예습을 한다",
        "복습을 한다",
        "출석을 한다",
        "과제를 미리 해두어야 마음이 놓인다",
        "공지사항을 자주 확인한다",
        "수업시간에 집중을 잘할 수 있다",
        "교수님께 모르는 부분을 바로 질문한다"
    ]
    # 진단 결과 주석을 리스트로 정의
    RESULT = [
        "학사경고를 조심하십시오.",
        "등록금이 아깝군요...",
        "혹시 학교에 놀러다니시나요?",
        "꽤 학생다운 구석이 있습니다.",
        "NOT BAD.",
        "목표를 높게 설정해 보는건 어떨까요?",
        "A+을 향해 조금만 더 노력해보세요~!",
        "A+을 쟁취하는 당신, 혹시 천재?"
    ]

    # 반복해서 체크 버튼 배치
    for i in range(7):
        bvar[i] = tkinter.BooleanVar()
        bvar[i].set(False)
        cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), 
                                        variable=bvar[i], bg="#dfe")
        cbtn[i].place(x=400, y=160 + 40*i)

    root.mainloop()
