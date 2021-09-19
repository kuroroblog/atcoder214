# 標準入力を受け付ける。
S, T = (int(x) for x in input().split())

# 組み合わせの数を格納する。
count = 0
# <方針>
# aの値を総当たりして、a + b + c <= Sの条件に当てはまるb, cの値の幅を決める。(b : S - a), (c : S - a - b)
for a in range(0, S + 1):
    for b in range(0, S - a + 1):
        for c in range(0, S - a - b + 1):
            # a, b, cに当てはまる値は、a + b + c <= Sに該当する値のみなので、a * b * c <= Tをcountすればいい。
            if a * b * c <= T:
                count = count + 1
print(count)
