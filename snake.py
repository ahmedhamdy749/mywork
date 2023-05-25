# import modules necessary for game
import random
import curses
# initialize the curses libariray to creat our screen
screen = curses.initscr()
# hide the mouse curser
curses.curs_set(0)
# get max screen hight and width
screen_hight, screen_width = screen.getmaxyx()
# creat a new window
window = curses.newwin(screen_hight, screen_width, 0, 0)
# allow window to recive input from keyboard
window.keypad(1)
# set the delay for updating the screen
window.timeout(100)
# set the y,x coordinates of the intial position of snake's head
snk_x = screen_width // 4
snk_y = screen_hight // 2
# define the intial position of the snake body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
# creat the food in the middel of the widow
food = [screen_hight//2, screen_width//2]

# add the food by using pi character from curses module
window.addch(food[0], food[1], curses.ACS_PI)
# set the initial movement direction to right
key = curses.KEY_RIGHT
# creat game loop that loops for ever untill player loses or quites the game
while True:

    # get the next key that well be pressed by user
    next_key = window.getch()
# if the user dosn't input anything,key remains same. else key will be set to the new pressed Key
    key = key if next_key == -1 else next_key
# check if the snake collided with the walls or it self
    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
# set the new position of the snake head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
# insert the head to the first position of the snake list
    snake.insert(0, new_head)
# check if the snake eat the food
    if snake[0] == food:
        food = None
# while food is removed generate new food on the screen in a random place
    while food is None:
        new_food = [
            random.randint(1, screen_hight-1),
            random.randint(1, screen_width-1)
        ]
# set the food to new food but not in the snake body
    food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_PI)
# otherwise remove the last segment of snake body
else:
   tail = snake.pop()
  
   window.addch(tail[0], tail[1], ' ')
   window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
