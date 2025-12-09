from fontTools.merge.util import first

c = [-45,6,0,72,1543]

for i in c:
    print(i)


print(f"the last item : {c[4]}")

s = 'hello'
print(len(s))


a_list = []

for number in range(1,6):
    a_list.append(number)


for j in a_list:
    print(j)

letters = []
letters+="python"
for letter in letters:
    print(letter)

a = [1,2,3]
b= [1,3,3]

print(a==b)
print(a!=b)

def cube_list(values:list[int])->list[int]:
    for value in range(len(values)):
        values[value]**= 3

    return values

print(cube_list([1,2,3,4,5,6,7,8,9,10]))

characters = []
characters+="Birthday"
for character in characters:
    print(character)



student_tuple = ('Amanda',[98,85,87])
first_name,grades = student_tuple
print(first_name)

# Displaying a bar chart

numbers = [19,3,15,7,11]
print('\nCreating a bar chart from numbers: ')
print(f'Index{"Value":>8}   Bar')
for index, value  in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')