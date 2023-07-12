    # 4. 후위 순위의 반대순서로 탐색

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]
data = [0]

while len(data) > 0:
    pos = data.pop() # 다음 노드 위치를 리스트 끝에서 꺼내기
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i) # 리스트 끝에 탐색할 위치 추가하기