# 데이터가 오름차순으로 정리되어 있을 때 찾는 위치를 절반으로 좁히면서 순서대로 검색

def binary_search(data, value):
    left = 0 # 검색 영역의 왼쪽 끝을 설정
    right = len(data) - 1 # 검색 영역의 오른쪽 끝을 설정
    while left <= right:
        mid = (left + right) // 2 # 검색 범위의 중앙을 계산
        if data[mid] == value:
            # 중앙값과 일치하면 위치를 반환
            return mid
        elif data[mid] < value:
            # 중앙값보다 크면 검색 범위의 왼쪽을 바꿈
            left = mid + 1
        else:
            # 중앙값보다 작으면 검색 범위의 오른쪽을 바꿈
            right = mid - 1
    return -1 # 발견되지 않을 경우

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data,90))

# left와 right 두 변수로 범위를 좁히고 있다.
# 일치하면 해당 위치 반환, 일치하지 않으면 left와 right값을 다시 설정