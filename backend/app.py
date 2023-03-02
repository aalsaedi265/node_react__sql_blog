
from flask import Flask,jsonify


#flask object
app = Flask(__name__)

#flask route
@app.route('/', methods = ['GET'])
def get_articles():
    return jsonify({'DIO': 'SCARY MONSTERS'})



#run the application
if __name__ =='__main__':
    app.run(debug=True)