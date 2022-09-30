import requests

getURL = 'http://127.0.0.1:5000/getData'
postURL = 'http://127.0.0.1:5000/addData'
flag = True

Payload = {
    "Contact": "",
    "Name": ""
}

print("Choose method:")
print("[1]GET")
print("[2]POST")

while flag == True:
    method = int(input("Choose appropriate number: "))

    if method == 1:
        flag = False
        response = requests.request("GET", getURL)
        print(response.text)
    elif method == 2:
        flag = False
        cont = input("Contact: ")
        name = input("Name: ")
        Payload["Contact"] = cont
        Payload["Name"] = name
        response = requests.request("POST", postURL, json=Payload)
        print(response.text)
    else:
        print("Error!")
        print("Choose again.")