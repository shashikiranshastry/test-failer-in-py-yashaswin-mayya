
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

#Assumption is size() requires t-shirt "length" along with "shoulder-measurements"

#Referencefor Test Case:
# Shoulder      Length          Size
#   <38           <72            S
# 38 to 42      72 to 75         M
#   <42           >75            L

assert(size(37, 71) == 'S')
assert(size(40, 74) == 'M')
assert(size(43, 76) == 'L')
print("All is well (maybe!)\n")
