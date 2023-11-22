# Formatting
 Formatação de expressões SQL e JSON

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/EduardoGomesJr/Formatting/blob/main/LICENCE)

# Projeto:
Aplicação para formatar expressões (textos) em SQL ou JSON sem a necessidade de recorrer a recursos da internet. 
Com a expressão formatada corretamente a analise/compreensão torna-se mais fácil pelo analista que está analisando e ajuda na construção final da expressão ou analise de um possível erro. 

## Tecnologia Usada:
DONWLOAD do PYTHON: https://www.python.org/downloads/

Instalador: Inno Setup Compiler (baixado do site: https://jrsoftware.org/isdl.php)

A aplicação precisa de quatro bibliotecas externas para o funcionamento. 

- customtkinter (criação de interfaces modernas no Tkinter) 
- sqlparse (parce SQL)
- Pillow (tratamento de imagens)
- packaging (pacotes diversos)

Detalhes no arquivo: requirements.txt

Para instalar ambas utilizar PIP: acesse o prompt de comando (como administrador) e execute os comandos abaixo:

pip install customtkinter 

pip install sqlparse

pip install Pillow

pip install packaging

Após os pré-requisitos acima realizar o clone do repositório: https://github.com/EduardoGomesJr/Formatting

## Funcionalides:

Após executar a aplicação será exibida a interface abaixo:

![Imagem01](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Figura_01.png)

A primeira linha da aplicação possui um GET para realizar pesquisas (marcações) dentro dos quadros de textos:

![Imagem02](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Figura_02.png)

Esse GET (campo) trabalha em conjunto com o botão localizar, após informar um texto no campo e pressionar o botão, caso exista o 
texto informado nos quadros de textos (tanto na expressão original como formatada) o texto é localizado e marcado em vermelho. 

	O próximo botão é o limpar. Como o nome sugere ele limpa ambos os quadros de textos.

 ![Imagem03](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Figura_03.png)

 


