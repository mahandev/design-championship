from os import name
from flask import Flask, render_template, url_for, request
import requests
app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("home.html")

@app.route("/funfacts")
def funfacts():
    return render_template("funfacts.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/bot")
def bot():
    return render_template("bot.html")

@app.route("/stats", methods=['POST', 'GET'])
def stats():
    death = "enter country name to get this stastics"
    confirmed = "enter country name to get this stastics"
    nameofcountry = "enter country name to get this stastics"
    updatedat = "enter country name to get this stastics"
    deathrate = "enter country name to get this stastics"
    recoveryrate = "enter country name to get this stastics"
    totaldeath = "enter country name to get this stastics"
    totalrecovered = "enter country name to get this stastics"
    if request.method == "POST":
        countrycode = request.form.get('countrytogetstatsfrom')
        print(countrycode)
        url = f"https://corona-api.com/countries/{countrycode}"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.json()["data"])
        death = response.json()["data"]['today']['deaths']
        confirmed = response.json()["data"]['today']['confirmed']
        nameofcountry = response.json()["data"]['name']
        updatedat = response.json()['data']['updated_at']
        deathrate = str(response.json()['data']['latest_data']['calculated']['death_rate'])[:5].strip()
        recoveryrate = str(response.json()['data']['latest_data']['calculated']['recovery_rate'])[:5].strip()
        totaldeath = response.json()['data']['latest_data']['deaths']
        totalrecovered = response.json()['data']['latest_data']['recovered']


    return render_template("stats.html", death=death, confirmed=confirmed, countryname=nameofcountry, dateofupdation=updatedat, deathrate=deathrate, recoveryrate=recoveryrate,totaldeath=totaldeath, totalrecovered=totalrecovered)

if __name__ == "__main__":
	app.run(debug=True)