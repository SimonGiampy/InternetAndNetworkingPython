import requests
import matplotlib.pyplot as plot

plot.figure()

websites = ['http://www.google.com', 'http://www.polimi.it', 'https://www.stackoverflow.com']

for url in websites:
    print('test ' + url)
    tempi = []
    for k in range(10):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds/1000)
    plot.plot(tempi, label=url)
    print('min: ', min(tempi))
    print('avg: ', sum(tempi) / len(tempi))
    print('max: ', max(tempi))
    m = max([0, max(tempi)])

plot.ylim([0, 1.1*max(tempi)])
plot.xlabel('id request')
plot.ylabel('[ms]')
plot.title('testing google servers')
plot.legend(loc='lower right', fontsize=8)
plot.grid()
plot.show()
