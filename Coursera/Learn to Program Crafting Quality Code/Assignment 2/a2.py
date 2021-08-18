# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'R'
RAT_2_CHAR = 'H'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType

        Initialize the Rat object
        Symbol as in the letter that represents the Rat
        Row and Col (column) as where the Rat is located

        num_sprouts_eaten is a variable that keeps track on how much sprouts this rat has eaten.

        >>> rat1 = Rat('R', 1, 2)
        None
        
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """
        (Rat, int, int) -> NoneType

        Relocates where the Rat is supposed to be.
        Sets the instance's row and column to the one specified in the method.

        >>> rat1 = Rat('R', 1, 2)
        >>> rat1.set_location(2, 3)
        
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> NoneType

        Eats the sprout that the rat is on top of.
        Adds 1 to the number of sprouts eaten by the rat.

        >>> rat1 = Rat('R', 1, 2)
        >>> rat1.num_sprouts_eaten
        0
        >>> rat1.eat_sprout()
        >>> rat1.num_sprouts_eaten
        1
        
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str

        Returns the string representation of the Rat

        >>> rat1 = Rat('R', 1, 2)
        >>> print(rat1)
        'R at (1, 2) ate 0 sprouts'
        
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'\
               .format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    def __init__(self, content, rat1, rat2):
        """
        (Maze, list of list, Rat, Rat) -> NoneType

        Initializes the object Maze when called.

        content is referring to the structure of the maze,
        e.g. [['#', '#', '#', '#'],
              ['#', '#', '#', '#'],
              ['#', '#', '#', '#']] as in a 3x4 maze with all walls.
              
        >>> maze1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
                  ['#', '.', '.', '.', '.', '.', '#'], 
                  ['#', '.', '#', '#', '#', '.', '#'], 
                  ['#', '.', '.', '@', '#', '.', '#'], 
                  ['#', '@', '#', '.', '@', '.', '#'], 
                  ['#', '#', '#', '#', '#', '#', '#']], 
                  Rat('J', 1, 1),
                  Rat('P', 1, 4))
        None

        >>> maze1.num_sprouts_left
        3

        This call generates a maze with two rats, J and P

        """
        self.maze = content
        self.rat_1 = rat1
        self.rat_2 = rat2

        self.num_sprouts_left = 0

        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == SPROUT:
                    self.num_sprouts_left += 1
        
    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool

        Returns whether or not if the specified location is a wall
        >>> maze1 = Maze([['.', '#'], ['#', '#']], Rat('J', 0, 0), Rat('P', 0, 0))
        >>> maze1.is_wall(1, 1)
        True
        """
        
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str

        Precondition: The block at (row, col) is not a wall

        Returns '.' if the specified location at (row, col) does not have a rat
        Returns the Rat's symbol otherwise

        >>> maze1 = Maze([['.', '.'], ['.', '#']], Rat('J', 0, 0), Rat('P', 0, 1))
        >>> maze1.get_character(0, 0)
        'J'

        >>> maze1.get_character(1, 0)
        '.'
        """
        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol

        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol

        else:
            return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """
        (Maze, Rat, int, int) -> None

        Updates the position of the rat, also eats the sprout if the desired location has a sprout

        >>> rat1 = Rat('J', 0, 0)
        >>> rat2 = Rat('P', 1, 0)

        >>> maze1 = Maze([['.', '@'], ['.', '#']], rat1, rat2)
        >>> maze1.move(rat1, 0, 1)
        >>> maze1.num_sprouts_left
        0

        >>> rat1.num_sprouts_eaten
        1
        
        """

        if self.maze[rat.row + vertical][rat.col + horizontal] == WALL:
            return False

        rat.row += vertical
        rat.col += horizontal

        if self.maze[rat.row][rat.col] == SPROUT:
            
            rat.num_sprouts_eaten += 1
            
            self.maze[rat.row][rat.col] = HALL
            
            self.num_sprouts_left -= 1

        return True

    def __str__(self):
        """
        (Maze) -> str
        Generates the map
        
        """

        line = ''
        
        for row in range(len(self.maze)):
            
            for col in range(len(self.maze[row])):
                if self.rat_1.row == row and self.rat_1.col == col:
                    line += self.rat_1.symbol

                elif self.rat_2.row == row and self.rat_2.col == col:
                    line += self.rat_2.symbol

                else:
                    line += self.maze[row][col]
                
            line += '\n'

        line += str(self.rat_1) + '\n'
        line += str(self.rat_2)

        return line
    
