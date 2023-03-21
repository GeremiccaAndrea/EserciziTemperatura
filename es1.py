from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') 
def ciao():
  return render_template("home.html")

@app.route('/home') 
def benvenuto():
    temperatura = float(request.args.get('temperatura'))
    return render_template("home.html")
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)