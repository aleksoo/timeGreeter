def decorator(func):
    def wrapper(time, name):
        if time.hour >= 6 and time.hour < 12:
            func(time.strTime, "morning", name)
        elif time.hour >= 12 and time.hour < 18:
            func(time.strTime, "day", name)
        elif (time.hour >= 18 and time.hour <= 24) or (time.hour < 6 and time.hour >= 0):
            func(time.strTime, "evening", name)
        else:
            print("Wrong hour, " + name + "!")
    # end of wrapper
        
    return wrapper    

@decorator
def welcomeMsg(time, timeOfDay, name="person"):
    print("Good " + timeOfDay + ", " + name + ", it\'s " + str(time) + ".")