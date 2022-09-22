import re


signature = [3, 2, 1]
n = 2
signature1 = [1, 2, 3]

def tribonacci(signature, n):
    signature = signature[:2]
    for i in range(n-3):
        signature.append(sum(signature[-3:]))
    return signature


def tribonacci2(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


def tribonacci1(signature, n):
  res = signature[:n]
  for i in range(n - 3):
      res.append(sum(res[-3:]))
  return res

# print(tribonacci(signature, n))


arr = [':D', ':~)', ';~D', ':)']


def count_smileys(arr):
    return len(re.findall('[:;][-~]?[)D]', str(arr)))

current = 'green'
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

print(update_light(current))


dic = {i: round(i**0.5,2) for i in range(1000)}
print(dic)