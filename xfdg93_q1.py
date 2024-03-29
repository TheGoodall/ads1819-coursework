

def hash_quadratic(data_input):
    table = ["-"]*19
    for data in data_input:
        if data in table:
            continue
        i = ((6*data) + 3) % 19
        io = i
        count = 0
        found_space = True
        while table[i] != "-":
            i = (io + count**2) % 19
            count += 1
            if count == 100:
                found_space = False
                break
        if found_space:
            table[i] = data
    return table


def hash_double(data_input):
    table = ["-"]*19
    for data in data_input:
        if data in table:
            continue
        i = ((6*data) + 3) % 19
        io = i
        count = 1
        diff  = 11-(data%11)
        found_space = True
        while table[i] != "-":
            i=(io+(diff*count))%19
            count += 1
            if count == 100:
                found_space = False
                break
        if found_space:
            table[i] = data
    return table


def test_hq():
    assert hash_quadratic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_quadratic([19,38,57,76,95,114,133,152,171,190]) == [95, 133, '-', 19, 38, '-', '-', 57, 190, 114, 171, '-', 76, '-', 152, '-', '-', '-', '-']
    assert hash_quadratic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 71, 3, 19, 43, 13, 29, 7, 23, 61, 17, 41, 11, 59, 5, 2, 37, 53, 31]
    print ("all tests passed")


def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == [304, 361, 266, 19, 76, 152, 228, 95, 171, 38, 114, 190, 57, 133, 209, 247, 285, 323, 342]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 67, 3, 19, 53, 13, 29, 7, 23, 59, 17, 41, 11, 61, 5, 2, 37, 43, 31]
    print ("all tests passed")


test_hq()
test_dh()


