from flask import Flask
from flask import request
from save_records  import CollectLatLongDetails

app = Flask(__name__)
CollectLatLongDetails.create('',1000)
@app.route('/VacationPlanner', methods=['POST'])
def save_record():
    result = CollectLatLongDetails.save(request.data)
    return result
