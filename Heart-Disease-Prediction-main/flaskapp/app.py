# To run D:\Heart-Disease-Prediction-main\flaskapp> python -m flask run
from flask import Flask, render_template,request
from api_routes import bp1

app = Flask(__name__)

app.register_blueprint(bp1)

@app.route('/pre')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
def log():
    if request.method == 'POST':

            usernames = request.form['username']
            passwords = request.form['password']

            if usernames != 'admin' or passwords != '@6789':
                return render_template('log.html', prediction_text="Please Enter a Valid Username And Password")

            else:
                return render_template('home.html')
    return render_template('log.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feed():
    return render_template('feedback.html')

@app.route('/req')
def req():
    return render_template('req.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/feedbackk',methods=['GET', 'POST'])
def feedbackk():
    from xlrd import open_workbook
    from xlutils.copy import copy
    import xlwt
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        comment = request.form['comment']

    rexcel = open_workbook("feedback.xls",formatting_info=True) #  Keep original style
#  The number provided by XLRD has obtained the number of rows now
    rows = rexcel.sheets()[0].nrows 
#  Use the Copy method provided by XLUTILS to translate XLRD objects to XLWT objects
    excel = copy(rexcel) 
#  Get the Sheet to operate with XLWT objec
    table = excel.get_sheet(0) 
    values = [name]
    valuess = [email]
    valuesss = [contact]
    valuessss = [comment]

# values1 = ['name', 'email', 'contact', 'comment']
    row = rows
    header_style = xlwt.XFStyle()
    for value in values:
          table.write(row, 0, value)
    
    for value in valuess:
          table.write(row, 1, value)
     
    for value in valuesss:
          table.write(row, 2, value)
    
    for value in valuessss:
          table.write(row, 3, value)
          row +=1


    excel.save("feedback.xls")    
    return render_template('feedback.html')

if __name__ == "__main__":

    app.run(debug=False)
