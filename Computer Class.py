import time, random,string


class Computer():
    def __init__(self,
                 login = "Logged in",
                 system_features = ["i7","8 gb Ram","512  gb SSD"],
                 apps = ["Python"]):
        self.login = login
        self.system_features = system_features
        self.apps = apps
    def __str__(self):
        return f"Computer features is: {self.system_features}]"
    def enter(self):
        while True:
            sys_user_id = "rKENSHIN"
            sys_password = "asd123asd"
            attempts = 0
            user_id = input("\nUser name: ")
            user_password = input("Password: ")
            if attempts == 3:
                print("Too much wrong try.")
                break
            elif user_id == sys_user_id and user_password == sys_password:
                time.sleep(0.5)
                print("\ninformation is checked...")
                time.sleep(0.3)
                print(f"Welcome {sys_user_id}")
                break
            elif user_id != sys_user_id or user_password != sys_password:
                attempts += 1
                time.sleep(0.5)
                print("\ninformation is checked...")
                time.sleep(0.5)
                print("User name or password incorrect.")
    def update_app(self,app_name):
        self.apps.append(app_name)
        time.sleep(0.3)
        print(f"The ({app_name}) is installed.")
    def __len__(self):
        return len(self.apps)
    def calculator(self):
        transactions = input("""
        1- Addtion
        2- Substraction
        3- Multiplication
        4- Division
        Please chose your transaction: """)
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter a number: "))
        if transactions == "1":
            print(f"İşlem sonucu: {num1 + num2}")
        elif transactions == "2":
            print(f"İşlem sonucu: {num1 - num2}")
        elif transactions == "3":
            print(f"İşlem sonucu: {num1 * num2}")
        elif transactions == "4":
            print(f"İşlem sonucu: {num1 / num2}")
    def bmi_calculator(self):
        weight = float(input("Please enter your weight: "))
        high = float(input("Please enter your heigh in meters: "))
        bmi = weight/high**2
        if bmi < 18.5:
            print(f"Your bmi: {bmi}. You are underwight.")
        elif bmi >= 18.5 and bmi < 25.0:
            print(f"Your bmi: {bmi}. You are normal weight.")
        elif bmi >= 25.0 and bmi < 30:
            print(f"Your bmi: {bmi}. You are overveight.")
        elif bmi >= 30.0 and bmi < 35:
            print(f"Your bmi: {bmi}. You are obesity class 1.")
        elif bmi >= 35.0 and bmi < 40:
            print(f"Your bmi: {bmi}. You are obesity class 2.")
        elif bmi >= 40:
            print(f"Your bmi: {bmi}. You are obesity class 3.")

    def random_password_generator(self):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        lenght = int(input("Enter password lenght: "))
        random.shuffle(characters)
        password = []
        for i in range(lenght):
            password.append(random.choice(characters))
            random.shuffle(password)
        print("".join(password))

    def prime_number_finder(self):
        number = int(input("Please enter the number: "))
        if number == 1:
            print("1 in not a prime number.")
        if number == 2:
            print("2 is a prime number.")
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                break
            else:
                print(f"{number} a prime number.")
                break
computer = Computer()
computer.enter()
time.sleep(1)
print("""
İşlem Menüsü
1- Computer Info
2- Install App
3- Show Installed Apps
4- Basic Calculator
5- BMI Calculator
6- Random Password Generator
7- Prime Number Finder
""")
while True:
    action = input("\nPlease select the action you want to do. Press ""q"" for leave: ")
    if action == "q":
        print("Computer is closing.")
        break
    elif (action == "1"):
        print(computer)
    elif (action == "2"):
        appname = input("Please enter the apps: ")
        appname = appname.split(",")
        for i in appname:
            computer.update_app(i)
    elif (action == "3"):
        print(computer.apps)
    elif (action == "4"):
        computer.calculator()
    elif (action == "5"):
        computer.bmi_calculator()
    elif (action == "6"):
        computer.random_password_generator()
    elif (action == "7"):
        print("Welcome the Prime Number Finder.")
        computer.prime_number_finder()

















































