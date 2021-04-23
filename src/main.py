# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
from typing import Tuple


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    test = datetime.datetime.now()

    test_str, test_str2 = first_method("aaa", "bb", "testC")

    print(test.year)
    print(test_str)
    print(test_str2)


def first_method(ai, ue, o) -> Tuple[str, str]:
    """
    :param ai:
    :param ue:
    :param o:
    :return str:
    """

    aaa = ai + ue + o
    return aaa, ai


if __name__ == '__main__':
    print_hi('PyCharm')
