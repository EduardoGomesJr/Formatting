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

## Execução:

Formatando expressões SQL:

Expressão exemplo 01:

SELECT 

A1_COD, 
A1_NOME, 
A1_CGC,
A1_CODSEG,
AOV_DESSEG,
A3_COD, 
A3_NOME, 
A1_CODMEMB,
ADK1.ADK_NOME,
A1_CODTER,
ADK2.ADK_NOME AS NOMETER,
CASE
WHEN AI0_SETPUB = '1' THEN 'SIM'
WHEN AI0_SETPUB <> '' THEN 'NÃO'
END AS AI0_SETPUB

FROM SA1000 SA1

LEFT JOIN SA3000 SA3 ON A3_FILIAL = ' ' 
AND SA3.D_E_L_E_T_ = ' ' 
AND A3_COD = A1_VEND

LEFT JOIN ADK000 ADK1 ON ADK1.ADK_FILIAL = ' ' 
AND ADK1.D_E_L_E_T_ = ' ' 
AND ADK1.ADK_COD = A1_CODMEMB

LEFT JOIN ADK000 ADK2 ON ADK2.ADK_FILIAL = ' ' 
AND ADK2.D_E_L_E_T_ = ' ' 
AND ADK2.ADK_COD = A1_CODMEMB

INNER JOIN AOV000 AOV ON AOV_FILIAL = ' ' 
AND AOV.D_E_L_E_T_ = ' ' 
AND AOV_CODSEG = A1_CODSEG
AND AOV_PAI = ' '

LEFT JOIN AI0000 AI0 ON AI0_FILIAL = ' '
AND AI0.D_E_L_E_T_ = ' '
AND A1_COD = AI0_CODCLI

WHERE A1_FILIAL = ' ' 
AND SA3.D_E_L_E_T_ = ' '
AND AOV_CODSEG = '000004'

![Imagem08](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_08.png)

Expressão exemplo 02: com localização de texto em ambas as caixas de texto.

SELECT NV_META ,CT_XAGRUP ,CD_PRODUTO ,DT_META ,CD_UNIDADE_ATENDIMENTO ,CD_UNIDADE_VENDA ,CD_ESN ,CD_GSN ,CD_DSN ,EMAIL_META ,DS_SEGMENTO ,DS_MACRO_SEGMENTO ,DS_AGRUPAMENTO_META ,VL_META  AS  VL_META_PRODUCAO ,DS_LINHA_RECEITA FROM ( SELECT 'Unidade' NV_META ,CT_XAGRUP CT_XAGRUP ,CT_DATA DT_META ,CT_XUNIDAD CD_UNIDADE_ATENDIMENTO ,ADK_XSUPER CD_UNIDADE_VENDA ,'-1' CD_ESN ,'-1' CD_GSN ,'-1' CD_DSN ,' ' EMAIL_META ,AOV_DESSEG DS_SEGMENTO ,CASE WHEN AOV_XAGRUP = '1' THEN 'PRODUCTS' WHEN AOV_XAGRUP = '2' THEN 'SERVICES' WHEN AOV_XAGRUP = '3' THEN 'SMALL' WHEN AOV_XAGRUP = '4' THEN 'SUPPLYCHAIN' WHEN AOV_XAGRUP = '5' THEN 'CONSUMER' WHEN AOV_XAGRUP = '6' THEN 'HEALTHCARE' WHEN AOV_XAGRUP = '7' THEN 'FINANCIAL SERVICES' WHEN AOV_XAGRUP = '8' THEN 'MERCADO INTERNACIONAL' WHEN AOV_XAGRUP IS NULL THEN 'NAO INFORMADO' END DS_MACRO_SEGMENTO ,PCI_DESCRI DS_AGRUPAMENTO_META ,PCN_MODPRO ,SUM(COALESCE(CT_VALOR,0)) VL_META FROM  SCT000 SCT LEFT JOIN  AOV000 AOV ON AOV_FILIAL =  '           ' AND CT_XCODSEG = AOV_CODSEG AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  ADK000 ADK ON ADK_FILIAL =  '           ' AND ADK_COD = SCT.CT_XUNIDAD AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  PCJ000 PCJ ON PCJ_FILIAL =  '           ' AND PCJ_PICPAD = CT_XAGRUP AND PCJ.D_E_L_E_T_= ' ' LEFT JOIN  PCI000 PCI ON PCI_FILIAL =  '           ' AND PCJ.PCJ_PICMET = PCI.PCI_CODIGO AND PCI.D_E_L_E_T_= ' ' LEFT JOIN  PCN000 PCN ON PCN_FILIAL =  '           ' AND PCN.PCN_CODMET = PCI.PCI_CODIGO AND TO_DATE(CT_DATA,'YYYYMMDD') BETWEEN TO_DATE(PCN.PCN_VIGDE,'YYYYMMDD') AND TO_DATE(PCN.PCN_VIGATE,'YYYYMMDD') AND PCN.D_E_L_E_T_= ' ' WHERE SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <> ' ' AND CT_XUNIDAD <> ' ' AND ( CT_VEND = ' ' OR CT_XCODSUP = ' ' ) AND CT_XAGRUP <>  '0101' AND SCT.D_E_L_E_T_= ' '     GROUP BY CT_XAGRUP ,CT_DATA ,CT_XUNIDAD ,ADK_XSUPER ,AOV_DESSEG ,AOV_XAGRUP ,PCI_DESCRI ,PCN_MODPRO UNION ALL SELECT 'DSN' NV_META ,CT_XAGRUP CT_XAGRUP ,CT_DATA DT_META ,CT_XUNIDAD CD_UNIDADE_ATENDIMENTO ,ADK_XSUPER CD_UNIDADE_VENDA ,'-1' CD_ESN ,'-1' CD_GSN ,A3_COD CD_DSN ,A3_EMAIL EMAIL_META ,AOV_DESSEG DS_SEGMENTO ,CASE WHEN AOV_XAGRUP = '1' THEN 'PRODUCTS' WHEN AOV_XAGRUP = '2' THEN 'SERVICES' WHEN AOV_XAGRUP = '3' THEN 'SMALL' WHEN AOV_XAGRUP = '4' THEN 'SUPPLYCHAIN' WHEN AOV_XAGRUP = '5' THEN 'CONSUMER' WHEN AOV_XAGRUP = '6' THEN 'HEALTHCARE' WHEN AOV_XAGRUP = '7' THEN 'FINANCIAL SERVICES' WHEN AOV_XAGRUP = '8' THEN 'MERCADO INTERNACIONAL' WHEN AOV_XAGRUP IS NULL THEN 'NAO INFORMADO' END DS_MACRO_SEGMENTO ,PCI_DESCRI DS_AGRUPAMENTO_META ,PCN_MODPRO ,SUM(COALESCE(CT_VALOR,0)) VL_META FROM  SCT000 SCT INNER JOIN  SA3000 SA3 ON A3_FILIAL =  '           ' AND A3_COD = CT_VEND AND A3_CARGO = '000001' AND SA3.D_E_L_E_T_= ' ' LEFT JOIN  AOV000 AOV ON AOV_FILIAL =  '           ' AND CT_XCODSEG = AOV_CODSEG AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  ADK000 ADK ON ADK_FILIAL =  '           ' AND ADK_COD = SCT.CT_XUNIDAD AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  PCJ000 PCJ ON PCJ_FILIAL =  '           ' AND PCJ_PICPAD = CT_XAGRUP AND PCJ.D_E_L_E_T_= ' ' LEFT JOIN  PCI000 PCI ON PCI_FILIAL =  '           ' AND PCJ.PCJ_PICMET = PCI.PCI_CODIGO AND PCI.D_E_L_E_T_= ' ' LEFT JOIN  PCN000 PCN ON PCN_FILIAL =  '           ' AND PCN.PCN_CODMET = PCI.PCI_CODIGO AND TO_DATE(CT_DATA,'YYYYMMDD') BETWEEN TO_DATE(PCN.PCN_VIGDE,'YYYYMMDD') AND TO_DATE(PCN.PCN_VIGATE,'YYYYMMDD') AND PCN.D_E_L_E_T_= ' ' WHERE SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <> ' ' AND CT_XAGRUP <>  '0101' AND SCT.D_E_L_E_T_= ' '     GROUP BY CT_XAGRUP ,CT_DATA ,CT_XUNIDAD ,ADK_XSUPER ,A3_COD ,A3_EMAIL ,AOV_DESSEG ,AOV_XAGRUP ,PCI_DESCRI ,PCN_MODPRO UNION ALL SELECT 'GSN' NV_META ,CT_XAGRUP CT_XAGRUP ,CT_DATA DT_META ,CT_XUNIDAD CD_UNIDADE_ATENDIMENTO ,ADK_XSUPER CD_UNIDADE_VENDA ,'-1' CD_ESN ,A3_COD CD_GSN ,CT_XCODSUP CD_DSN ,A3_EMAIL EMAIL_META ,AOV_DESSEG DS_SEGMENTO ,CASE WHEN AOV_XAGRUP = '1' THEN 'PRODUCTS' WHEN AOV_XAGRUP = '2' THEN 'SERVICES' WHEN AOV_XAGRUP = '3' THEN 'SMALL' WHEN AOV_XAGRUP = '4' THEN 'SUPPLYCHAIN' WHEN AOV_XAGRUP = '5' THEN 'CONSUMER' WHEN AOV_XAGRUP = '6' THEN 'HEALTHCARE' WHEN AOV_XAGRUP = '7' THEN 'FINANCIAL SERVICES' WHEN AOV_XAGRUP = '8' THEN 'MERCADO INTERNACIONAL' WHEN AOV_XAGRUP IS NULL THEN 'NAO INFORMADO' END DS_MACRO_SEGMENTO ,PCI_DESCRI DS_AGRUPAMENTO_META ,PCN_MODPRO ,SUM(COALESCE(CT_VALOR,0)) VL_META FROM  SCT000 SCT INNER JOIN  SA3000 SA3 ON A3_FILIAL =  '           ' AND A3_COD = CT_VEND AND A3_CARGO IN ('000002','000255') AND SA3.D_E_L_E_T_= ' ' LEFT JOIN  AOV000 AOV ON AOV_FILIAL =  '           ' AND CT_XCODSEG = AOV_CODSEG AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  ADK000 ADK ON ADK_FILIAL =  '           ' AND ADK_COD = SCT.CT_XUNIDAD AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  PCJ000 PCJ ON PCJ_FILIAL =  '           ' AND PCJ_PICPAD = CT_XAGRUP AND PCJ.D_E_L_E_T_= ' ' LEFT JOIN  PCI000 PCI ON PCI_FILIAL =  '           ' AND PCJ.PCJ_PICMET = PCI.PCI_CODIGO AND PCI.D_E_L_E_T_= ' ' LEFT JOIN  PCN000 PCN ON PCN_FILIAL =  '           ' AND PCN.PCN_CODMET = PCI.PCI_CODIGO AND TO_DATE(CT_DATA,'YYYYMMDD') BETWEEN TO_DATE(PCN.PCN_VIGDE,'YYYYMMDD') AND TO_DATE(PCN.PCN_VIGATE,'YYYYMMDD') AND PCN.D_E_L_E_T_= ' ' WHERE SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <> ' ' AND CT_XAGRUP <>  '0101' AND SCT.D_E_L_E_T_= ' '     GROUP BY CT_XAGRUP ,CT_DATA ,CT_XUNIDAD ,ADK_XSUPER ,A3_COD ,A3_EMAIL ,AOV_DESSEG ,AOV_XAGRUP ,PCI_DESCRI ,CT_XCODSUP ,PCN_MODPRO UNION ALL SELECT 'ESN' NV_META ,CT_XAGRUP CT_XAGRUP ,CT_DATA DT_META ,CT_XUNIDAD CD_UNIDADE_ATENDIMENTO ,ADK_XSUPER CD_UNIDADE_VENDA ,A3_COD CD_ESN ,CT_XCODSUP CD_GSN ,HRQ.DSN CD_DSN ,A3_EMAIL EMAIL_META ,AOV_DESSEG DS_SEGMENTO ,CASE WHEN AOV_XAGRUP = '1' THEN 'PRODUCTS' WHEN AOV_XAGRUP = '2' THEN 'SERVICES' WHEN AOV_XAGRUP = '3' THEN 'SMALL' WHEN AOV_XAGRUP = '4' THEN 'SUPPLYCHAIN' WHEN AOV_XAGRUP = '5' THEN 'CONSUMER' WHEN AOV_XAGRUP = '6' THEN 'HEALTHCARE' WHEN AOV_XAGRUP = '7' THEN 'FINANCIAL SERVICES' WHEN AOV_XAGRUP = '8' THEN 'MERCADO INTERNACIONAL' WHEN AOV_XAGRUP IS NULL THEN 'NAO INFORMADO' END DS_MACRO_SEGMENTO ,PCI_DESCRI DS_AGRUPAMENTO_META ,PCN_MODPRO ,SUM(COALESCE(CT_VALOR,0)) VL_META FROM  SCT000 SCT INNER JOIN  SA3000 SA3 ON A3_FILIAL =  '           ' AND A3_COD = CT_VEND AND A3_CARGO = '000003' AND A3_XAGN <> 'COP' AND SA3.D_E_L_E_T_= ' ' LEFT JOIN  AOV000 AOV ON AOV_FILIAL =  '           ' AND CT_XCODSEG = AOV_CODSEG AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  ADK000 ADK ON ADK_FILIAL =  '           ' AND ADK_COD = SCT.CT_XUNIDAD AND AOV.D_E_L_E_T_= ' ' LEFT JOIN  PCJ000 PCJ ON PCJ_FILIAL =  '           ' AND PCJ_PICPAD = CT_XAGRUP AND PCJ.D_E_L_E_T_= ' ' LEFT JOIN  PCI000 PCI ON PCI_FILIAL =  '           ' AND PCJ.PCJ_PICMET = PCI.PCI_CODIGO AND PCI.D_E_L_E_T_= ' ' LEFT JOIN  PCN000 PCN ON PCN_FILIAL =  '           ' AND PCN.PCN_CODMET = PCI.PCI_CODIGO AND TO_DATE(CT_DATA,'YYYYMMDD') BETWEEN TO_DATE(PCN.PCN_VIGDE,'YYYYMMDD') AND TO_DATE(PCN.PCN_VIGATE,'YYYYMMDD') AND PCN.D_E_L_E_T_= ' ' LEFT JOIN ( SELECT DISTINCT TRIM(CT_XUNIDAD) CD_UNIDADE ,CT_VEND ESN ,CASE WHEN SUBSTR(CT_XCODSUP,1,1) = ' ' THEN '-2' ELSE CT_XCODSUP END GSN ,DSN FROM  SCT000 SCT INNER JOIN  SA3000 SA3EX ON SA3EX.A3_FILIAL =  '           ' AND SA3EX.A3_COD = CT_VEND AND SA3EX.A3_CARGO = '000003' AND SA3EX.D_E_L_E_T_= ' ' AND A3_XAGN <> 'COP' LEFT JOIN ( SELECT DISTINCT CASE WHEN SUBSTR(CT_XCODSUP,1,1) = ' ' THEN '-2' ELSE CT_XCODSUP END DSN ,CT_VEND  AS  GSN FROM  SCT000 SCT INNER JOIN  SA3000 SA3 ON SA3.A3_FILIAL =  '           ' AND SA3.A3_COD = CT_VEND AND SA3.A3_CARGO IN ('000002','000255') AND SA3.D_E_L_E_T_= ' ' INNER JOIN  SA3000 SA3V ON SA3V.A3_FILIAL =  '           ' AND SA3V.A3_COD = CT_XCODSUP AND SA3V.A3_CARGO = '000001' AND SA3V.D_E_L_E_T_= ' ' WHERE SCT.D_E_L_E_T_= ' ' AND CT_VEND <> ' ' AND SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <>  '0101' AND CT_XAGRUP <> ' ') GSN ON SCT.CT_XCODSUP = GSN.GSN WHERE SCT.D_E_L_E_T_= ' ' AND CT_VEND <> ' ' AND SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <>  '0101' AND CT_XAGRUP <> ' ' ) HRQ ON HRQ.ESN = CT_VEND AND HRQ.GSN = CT_XCODSUP AND HRQ.CD_UNIDADE = SCT.CT_XUNIDAD WHERE SUBSTR(CT_DATA,1,4) =  '2022' AND CT_XAGRUP <> ' ' AND CT_XAGRUP <>  '0101' AND SCT.D_E_L_E_T_= ' '     GROUP BY CT_XAGRUP ,CT_DATA ,CT_XUNIDAD ,ADK_XSUPER ,A3_COD ,A3_EMAIL ,CT_XCODSUP ,DSN ,AOV_DESSEG ,AOV_XAGRUP ,PCI_DESCRI ,PCN_MODPRO ) X LEFT JOIN ( SELECT * FROM ( SELECT A.B1_COD  AS  CD_PRODUTO ,D.PLG_RELAC6  AS  DS_LINHA_RECEITA ,B.BM_GRUPO ,B.BM_XLINREC ,ROW_NUMBER() OVER ( PARTITION BY B.BM_XLINREC ORDER BY A.B1_COD )  AS  ID FROM ( SELECT B1_COD, B1_GRUPO FROM  SB1000 A WHERE D_E_L_E_T_= ' ' ) A LEFT OUTER JOIN ( SELECT BM_GRUPO,BM_XLINREC,BM_XGRPREC FROM  SBM000 B WHERE D_E_L_E_T_= ' ' ) B ON A.B1_GRUPO=B.BM_GRUPO LEFT OUTER JOIN ( SELECT PCJ_PICMET,PCJ_PICPAD FROM  PCJ000 C WHERE D_E_L_E_T_= ' ' ) C ON C.PCJ_PICPAD = B.BM_XLINREC LEFT OUTER JOIN ( SELECT PLG_RELAC6,PLG_TPLINK,PLG_DSCMAN FROM  PLG000 D WHERE D_E_L_E_T_= ' ' ) D ON D.PLG_TPLINK = '000134' AND D.PLG_DSCMAN = C.PCJ_PICMET || (CASE WHEN B.BM_XGRPREC = '1' THEN 'S' WHEN B.BM_XGRPREC = '2' THEN 'N' END) ) A WHERE ID =1 ) PRD ON X.CT_XAGRUP = PRD.BM_XLINREC OFFSET  0 ROWS FETCH NEXT  20 ROWS ONLY

![Imagem09](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_09.png)

Formatando expressões JSON:

Expressão exemplo 01:

{"ALINKUPLD":[{"ARQBASE64":"MAX_TOPMEMOMEGA","MD5HEXADECIMAL":"a05846057476ac87895555043dda3d88","NOMEARQUIVO":"TERMO_ACEITE_000010649.pdf"}],"CANALCORP":"1","CNPJCLI":"52138773620","CNPJREVENDA":"","CNPJVEND":"","CODVENDEDOR":"T17570","CONTATO":"","DDDCONTATO":"11","EMPRESAINT":"000008","ENTREGA":{"BAIRROENTR":"Sé","CEPENTR":"01001000","CIDADEENTR":"SAO PAULO","CNPJENT":"SP","CODCIDADE":"3550308","COMPLEMENTOENTR":" ","ENTREGPARA":"4","LOGRADOUROENTR":"Praça da Sé","NOMERESPENTR":"Polenguinho","NUMEROENTR":"32","UFENTR":"Polenguinho"},"FORMA":"2","ITENS":[{"ADZ_CONDPG":"278","ADZ_DT1VEN":"","ADZ_IDRSVC":"447","ADZ_MOEDA":"1","ADZ_PRCVEN":259,"ADZ_PRODUT":"3116001741","ADZ_QTDVEN":1,"ADZ_XMESDT":1,"ADZ_XSITUA":"F","ADZ_XTPDES":"","ADZ_XTPFAT":"1","ADZ_XVDEST":129.5}],"MODALIDADE":"0357","OBSNEGOCIACOES":"","PAPELVEND":"","PERDAGANHA":"1","PROJCONTBIL":"","PVEXTERNO":"000010649","SISTBEMAT":"3","TELCONTATO":"9999999999","TPVENDA":"6"}

![Imagem10](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_10.png)

Expressão exemplo 02: com tratamento de inconsistência

{
  "hasNext": true,
  "items": [
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20221001",
      "CD_UNIDADE_ATENDIMENTO": "TNE111",
      "CD_UNIDADE_VENDA": "TNE111",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "SERVICOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 392.89
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "02F2600108",
      "DT_META": "20220201",
      "CD_UNIDADE_ATENDIMENTO": "TSE402",
      "CD_UNIDADE_VENDA": "TSE402",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "SERVICOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CLOUD",
      "VL_META_PRODUCAO": 1161.69,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220201",
      "CD_UNIDADE_ATENDIMENTO": "TSE341",
      "CD_UNIDADE_VENDA": "TSE341",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "MANUFATURA",
      "DS_MACRO_SEGMENTO": "SUPPLYCHAIN",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 96972.1,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "02F2600108",
      "DT_META": "20220201",
      "CD_UNIDADE_ATENDIMENTO": "TSE341",
      "CD_UNIDADE_VENDA": "TSE341",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "CONSTRUCAO E PROJETOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CLOUD",
      "VL_META_PRODUCAO": 0.01,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "02F2600108",
      "DT_META": "20220301",
      "CD_UNIDADE_ATENDIMENTO": "TSE115",
      "CD_UNIDADE_VENDA": "TSE115",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "SERVICOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CLOUD",
      "VL_META_PRODUCAO": 811.35,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE018",
      "CD_UNIDADE_VENDA": "TSE018",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "MANUFATURA",
      "DS_MACRO_SEGMENTO": "SUPPLYCHAIN",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 15352.61,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000002194",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE010",
      "CD_UNIDADE_VENDA": "TSE010",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "LOGISTICA",
      "DS_MACRO_SEGMENTO": "SUPPLYCHAIN",
      "DS_AGRUPAMENTO_META": "SW COMPLEMENTAR",
      "VL_META_PRODUCAO": 0.01,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "02F2600108",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE010",
      "CD_UNIDADE_VENDA": "TSE010",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "EDUCACIONAL",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CLOUD",
      "VL_META_PRODUCAO": 0.01,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE010",
      "CD_UNIDADE_VENDA": "TSE010",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "EDUCACIONAL",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 364.51,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE108",
      "CD_UNIDADE_VENDA": "TSE108",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "SERVICOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 9000.01,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TNE106",
      "CD_UNIDADE_VENDA": "TNE106",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "SERVICOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 10136.06,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220201",
      "CD_UNIDADE_ATENDIMENTO": "TNE103",
      "CD_UNIDADE_VENDA": "TNE103",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "MANUFATURA",
      "DS_MACRO_SEGMENTO": "SUPPLYCHAIN",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 7333.5,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220201",
      "CD_UNIDADE_ATENDIMENTO": "TSE004",
      "CD_UNIDADE_VENDA": "TSE004",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "CONSTRUCAO E PROJETOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 59958.62,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220101",
      "CD_UNIDADE_ATENDIMENTO": "TSE500",
      "CD_UNIDADE_VENDA": "TSE500",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "LOGISTICA",
      "DS_MACRO_SEGMENTO": "SUPPLYCHAIN",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 433.38,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220501",
      "CD_UNIDADE_ATENDIMENTO": "TSL112",
      "CD_UNIDADE_VENDA": "TSL112",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "EDUCACIONAL",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 9180.09,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220601",
      "CD_UNIDADE_ATENDIMENTO": "TCO103",
      "CD_UNIDADE_VENDA": "TCO103",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "VAREJO",
      "DS_MACRO_SEGMENTO": "CONSUMER",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 3701.68,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000000008",
      "DT_META": "20220601",
      "CD_UNIDADE_ATENDIMENTO": "TNE106",
      "CD_UNIDADE_VENDA": "TNE106",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "CONSTRUCAO E PROJETOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "CDU SERIE 3,CDU SERIE T, TOTVS TEC, PROG",
      "VL_META_PRODUCAO": 16927.12,
      "DS_LINHA_RECEITA": "CDU"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220501",
      "CD_UNIDADE_ATENDIMENTO": "TSE110",
      "CD_UNIDADE_VENDA": "TSE110",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "VAREJO",
      "DS_MACRO_SEGMENTO": "CONSUMER",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 2310.01,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "0193303001",
      "DT_META": "20220501",
      "CD_UNIDADE_ATENDIMENTO": "TSE402",
      "CD_UNIDADE_VENDA": "TSE402",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "VAREJO",
      "DS_MACRO_SEGMENTO": "CONSUMER",
      "DS_AGRUPAMENTO_META": "SAAS INTERA SOFTWARE",
      "VL_META_PRODUCAO": 435.78,
      "DS_LINHA_RECEITA": "SAAS"
    },
    {
      "NV_META": "Unidade",
      "CD_PRODUTO": "000000000002194",
      "DT_META": "20220601",
      "CD_UNIDADE_ATENDIMENTO": "TSE341",
      "CD_UNIDADE_VENDA": "TSE341",
      "CD_ESN": "-1",
      "CD_GSN": "-1",
      "CD_DSN": "-1",
      "EMAIL_META": "",
      "DS_SEGMENTO": "CONSTRUCAO E PROJETOS",
      "DS_MACRO_SEGMENTO": "SERVICES",
      "DS_AGRUPAMENTO_META": "SW COMPLEMENTAR",
      "VL_META_PRODUCAO": 0.01,
      "DS_LINHA_RECEITA": "CDU"
    }
  ]
}

Comparando inconsistência apresentada com outro editor (VS-CODE).

![Imagem11](https://github.com/EduardoGomesJr/Formatting/blob/main/Imagens/Imagem_11.png)





