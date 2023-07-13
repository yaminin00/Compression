import io
import base64
from PIL import Image
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the API
@app.route('/compress', methods=['POST'])
def compress_image():
    try:
        input_data = request.json['file']
        output_format = request.json['format']
        max_size = request.json['size']

        decoded_image_data = base64.b64decode(input_data)

        image = Image.open(io.BytesIO(decoded_image_data))

        if max_size :
            width, height = image.size
            if width > height:
                new_width = max_size
                new_height = int(height * max_size /width)
            else:
                new_height = max_size
                new_width = int(width * max_size / height)

            image = image.resize((new_width, new_height), resample=Image.LANCZOS)

        if output_format.lower() in ('jpeg', 'jpg'):
            output_format = 'JPEG'
            quality = request.json.get('quality', 100)
        elif output_format.lower() in ('tiff', 'tif'):
            output_format = 'TIFF'
            quality = None
        elif output_format.lower() == 'pdf':
            output_format = 'PDF'
            quality = None
        else:
            return jsonify({'error': 'Invalid output format'}), 400
        
        output = io.BytesIO()
        image.save(output, format=output_format, quality=quality)
        compressed_data = output.getvalue()
        compressed_size = len(compressed_data)

        return jsonify({'file': base64.b64encode(compressed_data).decode('utf-8'), 'size': compressed_size}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
