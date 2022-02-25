import random
from tkinter import *
import tkinter as tk 
from datetime import datetime
#from PIL import ImageTk, Image
root = tk.Tk()
root.title("Сапер")
root.geometry("1200x1200")
root['bg']='#778899'



setin = tk.Toplevel()
setin.withdraw()

win = tk.Toplevel()
win.withdraw()

about = tk.Toplevel()
about.withdraw()

press_f = tk.Toplevel()
press_f.withdraw()
#Переменные
#way = os.getcwd()
#image_path = os.path.join(way,'image.png')
a=8
ayx=8
by=10
lasya=a
lasayx=ayx
u = 30
levelcount = 12
od = 0
dyshno = 0
tent = 0
k22 = 0
help1= ''#
tem = 0#
k1 = 0
gg = 0 
kkool = []#Массив для уровней
#photo1 = ("C:\\Users\\dimky\\Desktop\\game\\image2.jpg")
#image1 = ImageTk.PhotoImage(Image.open(photo1))

#photo2 = ("C:\\Users\\dimky\\Desktop\\game\\image3.png")
#image2 = ImageTk.PhotoImage(Image.open(photo2))




#Создание массивов в функциях


def check_min(a,fi):
	for i in range(ayx):
		for j in range(a):
			if fi[i][j]!='x':
				fi[i][j]=0

	for i in range(ayx):
		for j in range(a):
			if fi[i][j]!='x':
				if j<a-1 and fi[i][j+1]=='x':
					fi[i][j]+=1
               
				if i<ayx-1 and fi[i+1][j]=='x':
					fi[i][j]+=1
                
				if j>0 and fi[i][j-1]=='x':
					fi[i][j]+=1
               
				if i>0 and fi[i-1][j]=='x':
					fi[i][j]+=1
                    
				if i<ayx-1 and j<a-1 and fi[i+1][j+1]=='x':
					fi[i][j]+=1
                
				if i>0 and j>0 and fi[i-1][j-1]=='x':
					fi[i][j]+=1
                
        
				if i>0 and j<a-1 and fi[i-1][j+1]=='x':
					fi[i][j]+=1

        
				if i<ayx-1 and j>0 and fi[i+1][j-1]=='x':
					fi[i][j]+=1

def colour_change(fi):
	global a
	global ayx
	for i in range(ayx):
		for j in range(a):
			#print("mini =",mins[i][j]['text'])
			#print("masiv = ",fi[i][j])
			if fi[i][j] == 0:
				mins[i][j].config(fg='green')
			elif fi[i][j] == 1:
				mins[i][j].config(fg='#008B8B')

			elif fi[i][j] == 'x':
				mins[i][j].config(fg='black')

			elif fi[i][j] == 2:
				mins[i][j].config(fg='#B8860B')

			elif fi[i][j] == 3:
				mins[i][j].config(fg='#483D8B')

			elif fi[i][j] == 4:
				mins[i][j].config(fg='#FF1493')

			elif fi[i][j] == 5:
				mins[i][j].config(fg='#FF4500')

			elif fi[i][j] == 6:
				mins[i][j].config(fg='#8B4513')

			elif fi[i][j] == 7:
				mins[i][j].config(fg='#4B0082')

			elif fi[i][j] == 8:
				mins[i][j].config(fg='#808080')
	#print("END")




def field(a,by,*ickl):#Массив с полем сапера
	global mm
	global forloose
	mm=set()
	nympy = 0
	for ny in ickl:
		nympy = ny
	if nympy>0:
		#print(nympy)
		ber=((nympy-1)//a)
		rer=((nympy-1)%a)
		#print("ber",ber, "rer=",rer)
		for i in range(3):
			for j in range(3):
				cyi = ber+i-1
				cyj = rer+j-1
				if cyi>-1 and cyi<ayx and cyj>-1 and cyj<a:
					lend = (cyi*a)+cyj+1
					mm.add(lend)
					#print("massiv =",mm)

	f = [[0 for i in range(a)] for j in range(ayx)]
	forloose = [[0 for i in range(a)] for j in range(ayx)]
	for i in range(by):
		y = random.randint(1,a*ayx)
		if y in mm:
				while y in mm:
					y = random.randint(1,a*ayx)
		mm.add(y)
		b=((y-1)%a)
		r=((y-1)//a)
		f[r][b] = 'x'
		forloose[r][b]=10
	return f

def mass():
	global fi
	global mins
	hp = [[0 for i in range(a)]for j in range(ayx)]
	return hp

def label(a):
	global fi
	global mins
	fi = field(a,by)
	check_min(a,fi)
	mins = [[Label(root, text=fi[j][i],font=('arial 14 bold'),bg='silver',fg='red',activebackground='green',activeforeground='red') for i in range(a)] for j in range(ayx)]
	return mins

def labelb(num):	
	global a
	global ayx
	global kkool
	global forloose
	kkool = fullfi[num-1]
	forloose = [[0 for i in range(a)] for j in range(ayx)]
	for i in range(a):
		for j in range(ayx):
			if kkool[i][j] == 'x':
				forloose[i][j]=10


	mins = [[Label(root, text=kkool[j][i],font=('arial 14 bold'),bg='silver',fg='red',activebackground='green',activeforeground='red') for i in range(a)] for j in range(ayx)]
	return mins

def VI_KA():
	root.after_cancel(help1)
	win.deiconify()
	win['bg']='silver'
	wintext = Label(win,text="YOU WIN IN "+ str(f_tem),width=20,height=2,font=('Courier 20 bold'),fg='red')
	wintext.grid(row=1,column=1)
	ok = Button(win,text="Окей",font=('times 10 bold'),fg='#006400',bg='#FFC0CB',width = 20,height=2, command=lambda: win.withdraw())
	ok.grid(row=2,column=1)




def flag(mx,bx,but):
	global k1
	global mins
	global by
	global forloose
	if but[mx][bx]['text'] == "":
		but[mx][bx]['text'] = "F"
		but[mx][bx].config(state='disabled')
		k1+=1

	else: 
		but[mx][bx]['text'] = ""
		but[mx][bx].config(state='normal')
		k1-=1
	
	tablo['text'] = by-k1

def reflect(fik,mik):
	global a
	global ayx
	global by
	global k0
	global tent
	setin.withdraw()
	if mik-2 == 0 or mik-2==1:
		by = 5
	elif mik-2 == 2:
		by=8
	elif mik-2 == 3:
		by=10
	elif mik-2 == 4 or mik-2==5:
		by=16
	elif mik-2 == 6 or mik-2==7:
		by=24
	elif mik-2 == 8 or mik-2==9:
		by=32
	elif mik-2 == 10 or mik-2==11:
		by=40
	mer = mik//2
	a = mer*2+4
	ayx = mer*2+4
	rest(mik-1)
	tent=mik-1


def seting():
	setin.deiconify()
	level = [Button(setin, text=i+1,font=('arial 14 bold'),bg='silver',fg='red',activebackground='green',activeforeground='red',width=10) for i in range(levelcount)]
	for i in range(levelcount):
		level[i].grid(row=i,column=1)
		level[i].config(command=lambda k=fullfi[i],mik=i+2: reflect(k,mik))


def infor():
	about.deiconify()
	about['bg']='#778899'
	infor2 = Label(about,text='Игру разработал стундент 1 курса Кузнецов Дмитрий Владимирович из 159 группы, факультета РТФ.\n В рамках курсовой работы.',font=('times 14 bold'),fg='#2F4F4F',bg='#00FFFF')
	infor2.grid(row=1,column=1)
	clos = Button(about,text="Понятно",font=('times 14 bold'),width=20,height=5,fg='#2F4F4F',bg='#FFC0CB',command=lambda: about.withdraw())
	clos.grid(row=2,column=1)

#Глобальные переменные
hp = mass()
fi=[]
mm=set()
k0 = 0
im=1


def butt(a):
	global but
	but = [[Button(root, text='',font=('arial 14 bold'),bg='silver',fg='red',activebackground='green',activeforeground='red') for i in range(a)] for j in range(ayx)]
	return but


#Вызов функций для создания массивов


	
mins = label(a)
but = butt(a)
onee=StringVar()
twoo=StringVar()
minaas = StringVar()



#Создание кнопок
about1 = Button(root, text='Info',width=3,height=1,font=('arial 10 bold'),bg='silver',fg='#8B4513',activebackground='white',activeforeground='red',command=lambda: infor())
about1.place(x=570,y=0,width=30,height=20)

set11 = Button(root, text='Уровни',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='#00008B',activebackground='white',activeforeground='red',command=lambda: seting())
set11.place(x=35,y=300,width=120,height=25)

dis1 = Label(root,text='',width=3,height=1,font=('Ubuntu 14 bold'),bg='#00BFFF',fg='red')
dis1.place(x=0,y=190,width=2000,height=5)

dis2 = Label(root,text='',width=3,height=1,font=('Ubuntu 14 bold'),bg='#00BFFF',fg='red')
dis2.place(x=190,y=190,width=5,height=1000)

dis3 = Label(root,text='',width=3,height=1,font=('Ubuntu 14 bold'),bg='#00BFFF',fg='red')
dis3.place(x=600,y=0,width=5,height=195)

time = Label(root,text='00:00',width=3,height=1,font=('Ubuntu 14 bold'),bg='silver',fg='red')
time.place(x=70,y=220,width=60, height=20)

proc = Label(root,text='Процент мин',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='black')
proc.place(x=410,y=30,width=160, height=20)

znach = Label(root,text='',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='black')
znach.place(x=465,y=52,width=50, height=20)

chislmin = Entry(root,font=('arial 11 bold'),textvariable=minaas,bg='#00FF00')
chislmin.place(x=285,y=52,width=30, height=20)

minname = Label(root,text='Количество мин',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='black')
minname.place(x=220,y=30,width=160, height=20)

namee = Label(root,text='Размер поля',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='black')
namee.place(x=30,y=30,width=160, height=20)

propusk = Label(root,text='x',width=3,height=1,font=('arial 14 bold'),bg='#808080',fg='black')
propusk.place(x=100,y=52,width=20, height=20)

pole2 = Entry(root,font=('arial 11 bold'),textvariable=twoo,bg='#00FF00')
pole2.place(x=120,y=52,width=20, height=20)

pole1 = Entry(root,font=('arial 11 bold'),textvariable=onee,bg='#00FF00')
pole1.place(x=80,y=52,width=20, height=20)	

exit = Button(root, text='Exit',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='red',activebackground='white',activeforeground='red',command=lambda: dest())
exit.place(x=200+((a-2)/2)*u,y=200+(ayx+1)*u,width=u*2, height=u+5)

res = Button(root, text='Again',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='green',activebackground='white',activeforeground='green',command=lambda gr=tent: rest(tent))
res.place(x=200+((a-2)/2)*u,y=150,width=u*2	)

prinat = Button(root, text='Изменить размер',width=3,height=1,font=('arial 12 bold'),bg='silver',fg='green',activebackground='white',activeforeground='green',command=lambda: taketext())
prinat.place(x=115,y=90,width=150,height=30)

#Создание лейблов
tablo = Label(root,text='',width=3,height=1,font=('arial 14 bold'),bg='silver',fg='white',activebackground='white',activeforeground='red')
tablo.place(x=100+(a+2)*u+u,y=150,width=u, height=u)
#Циклы для наглядности



for i in range(a):
	for j in range(ayx):
		but[j][i].place(x=200+i*u,y=200+j*u,width=u,height=u)
		mins[j][i].place(x=200+i*u,y=200+j*u,width=u,height=u)	

for i in range(ayx):
	for j in range(a):
		global dm
		global km
		but[i][j].config(command=lambda mx=i,bx=j,kk=but: click22(mx,bx,but))
		but[i][j].bind("<Button-3>", lambda event,mx=i,bx=j,kk=but: flag(mx,bx,but))
		mins[i][j].bind("<Button-1>", lambda event,mx=i,bx=j,kk=mins: clicklabel(mx,bx,mins))



#Мясо
tablo['text'] = by
fi1=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1], ['x', 2, 0, 1, 'x', 2], ['x', 2, 0, 2, 3, 'x'], [1, 1, 0, 1, 'x', 2]]#click 2.2
fi2=[[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 'x'], [1, 1, 1, 0, 1, 1], [2, 'x', 1, 0, 1, 1], ['x', 2, 1, 0, 2, 'x'], [1, 1, 0, 0, 2, 'x']]
fi3=[[0, 0, 1, 'x', 'x', 1, 0, 0], [0, 0, 1, 2, 3, 2, 1, 0], [1, 1, 1, 0, 1, 'x', 1, 0], [2, 'x', 2, 0, 1, 1, 1, 0], [3, 'x', 2, 0, 0, 0, 0, 0], ['x', 2, 1, 1, 1, 1, 0, 0], [2, 2, 0, 1, 'x', 1, 0, 0], ['x', 1, 0, 1, 1, 1, 0, 0]]
fi4=[[0, 0, 0, 0, 0, 0, 1, 'x'], [0, 0, 0, 1, 2, 2, 2, 1], [0, 0, 1, 2, 'x', 'x', 2, 0], [1, 1, 1, 'x', 4, 'x', 2, 0], ['x', 2, 2, 2, 2, 1, 1, 0], [2, 3, 'x', 1, 1, 1, 1, 0], [1, 'x', 2, 1, 1, 'x', 2, 1], [1, 1, 1, 0, 1, 2, 'x', 1]]
fi5=[[0, 0, 0, 1, 'x', 2, 2, 'x', 1, 0], [0, 0, 1, 2, 3, 'x', 3, 2, 2, 0], [0, 1, 2, 'x', 2, 1, 2, 'x', 1, 0], [2, 3, 'x', 2, 1, 0, 1, 2, 2, 1], ['x', 'x', 4, 2, 1, 0, 0, 1, 'x', 1], ['x', 'x', 3, 'x', 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 3, 'x', 1, 0, 0, 0], [0, 0, 0, 1, 'x', 2, 1, 0, 0, 0], [0, 1, 1, 2, 1, 1, 0, 1, 1, 1], [0, 1, 'x', 1, 0, 0, 0, 1, 'x', 1]]
fi6=[[0, 0, 1, 'x', 'x', 1, 0, 0, 0, 0], [0, 0, 1, 2, 3, 2, 1, 0, 0, 0], [0, 0, 0, 0, 1, 'x', 1, 0, 1, 1], [0, 0, 1, 1, 2, 1, 1, 0, 2, 'x'], [0, 1, 2, 'x', 1, 0, 0, 0, 2, 'x'], [1, 3, 'x', 3, 2, 1, 2, 1, 2, 1], [2, 'x', 'x', 3, 2, 'x', 2, 'x', 1, 0], ['x', 4, 2, 2, 'x', 2, 2, 1, 1, 0], ['x', 2, 0, 1, 2, 2, 1, 0, 1, 1], [1, 1, 0, 0, 1, 'x', 1, 0, 1, 'x']]
fi7=[[0, 0, 0, 0, 0, 0, 0, 1, 'x', 3, 'x', 2], [0, 0, 1, 1, 1, 1, 2, 3, 3, 4, 'x', 2], [0, 0, 1, 'x', 1, 2, 'x', 'x', 3, 'x', 2, 1], [1, 1, 2, 1, 1, 3, 'x', 6, 'x', 2, 1, 0], [1, 'x', 1, 0, 0, 2, 'x', 'x', 3, 1, 0, 0], [2, 3, 2, 1, 0, 2, 4, 'x', 3, 2, 1, 1], ['x', 2, 'x', 1, 0, 2, 'x', 4, 'x', 2, 'x', 1], [1, 2, 1, 1, 0, 2, 'x', 3, 1, 2, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 'x', 3], ['x', 1, 1, 1, 1, 0, 0, 0, 0, 2, 'x', 'x'], [1, 1, 1, 'x', 1, 0, 0, 0, 0, 1, 2, 2]]
fi8=[[0, 0, 0, 1, 'x', 'x', 2, 1, 1, 0, 1, 1], [0, 0, 0, 1, 2, 3, 3, 'x', 1, 1, 2, 'x'], [0, 0, 0, 0, 0, 1, 'x', 3, 2, 1, 'x', 2], [1, 1, 0, 1, 1, 2, 2, 'x', 1, 1, 1, 1], ['x', 2, 0, 1, 'x', 1, 1, 1, 1, 0, 0, 0], ['x', 2, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1], [1, 1, 1, 'x', 1, 1, 'x', 2, 1, 2, 'x', 2], [1, 1, 2, 1, 2, 3, 4, 'x', 1, 2, 'x', 2], [2, 'x', 2, 0, 1, 'x', 'x', 3, 2, 1, 1, 1], [4, 'x', 3, 0, 1, 2, 3, 'x', 2, 1, 0, 0], ['x', 'x', 2, 0, 0, 0, 1, 3, 'x', 2, 0, 0], [2, 2, 1, 0, 0, 0, 0, 2, 'x', 2, 0, 0]]
fi9=[[0, 0, 1, 'x', 1, 1, 'x', 'x', 2, 'x', 'x', 3, 'x', 1], [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 'x', 2, 1], [0, 0, 0, 0, 0, 0, 0, 1, 'x', 1, 1, 2, 2, 1], [1, 1, 0, 0, 0, 0, 1, 2, 3, 2, 1, 1, 'x', 1], ['x', 1, 1, 1, 1, 0, 1, 'x', 3, 'x', 1, 1, 1, 1], [1, 1, 1, 'x', 1, 0, 2, 3, 'x', 3, 2, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 'x', 4, 'x', 2, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1, 1, 3, 'x', 2, 0, 0, 0], ['x', 2, 0, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0], ['x', 2, 0, 1, 'x', 3, 'x', 3, 1, 1, 1, 2, 1, 1], [1, 1, 1, 2, 2, 3, 'x', 'x', 2, 3, 'x', 3, 'x', 1], [0, 0, 1, 'x', 3, 3, 3, 2, 2, 'x', 'x', 3, 1, 1], [2, 2, 2, 2, 'x', 'x', 1, 0, 1, 2, 2, 1, 0, 0], ['x', 'x', 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]]
fi10=[[0, 0, 1, 1, 1, 0, 0, 1, 'x', 2, 2, 'x', 2, 'x'], [0, 0, 1, 'x', 2, 2, 1, 2, 1, 2, 'x', 3, 3, 2], [1, 1, 1, 2, 'x', 3, 'x', 3, 1, 1, 1, 2, 'x', 1], ['x', 2, 0, 1, 1, 3, 'x', 'x', 2, 1, 1, 2, 1, 1], ['x', 3, 1, 1, 1, 1, 3, 'x', 2, 1, 'x', 2, 1, 0], ['x', 2, 1, 'x', 1, 0, 1, 1, 1, 1, 2, 'x', 1, 0], [1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1], [0, 2, 'x', 3, 1, 0, 0, 0, 1, 1, 1, 0, 1, 'x'], [1, 3, 'x', 'x', 1, 1, 1, 2, 2, 'x', 1, 0, 1, 1], ['x', 2, 2, 2, 1, 1, 'x', 2, 'x', 2, 1, 0, 0, 0], [1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 0, 0], [0, 1, 'x', 'x', 1, 1, 1, 1, 0, 2, 'x', 2, 0, 0], [1, 2, 3, 2, 1, 1, 'x', 1, 0, 2, 'x', 3, 1, 1], [1, 'x', 1, 0, 0, 1, 1, 1, 0, 1, 1, 2, 'x', 1]]
fi11=[[0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0], [0, 0, 0, 1, 'x', 1, 1, 1, 2, 'x', 'x', 2, 0, 1, 2, 2], [0, 0, 0, 1, 1, 1, 1, 'x', 2, 3, 'x', 2, 1, 2, 'x', 'x'], [1, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 2, 2, 'x', 5, 'x'], [1, 'x', 'x', 1, 1, 1, 1, 0, 0, 0, 0, 1, 'x', 2, 3, 'x'], [1, 2, 3, 2, 2, 'x', 1, 0, 0, 0, 0, 2, 2, 2, 1, 1], [0, 0, 2, 'x', 3, 1, 1, 0, 0, 0, 0, 1, 'x', 1, 0, 0], [0, 0, 2, 'x', 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1], [1, 1, 3, 2, 2, 2, 'x', 4, 'x', 1, 1, 'x', 1, 1, 'x', 2], [2, 'x', 2, 'x', 1, 2, 'x', 'x', 2, 1, 1, 1, 2, 2, 3, 'x'], ['x', 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 2, 'x', 2, 1], [1, 1, 0, 1, 'x', 1, 0, 0, 0, 0, 1, 'x', 2, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [2, 'x', 2, 0, 1, 1, 2, 1, 1, 0, 1, 2, 2, 1, 0, 0], [3, 'x', 3, 1, 2, 'x', 3, 'x', 2, 1, 2, 'x', 'x', 1, 0, 0], [2, 'x', 2, 1, 'x', 3, 'x', 2, 2, 'x', 2, 2, 2, 1, 0, 0]]
fi12=[[0, 0, 0, 1, 1, 1, 0, 1, 'x', 'x', 2, 1, 0, 1, 'x', 1], [0, 0, 0, 1, 'x', 1, 0, 1, 2, 3, 'x', 2, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 'x', 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 3, 3, 1, 0, 0], [1, 1, 0, 0, 0, 1, 'x', 2, 1, 1, 1, 'x', 'x', 1, 0, 0], ['x', 1, 0, 0, 0, 1, 1, 3, 'x', 2, 1, 2, 3, 2, 1, 0], [1, 1, 0, 0, 1, 1, 1, 2, 'x', 2, 1, 1, 2, 'x', 1, 0], [0, 0, 0, 1, 2, 'x', 3, 3, 3, 3, 3, 'x', 2, 1, 1, 0], [0, 0, 0, 1, 'x', 3, 'x', 'x', 2, 'x', 'x', 2, 1, 0, 0, 0], [0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 1, 2, 2, 1], [1, 1, 1, 'x', 3, 'x', 'x', 'x', 3, 2, 2, 2, 2, 'x', 'x', 1], ['x', 1, 1, 1, 3, 'x', 6, 'x', 4, 'x', 'x', 2, 'x', 4, 3, 2], [1, 1, 0, 0, 1, 1, 3, 'x', 3, 2, 2, 2, 1, 2, 'x', 1], [0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1, 'x', 'x', 'x', 2, 1, 1, 1, 1], ['x', 1, 0, 0, 0, 0, 0, 1, 2, 3, 2, 2, 'x', 1, 1, 'x']]
fullfi = [fi1,fi2,fi3,fi4,fi5,fi6,fi7,fi8,fi9,fi10,fi11,fi12]

#Функции
def cek():
	global f_tem
	global tem
	global help1
	help1 = root.after(1000,cek)
	f_tem = datetime.fromtimestamp(tem).strftime("%M:%S")
	time['text'] = str(f_tem)
	tem +=1


def taketext():
	global a
	global ayx
	global by
	global tent
	mane = minaas.get()
	re = onee.get()
	rew = twoo.get()
	if mane !='' and re!='' and rew!='':
		mane = int(mane)
		re = int(re)
		rew = int(rew)

		by = mane
		a = re
		ayx = rew
	zin = (mane/(re*rew))*100
	znach['text'] = round(zin,1)#округление
	tent = 0

def check_win():
	global gg
	byyk = 0
	for i in range(a):
		for j in range(ayx):
			if forloose[j][i] == 20 and mins[j][i]['text'] != 'x':
				byyk+=1
	#print(byyk)
	if byyk == ((ayx*a)-by) and gg == 0:
		#print(byyk,"WHY")
		VI_KA()
	

def rest(o):
	global k1
	global k0
	global mins
	global but
	global im
	global hp
	global lasya
	global lasayx
	global tem
	global kkool
	global od
	global dyshno
	global gg
	global u

	if ayx>24:
		u =25
	if ayx >29:
		u=20
	for i in range(lasya):
		for j in range(lasayx):
			mins[j][i].destroy()
			but[j][i].destroy()
	im=1
	k1=0
	k0=0
	k22=0
	gg = 0
	if o != 0:
		mins = labelb(o)
		colour_change(kkool)
		k0+=1
		od = 1
		dyshno = 1
	else:
		dyshno = 0
		mins = label(a)

	but = butt(a)

	for i in range(a):
		for j in range(ayx):
			but[j][i].place(x=200+i*u,y=200+j*u,width=u,height=u)
			mins[j][i].place(x=200+i*u,y=200+j*u,width=u,height=u)
	for i in range(ayx):
		for j in range(a):
			but[i][j].config(command=lambda mx=i,bx=j,kk=but: click22(mx,bx,but))
			but[i][j].bind("<Button-3>", lambda event,mx=i,bx=j,kk=but: flag(mx,bx,but))
			mins[i][j].bind("<Button-1>", lambda event,mx=i,bx=j,kk=mins: clicklabel(mx,bx,mins))
	hp = mass()
	root.after_cancel(help1)	
	tem = 0
	tablo['text']= by
	time['text'] = '00:00'
	lasya =a
	lasayx =ayx
	res.place(x=200+((a-2)/2)*u,y=150,width=u*2)
	exit.place(x=200+((a-2)/2)*u,y=200+(ayx+1)*u,width=u*2, height=40)
	tablo.place(x=100+(a+2)*u+u,y=150,width=u, height=u)


def dest():
	root.destroy()	

def lyzer():
	root.after_cancel(help1)
	press_f.deiconify()
	press_f['bg']='silver'
	wintext = Label(press_f,text="YOU LOOSE",width=20,height=2,font=('Courier 20 bold'),fg='red')
	wintext.grid(row=1,column=1)
	ok = Button(press_f,text="PRESS F",font=('times 10 bold'),fg='#006400',bg='#FFC0CB',width = 20,height=2, command=lambda: press_f.withdraw())
	ok.grid(row=2,column=1)


def clicklabel(m,b,mins):
	global forloose
	global gg
	k=0
	for i in range(3):
			for j in range(3):
				mee = m+i-1
				bee = b+j-1
				if mee>-1 and mee<ayx and bee>-1 and bee<a:
					if but[mee][bee]['text'] == 'F':
						k+=1
	if mins[m][b]['text'] == k:
		for i in range(3):
			for j in range(3):
					mee = m+i-1
					bee = b+j-1
					if mee>-1 and mee<ayx and bee>-1 and bee<a:
						if but[mee][bee]['text'] != 'F':
							if mins[mee][bee]['text'] == 0 or mins[mee][bee]['text'] == 'x':
								click22(mee,bee,but)
							else:
								but[mee][bee].place_forget()
								forloose[mee][bee] = 20
								if gg == 0:
									check_win()





def click22(m,b,bat):
	global k0
	global fi
	global im
	global mins
	global fi
	global hp
	global but
	global a
	global ayx
	global forloose
	global od
	global dyshno
	global gg
	if bat == 228322:
		k0+=1
	but[m][b].place_forget()
	if  k0==0:
		chisl = (m*a)+b+1
		fi = field(a,by,chisl)
		check_min(a,fi)
		colour_change(fi)
		for i in range(ayx):
			for j in range(a):
				mins[i][j]['text'] = fi[i][j]
		cek()

	if od == 1:
		print(od)
		cek()
		od = 0
	if forloose[m][b] == 10:
		gg = 1
		if dyshno == 0:
			for i in range(a):
				for j in range(ayx):
					if forloose[j][i] == 10:
						but[j][i].place_forget()	
		lyzer()
	k0+=1
	enn=0
	cui =m
	cuj =b
	if (mins[cui][cuj])['text'] == 0:
		hp[m][b]= 'del'
		for checin in range(ayx):
			for i in range(ayx):	
				for j in range(a):
					for ic in range(3):
						for jc in range(3):
							meeb = i+ic-1
							beeb = j+jc-1
							if meeb>-1 and meeb<ayx and beeb>-1 and beeb<a:
								if hp[meeb][beeb] == 'del' and mins[i][j]['text']==0:
									hp[i][j] = 'del'
	for i in range(ayx):
		for j in range(a):
			if hp[i][j] == 'del':
				for ic in range(3):
					for jc in range(3):
						meeb = i+ic-1
						beeb = j+jc-1
						if meeb>-1 and meeb<ayx and beeb>-1 and beeb<a:
							but[meeb][beeb].place_forget()
							forloose[meeb][beeb] = 20
	forloose[m][b] = 20
	check_win()

	#for i in range(ayx):
	#		print(hp[i],"\n")
	#print("end",'\n')			

			


	
root.mainloop()
