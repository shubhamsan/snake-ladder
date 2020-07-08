import turtle
import random
import time

die = [1, 2, 3, 4, 5]

screen = turtle.Screen()
screen.screensize(700, 580)
screen.title("Shubham Ladder game Window")
image = "/tmp/mozilla_shubham160/board.gif"
screen.bgpic(image)

t1 = turtle.Turtle()
t1.speed(0)
t1.penup()
t1.goto(-350, -290)


t1.hideturtle()
t1.goto(-292,-232)
s1=t1.pos()
t1.goto(-176,-232)
s2=t1.pos()
t1.goto(-60,-232)
s3=t1.pos()
t1.goto(56,-232)
s4=t1.pos()
t1.goto(-172,-232)
s5=t1.pos()
t1.goto(-288,-232)
s6=t1.pos()
t1.goto(288,-116)
s7=t1.pos()
t1.goto(172,-116)
s8=t1.pos()
t1.goto(56,-116)
s9=t1.pos()
t1.goto(-60,-116)
s10=t1.pos()
t1.goto(-176,-116)
s11=t1.pos()
t1.goto(-292,-116)
s12=t1.pos()
t1.goto(-292,0)
s13=t1.pos()
t1.goto(-176,0)
s14=t1.pos()
t1.goto(-60,0)
s15=t1.pos()
t1.goto(56,0)
s16=t1.pos()
t1.goto(172,0)
s17=t1.pos()
t1.goto(288,0)
s18=t1.pos()
t1.goto(288,116)
s19=t1.pos()
t1.goto(172,116)
s20=t1.pos()
t1.goto(56,116)
s21=t1.pos()
t1.goto(-60,116)
s22=t1.pos()
t1.goto(-176,116)
s23=t1.pos()
t1.goto(-292,116)
s24=t1.pos()
t1.goto(-292,232)
s25=t1.pos()
t1.goto(-176,232)
s26=t1.pos()
t1.goto(-60,232)
s27=t1.pos()
t1.goto(56,232)
s28=t1.pos()
t1.goto(172,232)
s29=t1.pos()
t1.goto(288,232)
s30=t1.pos()






t1.showturtle()



t1.goto(-350+58,-290+58)
current_pos=1
max_pos=30
t1.speed(3)
time.sleep(1)

snake_ladder = {3:22,5:8,11:26,17:4,19:7,20:29,21:9,27:1}
while current_pos != max_pos :
   t1.speed(2)
   time.sleep(1)
   dice = random.choice(die)
   time.sleep(1)
   print("roll =",dice)
   print("Before =",current_pos)
   current_pos = current_pos + dice
   print("After =",current_pos)

   if current_pos in [1,2,3,4,5,13,14,15,16,17,25,26,27,28,29,30]:
       t1.fd(116)
   if current_pos in [6,12,18,24] :
       t1.left(90)
       t1.forward(116)
       t1.right(90)
   if current_pos in [7,8,9,10,11,19,20,21,22,23]:
       t1.backward(116)
   if current_pos in snake_ladder:
       current_pos=snake_ladder.get(current_pos)
   if current_pos >max_pos:
       current_pos=current_pos-dice

   if current_pos==1:
       t1.goto(s1)
   if current_pos==2:
       t1.goto(s2)
   if current_pos==3:
       t1.goto(s3)
   if current_pos==4:
       t1.goto(s4)
   if current_pos==5:
       t1.goto(s5)
   if current_pos==6:
       t1.goto(s6)
   if current_pos==7:
       t1.goto(s7)
   if current_pos==8:
       t1.goto(s8)
   if current_pos==9:
       t1.goto(s9)
   if current_pos==10:
       t1.goto(s10)
   if current_pos==11:
       t1.goto(s11)
   if current_pos==12:
       t1.goto(s12)
   if current_pos==13:
       t1.goto(s13)
   if current_pos==14:
       t1.goto(s14)
   if current_pos==15:
       t1.goto(s15)
   if current_pos==16:
       t1.goto(s16)
   if current_pos==17:
       t1.goto(s17)
   if current_pos==18:
       t1.goto(s18)
   if current_pos==19:
       t1.goto(s19)
   if current_pos==20:
       t1.goto(s20)
   if current_pos==21:
       t1.goto(s21)
   if current_pos==22:
       t1.goto(s22)
   if current_pos==23:
       t1.goto(s23)
   if current_pos==24:
       t1.goto(s24)
   if current_pos==25:
       t1.goto(s25)
   if current_pos==26:
       t1.goto(s26)
   if current_pos==27:
       t1.goto(s27)
   if current_pos==28:
       t1.goto(s28)
   if current_pos==29:
       t1.goto(s29)
   if current_pos==30:
       t1.goto(s30)




   time.sleep(1)






screen.exitonclick()




