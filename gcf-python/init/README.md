### Deployment
```
gcloud beta functions deploy getTodo --runtime python37 --trigger-http --project [ProjectID]
```

### HTTPSTrigger/Browse URL:
```
https://[region]-[projectID].cloudfunctions.net/getTodo
```

### Expected Output
```
{
  "completed": false, 
  "id": 1, 
  "title": "delectus aut autem", 
  "userId": 1
}
```
