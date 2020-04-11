import math
import numpy as np
# problem1
# sum = 0
# for i in range(1000):
#   if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
#     sum += i
# print(sum)

# problem2

# a = 1
# b = 0
# sum = a
# while a < 4000000:
#   a, b = a + b, a
#   if a % 2 == 0:
#     sum += a
#   print(a)
# print(sum)
# def get_sieve_of_eratosthenes(n):
#     if not isinstance(n, int):
#         raise TypeError("n is int-type.")
#     if n < 2:
#         raise ValueError("n is more than 2")
#     data = [i for i in range(2, n + 1)]
#     for d in data:
#         data = [x for x in data if (x == d or x % d != 0)]
#     return data

# nums = get_sieve_of_eratosthenes(600851475143)

# def select_max_prime_number(nums, obj):
#   maxVal = 0
#   for num in nums:
#     if obj % num == 0 and num > maxVal:
#       maxVal = num
#   return maxVal

# ans = select_max_prime_number(nums, 600851475143)

# problem3
# #試し割法
# def trial_division(n):
#     #素因数を格納するリスト
#     factor = []
#     maxVal = 0
#     #2から√n以下の数字で割っていく
#     tmp = int(math.sqrt(n)) + 1
#     for num in range(2,tmp):
#         while n % num == 0:
#             n //= num
#             factor.append(num)
#             if num > maxVal:
#               maxVal = num
#     #リストが空ならそれは素数
#     if not factor:
#         return 'prime number'
#     else:
#         factor.append(n)
#         return maxVal

# problem4


# def palindromes():
#     max = 0
#     num1 = 0
#     num2 = 0
#     for i in range(100, 1000):
#         for j in range(100, 1000):
#             tmp = i * j
#             tmp1 = str(tmp)
#             tmp2 = tmp1[::-1]
#             if tmp1 == tmp2:
#                 if tmp > max:
#                     max = tmp
#                     num1 = i
#                     num2 = j
#     print("Answer:"+str(max)+"num1:" + str(num1)+"num2:"+str(num2))

# problem5
# def no_remainder():
#     num = 230000000
#     232792560
#     ans = 0
#     while ans == 0:
#         num += 1
#         print(num)
#         for i in range(1, 21):
#             if num % i != 0:
#                 break
#             # elif num % i != 20:
#             #     print(i)
#             elif i == 20:
#                 ans = num
#                 print(ans)

# problem6
# def square_dif():
#     num1 = 0
#     num2 = 0
#     for i in range(1, 101):
#         num1 += i
#         num2 += i * i
#         tmp = num1 * num1
#     print(tmp-num2)

# problem7
# def prime_num(n):
#     primes = [2]
#     i = 3
#     while len(primes) < 10001:
#         for p in primes:
#             if i % p == 0:
#                 break
#             else:
#                 primes.append(i)
#             i += 2
#     print(primes)

# problem8
# def max_num():
#     max = 0
#     digits = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#     for t in range(len(digits)-13):
#         num = 1
#         for i in range(13):
#             num *= int(digits[t+i])
#             if num > max:
#                 max = num
#     print(max)

# problem9
# n = 1000

# seq = range(1, n+1)


# def is_pythagorean(a, b, c):
#     return a**2 + b**2 == c**2


# pythagorean = None
# for a in seq:
#     if(pythagorean):
#         break
#     for b in range(a+1, n+1):
#         c = n - b - a
#         if(c > b and is_pythagorean(a, b, c)):
#             pythagorean = (a, b, c)
#             break

# print(pythagorean)

# problem10
# def summarize_prime():
#     primes = [2]
#     i = 3
#     while primes[-1] < 2000000:
#         for p in primes:
#             if i % p == 0:
#                 break
#             else:
#                 primes.append(i)
#         i += 2
#         print(i)
#     total = sum(primes)
#     print(total)

# problem11
# def max_digit():
#     src = '''
#     08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
#     49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
#     81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
#     52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
#     22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
#     24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
#     32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
#     67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
#     24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
#     21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
#     78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
#     16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
#     86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
#     19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
#     04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
#     88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
#     04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
#     20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
#     20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
#     01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#   '''

#     ROW = 20
#     COLUMN = 20
#     DIMENSION = 4
#     greatest_product = 0

#     src = src.replace('\n', '').split(' ')
#     src = filter(lambda i: i != '', src)
#     src = np.array(src).reshape(ROW, COLUMN)
#     src = np.append(src, np.zeros((DIMENSION - 1, COLUMN)), axis=0)

#     for i in range(0, ROW - DIMENSION + 1):
#         for j in range(0, COLUMN - DIMENSION + 1):
#             dest = src[i:i + DIMENSION, j:j + DIMENSION]
#             h_product = reduce(lambda x, y: int(x) * int(y), dest[0])
#             v_product = reduce(lambda x, y: int(x) * int(y), dest.T[0])
#             d_product = reduce(lambda x, y: int(x) * int(y), np.diag(dest))
#             rd_product = reduce(lambda x, y: int(
#                 x) * int(y), np.diag(dest[::, ::-1]))

#             greatest_product = max(
#                 [h_product, v_product, d_product, rd_product, greatest_product])

#     print('greatest product is %d' % greatest_product)

# problem12


def count_divisors(src):
    divisors = 1
    i = 2
    while i < math.ceil(math.sqrt(src)):
        counter = 0
        while src % i == 0:
            counter += 1
            src = src / i
        divisors = divisors * (counter + 1)

        i = 3 if i == 2 else i + 2

        if src == 1:
            return divisors

    return divisors * 2


def triangle_number(n):
    return n * (n + 1) / 2


def divisors():
    n = 1
    while True:
        if n % 2 == 0:
            divisors = count_divisors(n / 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) / 2)

        if (divisors > 500):
            ans = triangle_number(n)
            print('answer is %d' % ans)
            break

        n += 1


def main():
    divisors()


if __name__ == "__main__":
    main()
