
from datetime import datetime
import pandas as pd
import streamlit as st

import numpy as np
np.random.seed(1)


class CalProc:
    def __init__(self):
        pass

    # method to assign a value to all elements of a list
    def data_reset(self, calander, days):
        calander = [((i * 0) + 4) for i in range(0, days)]

        return calander

    # method that assign dataframe's value to the list
    # according to the given date in dataframe
    def assign_data(self, data, calander):
        # convert data.dates into day_of_year
        for i in range(0, len(data)):
            # traversing dates and storing it into date_string
            date_string = data.loc[i, 'Date']
            # convert any date format into '%Y-%m-%d'
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            # generates the day of the year adn store it into day_of_year
            day_of_year = (date_obj - datetime(date_obj.year, 1, 1)).days + 1

            condition = data.loc[i, "Predicted State"]
            if condition == "Good":
                converted_condition = 0
            if condition == "Average":
                converted_condition = 1
            if condition == "Bad":
                converted_condition = 2
            if condition == "Critical":
                converted_condition = 3

            # append the data.Condition value into calander[day_of_year]
            calander[day_of_year] = converted_condition

        return calander
