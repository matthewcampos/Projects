from flask import Flask
app = Flask(__name__)
@app.route('/')
def run_website():
    homepage = open("index.html", "r")
    content = homepage.read()
    return content
    
@app.route('/thing.html')
def run_page():
    page = open("thing.html", "r")
    content = page.read()
    return content

@app.route('/database')
def mysql_connect():
    import mysql.connector

    cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              database='userinfo')

    cursor=cnx.cursor()

    cursor.execute("SHOW TABLES")

    tables = ""

    for table_name in cursor:
        tables += '<li>' + str(table_name[0]) + '</li>'

    cnx.close()
    return '<ul>' + tables + ' </ul>'


if __name__ == "__main__":
    app.run(port=8000, debug=True)