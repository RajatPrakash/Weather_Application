import tkinter as tk
from PIL import Image, ImageTk
import requests

# declaring the Frame of Application
window = tk.Tk()
window.geometry('600x600')
window.resizable(False, False)
window.title('Weather App')
image_open = Image.open('weather.jpg')
render = ImageTk.PhotoImage(image_open)

image_label = tk.Label(window, image=render)
image_label.place(relheight=1, relwidth=1)

top_frame = tk.Frame(window)
top_frame.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)
bottom_frame = tk.Frame(window)
bottom_frame.place(relx=0.1, rely=0.35, relwidth=0.85, relheight=0.6)
label = tk.Label(bottom_frame, bg='grey')
label.place(relwidth=1, relheight=1)


# Function to Retrieve data into the desire format from JSON
def weather_update(weather):
    try:
        name = weather['name']
        cur_weather = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, cur_weather, temp)

    except:
        final_str = 'There was a problem retrieving that information'
    return final_str


# function connecting Application To the API using the key and getting the Data into JSON Format


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
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

# function for getting the ICON from the Stored folder From System


def open_image(icon):
    size = int(bottom_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img

# rest of the Designing for the Same


entry = tk.Entry(top_frame, bg='white', borderwidth=5, font=('Arial BOLD', 20))
entry.place(relheight=1, relwidth=1)
button = tk.Button(window, text="Get Weather!", bg='black', fg='white', font=('Arial BOLD', 18,), command=get_weather)
button.place(relx=0.7, rely=0.2, relwidth=0.25, relheight=0.07)
# bg_color = 'white'
label = tk.Label(bottom_frame, anchor='nw', justify='left', bd=4)
label.config(font=('Arial', 12), bg='grey')
label.place(relwidth=1, relheight=1)
weather_icon = tk.Canvas(label, bd=0, highlightthickness=0, bg='grey')
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

window.mainloop()
