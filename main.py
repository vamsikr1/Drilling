#SCALE 1:10
from turtle import Turtle,Screen
import math


screen=Screen()
screen.title("Well profile-cross section")
screen.bgcolor("black")
screen.screensize(canvwidth=3000, canvheight=3000)


# turtle=Turtle()
# turtle.speed("fastest")


GAMMA=screen.numinput("Input","Build up rate in degrees")
TVD=screen.numinput("Input","True vertical depth in ft")
KOP=screen.numinput("Input","KOP in ft")
HD=screen.numinput("Input","Horizontal departure in ft")
RADIUS=(36000/(2*3.14*(GAMMA)))
xr=math.atan((HD-RADIUS)/(TVD-KOP))
x=math.degrees(xr)
yr=math.asin((RADIUS*math.cos(xr))/(TVD-KOP))
y=math.degrees(yr)
print(x)
print(y)
ALPHA=x+y

KOP_x=0
KOP_y=KOP/10

End_Hold_x=HD/10
End_Hold_y=(-TVD/10)
#VERTICAL SECTION
vertical=Turtle()
vertical.hideturtle()
vertical.penup()
vertical.goto(0,0)
vertical.color("White")
    # vertical.pendown()
    #vertical.pensize(20)
vertical.speed("fastest")
vertical.setheading(270)
vertical.forward(1)
vertical.goto(0,-TVD/10)

    #Build and Hold section
raw_1=Turtle()
raw_1.hideturtle()
raw_1.color("white")
raw_1.speed("fastest")
raw_1.penup()
raw_1.goto(0,-TVD/10)
    # raw_1.pendown()
raw_1.goto((HD/10,-TVD/10))



raw_2=Turtle()
raw_2.hideturtle()
raw_2.speed("fastest")
raw_2.color("white")
raw_2.penup()
raw_2.goto((HD/10,-TVD/10))

    # raw_2.pendown()
while raw_2.ycor()<=-KOP/10:

    raw_2.speed("fastest")
    raw_2.setheading(90+ALPHA)
    raw_2.forward(1)


raw_3=Turtle()
raw_3.hideturtle()
raw_3.speed("fastest")
raw_3.color("white")
raw_3.penup()
raw_3.goto(RADIUS/10,-KOP/10)
raw_3.setheading(180+ALPHA)
arc_help=True
while arc_help:
    # raw_3.pendown()
    if raw_3.distance(raw_2)!=0 and raw_3.xcor()>=0:
        raw_3.forward(1)
    elif raw_3.xcor()<0:
        arc_help=False
raw_4=Turtle()
raw_4.hideturtle()
raw_4.color("white")
raw_4.speed("fastest")
raw_4.goto(0,-KOP/10)
raw_4.pencolor("red")
raw_4.setheading(270)
raw_4.circle(RADIUS/10,ALPHA)


length_of_build_up_section=round(((ALPHA*2*3.14*RADIUS)/(360)),2)
ALPHA_r=math.radians(ALPHA)
arc_height=RADIUS*math.sin(ALPHA_r)
# BU_sc_x=raw_4.xcor()
# BU_sc_y=raw_4.ycor()
length_of_hold_section=round((TVD-KOP-arc_height)/(math.cos(ALPHA_r)),2)



wellbore=Turtle()
wellbore.penup()
wellbore.goto(0,0)
wellbore.pendown()
wellbore.pensize(10)
wellbore.setheading(270)
wellbore.pencolor("blue")
wellbore.goto(0,-KOP/10)
wellbore.write(f"Kick off started at {KOP} ft", move=False, align="left", font=("Courier", 15, "normal"))
wellbore.circle(RADIUS/10,ALPHA)
wellbore.write(f"LENGTH of build up section {length_of_build_up_section} ft", move=False, align="left", font=("Courier", 15, "normal"))
wellbore.goto(HD/10,-TVD/10)
wellbore.write(f"Hold section length: {length_of_hold_section} ft", move=False, align="left", font=("Courier", 15, "normal"))

wellbore.penup()
wellbore.hideturtle()
wellbore.goto(0,200)
wellbore.write(f"Measured depth at end of build up section: {KOP+length_of_build_up_section} ft", move=False, align="left", font=("Courier", 15, "normal"))
wellbore.goto(0,180)
wellbore.write(f"TVD at end of build up section: {KOP+arc_height} ft", move=False, align="left", font=("Courier", 15, "normal"))
wellbore.goto(0,160)
wellbore.write(f"Total measured depth: {KOP+length_of_build_up_section+length_of_hold_section} ft", move=False, align="left", font=("Courier", 15, "normal"))





screen.exitonclick()