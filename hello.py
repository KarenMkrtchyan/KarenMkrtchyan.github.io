class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True 

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["bob0", "bob1", "bob2", "bob3"]

for i in people: 
    if flight.add_passenger(i):
        print(f"{i} mf is in")
    else:
        print(f"{i} md in not in")