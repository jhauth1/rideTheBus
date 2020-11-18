class card():
    def __init__(self,num, suite):
        self.num = num
        self.suite = suite
        if suite == 'hearts' or suite == 'diamonds':
            self.color = 'red'
        else:
            self.color = 'black'

def on(old, new):
    # May just be the most recent
    return new.num == old.num

def notCardError(first):
    if not isinstance(first, card):
        # don't attempt to compare against unrelated types
        print('Attempted to compare a non card')
        quit()

def color(first, guess):
    notCardError(first)
    return first.color == guess

def upDown(first, second, guess):
    notCardError(second)
    if on(first, second):
        return guess == 'on'
    elif guess == 'up':
        return second.num > first.num
    else:
        return second.num < first.num

def inOut(first, second, third, guess):
    notCardError(third)
    if on(second, third):
        return guess == 'on'
    elif guess == 'out':
        if first.num > second.num:
            return third.num > first.num or third.num < second.num
        else:
            return third.num < first.num or third.num > second.num
    else:
        if first.num >  second.num:
            return third.num < first.num and third.num > second.num
        else:
            return third.num > first.num and  third.num < second.num

def suite(first, second, third, fourth, guess):
    notCardError(fourth)
    if on(third, fourth):
        return guess == 'on'
    else:
        return guess == fourth.suite