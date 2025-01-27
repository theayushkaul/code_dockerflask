from flask import Flask, request, render_template

app = Flask(__name__)
#abcd
@app.route('/')
def upload_form():
    return render_template('upload.html')  # Ensure the above HTML form is saved as 'upload.html'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csvFile' not in request.files:
        return "No file part", 400
    file = request.files['csvFile']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.csv'):
        # Save the file or process it
        file.save(f"./uploads/{file.filename}")  # Save to 'uploads' folder
        return f"File '{file.filename}' uploaded successfully!"
    else:
        return "Invalid file type. Please upload a CSV file.", 400

if __name__ == '__main__':
    app.run()
