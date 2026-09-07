name = input("What's yoour name?")
print("Welcome to "+ name + "'s Launch Console!")

running = True
while running:
    print("1) About Me")
    print("2) My Goals")
    print("3) Exit")
    choice = input("Pick 1-3: ")
    if choice =="1":
        print("...your about-me text...")
    elif choice == "2":
        print("My goal is to make Nationals this season for Swimming")
    elif choice =='3':
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")