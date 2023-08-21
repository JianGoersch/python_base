#numbers = [1, 2, 3, 4, 5, 6] #lista materializada, ocupa muito espaço e mem
numbers = range(1,11)  #start, next, stop.

# Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue #continua no próxio for, e não até o fim do código

    print(f"mais codigo com {number}")

for line in open("post.txt"):
    if line == "---\n":
        break
    print(line)    
