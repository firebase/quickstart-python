# Firebase Admin Python SDK ML quickstart

This sample script shows how you can use the Firebase Admin SDK to manage your
Firebase-hosted ML models.

Also see the [Firebase ML API Tutorial Colab/Jupyter notebook][colab].

[colab]: https://colab.research.google.com/github/firebase/quickstart-python/blob/master/machine-learning/Firebase_ML_API_Tutorial.ipynb

## Setup

1.  Install the Admin SDK (probably in a virtual environment):

    ```
    $ pip install -U pip setuptools
    $ pip install firebase_admin
    ```

2.  Clone the quickstart repository and change to the `machine-learning`
    directory:

    ```
    $ git clone https://github.com/firebase/quickstart-python.git
    $ cd quickstart-python/machine-learning
    $ chmod u+x manage-ml.py  # Optional
    ```

3.  If you don't already have a Firebase project, create a new project in the
    [Firebase console](https://console.firebase.google.com/). Then, open your
    project in the Firebase console and do the following:

    1.  On the [Settings][service-account] page, create a service account and
        download the service account key file. Keep this file safe, since it
        grants administrator access to your project.
    2.  On the Storage page, enable Cloud Storage. Take note of your default
        bucket name (or create a new bucket for ML models.)
    3.  On the ML Kit page, click **Get started** if you haven't yet enabled ML
        Kit.

4.  In the [Google APIs console][enable-api], open your Firebase project and
    enable the Firebase ML API.

[enable-api]: https://console.developers.google.com/apis/library/firebaseml.googleapis.com?project=_

5.  At the top of `manage-ml.py`, set the `SERVICE_ACCOUNT_KEY` and
    `STORAGE_BUCKET`:

    ```
    SERVICE_ACCOUNT_KEY = '/path/to/your/service_account_key.json'
    STORAGE_BUCKET = 'your-storage-bucket'
    ```

[service-account]: https://firebase.google.com/project/_/settings/serviceaccounts/adminsdk

## Example session

```
$ ./manage-ml.py list
fish_detector    8716935   vision
barcode_scanner  8716959   vision
smart_reply      8716981   natural_language
$ ./manage-ml.py new ~/yak.tflite yak_detector --tags vision,experimental
Uploading model to Cloud Storage...
Model uploaded and published:
yak_detector     8717019   experimental, vision
$ ./manage-ml.py update 8717019 --remove_tags experimental
$ ./manage-ml.py delete 8716959
$ ./manage-ml.py list
fish_detector    8716935   vision
smart_reply      8716981   natural_language
yak_detector     8717019   vision
$
```
