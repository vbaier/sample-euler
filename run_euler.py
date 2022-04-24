import time

def base_10_to_b(value_10, radix):
    value_b = []
    while value_10 > 0:
        value_b.append(value_10 % radix)
        value_10 //= radix
    value_b.reverse()
    return value_b


def base_b_to_10(src_value, radix):
    value_b = src_value.copy()
    value_b.reverse()
    weight_b = 1
    value_10 = 0
    for numeral_b in value_b:
        value_10 += numeral_b * weight_b
        weight_b *= radix
    return value_10

def build_superpans(radix):
    values = [1,0]
    for i in range(2,radix):
        values.append(i)

    superpan_list = []
    recurse_superpan([],values, superpan_list, radix)

    return superpan_list

def recurse_superpan(set, surviving, superpan_list, radix):
    if len(superpan_list) > 9:
        return

    if not surviving:
        #print(set)
        if(check_superpandigital(set, radix)):
            superpan_list.append(set)
            print(set)

        return

    for i in surviving:
        new_set = set.copy()
        new_surviving = surviving.copy()
        new_set.append(i)
        new_surviving.remove(i)

        if(new_set[0] == 0):
            continue

        recurse_superpan(new_set, new_surviving, superpan_list, radix)

def check_pandigital(test_value, test_radix):

    working_list = test_value.copy()

    search_list = list(range(0, test_radix))

    for position_value in working_list:
        if position_value in search_list:
            search_list.remove(position_value)

        if(not search_list):
            return True

    return False

def check_superpandigital(test_value, src_radix):

    decimal_value = base_b_to_10(test_value, src_radix)

    for radix in range (src_radix, 2, -1):
        next_check = base_10_to_b(decimal_value, radix)
        is_pan = check_pandigital(next_check, radix)

        if(not is_pan):
            return False

    return True;

class VaribaseNumber:
    def __init__(self, base, num_array):
        self.base = base
        self.num_array = num_array
        #self.representations[base] = num_array

    def __allBases(self):
        self

start_time = time.time()

superpan_list = build_superpans(10)
print(superpan_list)


accum = 0

for value in superpan_list:
    accum += base_b_to_10(value, 10)

print("\n")
print(accum)
print("time")
print(time.time() - start_time)
print("\n")

start_time = time.time()

superpan_list = build_superpans(12)
print(superpan_list)

accum = 0

for value in superpan_list:
    accum += base_b_to_10(value, 12)

print("\n")
print(accum)
print("time")
print(time.time() - start_time)
print("\n")