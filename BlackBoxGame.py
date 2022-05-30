# Name: Megan DeLong
# Date: 08/09/20
# Description: A game called black box in which four atoms are hidden on a 10x10
# square. The player can shoot rays from the border squares to locate the atom.
# Rays can hit the atom, deflect or exit the board directly.  The player can
# guess the location of atoms and will lose points if incorrect.

class BlackBoxGame:
    """
    Creates a BlackBoxGame class that has initializes a new board using
    the Board class and initializes a player using the Player class.  This
    class contains the methods: shoot_ray, guess_atom, get_score, atoms_left
    and displays the board.
    """


    def __init__(self, atoms):
        """
        Takes a list of atoms and initializes the BlackBoxGame class by creating a board and player,
        initializing the atom_count and guess trackeer.
        :param atoms: a list of atoms given
        """
        self._new_board = Board(atoms)
        self._board = self._new_board.get_board()
        self._player = Player()
        self._atom_count = len(atoms)
        self._guess_tracker = []

    def shoot_ray(self, row, column):
        """
        A method that checks for a valid move, returns False if invalid
        otherwise checks to see if ray is horizontal or vertical and calls
        the corresponding method.
        :param row: given row to start ray
        :param column: given column to start ray
        :return: False if move is not valid
        """

        if self._board[row][column] != "b" and self._board[row][column] != "u":
            return False
        #check if ray is vertical or horizontal and call method
        if row == 0 or row == 9:
            return self.shoot_vert_ray(row, column)
        if column == 0 or column == 9:
            return self.shoot_horiz_ray(row, column)

    def shoot_vert_ray(self, row, column):
        """
        Checks for reflection then calls shoot_ray_up or shoot_ray_down
        :param row: row where ray begins
        :param column: column where ray begins
        :return: (row, column) of exit point or None if move is a hit
        """

        if row == 0:
            # check for hit in first row
            if self._board[row+1][column] == "a":
                if self._board[row][column] != "u":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return None
            # check for reflection
            if self._board[row + 1][column - 1] == "a" or self._board[row + 1][column + 1] == "a":
                self._board[row][column] = "u"
                self._player.decrement_score(1)
                return (row, column)

            #Updates board and decrements score
            if self._board[row][column] != "u":
                self._board[row][column] = "u"
                self._player.decrement_score(1)

            return self.shoot_ray_down(row, column)

        if row == 9:
            # check for hit in first row
            if self._board[row-1][column] == "a":
                if self._board[row][column] != "u":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return None

            # check for reflection
            if self._board[row-1][column-1] == "a" or self._board[row-1][column+1] == "a":
                if self._board[row][column] == "b":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return (row, column)

            # updates board and decrements score
            if self._board[row][column] != "u":
                self._board[row][column] = "u"
                self._player.decrement_score(1)

            return self.shoot_ray_up(row, column)

    def shoot_horiz_ray(self, row, column):
        """
        Checks for deflections and hits or exits if none found
        :param row: row where ray begins
        :param column: row where ray begins
        :return: (row, column) of exit point or None if move is a hit
        """
        if column == 0:
            # check for hit in first column
            if self._board[row][column + 1] == "a":
                if self._board[row][column] == "b":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return None
            # check for reflection
            if self._board[row - 1][1] == "a" or self._board[row + 1][1] == "a":
                if self._board[row][column] == "b":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return (row, column)

            # Updates board and decrements score
            if self._board[row][column] != "u":
                self._board[row][column] = "u"
                self._player.decrement_score(1)

            return self.shoot_ray_right(row, column)

        if column == 9:
            # check for hit in first column
            if self._board[row][column-1] == "a":
                if self._board[row][column] == "b":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return None

            # check for reflection
            if self._board[row-1][8] == "a" or self._board[row + 1][8] == "a":
                if self._board[row][column] == "b":
                    self._board[row][column] = "u"
                    self._player.decrement_score(1)
                return (row, column)

            # Updates board and decrements score
            if self._board[row][column] != "u":
                self._board[row][column] = "u"
                self._player.decrement_score(1)
            return self.shoot_ray_left(row, column)


    def shoot_ray_down(self, row, column):
        """
        Shoots ray down
        Checks for deflections and hits or exits if none found
        :param row: row where ray begins
        :param column: column where ray begins
        :return: (row,column) of exit point or None if move is a hit
        """

        # check for atom in column
        atom_row = 9
        for i in range(row+1, 9):
            if self._board[i][column] == "a":
                atom_row = i
                break

         # check for deflection, if found, calls shoot_ray_right or shoot_ray_left
        for i in range(row+1,9):
            if self._board[i][column - 1] == "a" and self._board[i][column] != "a" and atom_row > i:
                return self.shoot_ray_right(i-1,column)
            if self._board[i][column + 1] == "a" and self._board[i][column] != "a" and atom_row > i:
                return self.shoot_ray_left(i-1, column)

        # check for hit
        for i in range(row+1, 9):
            if self._board[i][column] == "a":
                return None

        # No hit or deflection so ray exits
        for i in range(row+1, 11):
            if self._board[i][column] != "_":
                if self._board[i][column] == "b":
                    self._board[i][column] = "u"
                    self._player.decrement_score(1)
                return (i, column)

    def shoot_ray_up(self, row, column):
        """
        Shoots ray up
        Checks for deflections and hits or exits if none found
        :param row: row where ray begins
        :param column: column where ray begins
        :return: (row,column) of exit point or None if move is a hit
        """

        # check for atom in column
        atom_row = 0
        for i in range(row-1, 0, -1):
            if self._board[i][column] == "a":
                atom_row = i
                break

        # check for deflection, if found, call shoot_ray_right or shoot_ray_left
        for i in range(row-1, 0, -1):
            if self._board[i][column - 1] == "a" and self._board[i][column] != "a" and atom_row < i:
                return self.shoot_ray_right(i+1,column)
            if self._board[i][column + 1] == "a" and self._board[i][column] != "a" and atom_row < i:
                return self.shoot_ray_left(i+1, column)

        # check for hit
        for i in range(row-1, 0, -1):
            if self._board[i][column] == "a":
                return None

        # No hit or deflection so ray exits
        for i in range(row-1, -1, -1):
            if self._board[i][column] != "_":
                if self._board[i][column] == "b":
                    self._board[i][column] = "u"
                    self._player.decrement_score(1)
                return (i, column)

    def shoot_ray_right(self, row, column):
        """
        Shoots ray right
        Checks for deflections and hits or exits if none found
        :param row: row where ray begins
        :param column: column where ray begins
        :return: (row,column) of exit point or None if move is a hit
        """

        # check for atoms in same row
        hit_column = 9
        for i in range(column + 1, 9):
            if self._board[row][i] == "a":
                hit_column = i
                break

        # check for deflections
        for i in range(column+1, 9):
            if self._board[row - 1][i] == "a" and self._board[row][i] != "a" and hit_column > i:
                return self.shoot_ray_down(row, i - 1)
            if self._board[row + 1][i] == "a" and self._board[row][i] != "a" and hit_column > i:
                return self.shoot_ray_up(row, i - 1)

        # check for hit
        for i in range(column + 1, 9):
            if self._board[row][i] == "a":
                return None

        # No hit or deflection so ray exits
        for i in range(column+1, 10):
            if self._board[row][i] != "_":
                if self._board[row][i] == "b":
                    self._board[row][i] = "u"
                    self._player.decrement_score(1)
                return (row, i)

    def shoot_ray_left(self, row, column):
        """
        Shoots ray left
        Checks for deflections and hits or exits if none found
        :param row: row where ray begins
        :param column: column where ray begins
        :return: (row,column) of exit point or None if move is a hit
        """

        # check for atoms in same row
        hit_column = 0
        for i in range(column -1, 0, -1):
            # check for hit
            if self._board[row][i] == "a":
                hit_column = i
                break

        # check for deflections
        for i in range(column-1, 0, -1):
            if self._board[row - 1][i] == "a" and self._board[row][i] != "a" and hit_column < i:
                return self.shoot_ray_down(row, i + 1)
            if self._board[row + 1][i] == "a" and self._board[row][i] != "a" and hit_column < i:
                return self.shoot_ray_up(row, i + 1)

        # check for hit
        for i in range(column -1, 0, -1):
            if self._board[row][i] == "a":
                return None

        # No hit or deflection so ray exits
        for i in range(column-1, -1, -1):
            if self._board[row][i] != "_":
                if self._board[row][i] == "b":
                    self._board[row][i] = "u"
                    self._player.decrement_score(1)
                return (row, i)


    def guess_atom(self, row, column):
        """
        Returns True if player guess is correct, otherwise subtracts 5
        points and returns False
        :param row: given row of atom guess
        :param column: given column of atom guess
        :return: True if guess is correct, otherwise False
        """

        guess = (row, column)
        if guess in self._guess_tracker:
            return
        self._guess_tracker.append(guess)
        print(self._guess_tracker)
        if self._board[row][column] == "a":
            self._atom_count -= 1
            return True
        self._player.decrement_score(5)
        return False


    def get_score(self):
        """returns score"""
        return self._player.get_score()

    def atoms_left(self):
        """returns the number of atoms not guessed"""
        return self._atom_count

    def display_board(self):
        """
        displays board
        """

        for i in range(10):
            print(self._board[i])


class Board:
    """
    A Board class that creates a board with the status of each square.
    Board is called when BlackBoxGame is initialized
    "b" represents a border square, "c" represents a corner square
    "_" represents an open space, "a" reperesents an atom
    """
    def __init__(self, atoms):
        """
        Takes a list of atoms and initializes a board
        :param atoms: list of atoms from BlackBoxGame class
        """
        self._board = [[("_") for x in range(10)] for y in range(10)]
        self._board[0] = ["b" for b in range(10)]
        self._board[9] = ["b" for b in range(10)]

        for x in range(9):
            self._board[x][0] = "b"
            self._board[x][9] = "b"
        self._board[0][0] = "c"
        self._board[0][9] = "c"
        self._board[9][0] = "c"
        self._board[9][9] = "c"

        for atom in atoms:
            self._board[atom[0]][atom[1]] = "a"

    def get_board(self):
        """returns board"""
        return self._board


class Player:
    """
    A Player class that initializes, updates and stores the score for the player.
    Called by BlackBoxGame class in order to check or update score.
    """

    def __init__(self):
        """initializes the score  to 25"""
        self._score = 25

    def get_score(self):
        """returns score"""
        return self._score

    def decrement_score(self, loss):
        """decrements score by given number of points"""
        self._score -= loss

