import random


class CountDownSolver:
    def __init__(self, big_numbers, numbers=None, target=None, **kwargs):
        self.big_numbers = big_numbers
        self.numbers = self.number_generator() if numbers is None else numbers
        self.target = random.randint(100, 1000) if target is None else target
        if kwargs.get('sure_target') is True:
            self.target = 6969

        add = lambda a, b: a + b
        sub = lambda a, b: a - b
        mul = lambda a, b: a * b
        div = lambda a, b: a / b if a % b == 0 else 0 / 0

        self.operations = [(add, '+'), (sub, '-'), (mul, '*'), (div, '/')]

    def generate_target(self):
        stack = []
        numbers_used = random.randint(2,6)
        operations_used = numbers_used - 1


    def number_generator(self):
        high = random.sample([25, 50, 75, 100], int(self.big_numbers))
        low = random.sample(range(1, 11), (6 - int(self.big_numbers)))
        number_list = high + low
        return number_list

    def solve(self):
        numbers = self.numbers
        target = self.target
        add = lambda a, b: a + b
        operations = self.operations
        global print_limit
        global print_stack
        print_limit = 100
        print_stack = [0]

        def evaluate(stack):
            try:
                total = 0
                last_operation = add
                for item in stack:
                    if type(item) is int:
                        total = last_operation(total, item)
                    else:
                        last_operation = item[0]

                return total
            except ZeroDivisionError:
                return 0

        def repr_stack(stack):
            reps = [str(item) if type(item) is int else item[1] for item in stack]
            return ' '.join(reps)

        def recurse(stack, nums):
            global print_limit
            global print_stack
            for n in range(len(nums)):

                stack.append(nums[n])

                remaining = nums[:n] + nums[n + 1:]

                if evaluate(stack) == target:
                    if len(repr_stack(stack)) <= print_limit:
                        print_limit = len(repr_stack(stack))
                        print_stack[0] = repr_stack(stack)

                if len(remaining) > 0:
                    for op in operations:
                        stack.append(op)
                        stack = recurse(stack, remaining)
                        stack = stack[:-1]

                stack = stack[:-1]

            return stack

        recurse([], numbers)
        return print_stack
