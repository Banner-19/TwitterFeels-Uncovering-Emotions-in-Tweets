from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob,Word
import random
import time

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse',methods=['POST'])
def analyse():
    start=time.time()
    if request.method=='POST':
        rawtext=request.form['rawtext']
        blob=TextBlob(rawtext)
        received_text=blob
        blob_sentiment,blob_subjectivity=blob.sentiment.polarity,blob.sentiment.subjectivity
        number_of_tokens=len(list(blob.words))
        noun=[]
        for w,t in blob.tags:
            if t=='NN':
                noun.append(w.lemmatize())
                len_w=len(noun)
                rand_w=random.sample(noun,len(noun))
                final_w=[]
                for i in rand_w:
                    w=Word(i).pluralize()
                    final_w.append(w)
                    summary=final_w
                    end=time.time()
                    final_time=end-start
    return render_template('index.html',received_text=received_text,number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary,final_time=final_time)

if __name__ == '__main__':
	app.run(debug=True)