# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# Print out options
for i in range(len(pie_list)):
    print("[" + str(i) + "] " + pie_list[i])

done= "yes"

while done == "yes":
  pindex = int(input("Which pie would you like?"))
  name = pie_list[pindex]

  pie_purchases.append(name)
  print(f"Great! We'll have that {name} pie right out for you")
  done = input("Would you like more pies?")

number = len(pie_purchases)
print(f"You ordered {number} of pies")
