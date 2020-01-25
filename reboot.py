# import the kodi python modules we are going to use
# see the kodi api docs to find out what functionality each module provides
import xbmc
import xbmcgui
import xbmcaddon
import sys
import os

# create a class for your addon, we need this to get info about your addon
ADDON = xbmcaddon.Addon()
# get the full path to your addon, decode it to unicode to handle special (non-ascii) characters in the path
#CWD = ADDON.getAddonInfo('path').decode('utf-8')
CWD = ADDON.getAddonInfo('path') # for kodi 19 and up..

# this is the entry point of your addon, execution of your script will start here
if (__name__ == '__main__'):
  dialog = xbmcgui.Dialog()
  ret = dialog.select('Choose an OS', ['LibreELEC', 'RetroPie', 'Raspbian'])
  print('ret = ' + str(ret))
  if ret == 0:
    arg = 10
  elif ret == 1:
    arg = 6
  elif ret == 2:
    arg = 8
  else:
    sys.exit()
  
  #reboot!
  os.system('reboot ' + str(arg))
  
# the end!
