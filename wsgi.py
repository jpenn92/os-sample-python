from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    #return "Oh hai Mark!"
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
    

    
