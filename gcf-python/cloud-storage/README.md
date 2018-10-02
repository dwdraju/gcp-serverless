## Accessing Google Cloud Storage Buckets for Cloud Functions
* Grant Bucket access permission to Google Cloud Functions service account from IAM

#### Deployment
```
gcloud beta functions deploy storage --runtime python37 --trigger-http --project [projectID]
```

#### Browse
```
https://[Region]-[projectID].cloudfunctions.net/storage
```

#### View Logs
```
gcloud functions logs read storage
```
