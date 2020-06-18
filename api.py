"""[]
@author: Ocaka Alfred

This script accesses  DHIS2 REST API, extract the list of organization units as a csv from free training server
provided by DHIS https://play.dhis2.org/ (admin/district).

"""
import pandas as pd
import json
import requests


class Units:

    #DHIS2  REST API end point
    url =  "https://play.dhis2.org/demo/api/33/organisationUnits"

    def __init__(self):
        pass

    
    def organizational_units(self):
        """
        This method  gets data from the REST API endpoint,

        loads the json data into pandas dataframe and

        Save the organization units into csv

        """

        result = requests.get(self.url, auth=('admin','district'))
        
        data    = json.loads(result.text)
        
        df  = pd.DataFrame(data['organisationUnits'])
        
        df.to_csv("organisationUnits.csv")

"""
instantiating the class and the method
"""
unit  = Units()
unit.organizational_units()
