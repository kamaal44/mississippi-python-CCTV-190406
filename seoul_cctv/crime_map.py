import json
import folium
import pandas as pd
import numpy as np

ctx= '../data/'
df_police_norm = pd.read_csv(ctx+'police_norm.csv',
                             encoding='utf-8')
geo_path = ctx + 'geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))
map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=12,
                 tiles='Stamen Toner')
# map.save(ctx+'toner.html')
print(df_police_norm.columns)
"""
['구별', '강간', '강도', '살인', '절도', '폭력',
 '강간검거율', '강도검거율', '살인검거율', '절도검거율',
       '폭력검거율', '인구수', 'CCTV', '범죄', '검거']
"""
map_data = tuple(zip(df_police_norm['구별'],df_police_norm['범죄']))
map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=12,
                 tiles='Stamen Toner')
map.choropleth(geo_data = geo_str,
               data = map_data,
               columns = [df_police_norm.index, df_police_norm['범죄']],
               key_on = 'feature.id',
               fill_color = 'PuRd')
map.save(ctx+'toner2.html')