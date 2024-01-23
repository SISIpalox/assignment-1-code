def number_bracelet(n, start1, start2):
    bracelet = [start1, start2]
    for i in range(2, n):
        next_number = (bracelet[i-1] + bracelet[i-2]) % 10
        bracelet.append(next_number)
    return bracelet

# make a long bracelet starting with 1 and 5
print(number_bracelet(100, 1, 5))
def repeating_series(series):
    for i in range(1, len(series)):
        if series[:i] == series[i:2*i]:
            return series[:i]
    return series
# make a long bracelet starting with 1 and 5
long_bracelet = number_bracelet(1000, 1, 5)

# Find the repeating bracelet
repeating_bracelet = repeating_series(long_bracelet)
print("Repeating unit:", repeating_bracelet)
