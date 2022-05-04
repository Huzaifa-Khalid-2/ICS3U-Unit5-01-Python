#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the temprature in farrenheiht


def calculate_temprature():
    # calculate temprature

    # input
    number_as_string = input("Enter your temprature (c): ")

    # output
    try:
        temprature_in_degree_celsius = int(number_as_string)
        final_temprature = (temprature_in_degree_celsius * 1.8) + 32
        print("\nThe temprature is {} farrenheit".format(final_temprature))
    except Exception:
        print("Inavild, input")
    finally:
        print("\nDone")


def main():
    # This function just calls other functions

    # call functions
    calculate_temprature()


if __name__ == "__main__":
    main()
