from collections import OrderedDict
def remove_duplicate(str1):
	return "".join(OrderedDict.fromkeys(str1))
S=input()
print(remove_duplicate(S))
