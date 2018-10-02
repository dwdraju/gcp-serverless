## Examples for Running Python Functions on Google Cloud Functions

* Cloud Functions Python runtime is based on version 3.7.0
* The runtime uses Flask to handle incoming requests
* Your function's entrypoint must be contained in a Python source file named main.py
* Function dependencies must be specified on `requirements.txt` file

#### Deployment
```
gcloud beta functions deploy [FunctionName] --runtime python37 --trigger-http --project [ProjectID]
```
