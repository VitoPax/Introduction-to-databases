from flask import Flask,render_template
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

app = Flask(__name__)

ciclisti = {
    'CodC': '1',
     'Nome': 'vito'
}

@app.route("/")
def find_position():

    try:


        return render_template("form_interrogazione.html", ciclisti=ciclisti)


    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('errore.html', error_message=error)


app.run(debug=True, port=8080)
