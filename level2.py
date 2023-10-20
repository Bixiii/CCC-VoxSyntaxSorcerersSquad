
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
    coordsPairs = []
    for i in range(numCoordinates):
        pair = input_data[2 + map_size + i].split(" ")
        for element in pair:
            coordsPairs.append([int(coordinateString) for coordinateString in element.split(",")])

    with open(output_path, "w") as outfile:
        pass


def main():
    level = 1
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input_data/level{level}/level{level}_{i}.in"
        output_path = f"output_data/level{level}/level{level}_{i}.out"
        process_file(input_path, output_path)


if __name__ == "__main__":
    main()
