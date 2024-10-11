# Your first name: Sandra
# Your section: 2

"""
NOTE: I modified the code, because if the seed is in main, the same calculation
will be done each time, and the numbers generated won't work. It would only work
either if the seed is in the function itself, or if the 2 functions (calculating
and calling at 500 times) were 1 function.
I switched it so that a new seed is randomly generated inside each of the functions
when they are called so that the code functions properly.
"""

import random
import matplotlib.pyplot as plt


# Write your functions with their docstrings here

# nextMiddleSquare
def nextMiddleSquare():
    """
    this function generates a seed (2-digit number), then squares it, and takes the two middle digits of it,
    and then devides them to create a random number between 0 and 1
    :return: the randomly generated number
    """
    y = random.randint(10, 99)
    y2 = y**2
    x = int(y2 / 10) % 100
    return x/10


# listMiddleSquare
def listMiddleSquare():
    """
    this function calls the listMiddleSquare() function 500 times to generate a random number list
    :return: the function returns the number list generated
    """
    number_list = []
    for i in range(500):
        number_list.append((nextMiddleSquare() / 10))
    return number_list


# nextLehmer

def nextLehmer(a, m):
    """
    this function uses a mathematically calculated sequence called the Lehmer sequence
    to randomly generate a number between 0 and 1
    :param a: the factor that multiplies the random number (seed) in the equation
    :param m: the factor that we use % to take the remainder from in the equation
    :return: the function returns the random number generated
    """
    random_number = random.randint(0, 100)
    random_number = (random_number * a) % m
    return random_number


# listLehmer

def listLehmer():
    """
    this function calls the nextLehmer() function 500 times to generate a random number list
    :return: the function returns the number list generated
    """
    number_list2 = []
    for i in range(500):
        number_list2.append((nextLehmer(17, 101) / 100))
    return number_list2


# listRandom

def listRandom():
    """
    this function uses the random.random() function 500 times to generate a list of random numbers
    :return: returns the number list generated
    """
    number_list3 = []
    for i in range(500):
        number_list3.append(random.random())
    return number_list3


def chartRandomNumbers(mid, lehmer, rand):
    """
    This function draws a histogram of the three lists on the same plot
    :param mid: a list of random numbers from middle squares
    :param lehmer: a list of random numbers from lehmer
    :param rand: a list of random numbers from Python random module
    """
    multi = [mid, lehmer, rand]
    plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
    plt.legend(prop={'size': 10})
    plt.show()


def main():
    list1 = listMiddleSquare()
    list2 = listLehmer()
    list3 = listRandom()
    chartRandomNumbers(list1, list2, list3)


if __name__ == "__main__":
    main()
