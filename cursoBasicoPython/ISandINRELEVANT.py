seq = [78, 117, 110, 99, 104, 117, 107, 115]
seq1 = seq
elem = 8


def check(seq, elem):
    print(seq is seq1)
    return True if elem in seq else False
