    # 3. 중위 순회 구현

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], 
        [], [], [], [], [], [], [], []]

def search(pos):
    if len(tree[pos]) == 2: # 자식 노드가 2개 있을 때
        search(tree[pos][0])
        print(pos, end=' ') # 왼쪽 노드와 오른쪽 노드 사이에 출력
        search(tree[pos][1])
    elif len(tree[pos]) == 1: # 자식 노드가 하나일 때
        search(tree[pos][0])
        print(pos, end=' ') # 왼쪽 노드를 조사한 후 출력
    else: # 자식 노드가 없을 때
        print(pos, end=' ') # 현재 노드 출력
search(0)