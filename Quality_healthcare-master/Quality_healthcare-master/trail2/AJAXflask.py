from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('FinalAJAX.html')

@app.route('/process',methods= ['POST'])
def process():
    Info = (request.form['info']).lstrip()
    print("string:"+Info)
    output = Info+"/red/blue/"
    if Info:
       print(output)
       return jsonify({'output': output})
    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run(debug=True)
