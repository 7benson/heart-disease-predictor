
#import Flask
from flask import Flask, render_template,request
from os import path, walk
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler,RobustScaler,MinMaxScaler
import scipy.stats as stat
import pylab
from preprocessing import scale_test_point 

pd.pandas.set_option('display.max_columns',None)

#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #get form data
        age = request.form.get('age')
        sex = request.form.get('sex')
        chest_pain = request.form.get('chest_pain')
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        fbs = request.form.get('fbs')
        restecg = request.form.get('restecg')
        thalach = request.form.get('thalach')
        exang = request.form.get('exang')
        oldpeak = request.form.get('oldpeak')
        slope = request.form.get('slope')
        ca = request.form.get('ca')
        thal = request.form.get('thal')

        print('age : ',age)
        print('sex : ',sex)
        print('chest_pain : ',chest_pain)
        print('trestbps : ',trestbps)
        print('chol : ',chol)
        print('fbs : ',fbs)
        print('restecg : ',restecg)
        print('thalach : ',thalach)
        print('exang : ',exang)
        print('oldpeak : ',oldpeak)
        print('slope : ',slope)
        print('ca : ',ca)
        print('thal : ',thal)

        if sex.lower()=='m':
            sex=1
        else:
            sex=0

        test_point=[float(age),float(sex),float(chest_pain),float(trestbps),float(chol),float(fbs),float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]

        print(test_point)

        prediction=scale_test_point(test_point)
        print(prediction)
        if(prediction[0]==0):
            return render_template('predict.html',
                                    main_heading='You are Healthy',
                                    sub_heading="Please Note that the results are based upon Artificial Intelligence",
                                    go_back=True
                                   )
        else:
            return render_template('predict.html',
                                    main_heading='We Recommend you to Consult a Doctor',
                                    sub_heading="There's a high chance that you are diagnosed with a heart Disease. We Suggest you to consult a doctor to make sure of your Health Condition. Please Note that the results are based upon Artificial Intelligence",
                                    go_back=False
                                    )

extra_dirs = ['./static/styles','./templates']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)

if __name__ == '__main__':
    app.run(debug=True,extra_files=extra_files)