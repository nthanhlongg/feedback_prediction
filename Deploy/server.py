from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
# Import libraries

# Initialize the flask class and specify the templates directory
app = Flask(__name__, template_folder = "templates")
model = pickle.load(open('model.pkl', 'rb'))

# Default route set as 'home'
@app.route('/')
def home():
    return render_template('index2.html') # Render home.html

@app.route('/student')
def student():
    return render_template('student.html') # Render student.html

@app.route('/mlmodel')
def mlmodel():
    return render_template('mlmodel.html') # Render mlmodel.html

@app.route('/predict',methods=['POST','GET']) # Render results on HTML    
def predict():
    if request.method == 'POST':
        course = int(request.form['course'])
        lecturer = int(request.form['lecturer'])
        understanding = int(request.form['understanding'])
        expertise = int(request.form['expertise'])
        enthusiastic = int(request.form['enthusiastic'])
        approachable = int(request.form['approachable'])
        satisfaction = int(request.form['satisfaction'])
        features = [course,lecturer,understanding,expertise,enthusiastic,approachable,satisfaction]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = prediction[0]
        if output == 1:
            result = 'Học viên này sẽ tiếp tục học'
        else:
            result = 'Học viên này sẽ dừng học tiếp'
        return render_template('mlmodel.html', prediction_text='{}'.format(result))
    else:
        return render_template('mlmodel.html')

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)        