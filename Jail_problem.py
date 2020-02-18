# For 100 cells and 100 guards, if each guard in turn (starting with 1) changes the state
# of a cell that is divisible by his number, which cells are open at the end?


# Create cells in locked state
cell = [False]
cells = cell * 100

# For each guard, check each cell
for g in range(1,101):
	cell_count = 0
	for c in cells:
		cell_count = cell_count +1
		#print(cell_count)

		# If cell num mod guard num is zero, flip state
		if cell_count % g == 0:
			# print('cell ' + str(cell_count) + ' to ' + str(not c))
			cells[cell_count-1] = not c

# check which are open
cell_count = 0
open_cells = []
for c in cells:
	cell_count = cell_count +1
	if c:
		open_cells.append(cell_count)

print(open_cells)
		
		
	
