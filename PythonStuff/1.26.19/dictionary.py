mememe = {"name": "Laura",
          "age": 25,
          "hobbies": ["snowboarding", "fitness"],
          "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}


print(f'Hello I am {mememe["name"]} and I am a {mememe["age"]}')
print(f'I have {len(mememe["hobbies"])} hobbies!')
print(f'On Saturdays I get up at {mememe["wake-up"]["Saturday"]}')
