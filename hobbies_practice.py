mypet = {"name":"cat",
        "age":3,
        "hobbies":["meow","eat","sleep"],
        "wakeup":{"monday":7, "tuesday":7,"wednesday":7}}
print(f'Hello my name is {mypet["name"]} and I am {mypet["age"]} years old')
print(f'I have {len(mypet["hobbies"])} hobbies')
print(f'my favorite hobby is {mypet["hobbies"][2]}')
print(f'on monday i wake up at {mypet["wakeup"]["tuesday"]}')