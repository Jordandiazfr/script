#!/usr/bin/env python
# EXPLIQUEZ CETTE PARTIE
###
import os
import platform
import argparse


# EXPLIQUEZ CETTE PARTIE
###

# List 1
with open("list.txt") as l:
    my_list_txt = [int(n) for n in l.read().split(", ")]

# List 2
with open("list2.txt") as l:
    my_list2_txt = [int(n) for n in l.read().split(", ")]

my_nb = 10
multi_char = "0"

###

###

# AJOUTEZ LES INPUTS DES USERS
####
verbose = "The number of a function, the number 0 is a function to print a text, \n The number 1 " \
          "takes a list and a number and checks whether a specified value is contained in the list"

parser = argparse.ArgumentParser(description=verbose)
parser.add_argument('function', type=int, help='The number of the function')
parser.add_argument('-n', '--number', type=int, help='A single digit number', default=1)
parser.add_argument('-l', '--listone', help='A mutiple elements list', default=my_list_txt)
parser.add_argument('-s', '--strings', help='A mutiple elements list', default=multi_char)
parser.add_argument('-p', '--pos', help='The position of the new number in the list [beg] or [end]', default="end")

args = parser.parse_args()


####


# COMMENT ECRIRE UNE FONCTION DANS PYTHON ?
####

# **1
def merge_list(collection, collection2):
    print("We merge %s in %s without duplicates and only common factors" % (collection, collection2))
    collection3 = [n for n in set(collection) if n in set(collection2)]
    with open("merged.txt", mode="w") as merged:
        merged.write(str(collection3))
    return list(collection3)


# ** 2
def is_there(collection, number):
    print("is  %d in %s ?: " % (number, collection))
    return number in collection


# ** 3
def nb_char(string):
    chars = 0
    number = 0
    for s in string:
        try:
            int(s)
            number += 1
        except ValueError:
            chars += 1
    total = dict({"string": chars, "numbers": number})
    return total


# ** 4
def add_in_last(nb, list_1):
    one_list = list_1
    return one_list.append(int(nb))


# ** 5
def add_in_zero(nb, list_1):
    other_list = list_1
    return other_list.insert(0, int(nb))


# ** 6
def add_anywhere(nb, a_list, pos):
    if pos == "beg":
        add_in_zero(nb, a_list)
    elif pos == "end":
        add_in_last(nb, a_list)
    else:
        return "please insert a valid argument for position  to insert the number'beg' for beggining" \
               " and 'end' for the end"
    return a_list


# ** 7
def greater_than(num, a_list):
    return {lo: (num > lo) for lo in a_list}


# ** 8
def info_system():
    return "os name %s , platform %s, and release %s" % (os.name, platform.platform(), platform.release())


# ** 0
def exo1(argument=args.function, list_1=args.listone, list_2=my_list2_txt, numero=args.number, text=args.strings, pos=args.pos):
    # Takes the function number only
    if argument == 0:
        return "this is exercise 1"

    # Takes two optional lists from text files
    elif argument == 1:
        return merge_list(list_1, list_2)

    # Takes an optional number and list, or load a default number and a text file list
    elif argument == 2:
        if type(args.listone) == "int":
            print(type(args.listone))
            list_pro = args.listone.split(",")
            list_one = [int(n) for n in list_pro]
            print("hola")
            return is_there(list_one, numero)
        else:
            print("que tal")
            return is_there(list_1, numero)

    # Takes an string
    elif argument == 3:
        return nb_char(text)

    # Takes an optional number and add it into a list
    elif argument == 4:
        if args.number:
            with open("list.txt", mode="a") as add:
                add.write(str(f", {args.number}"))
            return add_in_last(args.number, my_list_txt)
        else:
            return add_in_last(numero, my_list_txt)

    # Takes an optional number and add it into  THE ZERO POSITION OF a list
    elif argument == 5:
        return add_in_zero(numero, my_list_txt)
    # Takes an optional number and add it into  A DEFINED POSITION OF THE LIST (BEG/END)

    elif argument == 6:
        return add_anywhere(numero, my_list_txt, pos)

    elif argument == 7:
        return greater_than(numero, my_list_txt)

    elif argument == 8:
        return info_system()

# AJOUTEZ UNE FONCTION POUR CHAQUE EXERCICE

''' 
** 1 - function that takes two lists as inputs and returns a list that contains only the elements 
that are common between the lists (without duplicates)

** 2 - function that takes a list and a number and checks whether a specified value is
contained in the list. whats the best type to return ? --  Boolean

** 3 - function that takes a string and calculate the number of digits and letters.
Choose the best return type, hint: dict

** 4 - function that takes as inputs a number and a list and adds my_nb to the end of the list. 
return list

** 5 - function that takes as inputs a number and a list and adds my_nb to the beggining of the list. 
return list

** 6 - function that takes as inputs a number and a list and adds my_nb either to the 
beginning or end of the list depending on an input specified by the user

** 7 - function that takes as inputs a number and a list and checks whether all numbers of the list
are greater than a certain number. whats the best return type ?

** 8 - function that gets OS name, platform and release information. what inputs do we need here ?
use package os

'''

# EXPLIQUEZ CETTE PARTIE
###
if __name__ == '__main__':
    function = exo1()
    print(function)

