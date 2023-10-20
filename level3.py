def path_intersects(route):
    route_deduplicated = []
    for coordinate in route:
        if coordinate in route_deduplicated:
            continue
        route_deduplicated.append(coordinate)
    if len(route) != len(route_deduplicated):
        return True
    if path_intersects_diagonally(route):
        return True
    return False

def path_intersects_diagonally(route):
    diagonal_routes = filter_not_diagonally(route)
    for diagonal in diagonal_routes:
        first,second = diagonal
        x1,y1 = first
        x2, y2 = second
        normal2_first = [x2, y1]
        normal2_second = [x1,y2]
        if [normal2_first, normal2_second] in diagonal_routes or [normal2_second, normal2_first] in diagonal_routes:
            return True
    return False




def filter_not_diagonally(route):
    new_routes = []
    for i in range(len(route)-1):
        x1,y1 = route[i]
        x2,y2 = route[i+1]
        if x1 != x2 and y1 != y2:
            new_routes.append([route[i],route[i+1]])
    return new_routes




def process_file(input_path, output_path):

    input_data = []
    with open(input_path, "r") as infile:
        for line in infile:
            input_data.append(line.strip())  # do some parsing here
    map_size = int(input_data[0])
    map = []
    for i in range(map_size):
        map.append(input_data[1+i])
    numPaths = int(input_data[1+map_size])
    routes = []
    for i in range(numPaths):
        routeCoordinates = input_data[2 + map_size + i].split(" ")
        route = []
        for element in routeCoordinates:
            coordinate = [int(coordString) for coordString in element.split(",")]
            route.append(coordinate)
        routes.append(route)

    with open(output_path, "w") as outfile:
        for route in routes:
            result = "VALID"
            if path_intersects(route):
                result = "INVALID"
            outfile.write(f"{result}\n")


def main():
    level = 3
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input_data/level{level}/level{level}_{i}.in"
        output_path = f"output_data/level{level}/level{level}_{i}.out"
        process_file(input_path, output_path)
    #
    # input_path = f"input_data/level{level}/level{level}_example.in"
    # output_path = f"output_data/level{level}/level{level}_example.out"
    # process_file(input_path, output_path)


if __name__ == "__main__":
    main()
