import requests
from datetime import datetime

# retrieve data
req = requests.get("https://petition.parliament.uk/petitions.csv?state=open")
data_path = "/home/pi/Documents/uk_parliament_petitions/"

if req.ok:
    lines = req.text.strip().split('\n')

    print("Found ", len(lines), " lines.")

    if len(lines) > 1:
        # datetime object containing current date and time
        now = datetime.now()

        # save it
        fh = open(data_path + 'data/' + now.strftime("%Y-%m-%d_%H-%M-%S") + '_ukpp.csv', 'w')

        fh.write(req.text)

        fh.close()
