# 헤더
for i in range(2, 10):
    print(f"#  {i}단  #", end="\t")
print()

# 구구단 출력
for i in range(1, 10):
    for k in range(2, 10):
        print(f"{k}X {i:>2}= {k*i:>2}", end="\t")
    print()
