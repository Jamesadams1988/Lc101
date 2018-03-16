class Car:
    def __init__(self,gas_level):
        self.gas = gas_level
    def add_gas(self,amount):
        if self.gas < 13:
            self.gas = self.gas + amount
            return amount
        else:
            return amount
    def fill_up(self):
        if self.gas >= 13:
            return 0
        else:
            amt = float(13 - self.gas)
            self.add_gas(amt)
            if amt % 1 == 0:
                return(int(amt))
            else:
                return(float(amt))

def main():
    cars = Car(5.5)
    print(cars.fill_up())
   

if __name__ == '__main__':
    main()