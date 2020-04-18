# coding=utf-8
import sys

MIN = -sys.maxint - 1
MAX = sys.maxint

def get_weather(name):
  data = {
      'clear_day': u'晴天',
      'clear_night': u'晴夜',
      'partly_cloudy_day': u'多云',
      'partly_cloudy_night': u'多云',
      'cloudy': u'阴',
      'rain': u'雨',
      'snow': u'雪',
      'wind': u'风',
      'fog': u'雾',
      'haze': u'霾',
      'sleet': u'冻雨',
  }
  name = name.lower()
  return data.get(name, name)

def get_wind_direction(wd):
  data = {
    (MIN, 22.5): u'北风',
    (22.5, 67.5): u'东北风',
    (67.5, 112.5): u'东风',
    (112.5, 157.5): u'东南风',
    (157.5, 202.5): u'南风',
    (202.5, 247.5): u'西南风',
    (247.5, 292.5): u'西风',
    (292.5, 337.5): u'西北风',
    (337.5, MAX): u'北风',
  }
  for l, r in data.keys():
    if l < wd <= r:
      return data[k]

def get_wind_speed(ws):
  data = {
      (MIN, 2): u'无风',
      (2, 6): u'软风',
      (6, 12): u'轻风',
      (12, 19): u'缓风',
      (19, 30): u'和风',
      (30, 40): u'清风',
      (40, 51): u'强风',
      (51, 62): u'疾风',
      (62, 75): u'烈风',
      (75, 87): u'增强烈风',
      (87, 103): u'暴风',
      (103, 149): u'台风',
      (149, MAX): u'出门就被风吹走',
  }
  for l, r in data.keys():
    if l < ws <= r:
      return data[k]
