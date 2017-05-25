from datetime import datetime

start = datetime.now()
l = [str(n) for n in range(10000000,30000001) if n%2 == 0]
end = datetime.now()

print ' '.join(l)


print start
print end
print end - start
