from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer, Manager, Serve
from Order import Order

def main():
    menu=Menu()
    pizza_1=Pizza('shutki Piza', 600, 'large', ['shtki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_item('drinks', coffee)

    # show menu
    menu.show_menu()

    restu = Restaurant('safa kabir restauratn', 2000, menu)

    # add employees
    manager = Manager('Kala Chan Manager', 5, 'kala@chan.com', 'kaliapur', '1500', 'Jan 1 2020','ok')
    restu.add_employee('manager', manager)
    chef = Chef('Rustom', 6, 'chupa@gmail.com', 'kahamakha', 60000, 'jan 1 ,2020', 'Chef','everything')
    restu.add_employee('chef', chef)
    server = Serve('Chotu server', 6, 'nai@gji.com', 'resturant', 500, 'jan 1,2002', 'server')
    restu.add_employee('server', server)

    # show employee
    restu.show_employee()

    customer_1=Customer('sakib vai', 6, 'khan@king.con', 'bosila', 600)
    order_1=Order(customer_1, [pizza_2, coffee])
    customer_1.pay_for_order(order_1)
    restu.add_order(order_1)
    # customer 
    restu.receive_payment(order_1, 2000, customer_1)

    print('revenue and balance: ',restu.revenue, restu.balance)

    # customer 2 placing an order
    customer_2=Customer('Jhaking vai', 6, 'khan@king.con', 'bosila', 600)
    order_2=Order(customer_2, [pizza_1,burger_2, coffee])
    customer_2.pay_for_order(order_2)
    restu.add_order(order_2)
    # customer 
    restu.receive_payment(order_2, 20000, customer_1)

    print('revenue and balance: ',restu.revenue, restu.balance)

    # pay rent
    restu.pay_expense(restu.rent, 'rent')
    print('after rent: ',restu.revenue, restu.balance, restu.expense)

    restu.pay_salary(server)
    print('after salary: ',restu.revenue, restu.balance, restu.expense)


# call the main
if __name__ == '__main__':
    main()