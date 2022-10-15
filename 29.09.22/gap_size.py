L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
len_L = len(L)
gaps = [L[i] - L[i - 1] for i in range(1, len_L)]
print('Gaps: ', gaps)
max_gap = max(gaps)
print('Maximum gap size: ', max_gap)
percentage_of_gaps2 = (gaps.count(2) / len(gaps)) * 100
print(f'Percentae of gaps that hve size 2: {percentage_of_gaps2}')
