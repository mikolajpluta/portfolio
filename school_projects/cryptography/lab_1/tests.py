import re
from collections import OrderedDict 

def group_list(lst):
    res = [(el, lst.count(el)) for el in lst]
    return list(OrderedDict(res).items())

def split_string_into_chunks(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def group_long_series(list):
    result = []
    longer_than_six = ['6+', 0]
    for serie in list:
        if len(serie[0]) < 6:
            result.append( (len(serie[0]), serie[1]) )
        else:
            longer_than_six[1] += serie[1]
    result.append(longer_than_six)
    return result


############################################ tests ########################################
def single_bit_test(data):
    z = 0
    o = 0
    for bit in data:
        if bit == '1':
            o += 1
        if bit == '0':
            z += 1

    if o > 9725 and o < 10275 and z > 9725 and z < 10275:
        return "single bit test PASSED"
    else:
        return "single bit test NOT passed"
    
def long_serie_test(data):
    result = re.findall("1{26,}", data)
    if len(result) > 0:
        return "long serie test NOT passed"
    result = re.findall("0{26,}", data)
    if len(result) > 0:
        return "long serie test NOT passed"
    
    return "long serie test PASSED"


def series_test(data):
    values = {
        1: (2315, 2685),
        2: (1114, 1386),
        3: (527, 723),
        4: (240, 384),
        5: (103, 209),
        '6+': (103, 209)
    }

    zeros = re.findall("0+", data)
    zeros = group_list(zeros)
    zeros = group_long_series(zeros)

    ones = re.findall("1+", data)
    ones = group_list(ones)
    ones = group_long_series(ones)

    for serie in zeros:
        if not values[serie[0]][0] < serie[1] < values[serie[0]][1]:
            return "seriest test NOT passed"

    for serie in ones:
        if not values[serie[0]][0] < serie[1] < values[serie[0]][1]:
            return "seriest test NOT passed"

    return "series test PASSED"

def poker_test(data):
    chunks = split_string_into_chunks(data, 4)
    grouped = group_list(chunks)
    sum = 0
    for i in grouped:
        sum += pow(i[1], 2)
    x = ((16 / 5000) * sum) - 5000
    if 2.16 < x < 46.17:
        return "poker test PASSED"
    else:
        return "poker test NOT passed"





