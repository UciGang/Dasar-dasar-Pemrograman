#program konversi suhu dari celcius ke farenheit dan reamur
#input
suhu = str(input("Pilih suhu yang ingin diubah (celcius,reamur,farenheit,kelvin) = "))
temperatur = int(input("Pilih temperatur yang ingin diubah = "))

#rumus
if suhu == "celcius":
    #reamur
    reamur = 4/5 * temperatur
    print("Suhu reamurnya adalah = ", reamur, "°R")
    #farenheit
    farenheit = 9/5 * temperatur + 32
    print("Suhu farenheitnya adalah = ", farenheit, "°F")
    #kelvin
    kelvin = temperatur + 273
    print("Suhu kelvinnya adalah = ", kelvin, "°K")
elif suhu == "reamur":
    #celcius
    celcius = temperatur / 0.8
    print("Suhu celciusnya adalah = ", celcius, "°C")
    #farenheit
    farenheit = (temperatur * 2.25) + 32
    print("Suhu farenheitnya adalah = ", farenheit, "°F")
    #kelvin
    kelvin = (temperatur / 0.8) + 273.15
    print("Suhu kelvinnya adalah = ", kelvin, "°K")
elif suhu == "farenheit":
    #celcius
    celcius = (temperatur - 32) * 5/9
    print("Suhu celciusnya adalah = ", celcius, "°C")
    #reamur
    reamur = 4/9 * (temperatur - 32)
    print("Suhu reamurnya adalah = ", reamur, "°R")
    #kelvin
    kelvin = (temperatur + 459.67) * 5/9
    print("Suhu kelvinnya adalah = ", kelvin, "°K")
else:
    #celcius
    celcius = temperatur - 273.15
    print("Suhu celciusnya adalah = ", celcius, "°C")
    #reamur
    reamur = 4/5 * (temperatur - 273)
    print("Suhu reamurnya adalah = ", reamur, "°R")
    #farenheit
    farenheit = (temperatur * 9/5) - 459.67
    print("Suhu farenheitnya adalah = ", farenheit, "°F")
