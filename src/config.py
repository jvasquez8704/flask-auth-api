import os
from constants import Props

class LOCAL:
  #[App Secrets]
  APP_SECRET_KEY='katch-app-504'
  APP_JWT_SECRET_SEED='s4P3r-s3cr3t_K@tCh-d3V_K3y'
 
  #[Credentials]
  GOOGLE_APPLICATION_CREDENTIALS = './src/db/keys/nrg_dev.json'
  CREDENTIALS_FIREBASE_SDK_PATH = './src/db/keys/nrg_dev.json'
  FIREBASE_WEB_API_KEY='AIzaSyBJM-U6ZGMF2iItNbXbDrds043_LM4htd0'

  #[Firebase]
  KATCH_FIREBASE_DB_URL='https://katch-nrg-nonprod.firebaseio.com/'
  KATCH_FIREBASE_SIGNIN_URL='https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
  KATCH_FIREBASE_SIGNUP_URL='https://identitytoolkit.googleapis.com/v1/accounts:signUp'

  #[Utelly]
  KATCH_UTELLY_URL = 'https://10.63.241.73:443/user' if os.getenv('CURRENT_ENV') is not None else 'https://dev-api.utelly.com/phoenix/9/user'
  HEADER_X_APP_KEY='9404481bdc5f765cba251e74a71ce15b'
  CURRENT_ENV = os.getenv('CURRENT_ENV', Props.DEV_MODE)
class DEV:
  #[App Secrets]
  APP_SECRET_KEY='katch-app-504'
  APP_JWT_SECRET_SEED='s4P3r-s3cr3t_K@tCh-d3V_K3y'
 
  #[Credentials]
  GOOGLE_APPLICATION_CREDENTIALS = './src/db/keys/nrg_dev.json'
  CREDENTIALS_FIREBASE_SDK_PATH = './src/db/keys/nrg_dev.json'
  FIREBASE_WEB_API_KEY='AIzaSyBJM-U6ZGMF2iItNbXbDrds043_LM4htd0'

  #[Firebase]
  KATCH_FIREBASE_DB_URL='https://katch-nrg-nonprod.firebaseio.com/'
  KATCH_FIREBASE_SIGNIN_URL='https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
  KATCH_FIREBASE_SIGNUP_URL='https://identitytoolkit.googleapis.com/v1/accounts:signUp'

  #[Utelly]
  KATCH_UTELLY_URL = 'https://10.63.241.73:443/user' if os.getenv('CURRENT_ENV') is not None else 'https://dev-api.utelly.com/phoenix/9/user'
  HEADER_X_APP_KEY='9404481bdc5f765cba251e74a71ce15b'
  CURRENT_ENV = os.getenv('CURRENT_ENV', Props.DEV_MODE)

class STG:
  #[App Secrets]
  APP_SECRET_KEY='katch-app-504'
  APP_JWT_SECRET_SEED='s4P3r-s3cr3t_K@tCh-d3V_K3y'
 
  #[Credentials]
  GOOGLE_APPLICATION_CREDENTIALS = './src/db/keys/nrg_staging.json'
  CREDENTIALS_FIREBASE_SDK_PATH = './src/db/keys/nrg_staging.json'
  FIREBASE_WEB_API_KEY='AIzaSyBJM-U6ZGMF2iItNbXbDrds043_LM4htd0'

  #[Firebase]
  KATCH_FIREBASE_DB_URL='https://katch-nrg-staging-106c2.firebaseio.com/'
  KATCH_FIREBASE_SIGNIN_URL='https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
  KATCH_FIREBASE_SIGNUP_URL='https://identitytoolkit.googleapis.com/v1/accounts:signUp'

  #[Utelly]
  KATCH_UTELLY_URL = 'https://10.63.241.73:443/user' if os.getenv('CURRENT_ENV') is not None else 'https://dev-api.utelly.com/phoenix/9/user'
  HEADER_X_APP_KEY='9404481bdc5f765cba251e74a71ce15b'
  CURRENT_ENV = os.getenv('CURRENT_ENV', Props.STG_MODE)
class PRD:
  #[App Secrets]
  APP_SECRET_KEY='katch-app-504'
  APP_JWT_SECRET_SEED='s4P3r-s3cr3t_K@tCh-d3V_K3y'
 
  #[Credentials]
  GOOGLE_APPLICATION_CREDENTIALS = './src/db/keys/nrg_prod.json'
  CREDENTIALS_FIREBASE_SDK_PATH = './src/db/keys/nrg_prod.json'
  FIREBASE_WEB_API_KEY='AIzaSyC97i-0okZvyXzXdX1Wn7-vnBL4JbvB0iQ'

  #[Firebase]
  KATCH_FIREBASE_DB_URL='https://katch-nrg-6b8c7.firebaseio.com/'
  KATCH_FIREBASE_SIGNIN_URL='https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
  KATCH_FIREBASE_SIGNUP_URL='https://identitytoolkit.googleapis.com/v1/accounts:signUp'

  #[Utelly]
  KATCH_UTELLY_URL='https://10.63.242.42:443/user'
  HEADER_X_APP_KEY='9404481bdc5f765cba251e74a71ce15b'
  CURRENT_ENV = Props.PRD_MODE
class Configuration:
  #Here SET Env to LOCAL or DEV to create users in Development, STG for staging and PRD for production
  Env = LOCAL

  #[App Secrets]
  APP_SECRET_KEY = Env.APP_SECRET_KEY
  APP_JWT_SECRET_SEED = Env.APP_JWT_SECRET_SEED
 
  #[Credentials]
  GOOGLE_APPLICATION_CREDENTIALS = Env.GOOGLE_APPLICATION_CREDENTIALS
  CREDENTIALS_FIREBASE_SDK_PATH = Env.CREDENTIALS_FIREBASE_SDK_PATH
  FIREBASE_WEB_API_KEY = Env.FIREBASE_WEB_API_KEY
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

  #[Firebase]
  KATCH_FIREBASE_DB_URL = Env.KATCH_FIREBASE_DB_URL
  KATCH_FIREBASE_SIGNIN_URL = Env.KATCH_FIREBASE_SIGNIN_URL
  KATCH_FIREBASE_SIGNUP_URL = Env.KATCH_FIREBASE_SIGNUP_URL

  #[Utelly]
  KATCH_UTELLY_URL = Env.KATCH_UTELLY_URL
  HEADER_X_APP_KEY = Env.HEADER_X_APP_KEY
  CURRENT_ENV = Env.CURRENT_ENV

  print('ENV {0}'.format(Env))
  print('Current Mode {0}'.format(Env))
  print('UTELLY URL {0}'.format(KATCH_UTELLY_URL))
