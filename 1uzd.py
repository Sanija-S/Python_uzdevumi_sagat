"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""

class AAA:
    def __init__(self,):
        self.roman.numerals={
             1:"I",
             4:"IV",
             5:"V",
             9:"IX",
             10:"X",
             40:"XL",
             50:"L",
             90:"XC",
             100:"C",
             400:"CD",
             500:"D",
             900:"CM",
             1000:"M",

        }
      
    def uz_roman(self, num):
     result=""#tuksa virkne
     for value, numeral in sorted(self.roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while num>= value:
            result+=numeral
            num-=value
     return result
 
    # piemers
    skaitlis = 1984 #ieddu vertibu
    convertet= AAA()
    roman_numeral= convertet.to_roman(skaitlis) # converter- objekts, kuram izsauc metodi- lai parverstu skatli uz romiesu
    print(f"{skaitlis} romiesu ciparos ir {roman_numeral}")