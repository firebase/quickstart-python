# Firebase Admin Python SDK ML quickstart

This sample script shows how you can use the Firebase Admin SDK to manage your
Firebase-hosted ML models.

Also see the [Firebase ML API Tutorial Colab/Jupyter notebook][colab].

[colab]: https://colab.research.google.com/github/firebase/quickstart-python/blob/master/machine-learning/Firebase_ML_API_Tutorial.ipynb

## Setup

1.  Install the Admin SDK and other dependencies (probably in a virtual
    environment):

    ```
    $ pip install -U pip setuptools
    $ pip install -r requirements.txt
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
         Name              ID            Tags
---------------------- ---------- ------------------
 fish_recognizer        12990533   vision
 barcode_scanner        12990544   vision
$ ./manage-ml.py new yak_detector -f model.tflite -t vision,experimental
Uploading to Cloud Storage...
Model uploaded and published:
 yak_detector   12990577   experimental, vision
$ ./manage-ml.py new flower_classifier -a projects/12345/locations/us-central1/models/ICN12345
Model uploaded and published:
 flower_classifier   12990597
$ ./manage-ml.py list
         Name              ID              Tags
---------------------- ---------- ----------------------
 fish_recognizer        12990533   vision
 barcode_scanner        12990544   vision
 yak_detector           12990577   experimental, vision
 flower_classifier      12990597
$ ./manage-ml.py update 12990577 --remove_tags experimental
$ ./manage-ml.py delete 12990544
$ ./manage-ml.py list
         Name              ID            Tags
---------------------- ---------- ------------------
 fish_recognizer        12990533   vision
 yak_detector           12990577   vision
 flower_classifier      12990597
$
```
