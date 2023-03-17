import time
from random import randint
import sys
import os

#(cmaxime)Running: Start Machine [ exec-time = 0.001 ms ]
def log(func):

    def decorator(*args, **kwargs):
        
        start_time = time.time_ns()
        ret = func(*args, **kwargs)
        elapsed_time = time.time_ns() - start_time
        if (elapsed_time < 1000000000):
            elapsed_time = f'{(elapsed_time / 1000000):.3f} ms'
        else:
            elapsed_time = f'{(elapsed_time / 1000000000):.3f} s'

        pretty_f_name = " ".join([w.capitalize() for w in func.__name__.split("_")])

        # Save a reference to the original standard output
        original_stdout = sys.stdout
        with open('machine.log', 'a') as f:
            # Change the standard output to the file we created
            sys.stdout = f
            print(f'({os.getlogin()})Running: {pretty_f_name:<14} [ exec-time = {elapsed_time} ]')
            # Reset the standard output to its 
            # original value
            sys.stdout = original_stdout
        
        return ret

    return decorator



class CoffeeMachine():

    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
        
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)