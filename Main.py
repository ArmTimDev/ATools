def Reverse():
  while True:
    A = input("Enter Your Text You Want To Reverse >>>")[::-1]
    print(A)
print("Hello And Welcome !")
A = input("Choose One Of These Tools :\n- Reverser\n- Tree\nEnter The Name Of One Tool From Above >>>")
if A == 'Reverser':
  Reverse()
elif A == 'Tree':
  import turtle as tu
import random 
my_turtle = tu.Turtle()
my_turtle.screen.bgcolor('black')
my_turtle.left(90)
my_turtle.speed(100)
my_turtle.color('red')
my_turtle.pensize(10)
my_turtle.screen.title("Tree")

def draw_fractal(blen):
    sfcolor = ["brown", "green", "yellow", "gray"]
    my_turtle.color(random.choice(sfcolor))

    if(blen<10):
        return
    else:


        my_turtle.forward(blen)
        my_turtle.left(30)
        draw_fractal(3*blen/4)
        my_turtle.right(60)
        draw_fractal(3*blen/4)
        my_turtle.left(30)
        my_turtle.backward(blen)

draw_fractal(100)
my_turtle
le = tu.done()

print("By PythonyTools")
else:
  print("Not Found")
