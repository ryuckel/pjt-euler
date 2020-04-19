import math
import string
import numpy as np
from functools import reduce
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
#     src = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

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


# def count_divisors(src):
#     divisors = 1
#     i = 2
#     while i < math.ceil(math.sqrt(src)):
#         counter = 0
#         while src % i == 0:
#             counter += 1
#             src = src / i
#         divisors = divisors * (counter + 1)

#         i = 3 if i == 2 else i + 2

#         if src == 1:
#             return divisors

#     return divisors * 2


# def triangle_number(n):
#     return n * (n + 1) / 2


# def divisors():
#     n = 1
#     while True:
#         if n % 2 == 0:
#             divisors = count_divisors(n / 2) * count_divisors(n + 1)
#         else:
#             divisors = count_divisors(n) * count_divisors((n + 1) / 2)

#         if (divisors > 500):
#             ans = triangle_number(n)
#             print('answer is %d' % ans)
#             break

#         n += 1

# problem13
# def large_sum():
#     nums_str = """
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690
# """[1:-1]

#     nums = map(int, nums_str.split("\n"))

#     result = int(str(sum(nums))[:10])

#     print(result)

# problem14
# def collatz(src):
#     if src % 2 == 0:
#         return src / 2
#     return 3 * src + 1


# def count(src, steps):
#     dest = collatz(src)
#     if dest not in steps:
#         count(dest, steps)
#     steps[src] = steps[dest] + 1
#     return steps


# def longest_collaz_sequence():
#     MAX = 10 ** 6
#     answer = None
#     longest_chain = 0
#     steps = {1: 1}

#     for i in range(MAX, 1, -1):
#         if i in steps:
#             continue
#         steps = count(i, steps)
#         if steps[i] > longest_chain:
#             longest_chain = steps[i]
#             answer = i

#     print('longest chain is %d, which starts with %d' %
#           (longest_chain, answer))


# problem15
# def lattice_paths():
#     n, r = 40, 20
#     permutation = math.factorial(n) / math.factorial(n - r)
#     answer = permutation / math.factorial(r)
#     print('answer is %d' % answer)

# problem16
# def power_digit_sum():
#     ans = 0
#     num = 2 ** 1000
#     string_list = list(str(num))
#     for i in string_list:
#         ans += int(i)
#     print(ans)

# problem17
# TEN = 10
# HUNDRED = 100
# THOUSAND = 1000
# WORDS = {
#     0: '',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
#     TEN: 'ten',
#     11: 'eleven',
#     12: 'twelve',
#     13: 'thirteen',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'nineteen',
#     20: 'twenty',
#     30: 'thirty',
#     40: 'forty',
#     50: 'fifty',
#     60: 'sixty',
#     70: 'seventy',
#     80: 'eighty',
#     90: 'ninety',
#     HUNDRED: 'hundred',
#     THOUSAND: 'thousand',
# }


# def convert_to_word(num):
#     word = ''
#     # 1000 ~ 9999
#     quotient, remainder = divmod(num, THOUSAND)
#     if quotient != 0:
#         word += WORDS[quotient] + WORDS[THOUSAND]
#     # 100 ~ 999
#     quotient, remainder = divmod(remainder, HUNDRED)
#     if quotient != 0:
#         word += WORDS[quotient] + WORDS[HUNDRED]
#         if remainder != 0:
#             word += 'and'
#     # 1 ~ 20
#     if remainder < 20:
#         word += WORDS[remainder]
#     # 21 ~ 99
#     else:
#         quotient, remainder = divmod(remainder, TEN)
#         if quotient != 0:
#             word += WORDS[quotient * TEN] + WORDS[remainder]

#     return word


# def number_letter_counts():
#     _len = 0
#     for i in range(1, 1001):
#         word = convert_to_word(i)
#         _len += len(word)
#         print('%d: %s' % (i, word))
#     print('answer is %d' % _len)


# problem18

# def maximum_sum_1():
#     src = '''
#       75
#       95 64
#       17 47 82
#       18 35 87 10
#       20 04 82 47 65
#       19 01 23 75 03 34
#       88 02 77 73 07 63 67
#       99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#       41 48 72 33 47 32 37 16 94 29
#       53 71 44 65 25 43 91 52 97 51 14
#       70 11 33 28 77 73 17 78 39 68 17 57
#       91 71 52 38 17 14 91 43 58 50 27 29 48
#       63 66 04 68 89 53 67 30 73 16 69 87 40 31
#       04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#     '''

#     src = src.strip().split('\n')
#     src = [row.lstrip().split(' ') for row in src]
#     src = [[int(x) for x in row] for row in src]

#     # iterate each row
#     for row_index, row in enumerate(src):
#         if row_index == len(src) - 1:
#             break
#         # iterate each column
#         next_row = src[row_index + 1]
#         for col_index, num in enumerate(next_row):
#             # left end
#             if col_index == 0:
#                 next_row[col_index] += row[0]
#             # right end
#             elif col_index == len(next_row) - 1:
#                 next_row[col_index] += row[-1]
#             else:
#                 next_row[col_index] += max(row[col_index - 1], row[col_index])

#     _sum = max(src[-1])
#     print('maximum total is %d' % _sum)

# problem19
# def get_days_of_month(year, month):
#     if month == 2:
#         if year % 400 != 0 and year % 4 == 0:
#             return 29
#         return 28
#     elif month in {9, 4, 6, 11}:
#         return 30
#     else:
#         return 31


# def counting_sunday():
#     total_days = 0
#     sum_of_sundays = 0

#     for year in range(1900, 2001):
#         for month in range(1, 13):
#             # begins with Sunday
#             if year != 1900 and total_days % 7 == 0:
#                 sum_of_sundays += 1

#             # this month has
#             days = get_days_of_month(year, month)
#             total_days += days

#     print('%d Sundays fell on the first of the month during the 20th century.' %
#           sum_of_sundays)

# problem20
# def factorial_digit_sum():
#     ans = 0
#     num = math.factorial(100)
#     tmp = list(str(num))
#     for i in tmp:
#         ans += int(i)
#     print(ans)

# problem21

# 約数の総和
# def sum_of_divisors(num):
#     factors = factoring(num)
#     operands = []
#     for divisor, power in factors.items():
#         operands.append(sum([divisor ** i for i in range(power + 1)]))
#     return reduce(lambda x, y: x * y, operands) + 1


# # 真約数の総和
# def sum_of_proper_divisors(num):
#     return sum_of_divisors(num) - (1 + num)


# # 素因数分解
# def factoring(num):
#     factors = {}
#     divisor = 2
#     power = 0
#     GREATEST_DIVISOR = num / 2
#     while num > 1 and divisor <= GREATEST_DIVISOR:
#         if num % divisor != 0:
#             if power != 0:
#                 factors[divisor] = power
#             power = 0
#             if divisor == 2:
#                 divisor += 1
#             else:
#                 divisor += 2
#         else:
#             num = num / divisor
#             power += 1
#     factors[divisor] = power
#     return factors


# def amicable_numbers():
#     checked = set()
#     amicable_pairs = []

#     for a in range(220, 10001):
#         if a in checked:
#             continue
#         b = sum_of_proper_divisors(a)
#         if b < a or b == a:
#             continue
#         sum_b = sum_of_proper_divisors(b)
#         if sum_b == a:
#             amicable_pairs.append((a, b))
#         checked.add(a)
#         checked.add(b)

#     _sum = sum([sum(pair) for pair in amicable_pairs])
#     print('amicable pairs: %s' % amicable_pairs)
#     print('sum is %d' % _sum)

# problem22
# def name_scores():
#     ALPHABET = {'"': 0}
#     for index, char in enumerate(list(string.ascii_uppercase)):
#         ALPHABET[char] = index + 1

#     with open('./p022_names.txt', 'r') as f:
#         names = sorted(f.read().split(','))

#     _sum = 0
#     for index, name in enumerate(names):
#         _sum += sum([ALPHABET[char] for char in list(name)]) * (index + 1)
#     print('sum is %d' % _sum)

# problem23
def sum_of_proper_divisors(MAX):
    sum_list = [1] * (MAX + 1)
    for divisor in range(2, int(math.sqrt(MAX)) + 1):
        sum_list[divisor ** 2] += divisor
        for times in range(divisor + 1, MAX // divisor + 1):
            sum_list[divisor * times] += divisor + times
    return sum_list


def is_sum_of_two_abundant_numbers(num, abundant_numbers):
    for abundant_number in abundant_numbers:
        if abundant_number > num / 2:
            break
        if (num - abundant_number) in abundant_numbers:
            return True
    return False


def non_abundant_sums():
    MAX = 28123
    tmp = sum_of_proper_divisors(MAX)
    abundant_numbers = set(
        [num for num, _sum in enumerate(tmp) if _sum > num])
    abundant_numbers.remove(0)
    _sum = sum([num for num in range(MAX + 1)
                if not is_sum_of_two_abundant_numbers(num, abundant_numbers)])
    print('sum is %d' % _sum)


def main():
    non_abundant_sums()


if __name__ == "__main__":
    main()
