import json
import folium
import pandas as pd
import numpy as np
import googlemaps

ctx= '../data/'
df_police_norm = pd.read_csv(ctx+'police_norm.csv',
                             encoding='utf-8')
geo_path = ctx + 'geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))
map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=12,
                 tiles='Stamen Toner')
# map.save(ctx+'toner.html')
# print(df_police_norm.columns)
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
# map.save(ctx+'toner2.html')
df_police_pos = pd.read_csv(ctx+'police_position.csv',
                             encoding='utf-8')
# print(df_police_pos.columns)

"""
['Unnamed: 0', '관서명', '살인 발생', 
'살인 검거', '강도 발생', '강도 검거', 
'강간 발생',
       '강간 검거', '절도 발생', '절도 검거',
       '폭력 발생', '폭력 검거']
"""
col = ['살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거']
tmp = df_police_pos[col] / df_police_pos[col].max()
df_police_pos['검거'] = np.sum(tmp, axis=1)


filename = 'crime_in_Seoul.csv'
df_crime = pd.read_csv(ctx+filename,
                       thousands=',',
                       encoding='euc-kr')
gmaps_key = 'AIzaSyD9d1pZQ-vrq-Gx1kWc1t-zcgP21S2zaso'
gmaps = googlemaps.Client(key=gmaps_key)
station_name = []

for name in df_crime['관서명']:
    station_name.append('서울'+str(name[:-1])+'경찰서')

station_addr = []
station_lat = [] #위도
station_lng = [] #경도

for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addr.append(tmp[0].get('formatted_address'))
    tmp_loc = tmp[0].get('geometry')
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    # print(name + '--------->'+tmp[0].get('formatted_address'))

df_police_pos['lat'] = station_lat
df_police_pos['lng'] = station_lng
arr = df_police_pos
print(arr.columns)
"""
['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '검거', 'lat', 'lng']
"""

map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=12)
map.choropleth(geo_data = geo_str,
               data = map_data,
               columns = [df_police_norm.index, df_police_norm['범죄']],
               key_on = 'feature.id',
               fill_color = 'PuRd')
for i in arr.index:
    folium.CircleMarker([arr['lat'][i], arr['lng'][i]],
                        radius=arr['검거'][i] * 10,
                        color = '#0a0a32',
                        fill_color = '#0a0a32').add_to(map)
map.save(ctx+'police_final.html')





