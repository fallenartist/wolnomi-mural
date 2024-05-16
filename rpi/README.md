#Raspberry Pi

Monitor:
https://gist.github.com/simlun/1b27b14d707abbba8fc1

Przypisanie pinów GPIO do klawiszy klawiatury - edytuj plik `/boot/firmware/config.txt`:

```
[all]
dtoverlay=gpio-key,gpio=23,active_low=0,gpio_pull=down,label=touch_P,keycode=25
dtoverlay=gpio-key,gpio=13,active_low=0,gpio_pull=down,label=touch_L,keycode=38
dtoverlay=gpio-key,gpio=19,active_low=0,gpio_pull=down,label=touch_R,keycode=19
```
