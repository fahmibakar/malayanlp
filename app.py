import os, os.path
import win32com.client
from flask import Flask, render_template

if os.path.exists("DGS-200078_NIISe_Master_Implementation_Plan_Projek_NIISe_20210117_0802_v0.3.docx"):
    file = "DGS-200078_NIISe_Master_Implementation_Plan_Projek_NIISe_20210117_0802_v0.3.docx"
    xl=win32com.client.Dispatch("Word.Application")
    xl.Documents.Open(os.path.abspath("DGS-200078_NIISe_Master_Implementation_Plan_Projek_NIISe_20210117_0802_v0.3.docx"), ReadOnly=1)
    xl.Application.Run("italicCorrection.detectLang")

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

#show the error
if __name__ == "__main__":
    app.run(debug=True)


