from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # if it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)

    # if it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Short Break", fg=PINK)

    # if it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_secs)
        timer_label.config(text="Work", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(reps // 2):                      # floor division
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=YELLOW, font=(FONT_NAME, 30, "bold"), bg=GREEN)
timer_label.grid(column=1, row=0,)

start_button = Button(text="Start", font=3, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=3, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=YELLOW, bg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
