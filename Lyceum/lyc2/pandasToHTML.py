import pandas as pd
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return """
    <a href='/data'><h1>1. Данные</h1></a>
    """
 
@app.route('/data')
def get_table():
    df = pd.read_csv('/home/user/work/data/data.csv',sep=';')
    return df.to_html(max_rows=10)
 
if __name__ == '__main__':
    app.run(debug=True)


import lxml.html
from lxml.html import builder
 
df = DataFrame(obj) # ваш dataframe
html = lxml.html.document_fromstring(df.to_html())
tree = builder.HTML(builder.BODY(builder.DIV(html,style="height:150px;overflow-y:scroll")))
html = lxml.html.tostring(tree,encoding='unicode')