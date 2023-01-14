from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

#Sets HIEGHT and WIDTH varibles
HEIGHT = 500
WIDTH = 800

#Creates the window
window = Tk()
window.title("Bubble Blaster")

#Creates a canvas
c = Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
c.pack()

#Creates the ship
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
ship_id2 = c.create_oval(0, 0, 30, 30, outline="red")
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 10

#Defines the ships movement
def move_ship(event):
    if event.keysym == 'w':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 's':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'a':
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'd':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship)

#Creates bubble varibles
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100

#This function creates bubbles
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white")
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))

#This function moves the bubbles
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)

#Gets coords of a bubble
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y

#Delets a bubble
def del_bubble(i):
    del bub_r[1]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

#Cleans up all bubbles that have floated off the screen
def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)

#This function will calculate the distance between two objects
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Makes the bubbles pop when collided with
def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points

#Creates the scoreboard
c.create_text(50, 30, text="Time", fill="white")
c.create_text(150, 30, text="Score", fill="white")
time_text = c.create_text(50, 50, fill="white")
score_text = c.create_text(150, 50, fill="white")
def show_score(score):
    c.itemconfig(score_text, text=str(score))
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))

#Sets the time limit and bonus varibles
BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

#MAIN GAME LOOP
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

#Shows the game over screen
c.create_text(MID_X, MID_Y, text="GAME OVER", fill="red", font=("Helvetica", 30))
c.create_text(MID_X, MID_Y + 35, text="Score: " + str(score), fill="yellow", font=("Helvetica", 15))
c.create_text(MID_X, MID_Y + 55, text="Bonus time: " + str(bonus*TIME_LIMIT), fill="green", font=("Helvetica", 15))

#Stops the game closing automatically when finished
input()
