from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return('Hello Elastic Beanstalk! Hello World!')