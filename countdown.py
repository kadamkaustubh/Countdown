import random
from time import sleep
import sys

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if a % b == 0 else 0 / 0

operations = [(add, '+'),
              (sub, '-'),
              (mul, '*'),
              (div, '/')]
def Solve(target, numbers):
    def Evaluate(stack):
        try:
            total = 0
            lastOper = add
            for item in stack:
                if type(item) is int:
                    total = lastOper(total, item)
                else:
                    lastOper = item[0]

            return total
        except:
            return 0

    def ReprStack(stack):
        reps = [str(item) if type(item) is int else item[1] for item in stack]
        return ' '.join(reps)
    def Recurse(stack, nums):
        for n in range(len(nums)):
            stack.append(nums[n])

            remaining = nums[:n] + nums[n + 1:]

            if Evaluate(stack) == target:
                print(ReprStack(stack))
                exit(0)

            if len(remaining) > 0:
                for op in operations:
                    stack.append(op)
                    stack = Recurse(stack, remaining)
                    stack = stack[:-1]

            stack = stack[:-1]

        return stack

    Recurse([], numbers)


target = random.randint(100, 1000)


# number = [ OneFromTheTop() ] + [ OneOfTheOthers() for i in range(5) ]


def number_generator():
    print('How many from the top? (pick between 1 and 4)')
    high_num = input()
    high = random.sample([25, 50, 75, 100], int(high_num))
    low = [random.randint(1, 10) for i in range(6 - int(high_num))]
    number_list = high + low
    return number_list


number = number_generator()
number_str = ''.join(str(number))
print('Great \nThe numbers are: \t', number_str)
sleep(2)
print('And the target is:\t', target)
# sleep(35)


for remaining in range(30, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    sleep(1)

sys.stdout.write("\rComplete!\n")

print("And the Answer is: \n")

Solve(target, number)
