#Import'larım#
import turtle
import random
import math
import winsound



#Arkaplanı ayarlama#
ap = turtle.Screen()
ap.bgcolor("midnight blue")
ap.screensize()
ap.setup(width = 1.0, height = 1.0)
#Oyun arkaplanı#
ap.bgpic("arkaplan1.gif")
#Akıcılık#
ap.delay(1)


#Sınır#
sınır = turtle.Turtle()
sınır.penup()
sınır.pencolor("white")
sınır.speed(0)
sınır.setposition(-400,-395)
sınır.pendown()
sınır.pensize(10)

#Sınır1(Ekranda skor ve canın aynı anda çıkması için ayrı bir turtle)#
sınır1 = turtle.Turtle()
sınır1.pencolor("white")
sınır1.hideturtle()

#Toplam skoru göstermesi için#
sınır2 = turtle.Turtle()
sınır2.pencolor("white")
sınır2.hideturtle()

#Sınırımız#
for side in range(4):
    sınır.forward(800)
    sınır.left(90)
sınır.hideturtle()


#Oyuncumuz#
oyuncu = turtle.Turtle()
oyuncu.shapesize(2)
oyuncu.color("lawn green")
oyuncu.shape("arrow")
oyuncu.penup()
oyuncu.speed(0)


#Yararlı hedef yaratma#
maxYhedefler = 6
yhedefler = []

#Yararlı hedefimiz#
for count in range(maxYhedefler):
    yhedefler.append(turtle.Turtle())
    yhedefler[count].shapesize(2)
    yhedefler[count].color("Magenta")
    yhedefler[count].shape("turtle")
    yhedefler[count].penup()
    yhedefler[count].speed(0)
    yhedefler[count].setposition(random.randint(-370,370), random.randint(-370,370))


#Zararlı hedef yaratma#
maxZhedefler = 3
zhedefler = []

#Zararlı hedefimiz#
ksekiller=("circle","square")
krenkler=("red","grey","brown","white")
for count in range(maxZhedefler):
    zhedefler.append(turtle.Turtle())
    zhedefler[count].shapesize(2)
    zhedefler[count].color(random.choice(krenkler))
    zhedefler[count].shape(random.choice(ksekiller))
    zhedefler[count].penup()
    zhedefler[count].speed(0)
    zhedefler[count].setposition(random.randint(-370,370), random.randint(-370,370))


#Hız#
hız = 1


#Hareketleri tanımlama#
def soladon():
    oyuncu.left(30)
def sagadon():
    oyuncu.right(30)
def hiziarttir():
    global hız
    hız += 1
def hizidusur():
    global hız
    hız -= 1


#Çarpışmayı tanımlama#
def carpisma(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 30:
        return True
    else:
        return False


#Tuş ataması#
turtle.listen()
turtle.onkey(soladon, "Left")
turtle.onkey(sagadon, "Right")
turtle.onkey(hiziarttir, "Up")
turtle.onkey(hizidusur, "Down")


#While döngüsü#

skor = 100
can = 3
skor2 = 0

while True:
    oyuncu.forward(hız)

    #Sınır çekme(x)#
    if oyuncu.xcor() > 380 or -380 > oyuncu.xcor():
        oyuncu.right(180)
        winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)
    #Sınır çekme(y)#
    if oyuncu.ycor() > 380 or -380 > oyuncu.ycor():
        oyuncu.right(180)
        winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)


    #Yararlı hedef hareketi#
    for count in range(maxYhedefler):
        yhedefler[count].forward(3)


        #Sınır çekme-2 (x)#
        if yhedefler[count].xcor() > 380 or -380 > yhedefler[count].xcor():
            yhedefler[count].right(180)
            winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)
        #Sınır çekme-2 (y)#
        if yhedefler[count].ycor() > 380 or -380 > yhedefler[count].ycor():
            yhedefler[count].right(180)
            winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)
        #Çarpışma 2#
        if carpisma(oyuncu, yhedefler[count]):
            yhedefler[count].setposition(random.randint(-370, 370), random.randint(-370, 370))
            yhedefler[count].right(random.randint(0, 360))
            winsound.PlaySound("skor1.mp3", winsound.SND_ASYNC)
            skor -= 10
            skor2 +=10
            #Ekrana skoru yazma#
            sınır.undo()
            sınır.penup()
            sınır.hideturtle()
            sınır.setposition(-410,410)
            skorstring = "Can kazanmak için:%s" % skor
            sınır.write(skorstring, False, align="left", font=("Arial",16, "normal"))
            #Ekrana toplam skoru yazma#
            sınır2.undo()
            sınır2.penup()
            sınır2.hideturtle()
            sınır2.setposition(-90,410)
            skor2string = "Toplam Skor:%s" % skor2
            sınır2.write(skor2string, False, align="left", font=("Arial", 16, "normal"))
            # Ekrana can yazma#
            if skor == 0:
                can += 1
                skor = 100
                winsound.PlaySound("can.mp3", winsound.SND_ALIAS)
                sınır1.undo()
                sınır1.penup()
                sınır1.hideturtle()
                sınır1.setposition(350, 410)
                canstring = "Can: %s" % can
                sınır1.write(canstring, False, align="left", font=("Arial", 16, "normal"))


    #Zararlı hedef hareketi#
    for count in range(maxZhedefler):
        zhedefler[count].forward(3)

        #Sınır çekme-1 (x)#
        if zhedefler[count].xcor() > 380 or -380 > zhedefler[count].xcor():
            zhedefler[count].right(180)
            winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)
        #Sınır çekme-1 (y)#
        if zhedefler[count].ycor() > 380 or -380 > zhedefler[count].ycor():
            zhedefler[count].right(180)
            winsound.PlaySound("Duvar.mp3", winsound.SND_ASYNC)
        #Çarpışma-1#
        if carpisma(oyuncu, zhedefler[count]):
            zhedefler[count].setposition(random.randint(-370, 370), random.randint(-370, 370))
            zhedefler[count].right(random.randint(0, 360))
            winsound.PlaySound("skor.mp3", winsound.SND_ASYNC)
            skor += 20
            skor2 -= 20
            can -= 1
            print(skor)
            print(can)
            #Ekrana skoru yazma#
            sınır.undo()
            sınır.penup()
            sınır.hideturtle()
            sınır.setposition(-410, 410)
            skorstring = "Can kazanmak için:%s" % skor
            sınır.write(skorstring, False, align="left", font=("Arial", 16, "normal"))
            # Ekrana toplam skoru yazma#
            sınır2.undo()
            sınır2.penup()
            sınır2.hideturtle()
            sınır2.setposition(-90,410)
            skor2string = "Toplam Skor:%s" % skor2
            sınır2.write(skor2string, False, align="left", font=("Arial", 16, "normal"))
            #Ekrana can yazma#
            sınır1.undo()
            sınır1.penup()
            sınır1.hideturtle()
            sınır1.setposition(350, 410)
            canstring = "Can: %s" % can
            sınır1.write(canstring, False, align="left", font=("Arial", 16, "normal"))



    if can == 0:
        maxYhedefler = 0

        maxZhedefler = 0

        hız = 0

        sınır1.penup()
        sınır1.hideturtle()
        sınır1.setposition(-360, 0)
        bittistring = "Canınız kalmadı,Skorunuz:", skor2
        sınır1.write(bittistring, False, align="left", font=("Arial", 35, "normal"))
        winsound.PlaySound("bitis.mp3", winsound.SND_ALIAS)
        turtle.bye()









