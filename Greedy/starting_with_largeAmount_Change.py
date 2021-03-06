"""
거스름돈 _ 가장 큰 화폐단위부터
500원 100원 50원 10원 동전 무한히 존재
<거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구해라>
단, 거슬러 줘야 할 돈 N은 항상 10배수
"""

# 1260원을 거슬러줘야 함
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin      # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin

print(count)

#500,500,100,100,50,10 => output : 6
# 시간 복잡도 : O(K)     // 화폐 종류 : K개