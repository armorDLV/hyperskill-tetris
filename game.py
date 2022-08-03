from grid import Grid

if __name__ == '__main__':

    size_x, size_y = map(int, input().split())
    grid = Grid(size_x, size_y)
    grid.print()

    while True:

        action = input()

        if action == 'piece' and not grid.piece:
            piece = input()
            grid.add_piece(piece)
            grid.print()
        elif action == 'break':
            grid.break_rows()
            grid.print()
        elif action == 'exit':
            break
        else:
            grid.command(action)
            grid.print()

        if grid.is_game_over():
            print('Game Over!')
            break
