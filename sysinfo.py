import platform
import sys

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"
def sysinfo():
  return("""Python version: %s
  dist: %s
  linux_distribution: %s
  system: %s
  machine: %s
  platform: %s
  uname: %s
  version: %s
  """ % (
  sys.version.split('\n'),
  str(platform.dist()),
  linux_distribution(),
  platform.system(),
  platform.machine(),
  platform.platform(),
  platform.uname(),
  platform.version(),
  ))
