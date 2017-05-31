from flask import Flask
from datetime import datetime
import sys
import buildinfo

# Overload std stream to local string
class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def flush(self):
        pass

x = ListStream()
sys.stdout = x
hasRun = False

from cogvents import *
app = Flask(__name__)

@app.route('/')
def homepage():
    global x, hasRun
    if hasRun == False:
        main()
        hasRun = True
    body = """
    <h1>COGVENTS</h1>
    <p>{}</p>
    """.format("".join(x.data).replace('\n', "<br>"))
    buildRev = "<br/><br/><i>Git revision: " + buildinfo.getRevision() + "</i>"
    
    return body + buildRev

if __name__ == '__main__':
    app.run(debug=False)