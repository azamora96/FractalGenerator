import turtle

from tkinter import *

from tkinter import messagebox
root = Tk()
# ^ importing libraries - Alec/Katie ^

entryB = ''
entryS = ''
entryA = ''
# ^ tree ^

entryI = ''
entryL = ''
entryS2 = ''
entryA2 = ''
# ^ snowflake ^
# ^ initial entry variables for global use - Alec/Katie ^

MINIMUM_BRANCH_LENGTH = 5
def build_tree(t, branch_length, shorten_by, angle):
    
    if branch_length > MINIMUM_BRANCH_LENGTH:
        global speed
        t.speed(speed)
        t.forward(branch_length)
        new_length = branch_length - shorten_by
        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)
        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle)
        t.left(angle)
        t.backward(branch_length)
        global killswitch
        killswitch = ''
        
def koch_curve(t, iterations, length, shortening_factor, angle):
  if iterations == 0:
    global speed
    t.speed(speed)
    t.forward(length)
  else:
    t.speed(speed)
    iterations = iterations - 1
    length = length / shortening_factor
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.right(angle * 2)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t.left(angle)
    koch_curve(t, iterations, length, shortening_factor, angle)
    t = turtle.Turtle()
    t.hideturtle()
    global killswitch
    killswitch = ''
# ^ built in functions from Turtle library(edited by us: speed, killswitch), all other functions created by us ^ 
# ^ - Alec/Katie ^

killswitch = ''

def QuitFractal():
    
    global killswitch
    killswitch = turtle.done()
# ^ initial variable and function to stop drawing - Alec/Katie ^

screen_status = ''

def closeScreen():
    
    global screen_status
    screen_status = turtle.bye()
# ^ initial variable and function to close turtle screen - Katie ^
    
speed = 3

def speedFastest():
    global speed
    speed = 0

def speedFast():
    global speed
    speed = 10
    
def speedNormal():
    global speed
    speed = 6
    
def speedSlow():
    global speed
    speed = 3
# ^ initial variable and functions for updating creation speed - Alec ^

def tree_fractal():
    
    branchlen = int(entryB.get())
    shortenby = int(entryS.get())
    angle = int(entryA.get())
    if branchlen <25 or branchlen >200:
        messagebox.showerror("Error: Your branch length must be between 25 and 200")
        return None
    if shortenby <5:
        messagebox.showerror("Error: Your shorten by must be greater than 5")
        return None
    if angle <0 or angle >180:
        messagebox.showerror("Error: Your angle must be between 0 and 180")
        return None
# ^ retrieve, pass, and error check parameters for tree fractal - Katie ^

    previous_parameters = [entryB.get(), entryS.get(), entryA.get()]
   
    input_history = '\n' + ' '.join(previous_parameters)
    
    with open('fractal_history.txt', 'a') as f:
    
        f.write(input_history)
# ^ gathers parameters into list, writes parameters history into a file - Alec ^

    tree = turtle.Turtle()
    tree.hideturtle()
    tree.setheading(90)
    #axis it creates on ^ 90 = up and down 
    tree.color('green')
    build_tree(tree, branchlen, shortenby, angle)
# ^ tree triggers with user entry parameters - Alec/Katie ^

    global screen_status
    screen_status = turtle.mainloop()
# ^ gives option to close the turtle window specifically - Katie ^ 
    
def snowflake_fractal():
    
    t = turtle.Turtle()
    iterations = int(entryI.get())
    length = int(entryL.get())
    shorten = int(entryS2.get())
    angle = int(entryA2.get())
    if iterations <0 or iterations >5:
        messagebox.showerror("Error: Your interation must be between 0 and 5")
        return None
    if length < 25 or length > 200:
        messagebox.showerror("Error: Your length must be between 25 and 200")
        return None
    if shorten <0 or shorten >5:
        messagebox.showerror("Error: Your shorten by must be between 0 and 5")
        return None
    if angle <0 or angle >180:
        messagebox.showerror("Error: Your angle must be between 0 and 180")
        return None
# ^ retrieve, pass, and error check parameters for snowflake fractal - Katie ^

    previous_parameters = [entryI.get(), entryL.get(), entryS2.get(), entryA2.get()]
   
    input_history = '\n' + ' '.join(previous_parameters)
    
    with open('fractal_history.txt', 'a') as f:
    
        f.write(input_history)
# ^ gathers parameters into list, writes parameters history into a file - Alec ^
    
    t.hideturtle()
    for i in range(3):
        koch_curve(t, iterations, length, shorten, angle)
        t.right(120)
# ^ tree triggers with user entry parameters - Alec/Katie ^

    global screen_status
    screen_status = turtle.mainloop()
# ^ gives option to close the turtle window specifically - Katie ^ 

    
def tree_input():
    
    Label(root, text="Simple Fractal Generator: Build Your Own Fractal!").grid(columnspan=4, row=0)
    
    Label(root, text="Tree:").grid(row=1, column=0)

    global entryB
    entryB = Entry(root)
    entryB.grid(column=1, row=3)
    
    Label(root, text="Branch Length(25-200):").grid(column=0, row=3)
    
    global entryS
    entryS = Entry(root)
 
    entryS.grid(column=1, row=4)
    
    Label(root, text="Shorten By Length(min 5):").grid(column=0, row=4)
    
    global entryA
    entryA = Entry(root)
    entryA.grid(column=1, row=5)
    
    Label(root, text="Angle(1-180):").grid(column=0, row=5)
    
    Button(root, text="Generate A Tree", command=tree_fractal).grid(row=6, column=1)
# ^ tree entry fields on canvas - Alec ^

def snowflake_input():
    
    Label(root, text="Snowflake:").grid(row=1, column=2)
    
    global entryI
    entryI = Entry(root)
    entryI.grid(column=3, row=3)
    
    Label(root, text="Points on Snowflake(1-5):").grid(column=2, row=3)
    
    global entryL
    entryL = Entry(root)
    entryL.grid(column=3, row=4)
    
    Label(root, text="Length(25-200):").grid(column=2, row=4)
    
    global entryS2
    entryS2 = Entry(root)
    entryS2.grid(column=3, row=5)
    
    Label(root, text="Shorten By Length(1-5):").grid(column=2, row=5)
    
    global entryA2
    entryA2 = Entry(root)
    entryA2.grid(column=3, row=6)
    
    Label(root, text="Angle(1-180):").grid(column=2, row=6)
    
    Button(root, text="Generate A Snowflake", command=snowflake_fractal).grid(row=7, column=3)
# ^ snowflake entry lines on canvas - Katie ^

def commandButtons():
    
    Button(root, text="Stop Drawing", command=QuitFractal).grid(row=13, columnspan=4)
    Button(root, text ="Close", command=closeScreen).grid(row=14, columnspan=4)
    Button(root, text="Slow", command=speedSlow).grid(row=8, columnspan=4)
    Button(root, text="Normal Speed", command=speedNormal).grid(row=9, columnspan=4)
    Button(root, text="Speed up", command=speedFast).grid(row=10, columnspan=4)
    Button(root, text="Speed up x2", command=speedFastest).grid(row=11, columnspan=4)
# ^ buttons for stopping, speeding up, and slowing down fractal creation - Alec ^
    
tree_input()
snowflake_input()
commandButtons()
# ^ calling the entry lines and buttons into canvas - Alec ^

root.mainloop()
