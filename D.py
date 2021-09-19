import sys

# 再起の上限を設定するために利用する。
# 参考 : https://note.nkmk.me/python-sys-recursionlimit/
sys.setrecursionlimit(10**6)

# 標準入力を受け付ける。
n = int(input())

edges = []
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    # 配列のインデックスが0から始めることを加味して、-1する。
    # インデックスとは? : https://wa3.i-3-i.info/word11906.html
    u -= 1
    v -= 1
    edges.append((w, u, v))

# 重みの小さい順に並べる。
# 「現在参照する重みの最大値 x 現在参照する重みの最大値が、最大値になる通りの数」を実現するため。
edges.sort()

# 親のインデックスを探索する関数
# 親のインデックスを見つけるまで再起処理を行う。
# 親のインデックスが見つかったら、再起が終了するまで、同じ値(親のインデックス値)を保持させ続ける。
def root(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]

# 頂点を繋ぎ合わせる処理。
# 親を洗い出して、子と繋ぎ合わせる。
def unite(x, y):
    x = root(x)
    y = root(y)
    parent[x] += parent[y]
    parent[y] = x

# 頂点に該当する親の値を返す。
def size(x):
    x = root(x)
    return -parent[x]

# 各頂点の親情報を格納する。親は-1とする。
parent = [-1] * n
# 答えを格納する変数
ans = 0

for w, u, v in edges:
    ans += w * size(u) * size(v)
    unite(u, v)

print(ans)
