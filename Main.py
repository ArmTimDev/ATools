import turtle as tu
import random 
def Reverse():
  while True:
    A = input("Enter Your Text You Want To Reverse >>>")[::-1]
    print(A)
def draw_fractal(blen):
    sfcolor = ["brown", "green", "yellow", "gray"]
    my_turtle.color(random.choice(sfcolor))
print("Hello And Welcome !")
A = input("Choose One Of These Tools :\n- Reverser\n- Tree\nEnter The Name Of One Tool From Above >>>")
if A == 'Reverser':
  Reverse()
elif A == 'Tree':
  print("Working On It...")
else:
  print("Not Found")
