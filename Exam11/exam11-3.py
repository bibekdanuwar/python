weather_detail_per_days = {
    "2025-04-28": {
        "weather": "くもり 昼過ぎ から 夕方 雨",
        "wind": "南西の風 後 北の風",
        "wave": "0.5メートル"
    },
    "2025-04-29": {
        "weather": "くもり 昼前 から 晴れ",
        "wind": "北西の風",
        "wave": "1メートル"
    },
    "2025-04-30": {
        "weather": "晴れ 昼前 から 雨",
        "wind": None,
        "wave": None
    }
}

weather_per_day_list = []

for day in weather_detail_per_days:
    weather_per_day_list.append({day: weather_detail_per_days[day]["weather"]})

print(weather_per_day_list)