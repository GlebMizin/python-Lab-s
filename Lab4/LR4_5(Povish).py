h = int(input())
m = int(input())
s = int(input())
if (h>11):
    h=h-12
    print(30*h + ((m/60) + (s/3600))*30)
else:
    print(30 * h + ((m / 60) + (s / 3600)) * 30)