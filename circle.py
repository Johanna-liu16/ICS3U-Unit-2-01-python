#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Sep 2022
# This program calculates the area and perimeter of a circle
#    with radius 12cm

import math


def main():
    # this function calculates the area and perimeter
    area = math.pi * 15**2
    perimeter = 2 * math.pi * 15

    print("If a circle has a radius of 15 cm: ")
    print("")
    print("Area = πr²")
    print("Area is {}mm².".format(round(area, 2)))
    print("Perimeter is {}mm.".format(round(perimeter, 2)))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
