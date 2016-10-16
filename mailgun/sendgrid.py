#from sendgrid import SendGridAPIClient
import sendgridapi

import requests
import json
from pprint import pprint
import uuid

#sg = SendGridAPIClient(apikey=sendgridapi.API_KEY)
headers = {
    'Authorization': 'Bearer ' + sendgridapi.API_KEY,
    'content-type': 'application/json'
}
# Murugan.Rajendran@in.tesco.com


def get_data():
    iframe = '<img src="http://www.google-analytics.com/collect?v=1&tid=UA-85798804-1&cid=' + str(uuid.uuid4()) + '&t=event&ec=email&ea=open&el=xyz&cn=hello&cm=email" />'
    data = {
        "personalizations":[
            {
                "to":[
                    {
                        "email": "nitt.murugan@gmail.com"
                    }
                ]
            }
        ],
        "from": {
            "email": "nitt.murugan@gmail.com"
        },
        "subject":"Test mail analytics",
        "content":[
            {"type":"text/html","value":"<html><body><h1>Heading</h1><p>Para<p>" + iframe + "</body></html>"}
        ]
    }
    return data

# response = sg.client.mail.send.post(request_body=data)
for x in xrange(5):
    response = requests.post("https://api.sendgrid.com/v3/mail/send", headers=headers, data=json.dumps(get_data()))
    print(response.status_code)
    pprint(response)
#print(response.body)
#print(response.headers)
