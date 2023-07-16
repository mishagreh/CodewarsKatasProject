from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/60576b180aef19001bce494d


def count_checkerboard(width, height, resolution):
    """ returns the total count of all individual black squares """

    rem1 = width % (2 * resolution)
    floor1 = width // (2 * resolution)

    row1 = floor1 * resolution + (rem1 - resolution) * (rem1 > resolution)
    row2 = floor1 * resolution + rem1 * (rem1 < resolution) + resolution * (rem1 >= resolution)

    rem2 = height % (2 * resolution)
    floor2 = height // (2 * resolution)

    blacks = resolution * (row1 + row2) * floor2 + rem2 * row1 * (rem2 <= resolution) + (
            row1 * resolution + (rem2 - resolution) * row2) * (rem2 > resolution)

    return blacks


width, height, resolution = 11, 6, 5
qq(count_checkerboard(width, height, resolution))

end = timer()
print(end - start)
