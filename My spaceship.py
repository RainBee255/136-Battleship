#create ships
#create ship loctations
#
#!/usr/bin/bash
import sys
import pygame
from random import randint
#Board for holding ship locations
HIDDEN_BOARD = [[""] * 10 for x in range(10)]
#Board for displaying hits and misses
GUESS_BOARD = [[""] * 10 for x in range(10)]
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7, 'I': 8, 'J': 9}
#create board
def print_board(board):
    print("  A B C D E F G H I J")
    print("                     ")
    row_number = 1
    for row in board:
        print("%d %s " % (row_number, ". ".join(row)))
        row_number += 1

#create ships
#X for placing ships and hit ships
#' ' for available space
#'O' for missed spot
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9), randint(0,9)
#check to avoid overlap
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
            
#getting ship location
def get_ship_location():
    row = input("Please enter a ship row 1-10:")
#if invalid answer inputed
    while row not in "123456789":
        print('Please enter a valid row:')
        row = input("Please enter a ship row 1-10:")
    column = input("Please enter a ship column A-J:").upper()
#if invalid answer inputed
    while column not in 'ABCDEFGHIJ':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-J').upper()
    return int(row) - 1, letters_to_numbers[column]
    
#count all hit ships
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column =="X":
                count += 1
    return count
create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to battleship')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "O":
        print('You already guessed that')
    elif HIDDEN_BOARD[row][column] == "X":
        print('Hit')
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print('Missed')
        GUESS_BOARD[row][column] = "O"
        turns -= 1
#check if all ships are hit
    if count_hit_ships(GUESS_BOARD) == 5:
        print('You won! Lets_play_again?')
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")
         
#print_board(HIDDEN_BOARD)
#print_board(GUESS_BOARD)
