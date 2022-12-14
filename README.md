# Artificial_Neural_Network
> **인공신경망을 학습하고, 이를 파이썬 코드로 구현해 본다.**

👉🏻 [인공신경망 내용 정리한 블로그](https://velog.io/@diduya/series/Intelligent-System)

### 🦋 [BAM](https://github.com/YeoJiSu/Artificial_Neural_Network/blob/main/BAM.py) 알고리즘
1. 가중치 행렬을 초기화한다.<br>
입력 벡터를 X, Y 층에 동시에 입력한다.<br>
비활성화 상태를 -1로, 활성화 상태를 +1로 사용한다. (바이폴라 적용)

2. net 식 (x*w 들의 합) 을 사용하여 다른 층에 입력 패턴을 전파한다.

3. 활성화 함수 식을 사용하여 목적지 층에서 새로운 활성 패턴(activation pattern)을 계산한다.

4. net 식을 사용하여 새로운 활성 패턴을 다시 출발 층으로 전파한다.

5. 활성화 함수 식을 사용하여 처음 층의 활성값을 수정한다.

6. 양쪽 층에서 활성 패턴이 변화를 멈출 때까지 2-5 과정을 반복한다.


### 🦋 [ART2](https://github.com/YeoJiSu/Artificial_Neural_Network/blob/main/ART2.py) 알고리즘

1. 클러스터(승자) 선택 
새로운 학습 패턴이 주어지면 **minimum distance**를 승자(클러스터)로 선택한다.<br>

2. 클러스터 in/out 여부 확인 
최소한의 한계값(클러스터의 반경) 내에 들어오는지 확인하는 **Vigilance test**를 거친다.<br>

3. 클러스터 가중치(W) 수정 or 생성<br>
    
    * ✔️ 가중치 수정<br>
만약 승자가 vigilance test를 통과하면, "기존값 + 새로 들어온 값" 의 평균으로 승자의 가중치를 수정한다.<br>

    * ✔️ 가중치 생성 (새 클러스터 생성)<br>
만약 승자가 vigilance test를 실패하면, 해당 승자는 자신의 가중치를 가지고 새로운 클러스터를 생성한다.<br>


