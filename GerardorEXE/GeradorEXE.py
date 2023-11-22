import PyInstaller.__main__

# Programa: GeradorEXE
# Versão: 1.0.00
# Descrição: Gerador de Executável
# Data Inicio: 19/11/2023
# Data Revisão: 19/11/2023
# Autor: Eduardo Gomes Júnior

PyInstaller.__main__.run([
    'Formatting.py',
    '--onefile',
    '--windowed',
    '--clean',
    '--icon=format_shapes.ico',
    '--add-data=Cancelar.png:img',
    '--add-data=clear.png:img',
    '--add-data=find.png:img',
    '--add-data=Historic.png:img',
    '--add-data=json.png:img',
    '--add-data=sql.png:img',
    '--add-data=format_shapes.ico:img'
])
