import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(clock, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    completed_label.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    st_break_sec = SHORT_BREAK_MIN * 60
    lg_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        count_down(lg_break_sec)
        timer_label.config(text="Long Beak", fg=RED)
    elif rep % 2 == 0:
        count_down(st_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config( text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min= math.floor(count / 60)
    count_sec= count%60
    if count_sec < 10:
        count_sec= f"0{count_sec}"

    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(rep/2)
        for _ in range(work_session):
            marks += "✔"
        completed_label.config(text= marks)


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
clock= canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row= 1, column=1)

timer_label=Label(text="Timer",font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row= 0, column= 1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row= 2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row= 2, column=2)

completed_label=Label( fg=GREEN, bg=YELLOW)
completed_label.grid(row= 3, column=1)




window.mainloop()