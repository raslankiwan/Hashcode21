print('Raslan is mnawer')
 
file_name = "a.txt"
 
f = open(file_name, "r")
first_line = f.readline()
simulation_line_D = int(first_line.split(" ")[0])
number_of_intersections_I = int(first_line.split(" ")[1])
number_of_streets_S = int(first_line.split(" ")[2])
number_of_cars_V = int(first_line.split(" ")[3])
bonus_points_F = int(first_line.split(" ")[4])

for i in range(number_of_streets_S):
    line = f.readline()
    intersection_start_B = int(line.split(" ")[0])
    intersection_end_E   = int(line.split(" ")[1])
    street_name = line.split(" ")[2]
    time_to_cross_L = line.split(" ")[3]

for i in range(number_of_cars_V):
    line = f.readline()
    number_of_streets_for_car_P = int(line.split(" ")[0])
    path_for_car = []
    for j in range(1, number_of_streets_for_car_P+1):
        path_for_car.append(line.split(" ")[j])
    print(path_for_car)