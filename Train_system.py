class Train():
    def __init__(self ,name, id, location, destination) -> None:
        self.name=name 
        self.id=id
        self.location=location
        self.destination=destination

class Admin(Train):
    train_list=[]
    passenger_list=[]
    seats={}

    def __init__(self, email) -> None:
        self.email=email

    def add_train(self, name, id, location, destination):
        new_train=Train(name, id, location, destination)
        self.train_list.append(new_train)
        seat=[]
        for i in range(10):
            seat.append(['a','a','a','a'])
        self.seats[id] = seat


    def show_available_train(self):
        for train in self.train_list:
            print(f"train name: {train.name}, location: {train.location}, destination: {train.destination}")

    def show_available_seats(self, id):
        # self.seats[id]
        for i in self.seats[id]:
            for j in i:
                print(j, end=' ')
            print()

    def book_seat(self, id):
        row=int (input("enter row: "))
        col=int(input("enter column: "))

        self.seats[id][row][col] = 'X'
        print("Seats booked")


class Users:
    def __init__(self, name, email, password) -> None:
        self.name=name 
        self.email=email
        self.password=password

admin=Admin("admin@gmail.com")

while(True):
    user_type= input("admin/user ? ")
    if user_type=='user':
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice= int(input("enter choice: "))

        if choice==1:
            email=input("enter mail: ")
            password= input("enter password: ")

            for user in admin.passenger_list:
                if user.email== email and user.password==password:
                    print(f"Welcome {user.name}")
                    while(True):
                        print("1. show available Trains")
                        print("1. show available seats")
                        print("3. Book seats")
                        print("4. logout")

                        choice = int(input("Enter option: "))
                        
                        if choice==1:
                            admin.show_available_train()
                        elif choice==2:
                            id=int(input("Enter train id: "))
                            admin.show_available_seats()
                        elif choice==3:
                            id=int(input("Enter train id: "))
                            admin.book_seat()

                        else:
                            break
                else:
                    print("No user found. Try again")

        elif choice==2:
            name= input("Enter name: ")
            email=input("enter mail: ")
            password= input("enter password: ")

            new_user = Users(name, email,password)
            admin.passenger_list.append(new_user)
            print("Registered Successfully")

        else:
            break

    elif user_type=='admin':
        email=input("enter mail: ")
        password= input("enter password: ")

        if email=='admin' and password=='admin':
            print("Admin logged in Successfull !!")

            while(True):
                print("Select a option below.")
                print("1. add trains")
                print("2. show all available trains")

                option= int(input("Select option: "))

                if option==1:
                    name=input("ENter name: ")
                    id=int(input("ENter Id : "))
                    location=input("Enter location: ")
                    destination=input("Enter destination: ")

                    admin.add_train(name, id, location, destination)
                    print("Successfully added train")

                elif option==2:
                    admin.show_available_train()

                else:
                    print("Select a valid option.")

        else:
            print("Wrong email or password")
    else:
        break




