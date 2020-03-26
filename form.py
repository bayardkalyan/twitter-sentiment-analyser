from flask import *
from wtforms import TextField, TextAreaField, SubmitField, validators, StringField, IntegerField
from flask_wtf import Form

class getData(Form):

    topic = StringField('topic: ',[validators.Length(min= 1, max=20)])
    count = IntegerField('Number')
    submit=SubmitField('Analyze')