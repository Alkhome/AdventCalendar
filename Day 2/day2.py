FILEPATH = "/Users/jakubchilczuk/Desktop/Python/programowanie/Advent/Day 2/adventtask2.txt"

if __name__ == '__main__':
    increased = 0

    text_file = open(FILEPATH, "r")
    lines = text_file.readlines()
    new_list = []
    fwd = 0
    depth = 0
    aim = 0
    for line in lines:
        new_list.append(line.split(" "))
    for i in range(len(new_list)):
        if new_list[i][0] == "forward":
            fwd += int(new_list[i][1])
            depth += int(new_list[i][1]) * aim
        elif new_list[i][0] == "up":
            #depth -= int(new_list[i][1])
            aim -= int(new_list[i][1])
        elif new_list[i][0] == "down":
            #depth += int(new_list[i][1])
            aim += int(new_list[i][1])
        else:
            print("QueHE?")
    text_file.close()

    print(fwd)
    print(depth)
    print(aim)
    print(depth*fwd)
