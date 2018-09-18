from google.cloud import storage
client = storage.Client()
def storage(request):
	global client
	try:
		bucket = client.get_bucket('gcf-test')
		blob = bucket.get_blob('requirements.txt')
		print(blob.download_as_string())
		#blob.upload_from_string('New contents!')
	except google.cloud.exceptions.NotFound:
		print('Sorry, that bucket does not exist!')
	for bucket_list in client.list_buckets():
		print(bucket_list)
	return "Bucket list checked"
