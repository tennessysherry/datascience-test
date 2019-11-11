# Create a method for requesting for a cab and paying for it
# have object attribute uber number plate and driver's name
class Uber:
    def __init__self(self,driver_name,uber_number_plate):  # function
        self.driver_name = driver_name
        self.uber_number_plate = uber_number_plate # number plate and driver are attributes

    def request_uber(self):
        return f"hi your uber's registration is  {self.uber_number_plate}"

    def pay_uber(self,amount):
       return f'pay KSh {amount} to {self.driver_name}'

uber_instance = Uber()
uber_instance.uber_number_plate = ('KBL 646 H')  # kbl is a value
uber_instance.driver_name = ('David')
print(uber_instance.request_uber())
print(uber_instance.pay_uber(250))

