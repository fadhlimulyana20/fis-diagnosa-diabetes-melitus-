from WebUI import app
from flask import render_template, request

from main import fuzzyInference

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {
        "tds": 0.0,
        "imt": 0.0,
        "kgd": 0.0
    }
    if request.method == "GET": 
        nk = [0,0,0]
        return render_template('index.html', data=data, nk=nk, diagnosis={})
    elif request.method == "POST": 
        data["kgd"] = float(request.form["kgd"])
        data["imt"] = float(request.form["imt"])
        data["tds"] = float(request.form["tds"])

        fi = fuzzyInference(data["tds"], data["imt"], data["kgd"])
        return render_template('index.html', data=data, nk=fi['nk'], diagnosis=fi['diagnosis'])