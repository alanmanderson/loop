from board import Board
from ai import AI

b = Board(5,5,{"1,1":3, '2,1':3})
#b.mark_line(True, '1,0', '1,1')
#b.mark_line(True, '0,1', '1,1')
#b.mark_line(True, '1,1', '2,1')
#b.mark_line(True, '1,1', '1,2')
#b.mark_line(False, '-1,0', '0,0')
#b.mark_line(False, '4,-1', '4,0')
#b.mark_line(False, '4,4', '5,4')
#b.mark_line(False, '4,4', '4,5')
b.print()

a = AI(b)

a.reduce()

