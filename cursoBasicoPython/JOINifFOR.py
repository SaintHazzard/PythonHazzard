string_ = "This website is for losers LOL!"


def disemvowel(string_):
    # string_ = string_.lower()
    return "".join(i for i in string_ if i not in 'aeiou')
