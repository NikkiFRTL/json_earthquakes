import json

# Изучение структуры данных
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

"""
# Использовалось 1 раз для формирования читаемого файла.
readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    # dump() получает объект JSON и файл куда нужно записать данные, indent - форматировать с отступами = 4.
    json.dump(all_eq_data, f, indent=4)
"""

# Словарь со всеми 158 землетресениями
all_eq_dicts = all_eq_data['features']

# Список с магнитудами и координатами (долгота + широта)
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)

print(mags[:10])
print(lons[:5])
print(lats[:5])
