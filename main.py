import tkinter as tk
import time
from tkinter import messagebox
#kısaltmalar

form = tk.Tk()

#giriş
form.title("dAb")
form.geometry('400x400')

yazi1 = tk.Label(form, text='Welcome To dAb', font=('Arial Bold', 20))
yazi1.pack()

#fonksiyonlar
        
def sonuclar():
    sayfa = int(entry1.get())
    sure = int(entry2.get())
    kere = sayfa / sure
    yazi3.config(text='{0} kere 25 dakikalık çalışma yapınız'.format(int(round(kere))))
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
        label.pack(padx=50, pady=150)
        button4.place(x=537, y=430)
        
def countdown():
    total_seconds = 24 * 60 + 59
    
    for i in range(total_seconds, 0, -1):
        minutes = i // 60
        seconds = i % 60
        time_str.set(f"{minutes:02d}:{seconds:02d}")
        form.update()
        time.sleep(1)
        
        if i == 5:
            messagebox.showinfo("Alarm", "5 dakika kaldı!")
        
    if messagebox.askyesno("Alarm", "Alarmı başlatmak istiyor musunuz?"):
        # Alarm müziği eklenmesi için ekleyebiliriz
        messagebox.showinfo("Alarm", "Alarm başlatıldı!")
        button4.config(text=durdur)
    else:
        messagebox.showinfo("Alarm", "Alarm başlatılmadı!")
        
root = tk.Tk()
root.title("Geri Sayım")

time_str = tk.StringVar()
time_str.set("25:00")

def start_alarm():
    if messagebox.askyesno("Alarm", "Alarmı başlatmak istiyor musunuz?"):
        countdown()
        # Alarm müziği kodu buraya eklenebilir
        messagebox.showinfo("Alarm", "Alarm başlatıldı!")
    else:
        messagebox.showinfo("Alarm", "Alarm başlatılmadı!")
                    
#butonlar

button4 = tk.Button(form, text="Alarmı Başlat", font=("Helvetica", 14), command=start_alarm)


button1 = tk.Button(form, text='Onayla', width=10, height=2,bg='green',command=sonuclar)
button1.place(x=575, y=350)

button2 = tk.Button(form, text='Alarm', width=10, height=2, command=alarm)
button2.place(x=575, y=450)

#entrylar

entry1 = tk.Entry(form)
entry1.place(x=575, y=150)

entry2 = tk.Entry(form)
entry2.place(x=575, y=200)

#yazılar

label = tk.Label(form, textvariable=time_str, font=("Helvetica", 48))

yazi1 = tk.Label(form, text='Sayfa sayısı')
yazi1.place(x=475, y=150)

yazi2 = tk.Label(form, text='25 dakikada çözülebilecek sayfa sayısı')
yazi2.place(x=275, y=200)

yazi3 = tk.Label(form, text='')
yazi3.place(x=475, y=250)

yazi4 = tk.Label(form, text='')
yazi4.place(x=475, y=300)

form.mainloop()       