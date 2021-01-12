#!/usr/bin/python

import os
from gpiozero import Button
from signal import pause
from kodijson import Kodi, PLAYER_VIDEO

gpio_dpi = 3
gpio_fwd = 5
gpio_rev = 6
gpio_lmb = 13
gpio_rmb = 19
gpio_mmb = 26

def Process(buttNum):
  if buttNum == gpio_dpi:
    kodi.Input.Back()
  elif buttNum == gpio_fwd:
    kodi.Input.Up()
  elif buttNum == gpio_rev:
    kodi.Input.Down()
  elif buttNum == gpio_lmb:
    kodi.Input.Left()
  elif buttNum == gpio_rmb:
    kodi.Input.Right()
  elif buttNum == gpio_mmb:
    kodi.Input.Select()

kodi_url = os.getenv('KODI_URL')
kodi_username = os.getenv('KODI_USERNAME')
kodi_password = os.getenv('KODI_PASSWORD')

kodi = Kodi(kodi_url + "/jsonrpc", kodi_username, kodi_password)

btn_dpi = Button(gpio_dpi)
btn_fwd = Button(gpio_fwd)
btn_rev = Button(gpio_rev)
btn_lmb = Button(gpio_lmb)
btn_rmb = Button(gpio_rmb)
btn_mmb = Button(gpio_mmb)

btn_dpi.when_pressed = Process
btn_fwd.when_pressed = Process
btn_rev.when_pressed = Process
btn_lmb.when_pressed = Process
btn_rmb.when_pressed = Process
btn_mmb.when_pressed = Process

print("KODI:")
print("  URL      : " + kodi_url)
print("  USERNAME : " + kodi_username)
print("  PASSWORD : " + kodi_password)
print()

print("Starting button monitoring...")
pause()
