from flask import Flask, request, render_template
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

# Initialize the Translator
translator = Translator()


@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""

    if request.method == 'POST':
        # Get text and target language from the form
        original_text = request.form['text']
        target_language = request.form['language']

        if original_text and target_language:
            try:
                # Perform the translation
                translation = translator.translate(original_text, dest=target_language)
                translated_text = translation.text
            except Exception as e:
                translated_text = f"Error: {str(e)}"

    # Pass available languages and translation result to the template
    languages = {code: name.title() for code, name in LANGUAGES.items()}
    return render_template('index.html', languages=languages, translated_text=translated_text,
                           original_text=original_text)


if __name__ == '__main__':
    app.run(debug=True)
