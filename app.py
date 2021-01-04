from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
@app.route("/")
def home():
    return "Api Working"
    

@app.route('/id',methods=['GET','POST'])
def id():
    w = request.args.get('user')
    a = "https://telegram.dog/"+(w)
    res= requests.get(a).content
    soup = bs(res,'html')
    dp = soup.find("img",class_="tgme_page_photo_image")['src']
    #description = soup.find("div",class_="tgme_page_description").text
    channel_name = soup.find("div", class_="tgme_page_title").text.replace("\n","")
    User = soup.find("div", class_="tgme_page_extra").text
    return render_template("main.html",dp=dp,channel_name=channel_name,User=User)


if __name__ == "__main__":
    app.run()