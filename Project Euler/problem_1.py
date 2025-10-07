def find_multiples(limit):
    return [x for x in range(limit) if x % 3 == 0 or x % 5 == 0]
print(sum(find_multiples(1000)))