from django.db import models

class ACTION(object):
    def __init__(self, player, action, card):
        self.player = player
        self.action = action
        self.card = card

class ACTIONS(object):
    def __init__(self):
        self.value = list()

    @property
    def status(self):
        return len(self.value)

    def insert(self, action):
        if isinstance(action, ACTION):
            self.value.append({'player':action.player,'action':action.action,'card':action.card})
        else:
            print 'warnging! U insert a wrong type action'

    def end(self):
        self.results = tuple(self.value)
