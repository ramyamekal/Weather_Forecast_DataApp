import requests

def get_data(place,forecast_days=None):
    API_KEY = "727d5c74edbb0fe968ac9e1150916d1b"

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data =response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days = 3))
