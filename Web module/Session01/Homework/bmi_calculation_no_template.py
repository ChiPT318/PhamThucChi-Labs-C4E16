from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')

def BMI_calc(weight, height):

    BMI = weight / ((height/100)**2)

    if BMI < 16:
        interpretation = "Severely underweight"
    elif 16 <= BMI < 18.5:
        interpretation = "Underweight"
    elif 18.5 <= BMI < 25:
        interpretation = "Normal"
    elif 25 <= BMI < 30:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"


    return '{} {} {}'.format(BMI, "You are", interpretation)
    
if __name__ == '__main__':
  app.run(debug=True)
