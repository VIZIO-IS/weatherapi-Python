# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import weatherapi.models.condition

class Day(object):

    """Implementation of the 'Day' model.

    See day element

    Attributes:
        maxtemp_c (float): Maximum temperature in celsius for the day.
        maxtemp_f (float): Maximum temperature in fahrenheit for the day
        mintemp_c (float): Minimum temperature in celsius for the day
        mintemp_f (float): Minimum temperature in fahrenheit for the day
        avgtemp_c (float): Average temperature in celsius for the day
        avgtemp_f (float): Average temperature in fahrenheit for the day
        maxwind_mph (float): Maximum wind speed in miles per hour
        maxwind_kph (float): Maximum wind speed in kilometer per hour
        totalprecip_mm (float): Total precipitation in milimeter
        totalprecip_in (float): Total precipitation in inches
        avgvis_km (float): Average visibility in kilometer
        avgvis_miles (float): Average visibility in miles
        avghumidity (float): Average humidity as percentage
        condition (Condition): TODO: type description here.
        uv (float): UV Index

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "maxtemp_c":'maxtemp_c',
        "maxtemp_f":'maxtemp_f',
        "mintemp_c":'mintemp_c',
        "mintemp_f":'mintemp_f',
        "avgtemp_c":'avgtemp_c',
        "avgtemp_f":'avgtemp_f',
        "maxwind_mph":'maxwind_mph',
        "maxwind_kph":'maxwind_kph',
        "totalprecip_mm":'totalprecip_mm',
        "totalprecip_in":'totalprecip_in',
        "avgvis_km":'avgvis_km',
        "avgvis_miles":'avgvis_miles',
        "avghumidity":'avghumidity',
        "condition":'condition',
        "uv":'uv'
    }

    def __init__(self,
                 maxtemp_c=None,
                 maxtemp_f=None,
                 mintemp_c=None,
                 mintemp_f=None,
                 avgtemp_c=None,
                 avgtemp_f=None,
                 maxwind_mph=None,
                 maxwind_kph=None,
                 totalprecip_mm=None,
                 totalprecip_in=None,
                 avgvis_km=None,
                 avgvis_miles=None,
                 avghumidity=None,
                 condition=None,
                 uv=None):
        """Constructor for the Day class"""

        # Initialize members of the class
        self.maxtemp_c = maxtemp_c
        self.maxtemp_f = maxtemp_f
        self.mintemp_c = mintemp_c
        self.mintemp_f = mintemp_f
        self.avgtemp_c = avgtemp_c
        self.avgtemp_f = avgtemp_f
        self.maxwind_mph = maxwind_mph
        self.maxwind_kph = maxwind_kph
        self.totalprecip_mm = totalprecip_mm
        self.totalprecip_in = totalprecip_in
        self.avgvis_km = avgvis_km
        self.avgvis_miles = avgvis_miles
        self.avghumidity = avghumidity
        self.condition = condition
        self.uv = uv


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        maxtemp_c = dictionary.get('maxtemp_c')
        maxtemp_f = dictionary.get('maxtemp_f')
        mintemp_c = dictionary.get('mintemp_c')
        mintemp_f = dictionary.get('mintemp_f')
        avgtemp_c = dictionary.get('avgtemp_c')
        avgtemp_f = dictionary.get('avgtemp_f')
        maxwind_mph = dictionary.get('maxwind_mph')
        maxwind_kph = dictionary.get('maxwind_kph')
        totalprecip_mm = dictionary.get('totalprecip_mm')
        totalprecip_in = dictionary.get('totalprecip_in')
        avgvis_km = dictionary.get('avgvis_km')
        avgvis_miles = dictionary.get('avgvis_miles')
        avghumidity = dictionary.get('avghumidity')
        condition = weatherapi.models.condition.Condition.from_dictionary(dictionary.get('condition')) if dictionary.get('condition') else None
        uv = dictionary.get('uv')

        # Return an object of this model
        return cls(maxtemp_c,
                   maxtemp_f,
                   mintemp_c,
                   mintemp_f,
                   avgtemp_c,
                   avgtemp_f,
                   maxwind_mph,
                   maxwind_kph,
                   totalprecip_mm,
                   totalprecip_in,
                   avgvis_km,
                   avgvis_miles,
                   avghumidity,
                   condition,
                   uv)

