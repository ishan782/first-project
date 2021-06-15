import requests
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import datetime as dt
root=tkinter.Tk()#####################ROOT WINDOW OR MAIN WINDOW
root.geometry("750x370")#########GEOMETRY OF MAIN WINDOW      
root.title("WEATHER FORECASTING")###########TITLE OF MAIN WINDOW
root.resizable(0,0)
root.configure(background="#E71989")#####BACKGROUND COLOUR OF MAIN WINDOW
lol2=Label(root,text="CITY",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
lol2.place(x=330,y=20)
locity=StringVar()
loe1=Entry(root,font=("comic sans ms",15),bg="white",textvariable=locity)
loe1.place(x=260,y=57)
def get_weather(city):
    api_key="e39a6478bd0071ed5988d2ab341cf88a"
    final_url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    result=requests.get(final_url)
    if result:
        data=result.json()
        place=data['name']
        country=data['sys']['country']
        temp_kelvin=data['main']['temp']
        temp_celcius=temp_kelvin-273.15
        temp_far=(temp_celcius)*9/5+32
        icon=data['weather'][0]['icon']
        wea=data['weather'][0]['main']
        hmdty=data['main']['humidity']
        win=data['wind']['speed']
        final=(place,country,temp_celcius,temp_far,temp_kelvin,icon,wea,hmdty,win)
        return final
    else:
        return None
def search():
    place=locity.get()
    weth=get_weather(place)
    if weth:
        location_lbl['text']='{},{}'.format(weth[0],weth[1])
        temp_lbl['text']='{:.2f}°C,{:.2f}°F,{:.2f}°K'.format(weth[2],weth[3],weth[4])
        wthr_lbl['text']=weth[6]
        hmdty_lbl['text']='{}%'.format(weth[7])
        wind_lbl['text']='{}kmph'.format(weth[8])
    elif place=="":
        messagebox.showerror('Error','Please Enter City Name')            
    else:
        messagebox.showerror('Error','Cannot Find City  {}'.format(place))
    
s_btn=Button(root,text="Search Weather",width=12,command=search)             
s_btn.place(x=320,y=102)
loc=Label(root,text="Location",font=("Times",20,"bold"),fg="green",bg="grey")
loc.place(x=100,y=130)
location_lbl=Label(root,text="",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
location_lbl.place(x=265,y=130)
hmdtyo=Label(root,text="Humidity",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
hmdtyo.place(x=100,y=180)
hmdty_lbl=Label(root,text="",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
hmdty_lbl.place(x=265,y=180)
ttemp=Label(root,text="Temperature",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
ttemp.place(x=100,y=230)
temp_lbl=Label(root,text="",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
temp_lbl.place(x=265,y=230)
wthro=Label(root,text="Weather",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
wthro.place(x=100,y=280)
wthr_lbl=Label(root,text="",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
wthr_lbl.place(x=265,y=280)
wind_sp=Label(root,text="Wind Speed",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
wind_sp.place(x=100,y=330)
wind_lbl=Label(root,text="",font=("Times",20,"bold"),fg="#AAC9CE",bg="#FEFBEA")
wind_lbl.place(x=265,y=330)
date=dt.datetime.now()
format_date=f"{date:%a,%b %d %Y}"
w=Label(root,text=f"{dt.datetime.now():%a, %b %d %Y}",fg="#AAC9CE",bg="#FEFBEA",font=("helvetica",20))
w.place(x=520,y=6)
root.mainloop()
    
