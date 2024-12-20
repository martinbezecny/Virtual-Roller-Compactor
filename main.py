import customtkinter
import numpy as np
from scipy.integrate import quad
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# function to be called when the calculate button is clicked
def calculate(event=None):
    P = float(P_entry.get())
    S = float(S_entry.get())
    K = float(K_entry.get())

    # Define the function to be integrated
    def f(x):
        return (((S*0.001)/0.25)/((1+((S*0.001)/0.25)-np.cos(x))*np.cos(x)))**K*np.cos(x)

    # Convert degrees to radians
    lower_bound = np.radians(0)   # Equivalent to 0 degrees
    upper_bound = np.radians(20)  # Equivalent to 20 degrees

    # Integrate the function from 0 to 20 (in radians)
    integral, error = quad(f, lower_bound, upper_bound)

    # Store the integral value in the variable "int" as a number
    integral_result = float(integral)

    # Calculate Pmax using the number stored in "integral_result"
    Pmax = round((2 * ((0.0878492377188029*P+0.138390739695089)*100000)) / (0.25 * (1.195**K) * integral_result) * 0.000001)
    Pmax_entry.config(state='normal')
    Pmax_entry.delete(0, 'end')
    Pmax_entry.insert(0, str(Pmax))
    Pmax_entry.config(state='readonly')

# function to be called when the help button is clicked
def help():
    messagebox.showinfo("Instructions", "Input the setpoint values of the roll pressure and roll gap of the compactor. Calculate the compressibility factor K of your blend and input the K value. Press Calculate to model the maximum pressure on the blend in the compactor.\n\nUse decimal points ( . ), not decimal commas ( , ).\n\nThis Virtual Roller Compactor specifically models the Alexanderwerk WP 120 Pharma, assumes a roll diameter of 250 mm, a roll width of 4 mm, and textured surface of the rolls.\n\nBased on the work of Chi So, Lap Y. Leung, Ariel R. Muliadi, Ajit S. Narang, Chen Mao.\n\n© 2023 Martin Bezecný, PRO.MED.CS Praha a.s.\n\nVersion 0.2 (2023-08-09)")

# creating main tkinter window/toplevel
master = tk.Tk()
master.title("Virtual Roller Compactor")

# Get screen width and height
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

# Calculate position adjustments
x = (screen_width / 2) - (390 / 2)
y = (screen_height / 2) - (460 / 2)

# Set the window size and position
master.geometry("%dx%d+%d+%d" % (390, 460, x, y))

# Bind the Enter key to the calculate function
master.bind('<Return>', calculate)

# title label
title_label = tk.Label(master, text="Virtual Roller Compactor v0.2", font=("Tahoma", 20))
title_label.pack(pady=(20,20)) # Add padding above the title

# creating entry fields and their labels
P_label = tk.Label(master, text="Roll pressure [bar]", font=("Tahoma", 12))
P_label.pack()
P_entry = ctk.CTkEntry(master, justify='center', font=("Tahoma", 16))
P_entry.pack(pady=(0,10))

S_label = tk.Label(master, text="Roll gap [mm]", font=("Tahoma", 12))
S_label.pack()
S_entry = ctk.CTkEntry(master, justify='center', font=("Tahoma", 16))
S_entry.pack(pady=(0,10))

K_label = tk.Label(master, text="Compressibility factor K", font=("Tahoma", 12))
K_label.pack()
K_entry = ctk.CTkEntry(master, justify='center', font=("Tahoma", 16))
K_entry.pack(pady=(0,10))

# button to call calculate function
calc_button = ctk.CTkButton(master, text="Calculate", command=calculate, font=("Tahoma", 16, 'bold'))
calc_button.pack(pady=(0,20))

# field to display Pmax
Pmax_label = tk.Label(master, text="Maximum Pressure [MPa]", font=("Tahoma", 12, 'bold'))
Pmax_label.pack()
Pmax_entry = tk.Entry(master, state='readonly', width=15, bg='white', font=("Tahoma", 16), justify='center')
Pmax_entry.pack(pady=(0,20))

# button to call help function
help_button = ctk.CTkButton(master, text="?", command=help, font=("Tahoma", 16, 'bold'), width=40)
help_button.pack(anchor='se', pady=(0,20), padx=(0,20))

# infinite loop which can be interrupted
master.mainloop()