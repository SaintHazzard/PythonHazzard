dna = "TTTT"

def dna_to_rna(dna):
    dna = dna.replace('T','U')
    
    return dna


print(dna_to_rna(dna))

string_ = "This website is for losers LOL!"
def disemvowel1(string_):
    for i in 'aeiouAEIOU':
        string_ = string_.replace(i, '')
    return string_


print(disemvowel1(string_))
