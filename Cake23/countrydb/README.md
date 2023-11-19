
# CountryDB
We are given a link to a web application and the source file. http://countrydb.2023.cakectf.com:8020/


The website lets us put in a country code and responds back with the corresponding county.

![](https://github.com/0xNev/CTF-Writeups/blob/main/Cake23/countrydb/1.png?raw=true)


Lets take a look at the src.
```Python
import flask
import sqlite3

app = flask.Flask(__name__)

def  db_search(code):
	with sqlite3.connect('database.db') as conn:
		cur = conn.cursor()
		cur.execute(f"SELECT name FROM country WHERE code=UPPER('{code}')")
		found = cur.fetchone()
		return  None  if found is  None  else found[0]

  
@app.route('/')
def  index():
	return flask.render_template("index.html")

@app.route('/api/search', methods=['POST'])
def  api_search():
	req = flask.request.get_json()
	if  'code'  not  in req:

	flask.abort(400, "Empty country code")

	code = req['code']

	if  len(code) != 2  or  "'"  in code:
		flask.abort(400, "Invalid country code")

	name = db_search(code)
	if name is  None:
		flask.abort(404, "No such country")

	return {'name': name}

if  __name__ == '__main__':
	app.run()
```


The application is accepting a JSON response with the following structure,
```JSON
{
	"code":"US" 
}
```
The program then does a few checks

 1. Check the length of the 'code' is equal to 2
 2. Make sure a single quotation is not in 'code'

If the above requirements are met, the program makes an SQL query to the local database to check for a corresponding  value by inserting the inputted value. To see the structure of the SQL database we'll take a look at the 'init_db.py' which was also included in the src file.

```Python
import sqlite3
import os
  
FLAG = os.getenv("FLAG", "FakeCTF{*** REDACTED ***}")
  
conn = sqlite3.connect("database.db")
conn.execute("""CREATE TABLE country (
code TEXT NOT NULL,
name TEXT NOT NULL
);""")
conn.execute("""CREATE TABLE flag (
flag TEXT NOT NULL
);""")
conn.execute(f"INSERT INTO flag VALUES (?)", (FLAG,))

# Country list from https://gist.github.com/vxnick/380904
countries = [...]

conn.executemany("INSERT INTO country VALUES (?, ?)", countries)

conn.commit()
conn.close()
```



We see that along with the countries names and codes, the flag is also included in the SQL database. From this we can conclude we need to leak the flag through SQL injection.

Looking back the requirements required for the SQL query to be executed we need to keep the length of the input to 2... or do we. Thinking back to how the program checks the length, it uses the built in Python function len(). This function works many other variable types, for example, arrays. Because the program never checks if the input is also a string we can send an array with our SQL injection in the JSON object. Here's that in action.
 

![](https://github.com/0xNev/CTF-Writeups/blob/main/Cake23/countrydb/2.png?raw=true)
