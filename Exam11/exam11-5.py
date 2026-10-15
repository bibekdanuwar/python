weather_info_per_days = {
    "temperature": {
        "2025-04-28": {"min": "10", "max": "20"},
        "2025-04-29": {"min": "12", "max": "24"},
        "2025-04-30": {"min": "15", "max": "23"}
    },
    "detail": {
        "2025-04-28": {"wave": "0.5"},
        "2025-04-29": {"wave": "1.0"},
        "2025-04-30": {"wave": "1.5"}
    }
}
onemeter_wind_temp_list = []

for day in weather_info_per_days["detail"]:
    wave = float(weather_info_per_days["detail"][day]["wave"])

    if wave >= 1:
        min_temp = weather_info_per_days["temperature"][day]["min"]
        max_temp = weather_info_per_days["temperature"][day]["max"]

        onemeter_wind_temp_list.append((day, min_temp, max_temp))

print(onemeter_wind_temp_list)