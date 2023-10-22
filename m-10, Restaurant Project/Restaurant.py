class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name=name
        self.rent=rent
        self.chef = None    
        self.server = None
        self.manager = None
        self.orders=[]
        self.rent=rent
        self.menu=menu
        self.revenue=0
        self.expense=0
        self.balance=0
        self.profit= 0

    def add_employee(self, employe_type, employee):
        if employe_type=="chef":
            self.chef=employee
        elif employe_type=='server':
            self.server= employee
        elif employe_type=='manager':
            self.manager=employee 
    
    def add_order(self, order):
        self.orders.append(order)

    def receive_payment(self, order, amount, customer):
        print(amount, order.bill)
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount - order.bill
        else:
            print('not enough money. pay more')
        
    def pay_expense(self,amount, description):
        if amount<self.balance:
            self.expense+=amount
            self.balance-= amount
            print(f'expencse {amount} for {description}')
        else:
            print(f'not enought {amount}')
    
    def pay_salary(self,employee):
        # print(employee.salary)
        if employee.salary <self.balance:
            self.balance-= employee.salary
            self.expense+= employee.salary
            employee.receive_salary()

    def show_employee(self):
        print(f'----Showing Employees---------')
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary {self.chef.salary}')
        if self.server is not None:
            print(f'Chef: {self.server.name} with salary {self.server.salary}')
