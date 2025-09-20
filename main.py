#Times Table 
#tarvk002
import random



def get_input_from_user():
    input_stm = "Choose a number(2-9),or A for All,or R for Random, Q to Quit: " 
    while True:
      user_input = input(input_stm).strip().upper()
      if(user_input== "Q" or user_input =="A" or user_input =="Q"):
       return user_input
      if(user_input == "R"):
       return random.randint(2,9);
      if(user_input.isdigit()):
        user_input_to_int = int(user_input)
        if(user_input_to_int>=2 & user_input_to_int<=9):
          return user_input_to_int
        else:
          print(f"Invalid input.{input_stm}")
          

def printing_func(num):
  print(f"Times Table of {num}")
  for i in range(1,10):
   print(f"{num} x {i} = {num * i}")
  
def printAll_func():
  for j in range (2,10):
    printing_func(j)

flag = True
while flag:
 input_from_user = get_input_from_user()
 if(input_from_user == "Q"):
   print("Goodbye, Sad to see you go!!!")
   flag = False
 elif(input_from_user == "A"):
     printAll_func()
 else:
   printing_func(int(input_from_user))
  