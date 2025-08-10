import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count


    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count


    def __str__(self):
        return f"{self.cells} = {self.count}"


    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """

        # check if it have the same number of cells and mines
        if len(self.cells) == self.count:
            return self.cells
        
        return set()


    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        # check mines around the cell
        if self.count == 0:
            return self.cells
        return set()


    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        
        # eliminate the mine from self.cells and decrease the count by 1
        if cell in self.cells:
             self.cells.discard(cell)
             self.count -= 1


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        
        # eliminate the cell from self.cells
        if cell in self.cells:
             self.cells.discard(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []


    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)


    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)


    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)

        #2) mark the cell as safe
        self.mark_safe(cell)
        
        # 3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        # we create all the data we will use
        posibilites = [(-1, -1) , (-1, 0),  (-1, +1), ( 0, -1), ( 0, +1), (+1, -1), (+1, 0), (+1, +1)]
        candidate_neighbours = set()
        new_count = count

        # add all possible neighbours 
        for options in posibilites:
            case = ((cell[0]+options[0]), (cell[1]+options[1]))
            if 0 <= case[0] < self.height and 0 <= case[1] < self.width:
                candidate_neighbours.add(case)

        # filter all candidate neighbours with safes and mines                                      
        filtered_neighbours = candidate_neighbours.copy()
        for option in candidate_neighbours:
            if option in self.safes:
                filtered_neighbours.remove(option)
            if option in self.mines:
                filtered_neighbours.remove(option)
                new_count -= 1

        # if there are cells left in the filtered set, add the new sentence to knowledge
        if filtered_neighbours:
            new_sentence = Sentence(filtered_neighbours, new_count)
            self.knowledge.append(new_sentence)

        # 4) mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        next_step = True
        while next_step:

            #flag to indicate if new information is found in this iteration
            next_step = False

            # search for new information in the knowledge base
            for sentence in list(self.knowledge):

                # if the knowledge indicates that these cells are mines
                if sentence.known_mines():
                    for mines in sentence.known_mines():
                        if mines not in self.mines:
                            self.mark_mine(mines)
                            next_step = True

                # if the knowledge indicates that these cells are safe
                if sentence.known_safes():
                    for safes in sentence.known_safes():
                        if safes not in self.safes:
                            self.mark_safe(safes)
                            next_step = True

        # 5) add any new sentences to the AI's knowledge base if they can be inferred from existing knowledge
        # clean up: drop empty sentences
        new_list = []
        for s in self.knowledge:
            if len(s.cells) > 0:
                    new_list.append(s)
            
        self.knowledge = new_list
        new_sentence = True

        
        while new_sentence:
            new_sentence = False

            # copy to iterate safely
            new_knowledge = self.knowledge.copy()

            for x in range(len(new_knowledge)):
                for i in range(x + 1, len(new_knowledge)):
                    s1 = new_knowledge[x]
                    s2 = new_knowledge[i]

                    # skip empty just in case
                    if len(s1.cells) == 0 or len(s2.cells) == 0:
                        continue

                    # case a    
                    if s1.cells.issubset(s2.cells):
                        new_cells = s2.cells - s1.cells
                        new_count = s2.count - s1.count

                        if new_cells and 0 <= new_count <= len(new_cells):
                            # avoid duplicates
                            if not any(s.cells == new_cells and s.count == new_count for s in self.knowledge):
                                self.knowledge.append(Sentence(new_cells, new_count))
                                new_sentence = True

                    # case b
                    if s2.cells.issubset(s1.cells):
                        new_cells = s1.cells - s2.cells
                        new_count = s1.count - s2.count

                        if new_cells and 0 <= new_count <= len(new_cells):
                            # avoid duplicates
                            if not any(s.cells == new_cells and s.count == new_count for s in self.knowledge):
                                self.knowledge.append(Sentence(new_cells, new_count))
                                new_sentence = True


            # if added new sentence, need do other time step 4
            """
                If we modify the statements, we must update the knowledge base and 
                remove duplicates again. This step isn't optimal; it would be better 
                to create a definition and refer to it constantly, but it can cause 
                errors when correcting the exercise.
            """
            if new_sentence:
                    next_step = True
                    while next_step:

                        #flag to indicate if new information is found in this iteration
                        next_step = False

                        # search for new information in the knowledge base
                        for sentence in list(self.knowledge):

                            # if the knowledge indicates that these cells are mines
                            if sentence.known_mines():
                                for mines in sentence.known_mines():
                                    if mines not in self.mines:
                                        self.mark_mine(mines)
                                        next_step = True

                            # if the knowledge indicates that these cells are safe
                            if sentence.known_safes():
                                for safes in sentence.known_safes():
                                    if safes not in self.safes:
                                        self.mark_safe(safes)
                                        next_step = True

                    # drop empty sentences other time    
                    new_list = []
                    for s in self.knowledge:
                        if len(s.cells) > 0:
                                new_list.append(s)
            
                    self.knowledge = new_list


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        # obtain the safes moves
        candidates = self.safes - self.moves_made
        
        # do one random safe move or return None
        if candidates:
            return random.choice(list(candidates))
        return None


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        # obtain moves
        candidates = (self.cells - self.moves_made) - self.mines

        # do one random move if can, else return None
        if candidates:
            return random.choice(list(candidates))
        return None
