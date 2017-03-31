import sys
sys.path.append("lib")

# [START import_sdk]
import firebase_admin
# [END import_sdk]
from firebase_admin import credentials
from firebase_admin import auth

def initialize_sdk_with_service_account():
    # [START initialize_sdk_with_service_account]
    import firebase_admin
    from firebase_admin import credentials

    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [END initialize_sdk_with_service_account]
    firebase_admin.delete_app(default_app)

def initialize_sdk_with_application_default():
    # [START initialize_sdk_with_application_default]
    default_app = firebase_admin.initialize_app()
    # [END initialize_sdk_with_application_default]
    firebase_admin.delete_app(default_app)

def initialize_sdk_with_refresh_token():
    # [START initialize_sdk_with_refresh_token]
    cred = credentials.RefreshToken('path/to/refreshToken.json')
    default_app = firebase_admin.initialize_app(cred)
    # [END initialize_sdk_with_refresh_token]
    firebase_admin.delete_app(default_app)

def access_services_default():
    cred = credentials.Certificate('path/to/service.json')
    # [START access_services_default]
    # Import the Firebase service
    from firebase_admin import auth

    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)
    print(default_app.name);  # "[DEFAULT]"

    # Retrieve services via the auth package...
    # auth.create_custom_token(...)
    # [END access_services_default]
    firebase_admin.delete_app(default_app)

def access_services_nondefault():
    cred = credentials.Certificate('path/to/service.json')
    otherCred = credentials.Certificate('path/to/service.json')

    # [START access_services_nondefault]
    # Initialize the default app
    default_app = firebase_admin.initialize_app(cred)

    #  Initialize another app with a different config
    other_app = firebase_admin.initialize_app(cred, name='other')

    print(default_app.name);    # "[DEFAULT]"
    print(other_app.name);      # "other"

    # Retrieve default services via the auth package...
    # auth.create_custom_token(...)

    # Use the `app` argument to retrieve the other app's services
    # auth.create_custom_token(..., app=other_app)
    # [END access_services_nondefault]
    firebase_admin.delete_app(default_app)
    firebase_admin.delete_app(other_app)

def create_token_uid():
    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [START create_token_uid]
    uid = 'some-uid'

    customToken = auth.create_custom_token(uid)
    # [END create_token_uid]
    firebase_admin.delete_app(default_app)
    return customToken

def create_token_with_claims():
    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [START create_token_with_claims]
    uid = 'some-uid'
    additional_claims = {
      "premiumAccount": True
    }

    custom_token = auth.create_custom_token(uid, additional_claims)
    # [END create_token_with_claims]
    firebase_admin.delete_app(default_app)
    return custom_token

def verify_token_uid(id_token):
    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [START verify_token_uid]
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token.uid
    # [END verify_token_uid]
    print(uid)
    firebase_admin.delete_app(default_app)

initialize_sdk_with_service_account()
initialize_sdk_with_application_default()
#initialize_sdk_with_refresh_token()
access_services_default()
access_services_nondefault()
create_token_uid()
token_with_claims = create_token_with_claims()
#verify_token_uid()
