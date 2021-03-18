
from turtle import Turtle, Screen
import random

# setings de screen
screen =  Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="Which turtle will win the race ? Enter a color : ").lower()

is_racing_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x = -230
y = -160

tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x , y)

myTurtles = [tim]

#TODO 1: Crear todos los competidores
for competitors in range(0,5):
	y +=50
	competitors = tim.clone()
	myTurtles.append(competitors)
	competitors.goto(x,y)
	competitors.color("white")

#TODO 2: Asignar un color

for give in range(6):
	paint = colors[give]
	myTurtles[give].color(paint)

#TODO 3: Crear el movimiento random

if user_bet:
	is_racing_on = True

while is_racing_on:
	for turtle in myTurtles:
		if turtle.xcor() > 230:
			winner= turtle.pencolor()
			if  winner == user_bet :
				print(f"You've won !! The win color {winner}")
			else:
				print(f"The winner is the turtle color {winner}. You Lost! ")
				is_racing_on = False
		distance = random.randint(0,10)
		turtle.forward(distance)


screen.exitonclick()
