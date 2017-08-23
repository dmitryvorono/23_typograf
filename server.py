from flask import Flask, render_template, request
import typograf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        raw_text = request.form['text']
        typografical_text = typograf.typographical_text(raw_text)
        return render_template('form.html',
                               raw_text=raw_text,
                               typografical_text=typografical_text)
    return render_template('form.html')


if __name__ == "__main__":
    app.run()
