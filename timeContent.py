from onlineTime import TimeHandler

class TimeContent(object):
    def __init__(self, timeZone = 0):
        self.hour, self.minutes = TimeHandler.updateTime()
        self.timeZone = timeZone
        self.hour += self.timeZone
        self._checkTime()
        self._setTimeStr()
    # end of __init__

    # Checks correction of values of hours and minutes
    def _checkTime(self):
        if self.minutes < 0:
            print("Wrong minutes, setting minutes to 0")
            self.minutes = 0
        if self.hour < 0 or self.hour > 24:
            print("Wrong hour, setting hour to 0")
            self.hour = 0

        if self.minutes >= 60:
            self.hour += 1
            self.minutes -= 60
        elif self.hour < 0:
            self.hour = 24 + self.hour
    # end of _checkTime

    def _setTimeStr(self):
        strHour = "0" + str(self.hour) if self.hour < 10 else str(self.hour)  
        strMinutes = "0" + str(self.minutes) if self.minutes < 10 else str(self.minutes)  
        self.strTime = strHour + ":" + strMinutes
    # end of setTimeStr

    def updateTime(self):
        self.hour, self.minutes = TimeHandler.updateTime()
        self.hour += self.timeZone
        self._checkTime()
        self._setTimeStr()
    # end of setTime