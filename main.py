from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def Heloo_world():
  return render_template('home.html')

if __name__ == "__main__":
  #print('I am inside the if now')
  app.run(host = '0.0.0.0', debug = True)
