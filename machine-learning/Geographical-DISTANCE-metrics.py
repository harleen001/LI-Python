from geopy.distance import geodesic
import pandas as pd
import numpy as np
data = pd.DataFrame({'Latitude': [40.7728, 34.0552, 41.8741],
                     'Longitude': [-74.0060, -118.2437, -87.6298]})

data['lat_bin'] = (data['Latitude'] // 0.1) * 0.1
data['lon_bin'] = (data['Longitude'] // 0.1) * 0.1

reference_point = (40.7128, -74.0060)
data['distance_to_reference'] = data.apply(
    lambda row: geodesic((row['Latitude'], row['Longitude']), reference_point).km, axis=1
)
print(data)