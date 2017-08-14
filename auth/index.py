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

    cred = credentials.Certificate('path/to/serviceAccountKey.json')
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

    custom_token = auth.create_custom_token(uid)
    # [END create_token_uid]
    firebase_admin.delete_app(default_app)
    return custom_token

def create_token_with_claims():
    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [START create_token_with_claims]
    uid = 'some-uid'
    additional_claims = {
      'premiumAccount': True
    }

    custom_token = auth.create_custom_token(uid, additional_claims)
    # [END create_token_with_claims]
    firebase_admin.delete_app(default_app)
    return custom_token

def verify_token_uid(id_token):
    cred = credentials.Certificate('path/to/service.json')
    default_app = firebase_admin.initialize_app(cred)
    # [START verify_token_uid]
    # id_token comes from the client app (shown above)
    
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    # [END verify_token_uid]
    print(uid)
    firebase_admin.delete_app(default_app)

def get_user(uid):
    # [START get_user]
    from firebase_admin import auth

    user = auth.get_user(uid)
    print 'Successfully fetched user data: {0}'.format(user.uid)
    # [END get_user]

def get_user_by_email():
    email = 'user@example.com'
    # [START get_user_by_email]
    from firebase_admin import auth

    user = auth.get_user_by_email(email)
    print 'Successfully fetched user data: {0}'.format(user.uid)
    # [END get_user_by_email]

def get_user_by_phone_number():
    phone = '+1 555 555 0100'
    # [START get_user_by_phone]
    from firebase_admin import auth

    user = auth.get_user_by_phone_number(phone)
    print 'Successfully fetched user data: {0}'.format(user.uid)
    # [END get_user_by_phone]

def create_user():
    # [START create_user]
    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
    print 'Sucessfully created new user: {0}'.format(user.uid)
    # [END create_user]
    return user.uid

def create_user_with_id():
    # [START create_user_with_id]
    user = auth.create_user(
        uid='some-uid', email='user@example.com', phone_number='+15555550100')
    print 'Sucessfully created new user: {0}'.format(user.uid)
    # [END create_user_with_id]

def update_user(uid):
    # [START update_user]
    user = auth.update_user(
        uid,
        email='user@example.com',
        phone_number='+15555550100',
        email_verified=True,
        password='newPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=True)
    print 'Sucessfully updated user: {0}'.format(user.uid)
    # [END update_user]

def delete_user(uid):
    # [START delete_user]
    auth.delete_user(uid)
    print 'Successfully deleted user'
    # [END delete_user]


initialize_sdk_with_service_account()
initialize_sdk_with_application_default()
#initialize_sdk_with_refresh_token()
access_services_default()
access_services_nondefault()
create_token_uid()
token_with_claims = create_token_with_claims()
#verify_token_uid()

uid = create_user()
create_user_with_id()
get_user(uid)
get_user_by_email()
get_user_by_phone_number()
update_user(uid)
delete_user(uid)
