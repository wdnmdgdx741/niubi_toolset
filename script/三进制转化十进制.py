num = 10201
def test(n):
    res = 0
    for index, value  in enumerate(str(n)[::-1]):
        res += int(value) * 3**index
    return res
print(test(num))