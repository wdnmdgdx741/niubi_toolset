# with open("misc2-weight.zip" , "rb+") as f:
#     wen = f.read()
#     def strReverse(strDemo):
#         return strDemo[::-1]
#     k = strReverse(wen)
#     f.write(k)
#     f.close()

r = open("misc2-weight.zip", "rb+")
r2 = open("dome.zip", "rb+")
wen = r.read()
def strReverse(strDemo):
    return strDemo[::-1]
k = strReverse(wen)
r2.write(k)
r2.close()
