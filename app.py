from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#rb - readbytes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distancia]])
    output = round(prediction[0], 2)

    return render_template('index.html', text_prediction=f'The house with {rooms} rooms and located at {distance} km² has a value of ${output}K dollars')

if __name__=='__main__':
    app.run(debug=True)
