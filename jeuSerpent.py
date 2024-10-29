import turtle as tl
import random as rd
import time as ti

player_score = 0
highest_score = 0
delay_time = 0

#Création de la fenêtre de jeu
wind = tl.Screen()
wind.title("Le Maze")
wind.bgcolor("aqua")

#Taille de l'écran
wind.setup(width=600, height=600)

#Création du serpent
serpent = tl.Turtle()
serpent.shape("square")
serpent.color("green")
serpent.penup()
serpent.goto(0,0)
serpent.direction ="Stop"
serpent.speed(1)

#Création de la nourriture
serpent_graille = tl.Turtle()
formes = rd.choice(("triangle", "circle"))
serpent_graille.shape(formes)
serpent_graille.color("white")
serpent_graille.speed(0)
serpent_graille.penup()
serpent_graille.goto(0,100)

crayon = tl.Turtle()
crayon.speed(0)
crayon.shape("square")
crayon.color("white")
crayon.penup()
crayon.hideturtle()
crayon.goto(0,250)
crayon.write("Votre Score: 0 Meilleur Score: 0", align="center", font=("Arial",24,"normal"))
tl.mainloop

#Attribution des directions
def gauche():
    if serpent.direction != "right":
        serpent.direction = "left"

def droite():
    if serpent.direction != "left":
        serpent.direction = "right"

def haut():
    if serpent.direction != "down":
        serpent.direction = "up"

def bas():
    if serpent.direction != "up":
        serpent.direction = "down"

def move():
    if serpent.direction == "up":
        coord_y = serpent.ycor()
        serpent.sety(coord_y+20)

    if serpent.direction == "down":
        coord_y = serpent.ycor()
        serpent.sety(coord_y-20)

    if serpent.direction == "right":
        coord_x = serpent.xcor()
        serpent.setx(coord_x+20)

    if serpent.direction == "left":
        coord_x = serpent.xcor()
        serpent.setx(coord_x-20)

wind.listen()
wind.onkeypress(gauche, "g")
wind.onkeypress(droite, "d")
wind.onkeypress(haut, "h")
wind.onkeypress(bas, "b")

segments= []

#Implémentation du gameplay
while True:
    wind.update()
    if serpent.xcor() > 290 or serpent.xcor() < -290 or serpent.ycor() > 290 or serpent.ycor() < -290:
        ti.sleep(1)
        serpent.goto(0,0)
        serpent.direction = "Stop"
        serpent.shape("square")
        serpent.color("green")

        for segment in segments:
            segment.goto(1000,1000)
            segments.clear()
            player_score = 0
            delay_time = 0.1
            crayon.clear()
            crayon.write("Score du Joueur: {} Meilleur Score {}".format(player_score, highest_score), align="center",font=("Arial", 24, "normal"))

        if serpent.distance(serpent_graille) < 20:
            coord_x = rd.randint(-270,270)
            coord_y = rd.randint(-270,270)
            serpent_graille.goto(coord_x,coord_y)

            #Ajout d'un segment
            segment_ajoute = tl.Turtle()
            segment_ajoute.speed(0)
            segment_ajoute.shape("square")
            segment_ajoute.color("green")
            segment_ajoute.penup()
            delay_time -= 0.001
            player_score += 5

            if player_score > highest_score:
                highest_score = player_score
                crayon.clear()
                crayon.write("Score du Joueur: {} Meilleur Score {}".format(player_score, highest_score), align="center",font=("Arial", 24, "normal"))

    #Détecteur de collisions
    for i in range(len(segments)-1, 0, -1):
        coord_x = segments[i-1].xcor()
        coord_y = segments[i-1].cor()
        segments[i].goto(coord_x, coord_y)

    if len(segments) > 0:
        coord_x = serpent.xcor()
        coord_y = serpent.ycor()
        segments[0].goto(coord_x,coord_y)
    move()

    for segment in segments:
        if segment.distance(serpent) < 20:
            ti.sleep(1)
            serpent.goto(0,0)
            serpent.direction = "Stop"
            serpent.color("green")
            serpent.shape("square")

            for segment in segments:
                segment.goto(1000,1000)
                segment.clear()
                player_score = 0
                delay_time = 0.1
                crayon.clear()
                crayon.write("Score du Joueur: {} Meilleur Score {}".format(player_score, highest_score), align="center",font=("Arial", 24, "normal"))

    ti.sleep(delay_time)

tl.mainloop()