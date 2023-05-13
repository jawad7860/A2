from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


# Homepage route
@app.route('/')
def home():

    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])

def predict():
    
    loaded_model = joblib.load('model1.pkl')

    open_price = float(request.form['open'])
    high_price = float(request.form['high'])
    low_price = float(request.form['low'])
    volume = float(request.form['volume'])
    
  
    

    
    # Make prediction
    new_features = [[open_price, high_price, low_price, volume]]
    predicted_price = loaded_model.predict(new_features)
    
    return render_template('index.html', prediction='Predicted Price: {}'.format(predicted_price[0]))


if __name__ == '__main__':
    app.run(debug=True)

    # Get form data
