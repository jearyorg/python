import sys
result = []
def f8(seq):     
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)] 
for line in open(sys.argv[1]):
	result.append(line)
result = f8(result)
for s in result:
	print s.strip()