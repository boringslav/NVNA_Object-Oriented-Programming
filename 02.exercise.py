import functools;

def exercise_01():
    arr = list(range(0,101))
    for i in range(0,len(arr),3):
        print("Every third num is: {}".format(arr[i]))

# exercise_01();

arr = list(range(0,50))

def exercise_02(arr):
    # sum = functools.reduce(lambda a,b: a+b,list)
    print("Sum: {}".format(sum(arr)))

# exercise_02(arr);

def exercise_03(arr):
    sum = 0;
    for i in range (0,len(arr)):
        if sum <= 50:
            sum += arr[i]
    print("Sum: {}".format(sum))

# exercise_03(arr)

def exercise_04(arr):
    sum = 0
    for i in range (0,len(arr)):
        if(list[i] % 2== 0): sum+=list[i]
        else: sum-= list[i]
    print("Sum is: {}".format(sum))

# exercise_04(arr)

def exercise_05():
    num_of_elements = int(input("Enter a value: "))
    arr = list(range(0, num_of_elements))
    print(arr)

exercise_05()