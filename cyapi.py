# coding=utf-8
import sys
import time
from workflow import Workflow3, notify

CACHE_TIME = 600

def request_api_if_need(wf, api_name, fn):
  import cPickle
  from workflow import web
  log = wf.logger

  latitude = wf.stored_data('latitude')
  longitude = wf.stored_data('longitude')
  api_key = wf.get_password('apiKey')

  if not all([api_key, latitude, longitude]):
    wf.add_item(u'请通过 cy-opt 重新设置 API key')
    wf.send_feedback()
    return

  now = int(time.time())
  cached_key = '__cy_%s_%s_%s__' % (api_name, latitude, longitude)
  cached = wf.stored_data(cached_key)

  if cached and now - cached[0] < CACHE_TIME:
    data = cached[1]
  else:
    url = 'https://api.caiyunapp.com/v2.5/{api_key}/{longitude},{latitude}/{api_name}.json'.format(
      api_key=api_key, api_name=api_name, latitude=latitude, longitude=longitude)
    log.debug(url)

    data = web.get(url).json()
    if 'ok' == data.get('status'):
      wf.store_data(cached_key, (now, data))

  if 'ok' != data.get('status'):
    wf.add_item(u'请求失败: %s' % data.get('error', 'unknow'))
    wf.send_feedback()
    return

  fn(data)
