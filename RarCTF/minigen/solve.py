exec("def f(x):" + "yield((x:=-~x)*x+-~-x)%727;" * 100)
# fmt: off
ar = [281, 547, 54, 380, 392, 98, 158, 440, 724, 218, 406, 672, 193, 457, 694, 208, 455, 745, 196, 450, 724]
# fmt: on

for i in range(727):
    g = f(i)
    s = "".join(map(lambda c: chr(c ^ next(g)), ar))
    if "rarctf" in s:
        print(s)