import random

file_name = "Hashcode21/b.txt"
 
class Intersection:
    def __init__(self, id, streets_in=[], streets_out=[], schedule=None):
        self.id = id,
        self.schedule = schedule
        self.streets_in = streets_in
        self.streets_out = streets_out
    
class Car:
    def __init__(self, path=[]):
        self.path = path # Array of streets
        self.priority = 0 # lowest possible vlaue ; while -1 being neglegted,
        self.path_time = 0

    def calculate_path_length(self):
        sum = 0 
        for street in self.path:
            sum += street.length_L
        self.path_time = sum
        return sum
    
    def set_priority(self, priority):
        self.priority = priority
    
class Street:
    def __init__(self, length, name, intersection_start_B, intersection_end_E):
        self.length_L =  length
        self.name = name
        self.intersection_start_B = intersection_start_B
        self.intersection_end_E = intersection_end_E
    
    @classmethod
    def get_street(cls, streets, name):
        for street in streets:
            if street.name == name:
                return street
    
    def __str__(self):
        return f'{self.name}'

if __name__ == '__main__':

    f = open(file_name, "r")
    first_line = f.readline()
    first_line = first_line.split(' ')
    simulation_line_D = int(first_line[0])
    number_of_intersections_I = int(first_line[1])
    number_of_streets_S = int(first_line[2])
    number_of_cars_V = int(first_line[3])
    bonus_points_F = int(first_line[4])

    print(f'simulation time = {simulation_line_D} seconds')
    print(f'bonus = {bonus_points_F} points')

    # initialize nodes.
    nodes = []
    for i in range(number_of_intersections_I):
        nodes.append(Intersection(id=i))

    # initialize streets
    streets = []
    for i in range(number_of_streets_S): # 5
        line = f.readline()
        line = line.split(' ')
        intersection_start_B = int(line[0])

        intersection_end_E   = int(line[1])
        street_name = line[2]
        time_to_cross_L = int(line[3])
        street = Street(length=time_to_cross_L,
                        name=street_name, 
                        intersection_start_B=intersection_start_B, 
                        intersection_end_E=intersection_end_E
                        )
        streets.append(street)
        nodes[intersection_start_B].streets_out.append(street)
        nodes[intersection_end_E].streets_in.append(street)

    cars = []
    for i in range(number_of_cars_V):
        line = f.readline()
        line = line.split(' ')
        number_of_streets_for_car_P = int(line[0])
        path_for_car = []
        for j in range(1, number_of_streets_for_car_P+1):
            path_for_car.append(Street.get_street(name=line[j].strip(), streets=streets))
        car = Car(path=path_for_car)
        cars.append(car)

    for index, car in enumerate(cars):
        starting_intersection = car.path[0].intersection_start_B
        path_time = car.calculate_path_length()
        car_priority = simulation_line_D - path_time
        car.set_priority(car_priority)
        
    # cars_prioritised  = sorted(cars, key=lambda x: x.priority, reverse=True)
    # for car in enumerate(cars_prioritised):
    #     print(f'{car.path[0]}')

    output_file = open("output.txt", "w+")

    ans_number_of_intersections = random.randint(a=1, b=number_of_intersections_I)
    output_file.write(ans_number_of_intersections+'\n')
    for i in range(ans_number_of_intersections):
        target_node = nodes[random.randint(a=0, b=ans_number_of_intersections)]
        node_id = target_node.id
        output_file.write(node_id+'\n')
        ans_number_of_in_streets = random.randint(a=0, b=len(target_node.streets_in))
        output_file.write(ans_number_of_in_streets+'\n')
        for j in range(ans_number_of_in_streets):
            target_street = target_node.streets_in[j]
            target_street_name = target_street.name
            ans_number_of_seconds = random.randint(a=1, b=target_street.length_L)
            output_file.write(target_street_name+' '+ans_number_of_seconds+'\n')
