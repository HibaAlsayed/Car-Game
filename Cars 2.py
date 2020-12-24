name=input("What is your name? ")
print(f'''
{name}, Welcome to the game!
Type help for instructions.''')
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car already started!')
        else:
            started = True
            print("Car started.. Ready to go!")
    elif command == "stop":
        if not started:
            print("Car already stopped!!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''Start - to start the car 
Stop - to stop the car
Quit - to exit the game.''')
    elif command == "quit":
        print("See you soon!")
        break
    else:
        print("I don't understand that...")
