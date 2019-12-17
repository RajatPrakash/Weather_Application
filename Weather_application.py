import tkinter as tk
from PIL import Image, ImageTk
import requests

# from flask import jsonify
# from pip._vendor import requests

window = tk.Tk()
window.geometry('600x600')
window.resizable(False,False)
# window.Tittle('Weather App')
image_open = Image.open('weather.jpg')
render = ImageTk.PhotoImage(image_open)

image_label = tk.Label(window,image=render)
image_label.place(relheight=1,relwidth=1)

top_frame = tk.Frame(window)
top_frame.place(relx=0.1,rely=0.2,relwidth=0.55,relheight=0.07)
bottom_frame = tk.Frame(window, bg='grey')
bottom_frame.place(relx=0.1, rely=0.35, relwidth=0.85, relheight=0.6)
label = tk.Label(bottom_frame, bg='grey', font=('Arial', 25))
label.place(relwidth=1, relheight=1)


def weather_update(weather):
    name = weather['name']
    cur_weather = weather['weather'][0]['description']
    temp = weather['main']['temp']
    final_str = name, cur_weather, temp
    return final_str


def get_weather():
    # print('this is the weather')
    user = entry.get()
    key = '6557bbd7dbca062ddf4fe097dc1ffab4'
    # api.openweathermap.org/data/2.5/weather?q={city name},{country code}
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': user, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()  # this also didn't worked
    print(weather)
    label['text'] = weather_update(weather)


entry = tk.Entry(top_frame,bg='white', borderwidth=5, font = ('Arial BOLD', 20))
entry.place(relheight=1,relwidth=1)
button = tk.Button(window,text="Get Weather!",bg='black',fg='white', font=('Arial BOLD', 18,), command=get_weather)
button.place(relx=0.7, rely=0.2, relwidth=0.25, relheight=0.07)




window.mainloop()