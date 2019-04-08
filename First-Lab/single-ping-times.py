import requests
import matplotlib.pyplot as plot

tempi = []

for url in range(10):
    r = requests.get('http://www.google.com')
    tempi.append(r.elapsed.microseconds/1000)

print('min: ', min(tempi))
print('avg: ', sum(tempi)/len(tempi))
print('max: ', max(tempi))

plot.figure()
plot.plot(tempi)
plot.ylim([0, 1.1*max(tempi)])
plot.xlabel('id request')
plot.ylabel('[ms]')
plot.title('testing google servers')
plot.grid()
plot.show()
