import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

train=pd.read_csv("data/train.csv")
val=pd.read_csv("data/val.csv")
X_data=pd.concat([train,val],axis=0).drop(columns="price")
# airline          640 non-null    object 
#  1   date_of_journey  640 non-null    object 
#  2   source           640 non-null    object 
#  3   destination      640 non-null    object 
#  4   dep_time         640 non-null    object 
#  5   arrival_time     640 non-null    object 
#  6   duration         640 non-null    int64  
#  7   total_stops      640 non-null    float64
#  8   additional_info 

class InputForm(FlaskForm):
    airline=SelectField(
        label="airline",
        choices=X_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    date_of_journey=DateField(
        label="Date of journey",
        validators=[DataRequired()]
    )
    source=SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination=SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    dep_time=TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    arrival_time=TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )
    duration=IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops=IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info=SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist()
    )
    submit=SubmitField("Predict")


