from stacknode import *
import contextlib

print("\n/-\ Ханойские башни /_\\")

# Create the Stacks
stacks = []
left_stack = Stack("a")
middle_stack = Stack("b")
right_stack = Stack("c")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input("\nСколько вы хотите добавить колец в первый массив ?\n"))
while num_disks < 3:
    num_disks = int(input("Вам надо добавить больше 2 колец \n"))

for x in range(num_disks, 0, -1):
    left_stack.push(x)

num_optimal_moves = 2 ** num_disks - 1
print("\n{0} Это оптимальное количество шагов для решения задачи".format(num_optimal_moves))


# Get User Input
def get_input():
    choices = [x.get_name()[0] for x in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("{0} : {1}".format(letter, name))
        user_input = input("")
        if user_input == 'exit':
            print("Вы вышли из игры")
            quit()
        print(user_input)
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
                    break


# Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Текущий Массив...")
    for i in range(len(stacks)):
        stacks[i].print_items()
    while True:
        print("\nС какого массива перенести колько?\n")
        from_stack = get_input()
        print("\nВ какой массив перенести кольцо ?\n")
        to_stack = get_input()


        if from_stack.peek() == None:
            print("\n\n Неверный шаг, попробуйте ещё раз")
        elif to_stack.peek() == None or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nНеверный шаг, попробуйте ещё раз")

    print("\n\nВы закончили игру за  {0} ходов.\nОптимальное количество ходов: {1}".format(num_user_moves,
                                                                                           num_optimal_moves))
