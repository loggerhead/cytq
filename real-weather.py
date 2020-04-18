# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import datetime
from workflow import Workflow3, notify
from cyapi import request_api_if_need
from data import *

def render_realtime(data):
  result = data['result']['realtime']
  weather = get_weather(result['skycon'])

  title = u'现在  %.0f°C %s ' % (result['temperature'], weather)
  subtitle = u'湿度 %.0f%% | 空气质量%s | PM2.5 %.0f' % (
      result['humidity'] * 100,
      result['air_quality']['description']['chn'],
      result['air_quality']['pm25']
  )

  wf.add_item(subtitle=subtitle, title=title, icon='icon.png')

def render_hourly(data):
  result = data['result']['hourly']
  description = result['description']
  skycons = result['skycon']
  temperatures = result['temperature']

  def iter_after_now(items):
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day + 1)

    filtered = {}
    for item in items:
      dtstr = item['datetime'].split('+')[0]
      dt = datetime.datetime.strptime(dtstr, '%Y-%m-%dT%H:%M')
      if dt > today:
        continue
      filtered[dt] = item
    return filtered

  skycons = iter_after_now(skycons)
  temperatures = iter_after_now(temperatures)

  tt = sorted(skycons.keys())
  for i in range(len(tt))[::2]:
    def gen_title(t):
      skycon = skycons[t]
      temperature = temperatures.get(t, {}).get('value', '')
      weather = get_weather(skycon['value'])
      title = '%02d:00 %.0f°C %s' % (t.hour, temperature, weather)
      return title

    title = gen_title(tt[i])
    subtitle = gen_title(tt[i + 1]) if i + 1 < len(tt) else ''
    wf.add_item(title=title, subtitle=subtitle, icon='icon.png')

def main(wf):
  request_api_if_need(wf, 'realtime', render_realtime)
  request_api_if_need(wf, 'hourly', render_hourly)
  wf.send_feedback()

if __name__ == '__main__':
  wf = Workflow3()
  sys.exit(wf.run(main))
