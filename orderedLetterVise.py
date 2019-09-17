N=int(input())
my_str=input()
words=my_str.split()[:N]
words.sort()
for word in words:
	print(word,end=" ")
