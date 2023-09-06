import streamlit as st
import pandas as pd
import pickle
import numpy as np

pickle_in = open('\Scripts\streamlit_resutado_casos\classifier.pkl','rb')
model = pickle.load(pickle_in)

# Título
st.write("""
         ### IA  - Previsão do Caso 
         """
        """
        Inteligência Artificial que realiza o previsão se um determinado processo judicial, 
        terá previsão de favorável ou desfavorável para o cliente.

        * * * * *
        """)

# Cabeçalho
st.markdown('#### CONFIRA OS DADOS INFORMADOS')
titulo = st.sidebar.title('INFORME OS DADOS ABAIXO:')
# slide bar com dados para serem imputados

pedido = st.sidebar.slider('NÚMERO DO PEDIDO', 0, 82, 0)
valor_requerido = st.sidebar.number_input('INSIRA VALOR REQUERIDO')
natureza_contigencia = st.sidebar.slider('INSIRA NATUREZA CONTIGÊNCIA', 0, 3, 0)

def prediction(pedido, valor_requerido, natureza_contigencia):
    
    # Criar um array NumPy com os dados de entrada
    input_data = np.array([[pedido, valor_requerido, natureza_contigencia]])
    
    # Fazer a previsão
    prediction = model.predict(input_data)

    # Label informativas para o usuário
    st.write('O pedido informado foi número: {} '.format(pedido))
    st.write('O valor requerido foi R$ {} '.format(valor_requerido))
    st.write('A natureza da contingência é: {}'.format(natureza_contigencia))
    st.write (""" **** """)

    if prediction == 0:
        pred = ' Desfavorável para o cliente  :x:'
    elif prediction == 1:
        pred = ' Favorável para o cliente  :white_check_mark:'
    elif prediction == 2:
        pred = 'Parcialmente Favorável ao Cliente'        
    return pred

# Chame a função prediction
resultado = prediction(pedido, valor_requerido, natureza_contigencia)

# Mostre o resultado na interface do Streamlit
st.write('#### Resultado da Previsão: ', resultado)
st.write (""" **** """)

#-----------------#-------------------#---------------------#

natureza = {
    'Classificação Natureza da Contingência' : [
        'Neutra',
        'Débito',
        'Crédito',
        'Honorário do BAS'
    ]
}

df_natureza = pd.DataFrame(natureza)

# Título do aplicativo
st.subheader('Classificação Natureza da Contingência')

# Exibir a tabela de dados usando st.table
st.table(df_natureza)

#------------------------#------------------------------#------------------------------#------------------------------------#

data = {
    'Descrição Pedido': [        
        'Fornecimento de Dados de Terceiro(s)',
        'Exclusão de Conteúdo',
        'Indenização por Danos Morais',
        'Indenização por Danos Materiais',
        'Entrega do(s) Produto(s)',
        'Multa Contratual',
        'Conversão da Obrigação de Fazer em Perdas e Danos',
        'Abstenção de Comunicar Usuário',
        'Fornecimento de Conteúdo de Terceiro(s)',
        'Honorários Advocatícios da Parte Contrária',
        'Honorários Advocatícios do BAS',
        'Fornecimento de Conteúdo Próprio',
        'Fornecimento de Dados Próprios',
        'Desbloqueio de Cadastro e/ou Retomada de Acesso à Conta',
        'Abstenção de Exibição/Publicação de Conteúdo',
        'Direito de Resposta',
        'Suspensão/Exclusão da Conta de E-mail',
        'Exclusão dos Órgãos de Restrição ao Crédito',
        'Custeio de Tratamento Médico/Cirúrgico/Estético/Psiquiátrico',
        'Recuperação de E-mails Apagados',
        'Abstenção de Exclusão de Conteúdo',
        'Habilitação de Crédito',
        'Correção de Problema na Ferramenta',
        'Cobrança',
        'Repetição de Indébito',
        'Inexigibilidade da Cobrança',
        'Efetuar Pagamento',
        'Extensão do Prazo de Armazenamento de Dados',
        'Atribuição de Autoria sobre o Conteúdo',
        'Anulação de Título de Crédito',
        'Cancelamento de Protesto',
        'Anulação de Multa Administrativa',
        'Suspensão da Exigibilidade de Multa Administrativa',
        'Sustação dos Efeitos de Protesto',
        'Cancelamento de Inscrição em Dívida Ativa',
        'Suspensão da Exigibilidade de Inscrição em Dívida Ativa',
        'Abstenção de Protesto de Título de Crédito',
        'Redução de Multa Administrativa',
        'Aplicação de Multa',
        'Indenização por Danos Estéticos',
        'Restabelecimento do Fornecimento de Energia',
        'Anulação de Termo de Ocorrência de Irregularidade',
        'Exclusão de Cadastro/Conta',
        'Interrupção de envio de SPAM e Publicidade por E-mail',
        'Multa Diária Executada',
        'Devolução do Valor do Produto em Dobro',
        'Suspensão de Obra',
        'Inexigibilidade do Valor Reajustado da Mensalidade',
        'Obrigação de Fazer',
        'Reembolso de Despesas',
        'Devolução do Valor do Produto',
        'Concessão de Crédito/Vale/Cupom',
        'Exibição de Documentos',
        'Alteração de Dados Cadastrais',
        'Substituição pelo Produto Correto',
        'Reembolso/Devolução do Valor Pago',
        'Rescisão Contratual',
        'Autorização de Cadastro no Aplicativo',
        'Reparo/Conserto do Produto',
        'Restituição em Dobro',
        'Devolução do Valor Cobrado a Maior',
        'Devolução do Valor da Mensalidade',
        'Emissão de Nota Fiscal',
        'Troca de(s) Produto(s) Defeituoso(s)',
        'Devolução do Valor do Frete',
        'Devolução do Valor da Mensalidade em Dobro',
        'Lucros Cessantes',
        'Exclusão de Cadastro/Conta Falsa',
        'Abstenção de Novos Bloqueios do Cadastro/Conta',
        'Liberação de Valor Retido',
        'Devolução do Valor da Corrida Cobrado a Maior',
        'Incompetência Absoluta - Cláusula Arbitral',
        'Incompetência Territorial',
        'Cumprimento à Oferta',
        'Solicitação de Esclarecimentos',
        'Declarar a Inexistência de Relação Jurídica entre as Partes',
        'Inversão do Ônus da Prova',
        'Justiça Gratuita',
        'Entrega do Prontuário',
        'Inexistência de Débito',
        'Custas e Despesas Processuais Arbitradas a Favor da Parte Contrária',
        'Cancelamento de Serviço',
        'Devolução do Valor da Passagem em Dobro',                          
],

}

df = pd.DataFrame(data)

# Título do aplicativo
st.subheader('Classificação Pedido')

# Exibir a tabela de dados usando st.table
st.table(df)








    
