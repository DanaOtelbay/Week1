x=int(input())

hour = x % (24*60) // 60
minute = x % 60

print(hour, minute)