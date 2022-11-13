# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_of_numbers = [({"bin": bin(num), "dec": num,
                   "hex": hex(num), "oct": oct(num)})
                 for num in range(16)]
pprint(list_of_numbers)
