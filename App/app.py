import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request




app=Flask(__name__)





@app.route('/', methods = ['GET', 'POST'])
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list,data_list):
    print(to_predict_list)
    to_predict = np.array(to_predict_list[0:11]).reshape(1,11)
    if(int(to_predict_list[-1])==0):
        data_list[-1] = 'Red'
        loaded_red_wine_model = pickle.load(open("model_red_wine.pkl",
        "rb"))
        result = loaded_red_wine_model.predict(to_predict)
        return result[0], data_list
    else:
        data_list[-1] = 'White'
        loaded_white_wine_model = pickle.load(open("model_white_wine.pkl","rb"))
        result = loaded_white_wine_model.predict(to_predict)
        return result[0], data_list

    


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        data_list = to_predict_list
        # print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        # print(to_predict_list)
        result, data_list = ValuePredictor(to_predict_list, data_list)
        # result="success"
        prediction=str(result)
        return render_template("result.html",prediction=prediction, data = data_list, length = int(result))

@app.route('/home')
def back():
    return render_template("index.html")

if __name__ == '__main__':
    # app.run(debug = True)
    app.DEBUG = True
    app.run()