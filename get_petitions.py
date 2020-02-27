import requests
from datetime import datetime

# retrieve data
req = requests.get("https://petition.parliament.uk/petitions.csv?state=open")

if req.ok:
    lines = req.text.strip().split('\n')

    if len(lines) > 1:
        # datetime object containing current date and time
        now = datetime.now()

        # save it
        fh = open('data/' + now.strftime("%Y-%m-%d_%H-%M-%S") + '_ukpp.csv', 'w')

        fh.write(req.text)

        fh.close()
