from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,com_name) -> None:
        self.com_name=com_name
        self.riders=[]
        self.drivers=[]
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.com_name} with riders: {len(self.riders)} and driver: {len(self.drivers)}'

class User(ABC):
    def __init__(self, name, email,nid) -> None:
        self.name=name
        self.email=email
        self.__nid=nid
        self.wallet=0
        # todo: set user id dynamically
        self.__id=0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid,current_location,inital_amount) -> None:
        self.current_ride=None
        self.wallet = inital_amount
        self.current_location=current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')

    def update_loc(self, current_location):
        self.current_location=current_location

    def load_cash(self, amount):
        if amount>0:
            self.wallet +=amount

    def request_ride(self, ride_sharing,destination):
        if not self.current_ride:
            ride_request= Ride_req(self,destination)
            ride_matcher =Ride_matching(ride_sharing.drivers)            
            ride=ride_matcher.find_driver(ride_request)
            print("got the ride",ride)
            self.current_ride = ride

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}')


    def accept_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start, end) -> None:
        self.start=start #
        self.end=end #
        self.driver = None 
        self.rider= None
        self.start_time=None 
        self.end_time=None 
        self.estimated_fare = None


    def set_driver(self, driver):
        self.driver=driver

    def set_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f"ride details: started {self.start} to {self.end}"

class Ride_req:
    def __init__(self,rider, end_loc) -> None:
        self.rider =rider
        self.end_loc=end_loc

    
class Ride_matching:
    def __init__(self,drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_req):
        if len(self.available_drivers)>0:
            # todo: find the closest driver of the rider
            driver = self.available_drivers[0]
            ride = Ride(ride_req.rider.current_location, ride_req.end_loc)
            driver.accept_ride(ride)
            return ride 
        

class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng':15
    }

    def __init__(self, vehicle_type, license, rate) -> None:
        self.vehicle_type=vehicle_type
        self.license=license
        self.rate = rate
        self.status='available'

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license, rate) -> None:
        super().__init__(vehicle_type, license, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license, rate) -> None:
        super().__init__(vehicle_type, license, rate)

    def start_drive(self):
        self.status = 'unavailable'

#check class integration:
bumper_ride = Ride_sharing("bumper_ride")
anamu = Rider("Anamul", "ana76@gmail.com", 1245, 'mohakhali', 1200)

bumper_ride.add_rider(anamu)
kapa_samsu  = Driver('kopa', 'kopakopi@gmail.com', 5380, 'gulshan')
bumper_ride.add_driver(kapa_samsu)

print(bumper_ride)

anamu.request_ride(bumper_ride,'Uttara')
anamu.show_current_ride()

