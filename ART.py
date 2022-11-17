import sys

print("총 몇 개의 패턴을 입력 받을 것인가요?")
# 총 패턴 개수
numPattern = int(sys.stdin.readline())
# 패턴들을 담을 배열
pattern = []
# 입력 값들을 배열에 넣기
for i in range(numPattern):
    pattern.append(list(map(float,sys.stdin.readline().split(" "))))
# 입력 값의 차원 
dimension = len(pattern[0])

print("경계가 되는 기준값은 얼마로 잡을 것인가요?")
# 임계값
threshold = float(sys.stdin.readline())

###########
# 학습 시키기
###########

# 클러스터의 가중치를 담을 배열
weight = []
# 클러스터에 몇개의 패턴이 들었는지 담을 배열
numWeight = []
# 첫 클러스터에는 첫 패턴 값을 넣음.
weight.append(pattern[0])
numWeight.append(1)

# 학습
for i in range(1, numPattern):
    # minimum distance 구하기
    distance = float("inf") 
    # minimum 클러스터 인덱스
    cluster = 0
    for j in range(len(weight)):
        newDistance = 0
        for k in range(dimension):
            newDistance += abs(pattern[i][k]- weight[j][k])
        # 더 작은 게 나오면 클러스터는 작은 걸 선택하도록
        if newDistance < distance:
            cluster = j
        distance = min(distance, newDistance)
    
    # vigilance test 하기
    newValue = pattern[i]
    vigilance = 0
    for k in range(dimension):
        vigilance += abs(weight[cluster][k]-newValue[k])
    if vigilance >= threshold : 
        # 새 클러스터 및 가중치 생성
        weight.append(newValue)
        numWeight.append(1)
    else:
        # 현재 클러스터 가중치 수정
        numWeight[cluster] += 1
        for k in range(0,dimension):
            weight[cluster][k] = (weight[cluster][k]*(numWeight[cluster]-1)+newValue[k])/numWeight[cluster]
            weight[cluster][k] = round(weight[cluster][k],2)

print("각 클러스터의 최종가중치는?")

index = 1
for w in weight:
    print("Cluster",index,"=",w)
    index+=1


