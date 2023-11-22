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

![Imagem01](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_01.png)

A primeira linha da aplicação possui um GET para realizar pesquisas (marcações) dentro dos quadros de textos:

![Imagem02](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_02.png)

Esse GET (campo) trabalha em conjunto com o botão localizar, após informar um texto no campo e pressionar o botão, caso exista o 
texto informado nos quadros de textos (tanto na expressão original como formatada) o texto é localizado e marcado em vermelho. 

	O próximo botão é o limpar. Como o nome sugere ele limpa ambos os quadros de textos.

 ![Imagem03](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_03.png)

 Já os botões SQL e JSON realizam a formatação do texto informado no quadro.

 ![Imagem04](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_04.png)

 Caso no quadro de expressão original seja informada um expressão SQL o botão de formatação deverá ser o SQL e caso seja uma JSON o botão JSON. A expressão informada no quadro original será formatada no quadro de expressão formatada. 

Observação: na biblioteca usada para formatar expressões SQL não possui nenhum tratamento de erro ou seja após a formatação a mesma tenta adequar a expressão, se a 
expressão original tiver algum erro ela não tratada ou exibida no quadro de expressão formatada. 
Agora a biblioteca que formatada a expressão JSON, possui tratamento de erro, caso esteja errado algum dados ou faltando alguma informação (exemplo: “,”,”{“ ) a mesma será tratada. 
A expressão original não é formatada será mostrada a inconsistência dela no quadro expressão formatada e no quadro expressão original será marcado em amarelo a linha que apresenta a 
inconsistência, somente após a correção que a mesma pode ser formatada.

Toda expressão formatada é gravada dentro da pasta “HISTORÍCO”. Caso haja necessidade de revisar alguma basta pressionar o botão abaixo: 

![Imagem05](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_05.png)

Na sequencia será aberto a interface de seleção:

![Imagem06](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_06.png)

O histórico selecionado será carregado na parte de texto: expressão original. Por DEFAULT sempre vem o histórico SQL, mas para carregar os demais basta mudar a opção de arquivo. 

O nome do histórico segue a seguinte nomenclatura: ANO+MÊS+DIA+Hora+minuto+segundos + extensão correspondente do texto formatado (.SQL ou .JSON).

As expressões devem ser informadas nas caixas de textos abaixo:

![Imagem07](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_07.png)

Lado esquerdo: recebe a expressão original
Lado direito: expressão formatada (conforme opção: SQL ou JSON).

A barra de rolagem vertical/horizontal movimenta ambas as caixas de texto para facilitar a analise da expressão.








 


