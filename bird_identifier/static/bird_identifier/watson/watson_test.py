import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def request_IBM_resources():
	authenticator = IAMAuthenticator('8VvzgIf3e8WJ_Lh6KlOiPD6KRj1Fm1jCzmjQVIbMNup7')
	visual_recognition = VisualRecognitionV3(
		version='2018-03-19',
		authenticator=authenticator
	)

	visual_recognition.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

	with open('./canadian_goose.jpg', 'rb') as images_file:
		classes = visual_recognition.classify(
			images_file=images_file,
			threshold='0.1',
			owners=["me"]).get_result()
		print(json.dumps(classes, indent=2))
	return json.dumps(classes)

data = request_IBM_resources()
print('----------------')
print(data)
