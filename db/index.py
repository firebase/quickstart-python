import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def authenticate_with_admin_privileges():
    # [START authenticate_with_admin_privileges]
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('path/to/serviceAccountKey.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://databaseName.firebaseio.com'
    })

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('restricted_access/secret_document')
    print(ref.get())
    # [END authenticate_with_admin_privileges]
    firebase_admin.delete_app(firebase_admin.get_app())

def authenticate_with_limited_privileges():
    # [START authenticate_with_limited_privileges]
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('path/to/serviceAccountKey.json')

    # Initialize the app with a custom auth variable, limiting the server's access
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://databaseName.firebaseio.com',
        'databaseAuthVariableOverride': {
            'uid': 'my-service-worker'
        }
    })

    # The app only has access as defined in the Security Rules
    ref = db.reference('/some_resource')
    print(ref.get())
    # [END authenticate_with_limited_privileges]
    firebase_admin.delete_app(firebase_admin.get_app())

def authenticate_with_guest_privileges():
    # [START authenticate_with_guest_privileges]
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('path/to/serviceAccountKey.json')

    # Initialize the app with a None auth variable, limiting the server's access
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://databaseName.firebaseio.com',
        'databaseAuthVariableOverride': None
    })

    # The app only has access to public data as defined in the Security Rules
    ref = db.reference('/some_resource')
    print(ref.get())
    # [END authenticate_with_guest_privileges]
    firebase_admin.delete_app(firebase_admin.get_app())

def get_reference():
    # [START get_reference]
    # Get a database reference to our blog.
    ref = db.reference('server/saving-data/fireblog')
    # [END get_reference]
    print(ref.key)

def set_value():
    ref = db.reference('server/saving-data/fireblog')

    # [START set_value]
    users_ref = ref.child('users')
    users_ref.set({
        'alanisawesome': {
            'date_of_birth': 'June 23, 1912',
            'full_name': 'Alan Turing'
        },
        'gracehop': {
            'date_of_birth': 'December 9, 1906',
            'full_name': 'Grace Hopper'
        }
    })
    # [END set_value]

def set_child_value():
    ref = db.reference('server/saving-data/fireblog')
    users_ref = ref.child('users')

    # [START set_child_value]
    users_ref.child('alanisawesome').set({
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    })
    users_ref.child('gracehop').set({
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    })
    # [END set_child_value]

def update_child():
    ref = db.reference('server/saving-data/fireblog')
    users_ref = ref.child('users')

    # [START update_child]
    hopper_ref = users_ref.child('gracehop')
    hopper_ref.update({
        'nickname': 'Amazing Grace'
    })
    # [END update_child]

def update_children():
    ref = db.reference('server/saving-data/fireblog')
    users_ref = ref.child('users')

    # [START update_children]
    users_ref.update({
        'alanisawesome/nickname': 'Alan The Machine',
        'gracehop/nickname': 'Amazing Grace'
    })
    # [END update_children]

def overwrite_value():
    ref = db.reference('server/saving-data/fireblog')
    users_ref = ref.child('users')

    # [START overwrite_value]
    users_ref.update({
        'alanisawesome': {
            'nickname': 'Alan The Machine'
        },
        'gracehop': {
            'nickname': 'Amazing Grace'
        }
    })
    # [END overwrite_value]

def push_value():
    ref = db.reference('server/saving-data/fireblog')

    # [START push_value]
    posts_ref = ref.child('posts')

    new_post_ref = posts_ref.push()
    new_post_ref.set({
        'author': 'gracehop',
        'title': 'Announcing COBOL, a New Programming Language'
    })

    # We can also chain the two calls together
    posts_ref.push().set({
        'author': 'alanisawesome',
        'title': 'The Turing Machine'
    })
    # [END push_value]

def push_and_set_value():
    ref = db.reference('server/saving-data/fireblog')
    posts_ref = ref.child('posts')

    # [START push_and_set_value]
    # This is equivalent to the calls to push().set(...) above
    posts_ref.push({
        'author': 'gracehop',
        'title': 'Announcing COBOL, a New Programming Language'
    })
    # [END push_and_set_value]

def get_push_key():
    ref = db.reference('server/saving-data/fireblog')
    posts_ref = ref.child('posts')

    # [START push_key]
    # Generate a reference to a new location and add some data using push()
    new_post_ref = posts_ref.push()

    # Get the unique key generated by push()
    post_id = new_post_ref.key
    # [END push_key]
    print(post_id)


service_account = '/usr/local/google/home/hkj/Projects/firebase-admin-python/public/scripts/cert.json'
database_url = 'https://admin-java-integration.firebaseio.com'

cred = credentials.Certificate(service_account)
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})

get_reference()
set_value()
set_child_value()
update_child()
update_children()
overwrite_value()
push_value()
push_and_set_value()
get_push_key()

firebase_admin.delete_app(firebase_admin.get_app())