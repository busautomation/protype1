import time
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#ds3231.write_now()

while True:
    print ('Raspberry Pi ' + time.strftime("%Y-%m-%d %H:%M:%S"))
    print(ds3231.read_datetime())
    time.sleep(10.0)
    