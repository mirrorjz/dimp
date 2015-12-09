import requests
import pandas as pd
import math


url = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?rows=10' 
resp = requests.get(url)
data = resp.json()

data_values = np.ndarray(data['dataset']['data'])
data_df = pd.DataFrame(data_values)
data = pd.DataFrame(resp)

url = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?rows=10&column_index=4' 
resp = requests.get(url)
data = resp.json()
data_values = data['dataset']['data']
data_date = [item[0] for item in data_values]





    data_df = pd.DataFrame(data['results'][0]['geometry'])
    lati = data['results'][0]['geometry']['location']['lat']
    lngti = data['results'][0]['geometry']['location']['lng']
    print lati, lngti
    return (lati, lngti)



if __name__ == '__main__':
    #address_input = '242+South+Mentor+Avenue,+Pasadena,+CA'
    #result = find_coord(address_input)
    x = 20.0
    y = 90.0
    lati, lngi = location_coord(x,y)
    print lati, lngi
    result = find_address(lati, lngi)