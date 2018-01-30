def print_stars(stars, diagonal):
    spaces_counter = diagonal // 2 - stars
    stars_counter = diagonal % 2 + 2 * stars
    print(' ' * spaces_counter, '*' * stars_counter)


def draw_rhombus():
    diagonal = 11
    stars = 0

    while stars < diagonal // 2:
        print_stars(stars, diagonal)
        stars += 1
    while stars >= 0:
        print_stars(stars, diagonal)
        stars -= 1


draw_rhombus()
