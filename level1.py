
def process_file(input_path, output_path):

    input_data = []
    with open(input_path, "r") as infile:
        for line in infile:
            input_data.append(line.strip())  # do some parsing here
    map_size = int(input_data[0])
    map = []
    for i in range(map_size):
        map.append(input_data[1+i])
    numCoordinates = int(input_data[1+map_size])
    coords = []
    for i in range(numCoordinates):
        coords.append([int(coordinateString) for coordinateString in input_data[2+map_size + i].split(",")])
    print(map_size, map, numCoordinates, coords, sep="\n")
    results = input_data
    with open(output_path, "w") as outfile:
        for coord in coords:
            x,y = coord
            value = map[x][y]
            outfile.write(f"{value}\n")


def main():
    level = 1
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input_data/level{level}/level{level}_{i}.in"
        output_path = f"output_data/level{level}/level{level}_{i}.out"
        process_file(input_path, output_path)


if __name__ == "__main__":
    main()
