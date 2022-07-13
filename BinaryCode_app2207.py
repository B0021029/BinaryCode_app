#python
# Binary_code app
#  YIC情報ビジネス専門学校
#　　情報システム科　2年
#　　　倉成　郁子
#     (B0021029@ib.yic.ac.jp)




import tkinter 

code = [0, 0, 0, 0, 0, 0, 0, 0]
Q = 1
correct = 0
total = 0


#数値ボタンクリック関数
def click_btn0():
    if button0['text'] == '0':
        button0['text'] = '1'
        code[7] = 1
    else:
        button0['text'] = '0'
        code[7] = 0
    

def click_btn1():
    if button1['text'] == '0':
        button1['text'] = '1'
        code[6] = 2
    else:
        button1['text'] = '0'
        code[6] = 0

def click_btn2():
    if button2['text'] == '0':
        button2['text'] = '1'
        code[5] = 4
    else:
        button2['text'] = '0'
        code[5] = 0

def click_btn3():
    if button3['text'] == '0':
        button3['text'] = '1'
        code[4] = 8
    else:
        button3['text'] = '0'
        code[4] = 0

def click_btn4():
    if button4['text'] == '0':
        button4['text'] = '1'
        code[3] = 16
    else:
        button4['text'] = '0'
        code[3] = 0

def click_btn5():
    if button5['text'] == '0':
        button5['text'] = '1'
        code[2] = 32
    else:
        button5['text'] = '0'
        code[2] = 0

def click_btn6():
    if button6['text'] == '0':
        button6['text'] = '1'
        code[1] = 64
    else:
        button6['text'] = '0'
        code[1] = 0

def click_btn7():
    if button7['text'] == '0':
        button7['text'] = '1'
        code[0] = 128
    else:
        button7['text'] = '0'
        code[0] = 0

#進行ボタンコマンド
def click_btnP():
    global Q, code
    if buttonP['text'] == 'START':
        label1['text'] = Q
        buttonP['text'] = 'JUDGE'
    elif buttonP['text'] == 'JUDGE':
        judge_code()
        if label3['text'] == '正解！！':
            buttonP['text'] = 'NEXT'
        else:                        #不正解の時はもう一度チャレンジできるようにする
            buttonP['text'] = 'JUDGE'
    elif buttonP['text'] == 'NEXT':  #NEXTボタンはコードボタンとコードリスト初期化する
        label3['text'] = ''
        button0['text'] = '0'
        button1['text'] = '0'
        button2['text'] = '0'
        button3['text'] = '0'
        button4['text'] = '0'
        button5['text'] = '0'
        button6['text'] = '0'
        button7['text'] = '0'
        buttonP['text'] ='JUDGE'
        code = [0, 0, 0, 0, 0, 0, 0, 0]
        if label1['text'] == '255':
            buttonP['text'] = 'FINISH!'
        elif label1['text'] == 'FINISH!':
            buttonP['text'] = 'START'           
        else:
            Q = questionCode()
            label1['text'] = Q
            buttonP['text'] = 'JUDGE'

#問題決定関数
def questionCode():
    global Q
    if Q < 255:
        Q = Q + 1
    return Q

#判定関数
def judge_code():
    global correct, total, code
    total += 1
    qes = int(label1['text'])
    ans = sum(code)
    print(qes, ans)
    print(code)
    if qes == ans:
        label3['text'] = '正解！！'
        correct += 1
    else:
        label3['text'] = '不正解！！'
    #正解率表示    
    score = '{} / {}'.format(correct, total)
    label2['text'] = score
   
                    
    
root = tkinter.Tk()
root.geometry('900x600')
root.title('Binary_code Learning')

#問題表示ラベル
label1 = tkinter.Label(root, text='', font=('Times New Roman', 50), bg='white')
label1.place(x=320, y=50, width=250, height=150)

#正解率ラベル
label2 = tkinter.Label(root, text='', font=('Times New Roman', 20))
label2.place(x=630, y=50, width=170, height=70)

#判定ラベル
label3 = tkinter.Label(root, text='', font=('Times New Roman', 40), fg='red')
label3.place(x=320, y=200, width=250, height=150)




#binary_codeボタン
button7 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn7)
button6 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn6)
button5 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn5)
button4 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn4)
button3 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn3)
button2 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn2)
button1 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn1)
button0 = tkinter.Button(root, text='0', font=('Times New Roman', 30), command=click_btn0)
buttonP = tkinter.Button(root, text='START', font=('Times New Roman', 20),command=click_btnP)

#ボタン配置
button7.place(x=15, y=350, width=100, height=200)
button6.place(x=125, y=350, width=100, height=200)
button5.place(x=235, y=350, width=100, height=200)
button4.place(x=345, y=350, width=100, height=200)
button3.place(x=455, y=350, width=100, height=200)
button2.place(x=565, y=350, width=100, height=200)
button1.place(x=675, y=350, width=100, height=200)
button0.place(x=785, y=350, width=100, height=200)
buttonP.place(x=100, y=80, width=100, height=50)


root.mainloop()