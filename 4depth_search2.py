    # 2. 후위 순위 구현

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]

def search(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ') # 자식 노드를 탐색한 후 출력

search(0)