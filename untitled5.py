# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qOE6e4pJ7ZlqyKCgNxhpgq7nibJWynzf
"""

def kasallik_tashxisi(belgi):
  if belgi=="Bosh og'rigi":
    return "Bolnol iching"
  if belgi=="Qorin og'rig'i":
    return "Espomizam iching"
  elif belgi=="Tish og'rig'i":
    return "Qupen iching"
  else:
    return "Shifokorga murojat qiling"
belgi=input("Kasallik belgisini kiriting ")
natija=kasallik_tashxisi(belgi)
print(natija)

def hafta_kunlari(kun):
  if kun=="Dushanba":
    return "1-para kiberxavszlik asoslari, 2-para suniy intelekt asoslari, 3-para malumotlar tuzilmasi va algoritmlar"
  if kun=="Seyshanba":
    return "1-para suniy intelekt asoslari, 2-para elektronika va sxemalari"
  if kun=="Chorshanba":
    return "1-elektronika va sxemalari, 2-para malumotlar tuzilmasi va algoritmlar"
  if kun=="Payshanba":
    return "1-para kompyuterni tashkil etish, 2-para malumotlar tuzilmasi va algoritmlar"
  elif kun=="juma":
    return "1-para kiberxavsizlik asoslari, 2-para elektronika va sxemalari"
  else:
      return "dars mavjud emas"
kun=input("hafta kunini kiriting")
natija=hafta_kunlari(kun)
print(natija)

