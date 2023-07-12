# 3) 트리 구조 탐색
# 1. 너비 우선 탐색 구현하기

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]
data = [0]

while len(data) > 0:
    pos = data.pop(0) # 맨 앞에서 꺼내기
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i) # 끝에 추가