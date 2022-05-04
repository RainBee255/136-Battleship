# This is where the most of the game logic should be written in, things like AI routines and turns should be stored here.



def Play():
    While(True): 
        import sys
import pygame
from random import randint
#Board for holding ship locations
PLAYER_BOARD = [[""] * 10 for x in range(10)]
COMPUTER_BOARD = [[""] * 10 for x in range(10)]
#Board for displaying hits and misses
PLAYER_GUESS_BOARD = [[""] * 10 for x in range(10)]
COMPUTER_GUESS_BOARD = [[""] * 10 for x in range(10)]
SIZE_OF_SHIPS = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7, 'I': 8, 'J': 9}
SHIP_TYPES = ('Carrier, Battleship, Cruiser, Submarine, Destroyer')


#create board
def print_board(board):
    print("  A B C D E F G H I J")
    #print("                     ")
    row_number = 1
    for row in board:
        print("%d %s " % (row_number, ". ".join(row)))
        row_number += 1

#create ship placement
def place_ships(board):
    #loop through size of ships
    for ship_size in SIZE_OF_SHIPS:
        #loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                 orientation, row,column = random.choice(["H", "V"]), random.randint(0,9), random.randint(0,9)
            if check_ship_fit(ship_size, row, column, orientation):
                #check if ship overlaps
                if ship_overlaps(board, row, column, orientation, ship_size) == False:
                    #place ship
                    if orientation == "H":
                        for i in range(column, column + ship_size):
                            board[row][i] = "X"
                else:
                        for i in range(row, row + ship_size):
                            board[column][i] = "X"
                print_board(COMPUTER_BOARD)
                break
            else:
                place_ship = True
                print('Place ship with size of ' + str(ship_size))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_size, row, column, orientation):
                #check if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_size) == False:
                    #place ship
                        for i in range(column, column + ship_size):
                            board[row][i] = "X"
                    else:
                        for i in range(row, row + ship_size):
                            board[column][i] = "X"
                    print_board(PLAYER_BOARD)
                break


#check if ship fits in board
def check_ship_fit(SHIP_SIZE, row, column):
        if column + SHIP_SIZE > 10:
            return False
        else:
            return True
        if row + SHIP_SIZE > 10:
            return False
        else:
            return True
        
def ship_overlaps(board, row,column, orientation,  ship_size):
    if orientation == "H":
        for i in range(column, column + ship_size):
            if board[row][i] == "X":
                return True
            else:
                for i in range(row, row + ship_size):
                    if board[column][i] == "X":
                        return True
                    else:
                        return False

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try:
                row = input("Enter the row 1-10 of the ship: ")
                if row in '12345678910':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-10')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHIJ':
                     column = LETTERS_TO_NUMBERS[column]
                     break
            except KeyError:
                    print('Enter a valid letter between A-J')
            return row, column, orientation
        else:
            while True:
                try:
                    row = input("Enter the row 1-10 of the ship: ")
                    if row in '12345678910':
                        row = int(row) - 1
                        break
                except ValueError:
                        print('Enter a valid letter between 1-10')
            while True:
                try:
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGHIJ':
                        column = LETTERS_TO_NUMBERS[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-J')
            return row, column
            
#count all hit ships
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column =="X":
                count += 1
    return count

       
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
    while row not in "12345678910":
        print('Please enter a valid row:')
        row = input("Please enter a ship row 1-10:")
    column = input("Please enter a ship column A-J:").upper()
#if invalid answer inputed
    while column not in 'ABCDEFGHIJ':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-J').upper()
    return int(row) - 1, letters_to_numbers[column]
    

create_ships(PLAYER_BOARD)
turns = 10
while turns > 0:
    print('Welcome to battleship')
    print_board(PLAYER_GUESS_BOARD)
    row, column = get_ship_location()
    if PLAYER_GUESS_BOARD[row][column] == "O":
        print('You already guessed that')
    elif PLAYER_BOARD[row][column] == "X":
        print('Hit')
        PLAYER_GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print('Missed')
        PLAYER_GUESS_BOARD[row][column] = "O"
        turns -= 1
        
#check if all ships are hit
    if count_hit_ships(PLAYER_GUESS_BOARD) == 5:
        print("You won! Let's_play_again?")
        break
    #computer turn
        print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("You ran out of turns")

        place_ships(COMPUTER_BOARD)
        print_board(COMPUTER_BOARD)
        place_ships(PLAYER_BOARD)
        print_board(PLAYER_BOARD)
        




