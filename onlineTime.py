from urllib.request import urlopen

class TimeHandler(object):
    @staticmethod
    def updateTime():
        url = str(urlopen('http://just-the-time.appspot.com/').read().strip())
        timeContents = url.split()[1].split(':')
        return int(timeContents[0]), int(timeContents[1])
