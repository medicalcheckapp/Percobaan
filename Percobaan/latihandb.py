import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/apps")
def apps():
  _test = request.args.get('test')
  conn = sqlite3.connect("perc.db")
  cursor = conn.cursor()
  if _test == "suhu":
    cursor.execute( "SELECT suhu FROM client " )
    rows = cursor.fetchone()
  return str(rows[0])  

@app.route("/hello")
def hello():

  _suhu = request.args.get('suhu')
  print(_suhu)
  conn = sqlite3.connect("perc.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM client " )
  rows = cursor.fetchone()
  if rows == None:
    cursor.execute("INSERT INTO client ( suhu ) VALUES ( %s )" % ( _suhu ))
    conn.commit()
    print("Data inserted")
  else:
    cursor.execute("UPDATE client SET suhu = %s" % (_suhu ))
    conn.commit()
    print("Data updated")
  cursor.execute("SELECT suhu FROM client")
  rows = cursor.fetchall()
  for row in rows:
    print(row[0], row[1], row[2])
  print("--->")
  
  cursor.close()
  conn.close()
  return "Ok"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)