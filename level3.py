def find_region(map, x, y):
    char = map[y][x]
    visited = {}
    get_region(map, char, visited, x, y)
    return visited


def get_key(x, y):
    return f'{x},{y}'


def get_region(map, char, visited, x, y):
    if get_key(x, y) in visited:
        return None
    if map[y][x] != char or x < 0 or y < 0 or x >= len(map) or y >= len(map):
        return None
    visited[get_key(x, y)] = {"coords": [x, y]}
    get_region(map, char, visited, x - 1, y)
    get_region(map, char, visited, x + 1, y)
    get_region(map, char, visited, x, y + 1)
    get_region(map, char, visited, x, y - 1)


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

    results = []
    print(routes)
    with open(output_path, "w") as outfile:
        outfile.writelines(results)


def main():
    level = 3
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input_data/level{level}/level{level}_{i}.in"
        output_path = f"output_data/level{level}/level{level}_{i}.out"
        process_file(input_path, output_path)

    # level = 2
    # input_path = f"input_data/level{level}/level2_example.in"
    # output_path = f"output_data/level{level}/level2_example.out"
    # process_file(input_path, output_path)


if __name__ == "__main__":
    main()
