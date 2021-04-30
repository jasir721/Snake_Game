from score import Scoreboard
from turtle import Turtle,Screen
import time
from food import Food
from score import Scoreboard
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
# Event listener
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
    #For detecting the collision with the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False
    #Detect collision with its own tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()