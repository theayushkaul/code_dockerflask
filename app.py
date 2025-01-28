from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    # Extract chunk metadata
    chunk = request.files['chunk']
    filename = request.form['filename']
    chunk_index = int(request.form['chunkIndex'])
    total_chunks = int(request.form['totalChunks'])
    
    # Path to save the chunked file
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Append the chunk to the file
    with open(file_path, 'ab') as f:
        f.write(chunk.read())
    
    # Return a response for each chunk
    if chunk_index + 1 == total_chunks:
        return jsonify({'message': f"File '{filename}' uploaded successfully!"}), 200
    else:
        return jsonify({'message': f"Chunk {chunk_index + 1}/{total_chunks} uploaded successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)