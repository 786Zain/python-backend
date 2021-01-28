from flask import Flask
from flask import jsonify
app = Flask(__name__)
# This method executes before any API request
@app.before_request
def before_request():
    print('before API request')
# This method returns students 
# list and by default method will be GET
@app.route('/api/students')
def get_students_list():
    d = calculate()
    # response = app.response_class(
    #     response=jsonify(d),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response
    data={"entry":1423,"id":1763}
    return jsonify(data)
# This is POST method which stores students details.
@app.route('/api/storestudents', methods=['POST'])
def store_student_data():
    return "Student list[POST]"
# This method executes after every API request.
@app.after_request
def after_request(response):
    # response="Request Completed"
    return response

def calculate():
    a=100
    b=100
    c=a+b
    return c