import pandas as pd
import numpy as np
data = pd.DataFrame({'Latitude': [40.7728, 34.0552, 41.8741],
                     'Longitude': [-74.0060, -118.2437, -87.6298]})

data['lat_bin'] = (data['Latitude'] // 0.1) * 0.1
data['lon_bin'] = (data['Longitude'] // 0.1) * 0.1
data['property_price'] = [500000, 300000, 700000]
data['avg_neighborhood_price'] = data.groupby(['lat_bin', 'lon_bin'])['property_price'].transform('mean')
print(data)