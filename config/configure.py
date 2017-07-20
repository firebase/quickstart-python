import argparse
import requests

from oauth2client.service_account import ServiceAccountCredentials


PROJECT_ID = '<PROJECT_ID>'
BASE_URL = 'https://www.googleapis.com'
REMOTE_CONFIG_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/remoteConfig'
REMOTE_CONFIG_URL = BASE_URL + '/' + REMOTE_CONFIG_ENDPOINT
REMOTE_CONFIG_SCOPE = 'https://www.googleapis.com/auth/firebase.remoteconfig'


def _get_access_token():
  """Retrieve a valid access token that can be used to authorize requests.

  :return: Access token.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', REMOTE_CONFIG_SCOPE)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token

def _fetch():
  """Fetch the current Firebase Remote Config template from server.

  Fetch the current Firebase Remote Config template from server and store it
  locally.
  """
  headers = {
    'Authorization': 'Bearer ' + _get_access_token()
  }
  resp = requests.get(REMOTE_CONFIG_URL, headers=headers)

  if resp.status_code == 200:
    with open('config.json', 'w') as f:
      f.write(resp.text)

    print('Fetched template has been written to config.json')
    print('ETag from server: {}'.format(resp.headers['X-Google-API-ETag']))
  else:
    print('Unable to fetch template')
    print(resp.text)


def _publish(etag):
  """Publish local template to Firebase server.

  Args:
    etag: ETag for safe (avoid race conditions) template updates.
        * can be used to force template replacement.
  """
  with open('config.json', 'r') as f:
    content = f.read()
  headers = {
    'Authorization': 'Bearer ' + _get_access_token(),
    'Content-Type': 'application/json; UTF-8',
    'If-Match': etag
  }
  resp = requests.put(REMOTE_CONFIG_URL, data=content, headers=headers)
  if resp.status_code == 200:
    print('Template has been published.')
    print('ETag from server: {}'.format(resp.headers['X-Google-API-ETag']))
  else:
    print('Unable to publish template.')
    print(resp.text)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--action')
  parser.add_argument('--etag')
  args = parser.parse_args()

  if args.action and args.action == 'fetch':
    _fetch()
  elif args.action and args.action == 'publish' and args.etag:
    _publish(args.etag)
  else:
    print('''Invalid command. Please use one of the following commands:
python configure.py --action=fetch
python configure.py --action=publish --etag=<LATEST_ETAG>''')



if __name__ == '__main__':
  main()
