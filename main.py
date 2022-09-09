import pandas
import turtle
import time
import random

screen=turtle.Screen()

p=turtle.Turtle()
p.shape("circle")
p.hideturtle()
p.penup()
p.pencolor("black")
colors=["red","blue","green","pink","silver","orange","yellow","black","purple"]
screen.setup(width=800,height=800)

x=0
y=350
p.goto(x,y)
dat=pandas.read_csv("50_states.csv")
dat_state=dat["state"]  #fetch the data of csv file .and print a series(1d) of states
p.write("list of state of name ('case sensitve')",font=("Arial", 15, "normal"),align="center")
y=y-50
#print the lit of state that we are fetch earlier
for i in dat_state:
    p.goto(x, y)
    p.write(i,font=("Arial", 10, "normal"),align="center")
    y=y-15
time.sleep(5)
screen.clear()
p.write("now game is begin",font=("Arial", 15),align="center")
time.sleep(3)
screen.clear()

#this function is use to fetch the coordinate of given location
def get_mouse_click_coor(x,y):
    print(x,y)

#import a back groud image
screen.setup(width=800,height=800)
screen.title("state guess name")
image="g.gif"
screen.bgpic(image)
#another way to import an image
#screen.addshape(image)
#turtle.shape(image)

#call function for find the coordinate
#print(turtle.onscreenclick(get_mouse_click_coor))
#turtle.mainloop()
screen=turtle.Screen()
A=1
b=26
c=26
score=0
while A<=26:
    c=c-1
    data=pandas.read_csv("50_states.csv")   #fetch the data from csv
    all_state=data.state.to_list()  #convert the data into list
    ans=turtle.textinput(title=f"score=>        {score}/{b}",prompt=f"enter the state \n turn reamining {c}")   #pop up box that will help to takes an input from user
    ans=ans.title() #this is use for making first latter capital
    if ans in all_state:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.pensize(5)
        t.pencolor("red")
        loc=data[data.state==ans]
        t.goto(int(loc.x),int(loc.y))
        t.write(loc.state.item(),font= ("Arial", 10, "normal"),align="center")
        p.goto(int(loc.x),int(loc.y))   #move turtle to the given location
        p.color(random.choice(colors))
        p.shapesize(stretch_wid=.3,stretch_len=.3)
        p.stamp()
        score=score+1
    A=A+1
screen.clear()  #for clear previous screen
p.goto(0,0)
p.write(f"the final score is {score}\{b}",align="center",font=("Arial", 18, "normal"))  #print final score
screen.exitonclick()