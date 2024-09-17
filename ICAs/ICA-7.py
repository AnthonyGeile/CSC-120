'''
Define a class called ClockTime that keeps track of information about time as
represented in a clock. Times are measured on the 12 hour clock scale where 11:59 PM
is followed by 12:00 AM. The class should have the following methods:

a) __init__()
Takes three arguments: hours, minutes, and isAM and sets three instance
variables accordingly. Note that isAM is a Boolean value.
b) __str__()
for AM, returns the time in the format hours:minutes AM for PM, returns
the time in the format hours:minutes PM
c) total_minutes()
returns the total number of minutes. If 4:12 PM were the time, it would
return the following: 60 * 4 + 12 = 252
d) tick()
advances the time by one minute
An example of creating and using a ClockTime object follows:
>>> t = ClockTime(11, 58, False)
>>> print(t)
11:58 PM
>>> t.tick()
>>> print(t)
11:59 PM
>>>
>>> t.tick()
>>> print(t)
12:00 AM
>>>'''

class ClockTime:

    def __init__(self, hours, mins, isam):
        self._hours = hours
        self._mins = mins
        self._isam = 'AM' if isam == True else 'PM'

    def __str__(self):
        return "{}:{} {}".format(self._hours, self._mins, self._isam)
    
    def total_minutes(self):
        return (self._hours*60) + self._mins
    
    def tick(self):
        if self._mins == 59:
            self._hours += 1
            self._mins = 0
            if self._hours == 13:
                self._hours = 1
            if self._hours == 12:
                self._isam = 'AM' if self._isam == 'PM' else 'PM'
        else:
            self._mins += 1


t = ClockTime(11, 58, False)
print(t)
t.tick()
print(t)
t.tick()
print(t)