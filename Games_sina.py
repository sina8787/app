
#کتاب خانه های موزد نیاز
from tkinter import *
import turtle
import time
import random
from tkinter import messagebox
import winsound


#بازی حدس

    
    

        
        
def hads():
    adad = random.randint(1,10)
    print(adad)
    
    def number():

        hads = int(num.get())
        cunt = 0

        for sina1 in range(3):

            if adad == hads:
                lb.config(text='افرین عدد درست است عدد : {}'.format(hads),fg='green')
            elif adad > hads:
                lb.config(text='عدد کوچک است بزرگتر بگو',fg='red')
            elif adad < hads:
                lb.config(text='عدد بزرگ است کوچکتر بگو ',fg='red')

            if cunt == 3:
                lb.config(text='شماباختید',fg='red')

            cunt += 1

    
        
    root = Tk()
    root.title('حدس عدد')
    root.geometry('300x200')


    Label(root,text="یک عدد حدس بزن بین 1 تا 10").pack()
    num = Entry(root)
    num.pack()

    Button(root,text='وارد کردن',command=number).pack()

    lb = Label(root,text='')
    lb.pack()


    
    
    root.mainloop()
            
        

#بازی اهنگین
# تابع دکمه ها برای صدا
def btn1s():
    btn1=sound = winsound.Beep(3000, 150)  

def btn2s():
    btn2=sound = winsound.Beep(3110, 150)

def btn3s():
    btn3=sound = winsound.Beep(3220, 150)

def btn4s():
    btn4=sound = winsound.Beep(3330, 150)

def btn5s():
    btn5=sound = winsound.Beep(3440, 150)

def btn6s():
    btn6=sound = winsound.Beep(3550, 150)

def btn7s():
    btn7=sound = winsound.Beep(3660, 150)

def btn8s():
    btn8=sound = winsound.Beep(3770, 150)

def btn9s():
    btn9=sound = winsound.Beep(3880, 150)

def btn10s():
    btn10=sound = winsound.Beep(3990, 150)

def btn11s():
    btn11=sound = winsound.Beep(1000, 150)

def btn12s():
    btn12=sound = winsound.Beep(1110, 150)

def btn13s():
    btn13=sound = winsound.Beep(1220, 150)

def btn14s():
    btn14=sound = winsound.Beep(1330, 150)

def btn15s():
    btn15=sound = winsound.Beep(1440, 150)

def btn16s():
    btn16=sound = winsound.Beep(1550, 150)

def btn17s():
    btn17=sound = winsound.Beep(1660, 150)

def btn18s():
    btn18=sound = winsound.Beep(1770, 150)

def btn19s():
    btn19=sound = winsound.Beep(1880, 150)

def btn20s():
    btn20=sound = winsound.Beep(1990, 150)

# تابه دکمه اهنگین
def muzic():
    btn1=sound = winsound.Beep(2000, 150)
    sina = Tk()
    sina.title("اهنگین")
    # به صورت اتفاقی یک رنگ را انتخاب میکند
    r1=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r2=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r3=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r4=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r5=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r6=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r7=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r8=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r9=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r10=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r11=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r12=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r13=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r14=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r15=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r16=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r17=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r18=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r19=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])
    r20=random.choice(['red','green','blue','pink','gray','gold','cyan','olive','yellow','orange','purple'])

    #در صفحه 20 تا دکمه ایجاد میکند
    btn1=Button(sina,text=' 1 ', command=btn1s ,font=('bold',20),bg=r1).place(x=0,y=0)
    btn2=Button(sina,text=' 2 ', command=btn2s ,font=('bold',20),bg=r2).place(x=60,y=0)
    btn3=Button(sina,text=' 3 ', command=btn3s ,font=('bold',20),bg=r3).place(x=120,y=0)
    btn4=Button(sina,text=' 4 ', command=btn4s ,font=('bold',20),bg=r4).place(x=180,y=0)
    btn5=Button(sina,text=' 5 ', command=btn5s ,font=('bold',20),bg=r5).place(x=240,y=0)
    btn6=Button(sina,text=' 6 ', command=btn6s ,font=('bold',20),bg=r6).place(x=0,y=60)
    btn7=Button(sina,text=' 7 ', command=btn7s ,font=('bold',20),bg=r7).place(x=60,y=60)
    btn8=Button(sina,text=' 8 ', command=btn8s ,font=('bold',20),bg=r8).place(x=120,y=60)
    btn9=Button(sina,text=' 9 ', command=btn9s ,font=('bold',20),bg=r9).place(x=180,y=60)
    btn10=Button(sina,text='10', command=btn10s ,font=('bold',20),bg=r10).place(x=240,y=60)
    btn11=Button(sina,text='11', command=btn11s ,font=('bold',20),bg=r11).place(x=0,y=120)
    btn12=Button(sina,text='12', command=btn12s ,font=('bold',20),bg=r12).place(x=60,y=120)
    btn13=Button(sina,text='13', command=btn13s ,font=('bold',20),bg=r13).place(x=120,y=120)
    btn14=Button(sina,text='14', command=btn14s ,font=('bold',20),bg=r14).place(x=180,y=120)
    btn15=Button(sina,text='15', command=btn15s ,font=('bold',20),bg=r15).place(x=240,y=120)
    btn16=Button(sina,text='16', command=btn16s ,font=('bold',20),bg=r16).place(x=0,y=180)
    btn17=Button(sina,text='17', command=btn17s ,font=('bold',20),bg=r17).place(x=60,y=180)
    btn18=Button(sina,text='18', command=btn18s ,font=('bold',20),bg=r18).place(x=120,y=180)
    btn19=Button(sina,text='19', command=btn19s ,font=('bold',20),bg=r19).place(x=180,y=180)
    btn20=Button(sina,text='20', command=btn20s ,font=('bold',20),bg=r20).place(x=240,y=180)
    #اندازه صفحه
    sina.geometry('300x250')

#بازی دوز

#در اینجا پلیر را با رندوم مساوی میکنیم ومیگیم از بین ایکس و او یکی را به صورت رندوم انتخاب کند
player = random.choice(['o','x'])
#در اینجا رنگ او را ابی و رنگ ایکس را قرمز میکنیم
color = {'o':'blue', 'x':'red'}
board= [[],[],[]]
#در اینجا کلیر را برای تکینتر تعریف میکنیم تا بشناسد
def clear():
    global player
    global board
    #در اینجا یک حلقه تکرار ایجاد میکنیم که سه بارای وسه بارجی تکرار شود 
    for i in range(3):
        for j in range(3):
            #ای صفحه خالی و جی صفحه بعداز پر شدن است است 
            board[i][j]["text"]=" "
            board[i][j]["state"]=NORMAL
            #پلیر از بین ایکس و او به صورت رندوم انتخواب میشود 
    player= random.choice(['o','x'])       
#در اینجا کلیک را تعریف میکنیم که ردیفی و ستونی است
def click(row, col):
    global player
    global color
    global board
    
    board[row][col].config(text=player, state=DISABLED, disabledforeground=color[player])
    for i in range(3):
        # در خانه های مشخص شده این کد برنده بازی را اعلام میکند
        if (board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"]==player
            or board[0][i]["text"]==board[1][i]["text"]==board[2][i]["text"]==player):
            messagebox.showinfo("بازی تمام", "برنده شد" +player)
            clear()
            # در این کد در خانه های مشخص شده برنده را اعلام میکند
        if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]==player
            or board[0][2]['text']==board[1][1]["text"]==board[2][0]["text"]==player):
            messagebox.showinfo("بازی تمام", "برنده شد" +player)
            clear()
            #در اینجا اگر هیچ بازی کنی برنده نشود به بازیکن ها اطلاع میدهد که کسی نبرده است
        elif (board[0][0]["state"]==board[0][1]["state"]==board[0][2]["state"]==DISABLED
            and board[1][0]["state"]==board[1][1]["state"]==board[1][2]["state"]==DISABLED
            and board[2][0]["state"]==board[2][1]["state"]==board[2][2]["state"]==DISABLED):
            messagebox.showinfo("بازی تمام", "مساوی")
            clear()
            #در این کد به بازی کنان مشخص میکند که کدام بازی کن نفراول شروع خواهد کرد
    if player=='x':
       player ='o'
    else:
        player ='x'
        

def Doze():
    sound = winsound.Beep(2000, 150)
    #این کد صفحه ای ایجاد میکند
    tkwindow=Tk()
    tkwindow.title("بازی دوز")

    #تمام باتن ها, مکعب هایی که قرارایکس و او در انها قرار بگیرن رو میسازن
    button1= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(0,0))
    button1.grid(row=0, column=0)
    board[0].append(button1)

    button2= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(0,1))
    button2.grid(row=0, column=1)
    board[0].append(button2)

    button3= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(0,2))
    button3.grid(row=0, column=2)
    board[0].append(button3)

    button4= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(1,0))
    button4.grid(row=1, column=0)
    board[1].append(button4)

    button5= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(1,1))
    button5.grid(row=1, column=1)
    board[1].append(button5)

    button6= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(1,2))
    button6.grid(row=1, column=2)
    board[1].append(button6)

    button7= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(2,0))
    button7.grid(row=2, column=0)
    board[2].append(button7)

    button8= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(2,1))
    button8.grid(row=2, column=1)
    board[2].append(button8)

    button9= Button(tkwindow, text=' ', font='Times 20 bold', bg='light gray', height=3, width=6 , command=lambda: click(2,2))
    button9.grid(row=2, column=2)
    board[2].append(button9)
    #این کد برای باز شدن و بسته نشدن صفحه ما است
    tkwindow.mainloop()

# بازی مار
# اینحا کل کد بازی مار را داخل تابع میگزارم
def Snake():
    sound = winsound.Beep(2000, 150)
    delay = 0.1

    # امتیاز
    score = 0
    high_score = 0

    # ساخت صفحه و تنظیمات
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0) # خاموش کردن اپدیت صفحه

    # تنظیمات سر مار
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # ساخت غذای مار
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # نمیاش امتیازه های بازی 
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("bold", 24, "normal"))

    # توابع و تنظیمات حرکت مار
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # وردوی های کیبورد برای حرکت مار
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # گزاشتن بازی داخل حلقه بی پایان
    while True:
        wn.update()

        # اینجا چک میکنه ببینه به دیوار خورده یا نه
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # مخفی کردن بخش های بدن مار
            for segment in segments:
                segment.goto(1000, 1000)

            # پاک کردن بدن مار
            segments.clear()

            # پاک کردن امتیازه بازی
            score = 0

            # پاک کردن تاخیر
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("bold", 24, "normal"))


        # اینجا چک میکنه چه غدا خورده یا نه
        if head.distance(food) < 20:
            # اضافه کردن غذا به نقشه به صورت تصادفی
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # اضافه کردن بخش های بدن
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("black")
            new_segment.penup()
            segments.append(new_segment)

            # کوتاه کردن تاخیر
            delay -= 0.001

            # اضافه کردن امتیاز بعد از خوردن غذا
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("bold", 24, "normal"))

        # بعد از مردن به جای اول خود برمیگرد
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # بخش های بدن را به جایی که سر است منتقل میکند
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()

        # برسی کردن خوردن سر به بدن
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                # مخفی کردن بدن
                for segment in segments:
                    segment.goto(1000, 1000)

                # پاک کردن بدن
                segments.clear()

                # تنظیم مجدد امتیاز
                score = 0

                # تنظیم مججد تاخیر
                delay = 0.1

                # تازه کردن امتیاز بعد از گرفتن امتیاز
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("bold", 24, "normal"))
        # شروع کردن با تاخیر تنظیم شده
        time.sleep(delay)

    wn.mainloop()

def about2():
    btn1=sound = winsound.Beep(2000, 150)
    top2 = Tk()
        # ساخت یک لیست
    Lb2 = Listbox(top2,font=('bold',13))
        # اضافه کردن متن به لیست
    Lb2.insert(1, " بازی حدس عدد یک بازی سالم است که این بازی هم برای "  )
    Lb2.insert(2, "اوقات فراغت و هم برای اموزش اعداد که کدام بزرگ تر ")
    Lb2.insert(3, "یا کوچک تر هست خوب است")
    Lb2.insert(4, "")
    Lb2.insert(5, "بازی دوز یک بازی فکری است که بازیکنان با انتخاب")
    Lb2.insert(6, "خانه ای ان خانه مال ان بازی کن خواهد شد اما باید")
    Lb2.insert(7, "یازیکنان حرکتشان را به خوبی انجام دهند تا نبازند")
    Lb2.insert(8, "")
    Lb2.insert(9, "بازی مار یک بازی دو بعدی است که چون دارای")
    Lb2.insert(10, "صحنه های خشونت امیز نیست بازی خیلی خوبی برای ")
    Lb2.insert(11, "بازی کردن هست")
    Lb2.insert(12, "")
    Lb2.insert(13, "بازی اهنگین یک بازی هست که کودکان زیر ده سال ")
    Lb2.insert(14, " میتوانند با ان موسیقی یاد بگیرندوسرگرم شوند")
    Lb2.insert(15, "")
    Lb2.insert(16, "بازی حدس عدد بازی فکری هست که زهن بازیکن را به خود جذب ")
    Lb2.insert(16, "میکند تابافکر کردن عدد درست را حدس بزند و برنده شود")



    Lb2.pack(fill=X)
      # پر کردن محور عرض
    Lb2.pack(fill=X)
    # اندازه صفحه
    top2.geometry('500x200')
    # بستن تغیر اندازه صفحه
    top2.resizable(width=True,height=True)
    # انداختن صفحه به حلقه
    top2.mainloop()

# صفحه اصلی برنامه
# تابع معرفی
def about():
    btn1=sound = winsound.Beep(2000, 150)
    # باز کردن صفحه
    top = Tk()

    # ساخت یک لیست
    Lb1 = Listbox(top,font=('bold',13))
    # اضافه کردن متن به لیست
    Lb1.insert(1, "Sina attarabbasi : سازنده")
    Lb1.insert(2, "sinaattarabbasi833@gmail.com : ایمیل")
    Lb1.insert(3, "مدرسه : شاهد شهید دوستان")
    Lb1.insert(4, "معلم مربوطه :اقای حسن رضایی")
    Lb1.insert(5, "winsound / Tkinter / turtle : فریم ورک ها")
    Lb1.insert(6, "                         V1.0         ")

    # پر کردن محور عرض
    Lb1.pack(fill=X)
    # اندازه صفحه
    top.geometry('300x200')
    # بستن تغیر اندازه صفحه
    top.resizable(width=False,height=False)
    # انداختن صفحه به حلقه
    top.mainloop()


colors = {'green':'#95eb34',
    'bule':'#7c80fc',
    'purple':'#d09dfc',
    'yellow':'#eef202',
    'cyan' :'#67dbb5'}

serv_lis = ['bule','purple','yellow','cyan']
scv = random.choice(serv_lis)
color = colors[scv]


home = Tk()
# گزاشتن اسم صفحه
home.title("Home")

home.configure(bg=color)

# گزاشتن دکمه
Button(home,text='بازی مار', command=Snake, font=('bold',20),width=10).place(x=15,y=380)
Button(home,text='بازی دوز', command=Doze, font=('bold',20),width=10).place(x=215,y=380)
Button(home,text='بازی اهنگین', command=muzic, font=('bold',20),width=10).place(x=80,y=180)
Button(home,text='بازی حدس عدد',command=hads, font=('bold',20),width=10).place(x=68,y=240)
# گزاشتن برچسب
Label(home,text="V1.0",font=("bold",11)).place(x=565,y=380)

button_btn = Button(home,text='درباره ما', command=about)
# فعال کردن دکمه در صفحه
button_btn.pack()

button_btn2 = Button(home,text='درباره بازی ها', command=about2).place(x=112, y=30)

home.resizable(width=False,height=False)
home.geometry('400x450')

home.mainloop()


##########################################################################################
##########################################################################################
##########################################################################################





import tkinter as tk
import random

class SumGame:
    def __init__(self, master):
        self.master = master
        master.title("Sum Game")

        self.number = random.randint(1, 10)
        self.current_sum = 0

        self.sum_label = tk.Label(master, text="Current Sum: {}".format(self.current_sum))
        self.sum_label.pack()

        self.button_1 = tk.Button(master, text="1", command=lambda: self.add_number(1))
        self.button_1.pack(side=tk.LEFT)

        self.button_2 = tk.Button(master, text="2", command=lambda: self.add_number(2))
        self.button_2.pack(side=tk.LEFT)

        self.button_3 = tk.Button(master, text="3", command=lambda: self.add_number(3))
        self.button_3.pack(side=tk.LEFT)

        self.button_4 = tk.Button(master, text="4", command=lambda: self.add_number(4))
        self.button_4.pack(side=tk.LEFT)

        self.button_5 = tk.Button(master, text="5", command=lambda: self.add_number(5))
        self.button_5.pack(side=tk.LEFT)

        self.button_6 = tk.Button(master, text="6", command=lambda: self.add_number(6))
        self.button_6.pack(side=tk.LEFT)

        self.button_7 = tk.Button(master, text="7", command=lambda: self.add_number(7))
        self.button_7.pack(side=tk.LEFT)

        self.button_8 = tk.Button(master, text="8", command=lambda: self.add_number(8))
        self.button_8.pack(side=tk.LEFT)

        self.button_9 = tk.Button(master, text="9", command=lambda: self.add_number(9))
        self.button_9.pack(side=tk.LEFT)

        self.button_10 = tk.Button(master, text="10", command=lambda: self.add_number(10))
        self.button_10.pack(side=tk.LEFT)

    def add_number(self, number):
        self.current_sum += number
        self.sum_label.config(text="Current Sum: {}".format(self.current_sum))

        if self.current_sum == self.number:
            self.sum_label.config(text="You win!")
            self.disable_buttons()

    def disable_buttons(self):
        self.button_1.config(state=tk.DISABLED)
        self.button_2.config(state=tk.DISABLED)
        self.button_3.config(state=tk.DISABLED)
        self.button_4.config(state=tk.DISABLED)
        self.button_5.config(state=tk.DISABLED)
        self.button_6.config(state=tk.DISABLED)
        self.button_7.config(state=tk.DISABLED)
        self.button_8.config(state=tk.DISABLED)
        self.button_9.config(state=tk.DISABLED)
        self.button_10.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = SumGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

##########################################################################################
#############################################################################################
##############################################################################################



