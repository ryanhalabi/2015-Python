'''
A simple client for USDA statistics
    http://quickstats.nass.usda.gov/api
Found the data set in the data.gov catalog:
    http://catalog.data.gov/dataset/quick-stats-agricultural-database-api
Fun fact: This actually queries a database with 31 million records
'''

import requests
import json
import pprint




try:
    with open('usda_key.txt') as f:
        usda_key = f.read().rstrip()
except FileNotFoundError:
    pass




def get_param_values(param, key = usda_key):
    '''
    Returns the possible values for a single parameter 'param'
    >>> get_param_values('sector_desc')[:3]
    ['ANIMALS & PRODUCTS', 'CROPS', 'DEMOGRAPHICS']
    '''
    query_params = { 'key': key, 'param': param }
    endpoint = 'http://quickstats.nass.usda.gov/api/get_param_values/'
    response = requests.get(endpoint, params=query_params).json()
#    print(response)
    return(response)
    pass





def query(parameters, key=usda_key):
    '''
    Returns the JSON response from the USDA agricultural database
    'parameters' is a dictionary of parameters that can be referenced here:
        http://quickstats.nass.usda.gov/api
    Example: Return all the records around cattle in Tehama County
    >>> cowparams = {'commodity_desc': 'CATTLE',
                     'state_name': 'CALIFORNIA',
                     'county_name': 'TEHAMA'}
    >>> tehamacow = query(cowparams)
    '''
    parameters['key'] = key
    endpoint = 'http://quickstats.nass.usda.gov/api/api_GET/'
    response = requests.get(endpoint, params=parameters).json()
#    print(response)
    return(response)
    pass

    

#response = get_param_values('commodity_desc')

#commodity_desc = get_param_values('commodity_desc')


#print(type(commodity_desc))

#riceparams = {'sector_desc': 'CROPS',
#                  'commodity_desc': 'RICE',
#                  'state_name': 'CALIFORNIA',
#                  'county_name': 'YOLO',
#                  'year__GE': '2005',
#                  'unit_desc': '$'
#                  }
#
#
#yolorice = query(riceparams)
#
#print(yolorice)
#
#
#print(yolorice['data'])
#
#
#yearvalue = {x['year']: x['Value'] for x in yolorice['data']}


#print(  get_param_values('class_desc'))


tobparams = {'sector_desc': 'CROPS',
                  'commodity_desc' : 'TOBACCO',
                  'year': '2012',
                  'statisticcat_desc' : 'PRODUCTION',
                  'unit_desc': '$',
#                  'state_alpha' : 'PA',
                  'class_desc' : 'ALL CLASSES'

                  }




tob = query(tobparams)

pprint.pprint(tob)

tobvalue = {x['state_alpha']: x['Value'] for x in tob['data']}
#print(tob['data'])
#print(tob['data'][0]['value'])




#print(tobvalue)

#patotal = 0

for x in tob['data']:
    print( x['state_alpha'] )
    print(x['Value'] )
#    patotal = patotal+ x['Value']

#print(patotal)

#print(type(x['Value']))










