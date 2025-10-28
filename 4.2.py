def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end="")
        print()
def draw_right_triangle(rows, ch):
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()
