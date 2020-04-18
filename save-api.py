# coding=utf-8
import sys
import subprocess
from workflow import Workflow3, notify

def main(wf):
  log = wf.logger
  args = wf.args
  api_key = args[0]

  # https://github.com/robmathers/WhereAmI/releases
  geoinfo = subprocess.check_output(["/usr/local/bin/whereami"])
  for line in geoinfo.split('\n'):
    line = line.lower().strip()
    if line.startswith('latitude'):
      wf.store_data('latitude', line.split()[-1])
    if line.startswith('longitude'):
      wf.store_data('longitude', line.split()[-1])

  wf.save_password('apiKey', api_key)

if __name__ == '__main__':
  wf = Workflow3()
  sys.exit(wf.run(main))
