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


student_tuple = ()
print (len(student_tuple))

student_tuple = 'John','Green',3.3
print(student_tuple)

another_student_tuple =('Mary','Red',3.3)
print(another_student_tuple)

a_singleton_tuple = ('red',)

print(another_student_tuple[1])

tuple2 = another_student_tuple
tuple2+=(10,40)

print(another_student_tuple)
print(tuple2)

print(another_student_tuple)

single_el_tuple = 123.45,
print(single_el_tuple[0])
list_1 = [1,2,3]
tuple_2 = (4,5,6)
list_1+=tuple_2
print(list_1)