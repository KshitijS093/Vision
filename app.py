from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload and processing here
        # For demonstration, we'll just pass dummy data
        output_without_model = "ಪರಿಶೀಲನೆ ಇಲ್ಲದೆ (Dummy Text)"
        output_with_model = "ಮಾದರಿಯೊಂದಿಗೆ (Dummy Text)"
        return render_template('index.html', output_without_model=output_without_model, output_with_model=output_with_model)
    return render_template('index.html', output_without_model=None, output_with_model=None)

if __name__ == '__main__':
    app.run(debug=True)
