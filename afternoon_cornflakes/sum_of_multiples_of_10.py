sum_of_multiples = 0
for count in range(1, 20_001,):
    if count % 10 == 0:
        sum_of_multiples += count
print("sum of multiples of 10: ", sum_of_multiples)

