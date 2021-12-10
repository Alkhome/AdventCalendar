FILEPATH = "/Users/jakubchilczuk/Desktop/Python/programowanie/adventtask1.txt"

if __name__ == '__main__':
    increased = 0

    text_file = open(FILEPATH, "r")
    line = text_file.readlines()
    count = 0
    compare = int(line[0]) + int(line[1]) + int(line[2])

    for i in range(len(line) - 3):
        meas = int(line[i + 1]) + int(line[i + 2]) + int(line[i + 3])
        if meas > compare:
            print("true")
            count += 1
        compare = meas
    print(count)
    text_file.close()
