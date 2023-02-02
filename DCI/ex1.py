def get_total(lst):
    index = 0
    total = 0
    while index < len(lst):
        total += lst[index]
        index += 1

    print(total)

    return total

print(get_total([1,2,3]))