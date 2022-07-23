import time
from urllib import response
import requests

def edit_script(img,bg_color):
    response =requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file':open(img,'rb')},
        data={'size':'auto','bg_color':bg_color},
        headers={'X-Api-Key': 'hx9X8hMcUNRuHwpFYkbTUwLc'}
    )

    if response.status_code == requests.codes.ok:
        output = 'output/'+str(time.time())+'.png'
        with open(output,'wb')as out:
            out.write(response.content)
            print('Check in :'+output)
    else:
        print('Error :',response.text)

edit_script('Images/pekora.png','blue')