
def process_file(input_path, output_path):

    input_data = []
    with open(input_path, "r") as infile:
        for line in infile:
            input_data.append(line.strip())  # do some parsing here

    results = input_data
    with open(output_path, "w") as outfile:
        for result in results:
            outfile.write(result + "\n")


def main():
    level = 1
    num_files = 5

    for i in range(1, num_files + 1):
        input_path = f"input_data/level{level}/level{level}_{i}.in"
        output_path = f"output_data/level{level}/level{level}_{i}.out"
        process_file(input_path, output_path)


if __name__ == "__main__":
    main()
