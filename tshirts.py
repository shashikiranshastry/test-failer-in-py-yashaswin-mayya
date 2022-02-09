
def size(cms):
    if cms <= 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

#Function to encapsulate assertions

def size_check(length_in_cm, size):
    assert(size(length_in_cm) == size)

size_check(size(37) == 'S')
size_check(size(40) == 'M')
size_check(size(43) == 'L')
size_check(size(38) == 'S')
print("All is well (maybe!)\n")
