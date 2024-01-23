import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
highScore = 0

#configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("dark green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#comida serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#cuerpo serpiente
segmentos = []

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       High Score: 0", align="center", 
            font=("Courier", 24, "normal"))
 

#funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)
    
#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#bucle de ejecucion
while True:
    wn.update()

    #colision borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 220 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #esconder elementos
        for segmento in segmentos:
            segmento. goto(1000,1000)

        #limpiar segmentos
        segmentos.clear()
        
        #resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, highScore), 
                    align="center", font=("Courier", 24, "normal"))
        
    #generar comida
    if cabeza.distance(comida) < 20:
        x =  random.randint(-280,280)
        y =  random.randint(-280,220)
        comida.goto(x,y)

        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.color("green")
        nuevoSegmento.penup()
        segmentos.append(nuevoSegmento)

        #aumentar marcador
        score += 10
        if score > highScore:
            highScore = score
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(score, highScore), 
                    align="center", font=("Courier", 24, "normal"))


    #Movimiento cuerpo
    totalSeg = len(segmentos)
    for i in range(totalSeg -1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder elementos 
            for segmento in segmentos:
                segmento.goto(1000,1000)
            
            #limpiar elementos
            segmentos.clear()

            #resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(score, highScore), 
                        align="center", font=("Courier", 24, "normal"))

    time.sleep(posponer)


