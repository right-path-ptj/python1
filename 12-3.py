import threading

# 합을 계산하는 함수
def calc_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(f"1+2+...+{n} = {total}")

# 스레드 생성
th1 = threading.Thread(target=calc_sum, args=(1000,))
th2 = threading.Thread(target=calc_sum, args=(100000,))
th3 = threading.Thread(target=calc_sum, args=(10000000,))

# 스레드 시작
th1.start()
th2.start()
th3.start()

# 모든 스레드가 끝날 때까지 대기
th1.join()
th2.join()
th3.join()