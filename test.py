# 1 ~ 50 중 짝수를 구하는 함수
def is_even():
    even_list = []
    for num in range(1, 51):
        if num % 2 == 0:
            even_list.append(num)
    return even_list