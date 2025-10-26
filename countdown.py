def countdown(n):
    if n == 0:
        print("Lift off!") 
    elif n>0:
        print(f"{n}!")
        countdown(n-1)
        print(f"{n}!")
        

start = input("Count down from ? ")
countdown(int(start))