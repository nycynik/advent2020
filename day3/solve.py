# day 3

def check_forest(x_offset, y_offset, forest):
    tree_count = 0

    forest_height = len(forest)
    forest_width = len(forest[0]) - 1

    x = 0
    y = 0
    while x < forest_height - 1:
        # move
        y += y_offset
        y_wrap = y % forest_width
        x += x_offset

        # count trees
        if forest[x][y_wrap] == tree:
            tree_count += 1
            print(f"Tree!{' ' * y_wrap}x\n     {forest[x]}")
        else:
            print(f"space{' ' * y_wrap}o\n     {forest[x]}")

    return tree_count


tree = '#'
empty = '.'

data_file = open("data.txt")

tree_count = 1

forest = []
for val in data_file:
    forest.append(val)
data_file.close()

to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for check in to_check:
    tree_count *= check_forest(check[1], check[0], forest)


print(f"encountered {tree_count} trees.")
