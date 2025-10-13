friend = {"name": "Mark", "phone": "932-9683"}

friends = [
    {"name": "Matt", "phone": "231-2341"},
    {"name": "John", "phone": "342-5831"},
    {"name": "Luke", "phone": "523-3997"},
]

print(f"{friend['name']}'s phone number is {friend['phone']}")


friends.append(friend)


def printDetails(name, phone):
    print(f"{name}'s phone number is {phone}")


def printFriendsList(friends):
    for friend in friends:
        printDetails(friend["name"], friend["phone"])


# new_friend ={}

# new_friend['name'] = input("name:")
# new_friend['phone']= input("phone:")

# print(f"Name:{new_friend['name']}\nPhone:{new_friend['phone']}")

# friends.append(new_friend)

printFriendsList(friends)


def getPhoneNumber(name):
    for fr in friends:
        if fr["name"] == name:
            return fr["phone"]
    return "None"

print(getPhoneNumber("Luke"))
print(getPhoneNumber("Bill"))
print(getPhoneNumber("John"))
