from re import sub


data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
def open_or_senior1(data):
    return [('Senior' if age >= 55 and handi > 7 else 'Open') for age, handi in data]


print(open_or_senior1(data))

s = 'ams'
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))


print(printer_error(s))


def printer_error(s):
  return f"{sum(c > 'm' for c in s)}/{len(s)}"
