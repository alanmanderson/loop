class Board:
    def __init__(self, width, height, numbers):
        self.width = width
        self.height = height
        self.numbers = numbers
        self.lines = {}

    def mark_line(self, value, first_coord, second_coord):
        if first_coord not in self.lines:
            self.lines[first_coord] = {}
        self.lines[first_coord][second_coord] = value

    def get_number(self,x,y):
        index = str(x) + ',' + str(y)
        if index in self.numbers:
            return str(self.numbers[index])
        return ' '

    def print(self):
        for y in range(self.height):
            top = ''
            middle = ''
            bottom = ''
            for x in range(self.width):
                top += '*' + self._get_top_line(x,y)
                middle += self._get_left_line(x,y) + ' ' + self.get_number(x,y) + ' ' 
                if y == self.height - 1:
                    bottom += '*' + self._get_bottom_line(x, y)
                if x == self.width - 1:
                    top += '*'
                    middle += self._get_right_line(x,y)
                    bottom += '*'
            print(top)
            print(middle)
        print(bottom)

    def _get_top_line(self, x, y):
        return self._get_line(self._get_coord_str(x, y-1), self._get_coord_str(x, y))

    def _get_left_line(self, x, y):
        return self._get_line(self._get_coord_str(x-1, y), self._get_coord_str(x, y))

    def _get_right_line(self, x, y):
        return self._get_line(self._get_coord_str(x, y), self._get_coord_str(x+1, y))

    def _get_bottom_line(self, x, y):
        return self._get_line(self._get_coord_str(x, y), self._get_coord_str(x, y+1))

    def _get_coord_str(self, x, y):
        return str(x) + ',' + str(y)

    def _get_coord(self, str_coord):
        return str_coord.split(',')

    def get_adjacent_squares(self, x, y):
        adjacents = []
        x = int(x)
        y = int(y)
        if x > 0:
            adjacents.append([x-1,y])
        if y > 0:
            adjacents.append([x, y-1])
        if x < self.width - 1:
            adjacents.append([x+1, y])
        if y < self.height - 1:
            adjacents.append([x, y+1])
        return adjacents

    def _get_line(self, first_coord, second_coord):
        vertical = self._is_vertical(first_coord, second_coord)
        if first_coord not in self.lines or second_coord not in self.lines[first_coord]:
            if vertical:
                return " "
            return "   "
        if self.lines[first_coord][second_coord]:
            if vertical:
                return "|"
            return "---"
        if vertical:
            return "x"
        return " x "

    def _is_vertical(self, first_coord, second_coord):
        first = first_coord.split(',')
        second = second_coord.split(',')
        return first[0] != second[0]
        
