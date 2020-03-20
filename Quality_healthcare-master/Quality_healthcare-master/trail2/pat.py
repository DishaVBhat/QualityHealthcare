from flask import Flask, redirect, url_for, request, render_template
import pview as ts
from SaveLoad import Doctor,Patient,Booking

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def doc1():
   return render_template('pat.html',result = ts.final_list)

@app.route('/confirm',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      user_id=request.form.keys()
      t_slot=request.form.values()
      for b in ts.final_list:
          if user_id[0] in b:
              b1=b[-1]
              b1.remove(t_slot[0])
              print(b1)
              print(ts.final_list)
      return render_template('confirm.html')

if __name__ == '__main__':
   app.run(debug = True)

"""if request.method == 'POST':
      result = request.form
      print(type(result))
   if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
"""
"""print(request.form['id'])"""
