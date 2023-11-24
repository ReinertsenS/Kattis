from collections import deque

numberOfOperations = int(input())

operations = []
for i in range(numberOfOperations):
    operation = input().split()
    operations.append(operation)

def updateTeque(front, back, command):
    number = int(command[1])
    if command[0] == 'push_front':
        front.appendleft(number)
    elif command[0] == 'push_middle':
        front.append(number)
    elif command[0] == 'push_back':
        back.append(number)

def reorganizeTeque(front, back):
    # Making sure the two deques' lengths are the same, or the front deque is the longer one (makes it easier to append when push_middle)
    if len(front) > len(back) + 1:
        back.appendleft(front.pop())
    elif len(front) < len(back):
        front.append(back.popleft())

front_deque = deque()
back_deque = deque()

for operation in operations:
    if operation[0] == 'get':
        index = int(operation[1])
        if index < len(front_deque):
            print(front_deque[index])
        else:
            print(back_deque[index - len(front_deque)])
    else:
        updateTeque(front_deque, back_deque, operation)
        reorganizeTeque(front_deque, back_deque)
