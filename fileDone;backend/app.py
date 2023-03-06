
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime


#flask object
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:C.attano1!@127.0.0.1/reactFlaskBlog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



def create_app():
    app = Flask(__name__)

    with app.app_context():
        db.init_app(app)

    return app



class Articles(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    date = db.Column(db.DateTime, default = datetime.datetime.now)


    def __init__(self,title, body, date):
        self.title = title
        self.body = body
        
        

#flask route
@app.route('/', methods = ['GET'])
def get_articles():
    return jsonify({'DIO': 'SCARY MONSTERS'})



#run the application
if __name__ =='__main__':
    app.run(debug=True)