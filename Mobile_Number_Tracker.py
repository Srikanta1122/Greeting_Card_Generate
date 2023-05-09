from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder 
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("PHONE NUMBER TRACKER")
root.geometry("365x584")             #dimension for pop up GUI interface
root.resizable(False,False)



def track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)

    #country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)

    #operator  idea/airtel/jio
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)

    #phone timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)

    #longitude and latitude
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    #time showing in phone
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)




#logo
logo=PhotoImage(file="C:\\Users\\srika\\Downloads\\logo image.png")  #searching in phone logo
Label(root,image=logo).place(x=240,y=70)

Heading=Label(root,text="TRACK NUMBER",font=("ariel",15,"bold"))        #heading at the top
Heading.place(x=65,y=110)


#entry
Entry_back=PhotoImage(file="C:\\Users\\srika\\Downloads\\search png.png")    # search bar for entering number
Label(root,image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=("ariel",19),justify="center")   #for taking input
enter_number.place(x=50,y=225)


#button
Search_image=PhotoImage(file="C:\\Users\\srika\\Downloads\\search.png")   #search button
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("ariel",16),command=track)  #command will call track() function
search.place(x=35,y=300)


#bottom box
Box=PhotoImage(file="C:\\Users\\srika\\Downloads\\bottom png.png")     #blue botton image
Label(root,image=Box).place(x=-2,y=355)


country=Label(root,text="Country",bg="#57adff",fg="black",font=("ariel",10,"bold"))     #for country inside bottom box
country.place(x=40,y=400)

sim=Label(root,text="Sim",bg="#57adff",fg="black",font=("ariel",10,"bold"))       #for sim inside bottom box
sim.place(x=210,y=400)

zone=Label(root,text="Time Zone",bg="#57adff",fg="black",font=("ariel",10,"bold"))   # for zone
zone.place(x=40,y=450)

clock=Label(root,text="Phone Time",bg="#57adff",fg="black",font=("ariel",10,"bold"))  #for time
clock.place(x=210,y=450)

longitude=Label(root,text="Longitude",bg="#57adff",fg="black",font=("ariel",10,"bold"))   #for longitude
longitude.place(x=40,y=500)

latitude=Label(root,text="Latitude",bg="#57adff",fg="black",font=("ariel",10,"bold"))     #for latitude
latitude.place(x=210,y=500)



root.mainloop()

