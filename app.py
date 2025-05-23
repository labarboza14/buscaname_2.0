from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    nome_busca = request.form['nome_busca'].strip().lower()
    uploaded_files = request.files.getlist('file')
    
    planilhas_com_nome = []

    for file in uploaded_files:
        try:
            xls = pd.ExcelFile(BytesIO(file.read()))
            for sheet_name in xls.sheet_names:
                df = xls.parse(sheet_name)
                if df.astype(str).apply(lambda x: x.str.lower()).isin([nome_busca]).any().any():
                    planilhas_com_nome.append(file.filename)
                    break
        except Exception as e:
            return f"Erro ao processar {file.filename}: {e}"
    
    return render_template('resultado.html', planilhas=planilhas_com_nome)

if __name__ == '__main__':
    app.run(debug=True)
