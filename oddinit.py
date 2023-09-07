def find_it(seq):
    count = {}
    for num in seq:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, occurrence in count.items():
         if occurrence % 2 != 0:
            return num
         
seq = [1, 2, 3, 2, 1, 3, 4]
odd_occurrence = find_it(seq)
print(odd_occurrence)  # Output: 4
