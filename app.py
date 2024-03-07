from flask import Flask, render_template, request
import logging
app = Flask(__name__)

# Suppress INFO level messages from Flask
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)


# ROUTE TO GENERATE THE FORM
@app.route('/')
def hello_form():
  return render_template('index.html')


# ROUTE TO PROCESS THE FORM
@app.route('/thank_you', methods=['POST'])
def handle_form():
  # GET THE FORM VALUE
    if request.method == 'POST':
        f = {}
        f["noun"] = request.form.get('noun')
        f["adjective"] = request.form.get('adjective')
        f["color"] = request.form.get('color')
        f["place"] = request.form.get('place')
        f["animal"] = str(request.form.getlist('animal')[0])
        return render_template('submitted.html', form=f)

app.debug = True
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)