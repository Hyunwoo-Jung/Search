# 리스트에서 원하는 값 '40' 찾기

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
found = False # 처리 상황을 관리(초기값은 False)

for i in range(len(data)):
    if data[i] == 40: # 찾는 값과 일치하는지
        print(i)
        found = True # 찾았음을 처리 상황에 설명
        break

if not found:
    print('Not Found')