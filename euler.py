import math
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
def summarize_prime():
    primes = [2]
    i = 3
    while primes[-1] < 2000000:
        for p in primes:
            if i % p == 0:
                break
            else:
                primes.append(i)
        i += 2
        print(i)
    total = sum(primes)
    print(total)


def main():
    summarize_prime()


if __name__ == "__main__":
    main()
