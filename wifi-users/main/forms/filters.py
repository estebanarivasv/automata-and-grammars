from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FilterForm(FlaskForm):
    username = StringField('Username')
    username_sum = StringField('User to sum the session times')
    datetime = StringField('Datetime', validators=[
        Regexp('\d\d/\d\d/\d\d\d\d \d\d:\d\d', message="Date must be in this format DD/MM/YYYY HH:MM")
    ])
    ap_mac = StringField('AP MAC address', validators=[
        MacAddress('(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', message="AP MAC address must be in this format 04-18-D6-22-94-E7:UM")
    ])
    client_mac = StringField('Client MAC address', validators=[
        RegMacAddressexp('(?:[0-9a-fA-F]{2}\-){5}[0-9a-fA-F]{2}(:UM)?', message="Client MAC address must be in this format 04-18-D6-22-94-E7")
    ])
    submit = SubmitField('Filter')


