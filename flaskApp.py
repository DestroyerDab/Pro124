from flask import Flask, jsonify, request

app = Flask(__name__)

contactList = [
     {
        'id': 1,
        'Name': u'1',
        'Contact': u'111', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'2',
        'Contact': u'222', 
        'done': False
    },
    {
        'id': 3,
        'Name': u'3',
        'Contact': u'333', 
        'done': False
    },
    {
        'id': 4,
        'Name': u'4',
        'Contact': u'444', 
        'done': False
    },
]

@app.route("/") 
def Homepage():
    return "Welcome to my contacts... :)"

@app.route("/add-data", methods = ["POST"] )
def add_task():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message": "Please provide the contact info!"
        },400)

    contacts = {
        'id': contactList[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contactList.append(contacts)
    return jsonify({
        "status":"SUCCESS",
        "message": "Your contact has been added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contactList
    }) 

if (__name__ == "__main__"):
    app.run(debug = True)