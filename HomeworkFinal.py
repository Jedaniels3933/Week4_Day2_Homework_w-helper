from helper import d , get_deets , update_owner
class Vehicle():
    def __init__(self, reg_num = "r74268", type = 'corvette', owner = 'none'):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner
         
my_car = Vehicle('s778443' , 'ford' , 'jeremiah daniels')
get_deets(my_car)
d()  
update_owner(my_car, 'ainz ooal gown')
get_deets(my_car)
d()
Neighbor_veh = Vehicle('f121544' , 'toyota' , 'john cena')
get_deets(Neighbor_veh)
d()
spaceship = Vehicle( 'b008135', 'garbage class', 'Rick Sanchez')
get_deets(spaceship)
d()
print("After Rick's portal gun accident, this happened:")
update_owner(spaceship, 'Morty Smith')
get_deets(spaceship)

d()
d()
d()

class Event:
    def __init__(self, name, date, participant_count = 0):
        self.name = name
        self.date = date
        self.participant_count = participant_count

    def add_participant(self, count):
        self.participant_count += count

    
    def get_participant_count(self):
        print(f"Participant count: {self.participant_count}")

my_event = Event('Divorce Party', '12/12/2021', 50)
d()  
my_event.add_participant(10)
my_event.get_participant_count()
my_event.add_participant(5)
d()
my_event.get_participant_count()


    

    

    
    





    

