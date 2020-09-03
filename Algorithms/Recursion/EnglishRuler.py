def draw_line(tick_length, tick_label = ''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(tick_lengh):
    if tick_lengh:
        draw_interval(tick_lengh-1)
        draw_line(tick_lengh)
        draw_interval(tick_lengh-1)


def draw_ruler(num_inches, major_lengh):
    draw_line(major_lengh, '0')
    for i in range(1, num_inches):
        draw_interval(major_lengh -1)
        draw_line(major_lengh, str(i))


def test():
    draw_ruler(3,5)


if __name__ == '__main__':
    test()