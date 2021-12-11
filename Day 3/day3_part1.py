FILEPATH = "/Users/jakubchilczuk/Desktop/Python/programowanie/Advent/Day 3/data3.txt"
LINE_LENGTH = 12

if __name__ == '__main__':
    text_file = open(FILEPATH, "r")
    lines = text_file.readlines()
    str_gamma_rate = ""
    str_epsilon_rate = ""
    zeros = 0
    ones = 0
    for i in range(LINE_LENGTH):
        for j in range(len(lines)):
            if int(lines[j][i]) == 0:
                zeros += 1
            elif int(lines[j][i]) == 1:
                ones += 1
        if zeros > ones:
            str_gamma_rate += "0"
        elif ones > zeros:
            str_gamma_rate += "1"
        else:
            print("equals!")
        # due to the fact that there are no equals, I will omit the part of code that takes this
        # into consideration (just here)
        zeros = 0
        ones = 0

    for i in range (len(str_gamma_rate)):
        if str_gamma_rate[i] == "0":
            str_epsilon_rate += "1"
        elif str_gamma_rate[i] == "1":
            str_epsilon_rate += "0"

    text_file.close()
    print(str_gamma_rate)
    print(str_epsilon_rate)
    gamma_rate = int(str_gamma_rate, 2)
    epsilon_rate = int(str_epsilon_rate, 2)
    print(gamma_rate * epsilon_rate)



