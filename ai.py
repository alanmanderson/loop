class AI:
    def __init__(self, board):
        self.board = board

    def reduce(self):
        self.adjacent_threes()

    def adjacent_threes(self):
        for coord, number in self.board.numbers.items():
            if number == 3:
                coords = self.board._get_coord(coord)
                for adjacent in self.board.get_adjacent_squares(coords[0], coords[1]):
                    if self.board.get_number(adjacent[0], adjacent[1]) == str(3):
                       if self.board.is_vertical(coord, str(adjacent[0])+','+str(adjacent[1])):
                           
                       self.board.mark_line(True, before, after)

        
