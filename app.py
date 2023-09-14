from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

@app.route("/")  ##Route   ##if nothing is given then it will be get method by default
def hello_world():
    return render_template("index.html")

@app.route("/aboutus")
def about_us():
    return "we are ineuron"

@app.route('/demo',methods=['POST'])   ##To run this post method there is different process we have to use the postman..it is used to test the API
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return "The operation is {} and the result is {}".format(operation ,result)

@app.route('/operation',methods=['POST'])   ##To run this post method there is different process we have to use the postman..it is used to test the API
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return render_template("result.html",result=result)

  ##To run this post method there is different process we have to use the postman..it is used to test the API           ## for different different route function name must be different otherwise it will show error

@app.route("/home")
def homepage():
    return "<h1>welcome to ineuron<h1>"   

##To run this post method there is different process we have to use the postman..it is used to test the API




if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)