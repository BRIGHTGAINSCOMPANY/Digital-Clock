import sys
from customtkinter import *
import time

def times():
    current_time = time.strftime("%a- %I:%M:%S %p")
    
    clock.configure(text = current_time)
   
    clock.after(200, times)

root = CTk()
root.geometry("630x230")
root.title("Digital Clock")
root.resizable('false','false')


font1= ('Arial', 53, 'bold')
font2 =('Arial', 29, 'bold')
font3 = ('Times', 30, 'bold')

clock = CTkLabel(root, font = font1)
clock.grid(row=2, column=2, pady=25, padx=100)

times()

title = CTkLabel(root, text="TIME IS:", font = font2)
title.grid(row = 1, column = 2, pady=10, padx= 100)

bottom_text = CTkLabel(root, text = "H     M     S", font= font3)
bottom_text.grid(row=3, column=2)


root.mainloop()