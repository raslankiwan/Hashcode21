
file_name = "Hashcode21/a.txt"
 
class Intersection:
    def __init__(self, id, streets_in, streets_out, schedule=None):
        self.id = id,
        self.schedule = schedule
        self.streets_in = streets_in
        self.streets_out = streets_out
    
class Car:
    def __init__(self, path):
        self.path = path # Array of streets

class Street:
    def __init__(self, length, name, intersection_start_B, intersection_end_E):
        self.length_L =  length
        self.name_N = name
        self.intersection_start_B = intersection_start_B
        self.intersection_end_E = intersection_end_E

if __name__ == '__main__':
    f = open(file_name, "r")
    first_line = f.readline()
    first_line = first_line.split(' ')
    simulation_line_D = int(first_line[0])
    number_of_intersections_I = int(first_line[1])
    number_of_streets_S = int(first_line[2])
    number_of_cars_V = int(first_line[3])
    bonus_points_F = int(first_line[4])

    Nodes = []
    for i in range(number_of_streets_S):
        line = f.readline()
        line = line.split(' ')
        intersection_start_B = int(line[0])
        intersection_end_E   = int(line[1])
        street_name = line[2]
        time_to_cross_L = line[3]

    for i in range(number_of_cars_V):
        line = f.readline()
        line = line.split(' ')
        number_of_streets_for_car_P = int(line[0])
        path_for_car = []
        for j in range(1, number_of_streets_for_car_P+1):
            path_for_car.append(line[j].strip())
        print(path_for_car)

