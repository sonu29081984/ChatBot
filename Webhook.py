import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):
    # if req.get("result").get("action") != "GetOrderStatus":
    #     return {}
    # result = req.get("result")
    # parameters = result.get("parameters")
    # Brand = parameters.get("Brand")
    # OrderNumber = parameters.get("OrderNumber")
    # url = 'https://cloud.10-4.com/atlas/frexapi/shipment/' + OrderNumber
    # Pass='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJlYjI1NTA4Zi1mNTQwLTRjNDItYjQwNi0zNzMyMDVhZThmOTkiLCJodHRwOi8vMTAtNC5jb20vY2xhaW1zL3VzZXJJZCI6IjIzNTEiLCJpc3MiOiJodHRwczovL2Nsb3VkLjEwLTQuY29tIiwiYXVkIjoiaHR0cHM6Ly9jbG91ZC4xMC00LmNvbSIsImV4cCI6MjE0NzM5NTgxMCwibmJmIjoxNTE2MjQzODEwfQ.YtnGLxWij4sZ-NhAiEVLXgbUXrKZmsKb1uZn_ISH5GU'
    # headers = {
    #     'Authorization': Pass}
    # if OrderNumber is None:
    #     return None
    # r = requests.get(url, headers=headers)
    # json_object = r.json()
    # ShareUrl = json_object['ShareUrl']
    speech = "The Order status can be obtained by clicking the below URL :: " + ShareUrl
    return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-getOrderStatus-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
