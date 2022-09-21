#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Sep 2022
# This program calculates the area and perimeter of a circle
#    with radius 12cm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 12 cm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 12**2))
    print("Perimeter is {} mm.".format(2 * math.pi * 12))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
