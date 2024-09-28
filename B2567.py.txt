# [1] 입력처리
N = int(input())

# arr 선언 : 상하좌우 1씩 패딩 있는 100크기 매트릭스
arr = [[0]*102 for _ in range(102)]

# N개 입력받아서 색종이 체크하기
for _ in range(N):
    sj,si = map(int,input().split())

    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

# [2-1] 행단위 처리하면서 값이 바뀌면 - 경계
result = 0
for list in arr:
    # 다음거랑 비교해야되니까 0~100까지 인덱스 처리
    for i in range(0,101):
        if list[i] != list[i+1]:
            result += 1



# [2-2]  di/dj 인접한 네방향 처리로 계산
result = 0

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 어떤 칸에서 상하좌우에 0이 있는 개수가 둘레의 개수이다
for i in range (1,101):
    for j in range(1,101):
        if arr[i][j] == 1 : # 색종이인 경우
            for k in range(4):
                ni,nj = i+di[k], j+dj[k]
                if arr[ni][nj] == 0 : result += 1


# [3] 결과값 출력
print(result)