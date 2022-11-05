from pprint import pprint

list_of_dict = [{'bin': bin(count), 'dec': count, 'hex': hex(count), 'oct': oct(count)} for count in range(16)]
pprint(list_of_dict)
