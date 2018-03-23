from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


def get_relevant_tags(image):
    app = ClarifaiApp(api_key='acf6a2bf11304fc9ba343d0a780b4b8e')

    im = ClImage(file_obj=open(image, 'rb'))
    model = app.models.get('general-v1.3')
    response_data = model.predict([im])
    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        print(concept['name'])
        if concept['name'] == 'car' and concept['value'] >= .20:

            return True

    return False
