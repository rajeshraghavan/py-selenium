######################################################
#This checkes the roundtrip time for a http request
#Author - rajeshr
#Date: 12/06/2020
#####################################################

import time
import requests
import sys
def roundtriptime(url):
    initial_time = time.time()  # Store the time when request is sent
    request = requests.get(url)
    ending_time = time.time()  #Time when acknowledged the request
    elapsed_time = str(ending_time - initial_time)
    print('The Round Trip Time for {} is {}'.format(url, elapsed_time))

roundtriptime("https://server.company.com")
