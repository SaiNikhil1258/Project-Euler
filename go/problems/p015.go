/* Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a given gridSize? */

package problems

func Lattice_paths() uint64 {
	size := 20
	grid := make([][]uint64, size+1)
	for i := 0; i < size+1; i++ {
		grid[i] = make([]uint64, size+1)
	}
	for i := 0; i < size; i++ {
		grid[size][i] = 1
		grid[i][size] = 1
	}
	grid[size][size] = 0
	for x := size - 1; x >= 0; x-- {
		for y := size - 1; y >= 0; y-- {
			grid[x][y] = grid[x+1][y] + grid[x][y+1]
		}
	}
	return grid[0][0]
}
