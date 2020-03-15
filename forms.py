from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, URL, ValidationError, InputRequired
import re

# ---------------------------------------------------------------------------------
# Enum restrictions
# ---------------------------------------------------------------------------------

## Enum restriction
state_enum = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

genre_enum = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]


# ---------------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------------

# Validates Genres
def validate_genres(form, field):
    genres_values = [choice[1] for choice in genre_enum]
    for value in field.data:
        if value not in genres_values:
            raise ValidationError('Invalid genres value.')


# validates phone number
def validate_phone_Number(form, field):
    if not re.search(r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$", field.data):
        raise ValidationError("Invalid phone number.")


# ---------------------------------------------------------------------------------
# Forms
# ---------------------------------------------------------------------------------
# New Venue form
class VenueForm(Form):
    name = StringField('name', validators=[InputRequired('Please Enter Venue Name.')])
    city = StringField('city', validators=[InputRequired('Please Enter City.')])
    state = SelectField('state', validators=[InputRequired('Please select state')], choices=state_enum)
    address = StringField('address', validators=[InputRequired('Please Enter Your Address')])
    phone = StringField('phone', validators=[InputRequired('Please Enter Your Phone'), validate_phone_Number])
    image_link = StringField('image_link', validators=[InputRequired('Please Enter an Image link'), URL()])
    genres = SelectMultipleField('genres', validators=[InputRequired(), validate_genres], choices=genre_enum)
    facebook_link = StringField('facebook_link', validators=[InputRequired('Please Enter Your Facebook link!'), URL(),
                                                             URL()])
    website_link = StringField('website_link', validators=[InputRequired('Please Enter Your Website link!'), URL()])
    seeking_talent = BooleanField('seeking_talent')
    seeking_description = StringField('seeking_description')


# New Artist form
class ArtistForm(FlaskForm):
    name = StringField('name', validators=[InputRequired('Please Enter your Name')])
    city = StringField('city', validators=[InputRequired('Please Enter Your City.')])
    state = SelectField('state', validators=[InputRequired('Please select state')], choices=state_enum)
    phone = StringField('phone', validators=[InputRequired('Please Enter Your Phone'), validate_phone_Number])
    image_link = StringField('image_link', validators=[InputRequired('Please Enter an Image link'), URL()])
    genres = SelectMultipleField('genres', validators=[InputRequired(), validate_genres], choices=genre_enum)
    facebook_link = StringField('facebook_link', validators=[InputRequired('Please Enter Your Facebook link!'), URL(),
                                                             URL()])
    website_link = StringField('website_link', validators=[InputRequired('Please Enter Your Website link!'), URL()])
    seeking_venue = BooleanField('seeking_venue')
    seeking_description = StringField('seeking_description')


# Show form
class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )
