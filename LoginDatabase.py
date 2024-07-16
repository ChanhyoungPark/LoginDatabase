import pandas as pd
import pymysql
from tkinter import *
import tkinter
from tkinter import messagebox
import tkinter.ttk as ttk

w = Tk()
w.title("상품관리 데이터베이스")
w.geometry('1200x1000')
w.resizable(width=False, height=False)

def login_confirm(inputid, inputpw):
    connect = pymysql.connect(host='localhost',
                              user='root',
                              passwd='1234',
                              db='상품판매db',
                              charset='utf8')

    cursor = connect.cursor()

    sql = "SELECT id, pass, 구분 FROM 고객 WHERE ID='" + inputid + "';"
    cursor.execute(sql)
    resultSearch = cursor.fetchone()

    global label3, label4

    if label3:
        label3.place_forget()

    if label4:
        label4.place_forget()

    if resultSearch is None:
        label3 = tkinter.Label(w, text="회원 정보가 없습니다.", fg='red')
        label3.place(x=530, y=550)

    elif resultSearch[2] == "사용자":
        messagebox.showinfo("경고", "접근 권한이 없습니다.")

    elif resultSearch[0] == inputid and resultSearch[1] == inputpw:
        identification.place_forget()
        label1.place_forget()
        password.place_forget()
        label2.place_forget()
        b1.place_forget()
        login_title.place_forget()

        def clear():
            for widget in w.winfo_children():
                widget.place_forget()

            conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')

            sql = "SELECT 고객번호, id, pass, 성별, 주소, 우편번호, 전화번호, 휴대폰번호, 구분 FROM 고객 ;"


            treeview = ttk.Treeview(w, columns=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"],
                                    displaycolumns=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"])
            treeview.pack()

            treeview.column("zero", width=90, anchor="center")
            treeview.heading("zero", text="고객번호")

            treeview.column("one", width=90, anchor="center")
            treeview.heading("one", text="id")

            treeview.column("two", width=90, anchor="center")
            treeview.heading("two", text="pass")

            treeview.column("three", width=90, anchor="center")
            treeview.heading("three", text="성별")

            treeview.column("four", width=90, anchor="center")
            treeview.heading("four", text="주소")

            treeview.column("five", width=90, anchor="center")
            treeview.heading("five", text="우편번호")

            treeview.column("six", width=90, anchor="center")
            treeview.heading("six", text="전화번호")

            treeview.column("seven", width=90, anchor="center")
            treeview.heading("seven", text="휴대폰번호")

            treeview.column("eight", width=90, anchor="center")
            treeview.heading("eight", text="구분")


            treeview["show"] = "headings"

            cur = conn.cursor()
            cur.execute(sql)
            line = cur.fetchall()
            conn.close()

            customer = pd.DataFrame(line)

            for i, row in customer.iterrows():
                treeview.insert('', 'end', values=row.tolist())

        button_customer = Button(w, text="고객관리", width=20, height=5, command=clear)
        button_customer.pack()
        button_customer.place(x=300, y=450)

        button_product = Button(w, text="상품관리", width=20, height=5)
        button_product.pack()
        button_product.place(x=750, y=450)

    else:
        label4 = Label(w, text="아이디 또는 비밀번호를 확인하세요.", fg='red')
        label4.place(x=500, y=550)


login_title = tkinter.Label(w, text="Login", font=50)
login_title.pack()
login_title.place(x=570, y=310)

b1 = Button(w, text="로그인", width=10, height=2, command=lambda: login_confirm(identification.get(), password.get()))
b1.pack()
b1.place(x=550, y=600)

identification = tkinter.Entry(w)
identification.place(x=550, y=400)

label1 = tkinter.Label(w, text="ID")
label1.place(x=500, y=400)

password = tkinter.Entry(w, show="*")
password.place(x=550, y=500)

label2 = tkinter.Label(w, text="Pw")
label2.place(x=500, y=500)

label3 = None

label4 = None

w. mainloop()