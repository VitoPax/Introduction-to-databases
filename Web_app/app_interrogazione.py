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

    CodT = request.args.get('CodT')

    try:

        con = engine.connect()

        # QUERY SQL
        query = "SELECT CodC\
                 FROM CICLISTA\
                 WHERE CodC IN\
                    (SELECT *\
                     FROM CLASSIFICA_INDIVIDUALE AS CI\
                     WHERE CodT= '%s')"%(CodT)

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



    try:
        con = engine.connect()

        # QUERY SQL
        query = "SELECT Nome,Cognome,NomeS, CI.Edizione, CI.CodT \
                 FROM CICLISTA AS C, SQUADRA AS S, CLASSIFICA_INDIVIDUALE AS CI\
                 WHERE C.CodS=S.CodS AND C.CodT=CI.CodT\
                 GROUP BY C.CodC, Nome,Cognome,NomeS, CI.Edizione, CI.CodT "

        ciclisti = con.execute(query)

        con.close()
        return render_template("risultato_interrogazione.html", ciclista=ciclisti)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
    return render_template('errore.html', error_message=error)




app.run(port=8080, debug=True)
