from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25#25
SHORT_BREAK_MIN =5#5
LONG_BREAK_MIN = 30#20
reps = 0
useless = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(useless)
    canvas.itemconfig(time_display, text="00:00")
    labeltimer.config(text="Timer", fg=GREEN)
    labeltick.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps % 2 == 0 and reps < 8:
        labeltimer.config(text="Work",fg=RED)
        timer(work)
    elif reps % 2 != 0 and reps < 8:
        labeltimer.config(text="BREAK", fg=PINK)
        timer(short_break)
    elif reps == 8:
        labeltimer.config(text="HUGE BREAK", fg=GREEN)
        timer(long_break)
        reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    global reps

    minu = math.floor(count/60)
    seco = count % 60
    if seco < 10 :
        seco = f"0{seco}"
    if minu <10 :
        minu = f"0{minu}"
    canvas.itemconfig(time_display, text=f"{minu}:{seco}")

    if count > 0:
        global useless
        useless = window.after(1000, timer, count-1)
    else:
        reps += 1
        start_timer()
        stickers = ""
        work_cycles = math.floor(reps/2)
        for _ in range(work_cycles):
            stickers += "✔"
        labeltick.config(text=stickers)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#CANVAS
canvas = Canvas(width=210, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
time_display = canvas.create_text(106, 132, text="00:00",fill="white",font=(FONT_NAME, 29, "bold"))
canvas.grid(row=1, column=1)

#Labels
labeltimer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
labeltimer.grid(row=0, column=1)

labeltick = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
labeltick.grid(row=3, column=1)

#Buttons

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

start = Button(text="Reset", command=reset_timer )
start.grid(row=2, column=2)

window.mainloop()
