import sys

from crossword import *
from collections import deque


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }


    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters


    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()


    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)


    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())


    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        # through all the variables
        for var in self.domains:

            # create a new set to add the candidates
            candidate_words = set()

            # through all words in the domain of this variable
            for word in self.domains[var]:

                # compare words with positions and add words to candidate if have the same lenght
                if len(word) == var.length:
                    candidate_words.add(word)
                
            # replace old words per domain for the new words per domain
            self.domains[var] = candidate_words
        

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        
        overlap = self.crossword.overlaps[(x, y)]
        deleted = False
        to_remove = set()

        # check overlap
        if overlap is None:
            return False              

        # asign indices of the overlap
        i, j = overlap

        # check all word in domains
        for xword in self.domains[x]:
            need_remove = True
            for yword in self.domains[y]:
                if xword[i] == yword[j]:
                    need_remove = False
                    break
            if need_remove:
                to_remove.add(xword)
                
        # if need remove words
        if to_remove:
            for w in to_remove:
                self.domains[x].remove(w)
            deleted = True

        # return true or false
        return deleted


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # create queue of arcs
        deque_arcs = deque()


        # initialize the queue
        if arcs is None:
            # if no arcs are provided, include all pairs (x, y) that overlap
            for x in self.crossword.variables:
                for y in self.crossword.neighbors(x):
                    if self.crossword.overlaps[(x, y)] is not None:
                        deque_arcs.append((x,y))
        else:
            # if arcs are provided, use them directly
            deque_arcs = deque(arcs)


        # process the queue until it is empty
        while deque_arcs:
            x, y = deque_arcs.popleft()

            # check if domain of x needs revision relative to y
            changed = self.revise(x, y)

            # if no change, skip this arc
            if not changed:
                continue

            # if domain of x is now empty = no solution is possible
            if changed and not self.domains[x]:
                return False

            # if domain of x was reduced but is still non-empty
            if changed:
                # re-enqueue all arcs (z, x) for neighbors z of x, except y
                for z in self.crossword.neighbors(x):
                    if z != y:
                        deque_arcs.append((z, x))
        

        # if queue is empty and no domain is empty = arc consistency enforced
        return True   


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # check values in assignment
        for value in self.crossword.variables:
            if value not in assignment or assignment[value] is None:
                return False
            
        return True


    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # iterate over assigned variables
        for var in assignment:
            
            # check length
            if len(assignment[var]) != var.length: 
                return False
            
            # check intersections with assigned neighbors
            for neighbor in self.crossword.neighbors(var):
                    if neighbor in assignment:

                        # overlap gives indices
                        overlap = self.crossword.overlaps[(var, neighbor)]
                        if overlap is not None:
                            i,j = overlap
                            if assignment[var][i] != assignment[neighbor][j]:
                                return False
        
        # check uniqueness of words
        if len(assignment.values()) != len(set(assignment.values())):
                return False
            
        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        raise NotImplementedError


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        domain_size = float("inf")
        candidate_var = []

        # find minimum domain size among unassigned variables
        for var in self.domains:
            if var not in assignment:
                size = len(self.domains[var])
                if size < domain_size:
                    domain_size = size

        # collect all unassigned variables with that minimum domain size
        for var in self.domains:
            if var not in assignment and len(self.domains[var]) == domain_size:
                candidate_var.append(var)
    
        # return None if haven't candidates
        if len(candidate_var) == 0:
            return None
        
        # if more than one candidate, break ties by degree
        if len(candidate_var) > 1:
            final_candidate = None
            final_neighbors = -1
            for var in candidate_var:
                neighbors = self.crossword.neighbors(var)
                unassigned_neighbors = {n for n in neighbors if n not in assignment}
                degree = len(unassigned_neighbors)
                if degree > final_neighbors:
                    final_candidate = var
                    final_neighbors = degree
            return final_candidate
        
        # if exactly one candidate, return it
        return candidate_var[0]


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
