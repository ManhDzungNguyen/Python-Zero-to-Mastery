from functools import wraps


def print_christmas_tree():
    print("    *     ")
    print("   ***    ")
    print("  *****   ")
    print(" *******  ")
    print("********* ")
    print("    |     ")
    print("    |     ")


from functools import wraps


class SuperPrint:
    def __init__(self) -> None:
        def idx():
            i = 0
            while True:
                yield i
                i += 1

        self.id = idx()

    def _index(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print(self.id.__next__(), end="  ")
            func(self, *args, **kwargs)

        return wrapper

    @_index
    def print_idx(self, *values):
        print(*values)
