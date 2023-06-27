class File:
    def __init__(self, name, files=None):
        self.name = name
        self.files = files
        self.is_dir = files is not None

# Nested structue representing a directory hierarchy
my_dir = File(
            'root', 
            files=[
                File(
                    'fnjjhqi', 
                    files=[
                        File(
                            'acfmfoj', 
                            files=[
                                File('oejibug')
                            ]
                        ),
                        File(
                            'bxineex', 
                            files=[
                                File('hbimokp')
                            ]
                        )
                    ]
                ),
                File(
                    'juixomy', 
                    files=[
                        File('mhrsska'),
                        File('rshijkq', files=[])
                    ]
                ),
                File('wimnnqz')
            ]
        )

# Each "file" dict has the following attributes:
# name: (str) the name of the file
# is_dir: (bool) whether this file is a directory
# files: (list) a list of the files in the directory
#               None if this file is not directory

# The equivalent structure
# root
# ├── fnjjhqi
# │   ├── acfmfoj
# │   │   └── oejibug
# │   └── bxineex
# │       └── hbimokp
# ├── juixomy
# │   ├── mhrsska
# │   └── rshijkq (dir, but empty)
# └── wimnnqz

# Write a recursive function to print just the files (non directories)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def print_files(file):
    if not file.is_dir:
        print(file.name)

        # notice that if this isn't a directory, we don't make
        # a recursive call. So this serves as the base case
        # which eventually stops the recursion
    else:
        for child in file.files:
            print_files(child)

print("== print_files ==")
print_files(my_dir)

# should print
# oejibug
# hbimokp
# mhrsska
# wimnnqz

# Write a recursive function to print just the directories
def print_dirs(file):
    # notice that if this isn't a directory, we don't make
    # a recursive call, which serves as the base case
    # that eventually stops the recursion

    if file.is_dir:
        print(file.name)
        for child in file.files:
            print_dirs(child)

print("== print_dirs ==")
print_dirs(my_dir)

# should print
# root
# fnjjhqi
# acfmfoj
# bxineex
# juixomy
# rshijkq

#
# CHALLENGING QUESTION
#############################

# Write a recursive function to print an indented view of the structure
# (indent by four spaces for each layer down in the structure)
def print_indented(file, depth=0):
    indent = "    " * depth  # build an indentation of 4 spaces for each level of depth in the directory hierarchy
    print(f"{indent}{file.name}")

    # exit if this file isn't a directory (it won't have a files collection)
    # this is the base case that eventually stops the recursion
    if not file.is_dir:
        return

    for child in file.files:
        print_indented(child, depth + 1)

print("== print_indented ==")
print_indented(my_dir)

# should print
# root
#     fnjjhqi
#         acfmfoj
#             oejibug
#         bxineex
#             hbimokp
#     juixomy
#         mhrsska
#         rshijkq
#     wimnnqz

#
# SUPER ULTRA BONUS QUESTION
#############################

#
# SERIOUSLY, THIS IS TOUGH
#############################

#
# OK, YOU'VE BEEN WARNED
#############################

# Write a recursive function that duplicates the structure display from the top of the explanation
def print_tree(file, has_next=None):
    # has_next tracks, at each level of indentation,
    # whether there is a next sibling,
    # which affects the glyphs used for indentation

    # notice that while the logic for building up the indenting
    # patterns is more complex here, in the main, the way
    # we move through the directory structure is identical
    # to the simpler print_indented

    has_next = has_next or []  # init to new empty list if default

    depth = len(has_next)

    # calculate the portion of the line related to indenting
    # a series of "│   " or "    "
    # we could move this to a helper
    indent = ""
    if depth > 1:  # we need to indent
        parts = []
        for i in range(depth - 1):
            joiner = "│" if has_next[i] else " "
            parts.append(f"{joiner}   ")
        indent = "".join(parts)

    # calculate the portion of the line that leads in to the name
    # either "├── " if it has a next sibling, otherwise "└── "
    # we could move this to a helper
    lead_in = ""
    if depth > 0:  # we need to attach the lead in
        joiner = "├" if has_next[-1] else "└"
        lead_in = f"{joiner}── "

    # print the line with its indentation and lead in
    print(f"{indent}{lead_in}{file.name}")

    # exit if this file isn't a directory (it won't have a files collection)
    # this is the base case that eventually stops the recursion
    if not file.is_dir:
        return

    child_count = len(file.files)
    for i, child in enumerate(file.files, 1):
        # for each child, include the built up history of what 
        # levels had next siblings, and include whether _this_
        # child has a next sibling
        print_tree(child, has_next + [i < child_count])

print("== print_tree ==")
print_tree(my_dir)

# should print
# root
# ├── fnjjhqi
# │   ├── acfmfoj
# │   │   └── oejibug
# │   └── bxineex
# │       └── hbimokp
# ├── juixomy
# │   ├── mhrsska
# │   └── rshijkq
# └── wimnnqz

#
# SUPER DUPER EXTRA CHALLENGE
##################################

# Research how to get actual file and directory information in
# Python, and build a little script to draw the above tree structure
# for some directory on your computer!

from os import listdir
from os.path import isfile, basename, join

def dirtree(path, has_next=None):
    has_next = has_next or []  # init to new empty list if default

    depth = len(has_next)

    # calculate the portion of the line related to indenting
    indent = ""
    if depth > 1:  # we need to indent
        parts = []
        for i in range(depth - 1):
            joiner = "│" if has_next[i] else " "
            parts.append(f"{joiner}   ")
        indent = "".join(parts)

    # calculate the portion of the line that leads in to the name
    lead_in = ""
    if depth > 0:  # we need to attach the lead in
        joiner = "├" if has_next[-1] else "└"
        lead_in = f"{joiner}── "

    print(f"{indent}{lead_in}{basename(path)}")

    if isfile(path):
        return

    files = sorted(listdir(path))
    child_count = len(files)
    for i, child in enumerate(files, 1):
        dirtree(join(path, child), has_next + [i < child_count])

print("== dirtree ==")
dirtree(".")

# in your own file, include the following to be able to run
# from the command line

# from sys import argv
# from os.path import realpath
#
# if __name__ == "__main__":
#     path = argv[1] if len(argv) == 2 else "."
#     path = realpath(path)
#     dirtree(path)
