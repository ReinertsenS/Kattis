import math

def calculate_location(tests):
    x_values = [] # For use as a parameter when calculatin the average
    y_values = [] # For use as a parameter when calculatin the average

    for i in range(tests):
        direction = input()
        parts = direction.split()
        
        initial_x = float(parts[0])
        initial_y = float(parts[1])
        initial_direction = 0

        # The start/turn and walk calculation
        for i in range(3, len(parts), 4):

            # Given angle in degrees and distance
            angle_degrees = initial_direction + float(parts[i])
            initial_direction = (initial_direction + float(parts[i])) % 360
            distance = float(parts[i+2])

            # Convert angle to radians for Python's trigonometric functions
            angle_radians = math.radians(angle_degrees)

            # Calculate the change in x and y
            change_in_x = math.cos(angle_radians) * distance
            change_in_y = math.sin(angle_radians) * distance

            # Updating x and y for every instruction
            initial_x += change_in_x
            initial_y += change_in_y

        x_values.append(initial_x)
        y_values.append(initial_y)

    # result = calculate_average(x_values, y_values) # ! For when you want to print all the results at the end (after n==0)
    # return result                                  # ! For when you want to print all the results at the end (after n==0)

    calculate_average(x_values, y_values) # ? Activate this to print result from each test as you go

def calculate_average(x, y):
    x_average = sum(x) / len(x)
    y_average = sum(y) / len(y)

    distances = []

    # Calculate distances of each point from the average
    for x, y in zip(x, y):
        distance = math.sqrt((x - x_average)**2 + (y - y_average)**2)
        distances.append(distance)

    # Find the maximum distance among the points
    max_distance = max(distances)

    print("{:.6f} {:.6f} {:.6f}".format(x_average, y_average, max_distance)) # ? Activate this to print result from each test as you go
    # result = "{:.6f} {:.6f} {:.6f}".format(x_average, y_average, max_distance) # ! For when you want to print all the results at the end (after n==0)
    # return result                                                              # ! For when you want to print all the results at the end (after n==0)

def main():
    # all_results = []
    while True:
        numberOfTests = int(input())

        if numberOfTests == 0:
            break
        else:
            # all_results.append(calculate_location(numberOfTests)) # ! For when you want to print all the results at the end (after n==0)
            calculate_location(numberOfTests) # ? Activate this to print result from each test as you go
            
    # for result in all_results: # ! For when you want to print all the results at the end (after n==0)
    #     print(result)          # ! For when you want to print all the results at the end (after n==0)

if __name__ == '__main__':
    main()
