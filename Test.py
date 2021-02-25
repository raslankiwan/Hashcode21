
from os import name, write


dataset = "f"
file_name = "./{}.txt".format(dataset)


class Intersection:
    def __init__(self, id, streets_in, streets_out, schedule=None):
        self.id = id,
        self.schedule = schedule
        self.streets_in = streets_in
        self.streets_out = streets_out


class Car:
    def __init__(self, path):
        self.path = path  # Array of streets

class Road:
    def __init__(self, name, used_times) -> None:
        self.name = name
        self.used_times = used_times

class Street:
    def __init__(self, length, name, intersection_start_B, intersection_end_E):
        self.length_L = length
        self.name_N = name
        self.intersection_start_B = intersection_start_B
        self.intersection_end_E = intersection_end_E


if __name__ == '__main__':
    f = open(file_name, "r")
    first_line = f.readline().strip()
    first_line = first_line.split(' ')

    simulation_time_D = int(first_line[0])
    number_of_intersections_I = int(first_line[1])
    number_of_streets_S = int(first_line[2])
    number_of_cars_V = int(first_line[3])
    bonus_points_F = int(first_line[4])

    Nodes = []

    street_dict = {}

    for i in range(number_of_streets_S):
        line = f.readline().strip()
        line = line.split(' ')
        intersection_start_B = int(line[0])
        intersection_end_E = int(line[1])
        street_name = line[2]
        time_to_cross_L = line[3]
        street = Street(time_to_cross_L, name=name,
                                   intersection_start_B=intersection_start_B, intersection_end_E=intersection_end_E)
        street_dict[street_name] = street

    cars_list = []

    for i in range(number_of_cars_V):
        line = f.readline().strip()
        line = line.split(' ')
        number_of_streets_for_car_P = int(line[0])
        path_for_car = line[1:]
        cars_list.append(Car(path_for_car))

    used_intersections = {}

    for car in cars_list:
        for road in car.path[:len(car.path) - 1]:
            street = street_dict[road]
            if street.intersection_end_E in used_intersections:
                if road in used_intersections[street.intersection_end_E]:
                    used_intersections[street.intersection_end_E][road] = used_intersections[street.intersection_end_E][road] + 1
                else:
                    used_intersections[street.intersection_end_E][road] = 1
            else:
                used_intersections[street.intersection_end_E] = {}
                used_intersections[street.intersection_end_E][road] = 1
    
    output_file = open("out_file_{}.txt".format(dataset), "w")

    output_file.write(str(len(used_intersections)))

    for intersection in used_intersections:
        output_file.write("\n")
        output_file.write(str(intersection))
        output_file.write("\n")
        output_file.write(str(len(used_intersections[intersection])))

        roads = []

        for road in used_intersections[intersection]:

            r = Road(road, used_intersections[intersection][road])
            roads.append(r)

        sorted_roads = sorted(roads, key=lambda x: x.used_times)
        
        time = 0

        old_value = -1

        for road in sorted_roads:
            output_file.write("\n")
            if road.used_times != old_value:
                time += 1
            output_file.write(road.name + " " + str(time))
            old_value = road.used_times

    output_file.close()