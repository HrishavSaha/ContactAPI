from flask import Flask, request, jsonify

app = Flask(__name__)

Contacts = [
    {
        "ID":1,
        "Contact":"223",
        "Name":"Ravi",
        "Done":False
    },
    {
        "ID":2,
        "Contact":"665",
        "Name":"Rahul",
        "Done":False
    }
]

@app.route("/addData", methods=["POST"])
def addContact():
    if not request.json:
        return jsonify({
            "status":"Error",
            "Message":"Please provide data"
        }, 400)
    else:
        contact = {
            "ID":Contacts[-1]["ID"] + 1,
            "Contact":request.json["Contact"],
            "Name":request.json["Name"],
            "Done":False
        }

        Contacts.append(contact)
        return jsonify({
            "status": "success!",
            "Message": "Task was added successfully"
        })

@app.route("/getData")
def getTask():
    return jsonify({
        "data": Contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)