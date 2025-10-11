from collections import deque
from collections import defaultdict

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
print(my_queue)


my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)


def double(x):
    """
    multiplies its input by 2
    """
    return x * 2


def apply_to_one(f):
    """calls the function f with 1 as it's argument"""
    return f(1)


my_double = double

x = apply_to_one(my_double)
print(x)


def my_print(message="my default message"):
    print(message)


my_print()


def full_name(first="What's his name", last="Something"):
    return first + " " + last


full_name("John", "doe")

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[:3])


every_third = x[::3]
print(every_third)

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

"""Tuples are immutable"""
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
print(sp)
s, p = sum_and_product(5, 10)
print(s)

x, y = 1, 2
y, x = x, y

print(x)

empty_dict = {}
empty_dict2 = dict()
grades = {"joel": 80, "Tim": 95}


joels_grade = grades["joel"]

print(joels_grade)

print("Joel" in grades)
joels_grade = grades.get("Joel", 0)
no_ones_grade = grades.get("No one")
print(no_ones_grade)

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

print(grades)

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"],
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print(
    f"tweet keys: {tweet_keys}\ntweet values: {tweet_values}\ntweet items:{tweet_items}"
)

print("joelgrus" in tweet)

print("Dictionary exercises \n")
my_dict = {"name": "Alice", "age": 35, "city": "New York"}
my_dict["profession"] = "Doctor"
my_dict["age"] = 40
my_dict.pop("profession")
print(my_dict)
print("Printing all key-value pairs")
for key, value in my_dict.items():
    print(key, ":", value)


print("Dictionary from lists")

keys = ['Ten','Twenty','Thirty']
values = [10,20,30]

new_dict = dict(zip(keys,values))
print(new_dict)

my_dict.clear()

print(my_dict)
dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

merged = dict1|dict2

print(merged)

string1 = 'Jessa'
char_counts = {}
for char in string1:
    try:
        char_counts[char]+=1
    except KeyError:
        char_counts[char] = 1

print(f"Frequencies for 'Jessa' : {char_counts}")

data = {"person": {"name": "Alice", "age": 30}}

print(f"Alice's age is : {data['person']['age']}")


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
              "marks": {
                  "physics": 70, "history": 80
                  }
                  }
                  }
}

history_value = sampleDict['class']['student']['marks']['history']
print(history_value)

sampleDict['class']['student']['name'] = 'Jessa'

print(sampleDict['class']['student'])

employees = ["Kelly", "Emma"]
defaults = {"designation": "Developer", "salary": 8000}

employee_dict = dict.fromkeys(employees,defaults)

print(employee_dict)