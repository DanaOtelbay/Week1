x=int(input())

hour = x % (24*60*60) // (60*60)
minute = x % (60*60) // 3600
sek=x-(hour*3600)-(minute*60)

if minute>=0 and minute<10:
   minute = '0'+str(minute)
if sek>=0 and sek<10:
   sek = '0'+str(sek)

print()