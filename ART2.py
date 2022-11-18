import sys

def main():
    # 총 패턴 개수 입력 받기
    print("-----------"*4)
    print("총 몇 개의 패턴을 입력 받을 것인가요?")
    print("입력 예시: 10")
    print("-----------"*4)
    numPattern = int(sys.stdin.readline())
    if numPattern <= 0:
        exit()
    # 패턴 값 입력 받기 
    print("-----------"*4)
    print("패턴을 입력하시오")
    print("입력예시:")
    print("1.0 0.1")
    print("1.3 0.8")
    print("1.4 1.8")
    print("1.5 0.5")
    print("0.0 1.4")
    print("0.6 1.2")
    print("1.5 1.9")
    print("0.7 0.4")
    print("1.9 1.4")
    print("1.5 1.3")
    print("-----------"*4)
    # 패턴들을 담을 배열
    pattern = []
    # 입력 값들을 배열에 넣기
    for i in range(numPattern):
        pattern.append(list(map(float,sys.stdin.readline().split(" "))))
    
    # 임계값 입력 받기 
    print("-----------"*4)
    print("경계가 되는 기준값은 얼마로 잡을 것인가요?")
    print("입력 예시: 1.5")
    print("-----------"*4)
    threshold = float(sys.stdin.readline())
    
    art2 = ART2()
    art2.setData(pattern, threshold)
    art2.train()
    art2.report()

class ART2:
    def __init__(self):
        self._pattern = []
        self._threshold = 0
        self._dimension = len(self._pattern)
        self._weight = []
        self._numWeight = []

    def setData(self, pattern, threshold):
        self._pattern = pattern
        self._threshold = threshold
        self._dimension = len(pattern[0])
        self._weight.append(pattern[0])
        self._numWeight.append(1)
        
    def minDistanceWinner(self, index):
        pattern = self._pattern
        weight = self._weight
        dimension = self._dimension

        distance = float("inf") 
        cluster = 0 # minimum 클러스터 인덱스
        for j in range(len(weight)):
            newDistance = 0
            for k in range(dimension):
                newDistance += abs(pattern[index][k]- weight[j][k])
            # 더 작은 게 나오면 클러스터는 작은 걸 선택하도록
            if newDistance < distance:
                cluster = j
            distance = min(distance, newDistance)
        
        return cluster
    
    def vigilanceTest(self, cluster, index):
        pattern = self._pattern
        threshold = self._threshold
        dimension = self._dimension
        weight = self._weight
        
        newValue = pattern[index]
        vigilance = 0
        
        for k in range(dimension):
            vigilance += abs(weight[cluster][k]-newValue[k])
        
        if vigilance >= threshold : 
            # 새 클러스터 및 가중치 생성
            self._weight.append(newValue)
            self._numWeight.append(1)
        else:
            # 현재 클러스터 가중치 수정
            self._numWeight[cluster] += 1
            for k in range(0,dimension):
                self._weight[cluster][k] = (self._weight[cluster][k]*(self._numWeight[cluster]-1)+newValue[k])/self._numWeight[cluster]
                self._weight[cluster][k] = round(self._weight[cluster][k],2)
    
    def train(self):
        for i in range(1, len(self._pattern)):
            cluster = self.minDistanceWinner(i)
            self.vigilanceTest(cluster,i)
    
    def report(self):  
        
        print("각 클러스터의 최종가중치는?")

        index = 1
        for w in self._weight:
            print("Cluster",index,"=",w)
            index+=1



main()