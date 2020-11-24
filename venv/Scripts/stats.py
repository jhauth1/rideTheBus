import Deck
from statistics import mean
import time
import math

start_time = time.time()
scores = []
for x in range(0, 10000000):
    scores.append(Deck.play())
print(mean(scores))
time = (time.time() - start_time)
print()
if time < 60:
    print("Seconds: %s" % time)
elif time < (60*60):
    minutes = math.floor(time/60)
    print('Minutes: %s\nSeconds: %s ' % (minutes, (time - math.floor(minutes*60))))
else:
    hour = math.floor(time/(60*60))
    minutes = math.floor(time/60 - (hour*60))
    print('Hours: %s\nMinutes: %s\nSeconds: %s' %
          (hour, minutes, math.floor(time - (60*60*hour) - (minutes*60))))