import tkinter as tk

form = tk.Tk()

form.title("dAb")
form.geometry('400x400')

yazi1 = tk.Label(form, text='Welcome To dAb', font=('Arial Bold', 20))
yazi1.pack()

#fonksiyonlar

def sonuclar():
    sayfa = int(entry1.get())
    sure = int(entry2.get())
    kere = sayfa / sure
    yazi3.config(text='{0} kere 25 dakikalık çalışma yapınız'.format(int(kere)))
    toplam = kere*25
    yazi4.config(text='Toplam {0} dakika'.format(int(toplam)))

def alarm():
    if yazi3.winfo_ismapped():
        button2.place_forget()
        button1.place_forget()
        yazi1.place_forget()
        yazi2.place_forget()
        yazi3.place_forget()
        yazi4.place_forget()
        entry1.place_forget()
        entry2.place_forget()


#butonlar

button1 = tk.Button(form, text='Onayla', width=10, height=2,bg='green',command=sonuclar)
button1.place(x=575, y=350)

button2 = tk.Button(form, text='Alarmı başlat', width=10, height=2, command=alarm)
button2.place(x=575, y=450)

#entrylar

entry1 = tk.Entry(form)
entry1.place(x=575, y=150)

entry2 = tk.Entry(form)
entry2.place(x=575, y=200)

#yazılar

yazi1 = tk.Label(form, text='Sayfa sayısı')
yazi1.place(x=475, y=150)

yazi2 = tk.Label(form, text='25 dakikada çözülebilecek sayfa sayısı')
yazi2.place(x=275, y=200)

yazi3 = tk.Label(form, text='')
yazi3.place(x=475, y=250)

yazi4 = tk.Label(form, text='')
yazi4.place(x=475, y=300)



form.mainloop()