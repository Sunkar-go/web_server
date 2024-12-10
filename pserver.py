from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def main_template():
    return render_template('index.html')

@app.route('/<string:page_name>')
def temp_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        datas=request.form.to_dict()
        print(datas)
        write_data(datas)
        write_data_csv(datas)
        return redirect('/thankyou.html')
    else: return "Entschuldigung. Something wrong"

def write_data(data):
    with open('database.txt', mode='a') as database:
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n Name: {name},\n Email: {email},\n Subject: {subject},\n Message: {message}')
def write_data_csv(data):
    with open('database.csv', 'a', newline='') as csv_database:
        fieldnames = []
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(csv_database,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])

if __name__=='__main__':
    app.run(debug = True)
