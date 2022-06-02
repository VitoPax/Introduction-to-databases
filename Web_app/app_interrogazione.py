from flask import Flask,render_template, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route("/")
def find_position():

    dialect = "mysql"
    username = "root"
    password = ""
    host = "127.0.0.1"
    dbname = "Ciclisti"
    # Connection object creation
    engine = create_engine("%s://%s:%s@%s/%s" % (dialect, username, password, host, dbname))

    try:

        con = engine.connect()

        # QUERY SQL
        query = "SELECT CodC\
                 FROM CICLISTA "

        result = con.execute(query)

        con.close()
        return render_template("form_interrogazione.html", rows=result)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
    return render_template('errore.html', error_message=error)

@app.route("/ciclista")
def show_position():

    dialect = "mysql"
    username = "root"
    password = ""
    host = "127.0.0.1"
    dbname = "Ciclisti"
    # Connection object creation
    engine = create_engine("%s://%s:%s@%s/%s" % (dialect, username, password, host, dbname))

    CodT = request.args.get('CodT')

    try:
        con = engine.connect()

        # QUERY SQL
        query = "SELECT Nome,Cognome,NomeS\
                 FROM CICLISTA AS C, SQUADRA AS S, CLASSIFICA_INDIVIDUALE AS CI\
                 WHERE C.CodS=S.CodS AND C.CodT=CI.CodT AND C.CodT= '%s' \
                 GROUP BY "

        ciclisti = con.execute(query)

        con.close()
        return render_template("risultato_interrogazione.html", ciclista=ciclisti)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
    return render_template('errore.html', error_message=error)



app.run(port=8080, debug=True)
