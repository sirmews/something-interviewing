import base64
from io import BytesIO

from flask import Flask, render_template, request, send_file
from question_generator import generate_questions_from_description
from social_media_images import SOCIAL_MEDIA_SIZES

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    # Get list of requirements from the form
    requirements_list = request.form.getlist('requirements[]')
    
    # Initiate an empty list to store all questions
    all_questions = []

    # Loop through each requirement and generate questions
    for requirement in requirements_list:
        questions_for_requirement = generate_questions_from_description(requirement)
        all_questions.extend(questions_for_requirement)

    return render_template('questions.html', questions=all_questions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
