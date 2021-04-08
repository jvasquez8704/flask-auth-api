import os
import time
class Props:
  DEFAULT_USER_ROLE = 'Viewer'
  LOCAL_MODE = 'local'
  PRD_MODE = 'production'
  DEV_MODE = 'development'
  STG_MODE = 'staging'
  USER_SCHEME = 'Users'
  CURRENT_TIME = int(round(time.time() * 1000))