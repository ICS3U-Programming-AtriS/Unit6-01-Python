#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 15, 2025
# Program that generates a random list of random numbers.
# It then displays the average of all the random numbers in the list.

import random
import constants


def main():
    # Initialize an empty list
    list_of_int = []

    # Fill the list up with random numbers
    for index in range(0, constants.MAX_ARRAY_SIZE):
        # Generate a random integer between MIN_NUM AND MAX_NUM
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        # Append it to the list
        list_of_int.append(random_number)
        # Display the list operation
        print(f"{random_number} added to the list at position {index}.")

    # Initialize variable to hold the sum
    sum = 0
    # Loop through all index positions
    for index in range(0, constants.MAX_ARRAY_SIZE):
        # Increase sum by the value found at the index
        sum += list_of_int[index]
    # Calculate the average
    average = sum / constants.MAX_ARRAY_SIZE
    # Display the average
    print(f"The average is {average}")


if __name__ == "__main__":
    main()
