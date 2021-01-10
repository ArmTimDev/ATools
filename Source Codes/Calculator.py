def Calculate():
  A = int(input("Hello ! Please Enter Your First Number You Want To Calculate : "))
  B = int(input("Great ! Please Enter Your Second Number You Want To Calculate : "))
  C = input("Now Choose An Action !\n\n1. Sum\n2. Minus\nEnter The Name Of Option You Want To Chose >>> ")
  if C == 'Sum':
    print(A+B)
  elif C == 'Minus':
    print(A-B)
  else:
    Calculate()

Calculate()
