import requests




# Use the Weather stations around a Geo point weather station API to find the 30 weather stations
# closest to our campus. Our latitude: 29.5154448 Our longitude: -98.5555793



apiKey = '3421e27229a9355e86e2cb6e11ce2abc' # Put your API key in this string.



# Get the current weather for your home town.

homeTownUrl = 'http://api.openweathermap.org/data/2.5/weather?id=2963398&APPID='+apiKey
hT_Resp  =  requests.get(homeTownUrl)
if hT_Resp.status_code in [200, 201]:
    hT_weatherData = hT_Resp.json()
    print("Top o the mornin to ya! In {}, Ireland I bet ya its fackin raining... And whatcha know! There is {}".format(hT_weatherData['name'],
          hT_weatherData['weather'][0]['description']))

else:
    print('ERROR: ' + str(hT_Resp.status_code))



# Print out a nicely-formatted summary of the five day forecast for a city near your dream vacation.
fiveDayUrl = 'http://api.openweathermap.org/data/2.5/forecast?id=1894616&APPID=' + apiKey
fD_Response = requests.get(fiveDayUrl)
if fD_Response.status_code in [200,201]:
    fD_weatherData = fD_Response.json()

    for i in range(40):
        print('On {} the weather in Okinawa, Japan will be {}'.format(str(
              fD_weatherData['list'][i]['dt_txt']),
              str(fD_weatherData['list'][i]['weather'][0]['description'])))

else:
    print('ERROR: ' +str(fD_Response.status_code))



#geo points
# Our latitude: 29.5154448 Our longitude: 29.5154448


geoPointURL = 'http://api.openweathermap.org/data/2.5/station/find?lat=29.5154448&lon=29.5154448&cnt=30&APPID=' + apiKey
gP_Response = requests.get(geoPointURL)

if gP_Response.status_code in [201, 200]:
    gP_weatherData = gP_Response.json()
    for i in range(30):
        print('Weather Station {} Readying Defense Protocols. Authorization--SIGMA : Readying Satalite... '.format(gP_weatherData[i]['station']['name']))
else:
    print('error' + str(gP_Response.status_code))
