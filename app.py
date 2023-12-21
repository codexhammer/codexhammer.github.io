from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Assuming you want to retrieve form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Do something with the form data (e.g., save to a database)
        # For this example, let's print the data
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)