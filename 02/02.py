f = open('input.txt', 'r')
in_data = f.read()
in_data = in_data.split(',')

filtered_in_data = []
for i in in_data:
    if i != ',' and i != '\n':
        filtered_in_data.append(int(i))


def intcode(program):
    reading_point = 0
    program_length = len(program)
    while reading_point < program_length:
        if program[reading_point] == 99:
            return program
        value1 = program[reading_point + 1]
        value2 = program[reading_point + 2]
        storage_place = program[reading_point + 3]
        value = 0
        if program[reading_point] == 1: # Addition
            value = program[value1] + program[value2]
        if program[reading_point] == 2: # Addition
            value = program[value1] * program[value2]
        program[storage_place] = value
        reading_point = reading_point + 4
    return program


test1 = [1, 0, 0, 0, 99]
test2 = [2, 3, 0, 3, 99]
test3 = [2, 4, 4, 5, 99, 0]
test4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
print(f"""Test 1 success: {intcode(test1) == [2, 0, 0, 0, 99]}""")
print(f"""Test 2 success: {intcode(test2) == [2, 3, 0, 6, 99]}""")
print(f"""Test 3 success: {intcode(test3) == [2, 4, 4, 5, 99, 9801]}""")
print(f"""Test 4 success: {intcode(test4) == [30, 1, 1, 4, 2, 5, 6, 0, 99]}""")
print(f"""Main program: {intcode(filtered_in_data)}""")

# Part2
f = open('inputpart2.txt', 'r')
in_data = f.read()
in_data = in_data.split(',')

filtered_in_data = []
for i in in_data:
    if i != ',' and i != '\n':
        filtered_in_data.append(int(i))

for k in range(0, 100):
    for i in range(0, 100):
        filtered_in_data[1] = k
        filtered_in_data[2] = i
        input_program = filtered_in_data[:]
        try:
            p = intcode(input_program)
            if p[0] == 19690720:
                print(f"""SUCCESS k={k}, i={i}""")
        except:
            print("fail")
