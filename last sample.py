# import packages for program
import copy, random

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,'G': 6, 'H': 7, 'I': 8, 'J': 9}
# class to contain all of the battleship game
class BattleshipGame:
    # function to print the board
    def print_board(self, s, board):
        # see if computer or user turn
        player = "Computer"
        if s == "u":
            player = "User"
        print(""+ player + "'s Grid")
        print("                    ")
        # print the horiz numbers
        print("    A     B     C     D     E     F     G     H     I     J")
        print("                                                           ")
        for i in range(10):
            # print the vertical line number
            if i != 9:
                print(str(i + 1) + "  ", end=' ')
            else:
                print(str(i + 1) + "  ", end=' ')
            # print the board values
            for j in range(10):
                if board[i][j] == -1:
                    print(' ', end=' ')
                elif s == "u":
                    print(board[i][j], end=' ')
                elif s == "c":
                    if board[i][j] == "O" or board[i][j] == "X":
                        print(board[i][j], end=' ')
                    else:
                        print(" ", end=' ')
                if j != 9:
                    print(" . ", end=' ')
            print()
            

# function to let the user place the ships
    def user_place_ships(self, board, ships):
        #lets the user place ships and also check if they are valid positions
        for ship in list(ships.keys()):
            # get coords and validate position
            valid = False
            while (not valid):
                self.print_board("u", board)
                type_of_ship = self.ship_type()
                x, y = self.get_coor()
                ori = self.V_or_H()
                valid = self.validate(board, ships[ship], x, y, ori)
                if not valid:
                    print("Illegal placement")
            # place the ship
            board = self.place_ship(board, ships[ship], ship[0], ori, x, y)
            self.print_board("u", board)
        input("No more ships to set. Ready to play.")
        return board

    # let the computer place/validate ships
    def computer_place_ships(self, board, ships):
        #computer will user random to generate ship places
        for ship in list(ships.keys()):
            # genreate random coordinates and validate the postion
            valid = False
            while (not valid):
                # use randint from import random
                x = random.randint(1, 10) - 1
                y = random.randint(1, 10) - 1
                o = random.randint(0, 1)
                # vertical or horiz
                if o == 0:
                    ori = "V"
                else:
                    ori = "H"
                valid = self.validate(board, ships[ship], x, y, ori)
            # place the ship
            print("Computer placing " + ship)
            board = self.place_ship(board, ships[ship], ship[0], ori, x, y)
        return board

    # let the user place a ship
    def place_ship(self, board, ship, s, ori, x, y):
        #accepts board, ship size, and position, places ship, it should already be verified by user_place_ships function
        
        # orient ships
        if ori == "V":
            for i in range(ship):
                board[x + i][y] = s
        elif ori == "H":
            for i in range(ship):
                board[x][y + i] = s
        return board

    # check if the ship fits
    def validate(self, board, ship, x, y, ori):
        #check if ship will fit, based on ship size, board, orientation, and coordinates
        if ori == "V" and x + ship > 10:
            return False
        elif ori == "H" and y + ship > 10:
            return False
        else:
            if ori == "V":
                for i in range(ship):
                    if board[x + i][y] != -1:
                        return False
            elif ori == "H":
                for i in range(ship):
                    if board[x][y + i] != -1:
                        return False
        return True

    # see if ship is horizontal or vertical
    def V_or_H(self):
        # get ship orientation from user
        while (True):
            user_input = input("vertical or horizontal (V,H) ? ").upper()
            if user_input == "V" or user_input == "H":
                return user_input
            else:
                print("Invalid input. Please only enter V or H").upper()

    
    
    def get_coor(self):
        """
        user will enter coordinates (row and column) for the ship to go
        """
        while (True):
            user_input = input("Please enter coordinates (row,col) ? ")
            try:
                # see that user entered 2 values seprated by comma
                coor = user_input.split(",")
                if len(coor) != 2:
                    raise Exception("Invalid entry.");
                # check that 2 values are integers
                coor[0] = int(coor[0]) - 1
                coor[1] = int(coor[1]) - 1
                # check that values of integers are between 1 and 10 for both coordinates
                if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                    raise Exception("Invalid entry. Please use values between 1 to 10 only.")
                # if everything is ok, return coordinates
                return coor
            # if the user enters something different
            except ValueError:
                print("Invalid entry. Please enter only numeric values for coordinates")
            except Exception as e:
                print(e)


    def ship_type(self):
        #get ship type from user
       while (True):
            print('1 Carrier, 1 Battleship, 1 Cruiser, 1 Submarine, 1 Destroyer')
            user_input = input("Place a ship of your fleet:")
            if user_input == "Carrier" or "Battleship" or "Cruiser" or "Submarine" or "Destroyer":
                return user_input
            else:
                print("Invalid input.")
    

    # see what move does
    def make_move(self, board, x, y):
       # make the move on the board and return the board, modified
        if board[x][y] == -1:
            return "miss"
        elif board[x][y] == 'O' or board[x][y] == 'X':
            return "try again"
        else:
            return "hit"


    def user_move(self, board):
        #keep getting coordinates from the user and check if its a hit miss or sink
    
        while (True):
            x, y = self.get_coor()
            res = self.make_move(board, x, y)
            if res == "hit":
                print("Hit")
                self.check_sink(board, x, y)
                board[x][y] = 'X'
                if self.check_win(board):
                    return "WIN"
            elif res == "miss":
                print("Miss.")
                board[x][y] = "O"
            elif res == "try again":
                print("Sorry, that coordinate was already hit. Please try again")
            if res != "try again":
                return board

    
    def computer_move(self, board):
        #generate random coorindates for the computer to try using random same as user_move function, check for hit, sink, miss
        while (True):
            x = random.randint(1, 10) - 1
            y = random.randint(1, 10) - 1
            res = self.make_move(board, x, y)
            if res == "hit":
                print("Hit")
                self.check_sink(board, x, y)
                board[x][y] = 'X'
                if self.check_win(board):
                    return "WIN"
            elif res == "miss":
                print("Miss.")
                board[x][y] = "O"
            if res != "try again":
                return board

    
    def check_sink(self, board, x, y):
        #figure out which ship is hit, then see how many points still exist in the ship, then see if sunk.
        #the ship is sunk if there are no more points left
        if board[x][y] == "C":
            ship = "Carrier"
        elif board[x][y] == "B":
            ship = "Battleship"
        elif board[x][y] == "C":
            ship = "Cruiser"
        elif board[x][y] == "S":
            ship = "Submarine"
        else:
            board[x][y] == "D"
            ship = "Destroyer"
        # mark cell as hit and check if sunk
        board[-1][ship] -= 1
        if board[-1][ship] == 0:
            print(ship + " Sunk")

    
    def check_win(self, board):
        #once all ships are sunk, then someone wins, end game. If anything is not a hit, then return false
        for i in range(10):
            for j in range(10):
                if board[i][j] != -1 and board[i][j] != 'O' and board[i][j] != 'X':
                    return False
        return True

    # function called to start program
    def main(self):
        # types of ships
        ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2,}
        # setup blank 10x10 board
        board = []
        for i in range(10):
            board_row = []
            for j in range(10):
                board_row.append(-1)
            board.append(board_row)
        # setup user and computer boards
        user_board = copy.deepcopy(board)
        comp_board = copy.deepcopy(board)
        # add ships in array
        user_board.append(copy.deepcopy(ships))
        comp_board.append(copy.deepcopy(ships))
        # ship placement
        user_board = self.user_place_ships(user_board, ships)
        comp_board = self.computer_place_ships(comp_board, ships)
        # game main loop
        while (1):
            # user move
            self.print_board("c", comp_board)
            comp_board = self.user_move(comp_board)
            # check if user won
            if comp_board == "WIN":
                print("User WON! :)")
                quit()
            # display current computer board
            self.print_board("c", comp_board)
            input("To end user turn hit ENTER")
            # computer move
            user_board = self.computer_move(user_board)
            # check if computer move
            if user_board == "WIN":
                print("Computer WON! :(")
                quit()
            # display user board
            input("To end computer turn hit ENTER")


root = BattleshipGame()
root.main()
