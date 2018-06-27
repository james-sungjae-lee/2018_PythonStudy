def solution(n, m):
    # 큰 수를 n으로, 작은 수를 m으로 설정한다.
    if m > n:
        (n, m) = (m, n)
    # 최소공배수를 구하기 위한 m * n 을 mn 으로 정의한다.
    mn = m * n
    # 유클리드 호제법을 이용하여 최대공약수를 구한다.
    while m is not 0:
        (n, m) = (m, n % m)
    # 최대공약수는 n, 최소공배수는 mn을 n으로 나눈 몫이 된다.
    gcd = n
    lcm = int(mn / n)
    return [gcd, lcm]
