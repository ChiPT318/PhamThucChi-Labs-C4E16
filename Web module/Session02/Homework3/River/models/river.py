from mongoengine import *

class Rivers(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
