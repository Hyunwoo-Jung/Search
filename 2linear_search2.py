# 리스트의 위치를 반환하는 함수

def linear_search(data, value): # 리스트에서 찾을 값의 위치를 검색하는 함수 정의
    for i in range(len(data)):
        if data[i] == value: # 원하는 값을 찾은 경우
            return i
    return -1 # 원하는 값이 없으면 -1을 반환
        
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

print(linear_search(data, 40))
