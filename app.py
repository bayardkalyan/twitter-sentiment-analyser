from flask import Flask, render_template, request
from main import SentimentAnalysis
from form import getData
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
sa=SentimentAnalysis()

@app.route('/')
def index():
    form=getData()
    return render_template('m.html',form=form)

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        #Parse form data  
        getData.topic = request.form['topic']
        getData.count = request.form['count']
        sa.DownloadData()
        return render_template('m.html')

if __name__ == "__main__":
    app.run(debug=True)