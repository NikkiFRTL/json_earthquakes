import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Изучение структуры данных
filename = 'eq_data_30_days_2021.geojson'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

"""
# Использовалось 1 раз для формирования читаемого файла для просмотра кода самому.
readable_file = 'readable_eq_data_30_days_2021.json'
with open(readable_file, 'w') as f:
    # dump() получает объект JSON и файл куда нужно записать данные, indent - форматировать с отступами = 4.
    json.dump(all_eq_data, f, indent=4)
"""

# Словарь со всеми землетресениями
all_eq_dicts = all_eq_data['features']

# Список с магнитудами и координатами (долгота + широта), информация о месте землетрясерния при наведении на маркер.
mags, lons, lats, info = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    if mag and mag > 1:
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        text = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        info.append(text)

# Нанесение данных на карту
data = [{
    'type': 'scattergeo',  # Scattergeo позволяет определить данные на диаграмме карты мира
    'lon': lons,  # Долгота
    'lat': lats,  # Широта
    'text': info,  # Информация о месте землетрясерния при наведении мышью на маркер
    'marker': {
        'size': [mag * 5 for mag in mags],  # Увеличение точек землетрясений для ощещния разницы в их силе
        'color': mags,  # Сообщает Plotly какое значение должно использоваться для определения маркера на цветовой шкале
        'colorscale': 'Viridis',  # Какой цветовой диапозон должен использоваться
        'reversescale': True,  # Подобрать наиболее подходящий вариант True / False(по умолчанию)
        'colorbar': {'title': 'Magnitude'},  # Цветовой шкале рписваиватся имя для понимания значения каждого цвета
    },
}]

filename_html = f"{all_eq_data['metadata']['title']}.html"
my_layout = Layout(title='Global Earthquakes in 30 days')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=filename_html)
