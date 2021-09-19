# 標準入力を受け付ける。
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# 最初に高橋くんからすぬけくんへ宝石を渡した最小時間を見つける。宝石の授受がここから始まる。
minIdx = 0
for i in range(0, N):
    if T[i] <= T[minIdx]:
        minIdx = i

# 最小時間を格納しておく。
currentTime = T[minIdx]
# 答えリスト。
ans = [0] * N

for i in range(0, N):
    # 現在時間 + すぬけくんから隣のすぬけくんへ宝石を渡す時間 = 始めて宝石をもらう時間にすべきか、それとも高橋くんから直接宝石をもらう時間 = 始めて宝石をもらう時間にすべきか、最小時間で高橋くんから直接宝石をもらった、すぬけくんのところから検証を始める。
    # % N : minIdxが0から始まるとは限らない。1周して1番目のすぬけくんに戻ることを加味する。
    nowIdx = (minIdx + i) % N

    # 宝石をすぬけくんからもらった時間にすべきか、それとも高橋くんからもらった時間にすべきか判定する。
    currentTime = min(currentTime, T[nowIdx])

    # i番目の時間を記録しておく。
    ans[nowIdx] = currentTime

    # すぬけくんから宝石をもらった場合の時刻を記録しておく。
    currentTime += S[nowIdx]

# 答え出力
print(*ans)
