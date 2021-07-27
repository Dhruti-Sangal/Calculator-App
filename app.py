from flask import Flask, render_template, request

#Decalre the app
app = Flask(__name__)

#Start an app route which is '/'
@app.route('/')

#Decalre the main function
def main():
    return render_template('app.html')

#Form Submission Route
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':

        #Start pulling data from from Input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)

