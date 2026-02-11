#Biblioteca Pandas para analise de dados
import pandas as pd

#Consulta em uma base de dados (DataSets)
import csv

#Biblioteca para tratamento de string
import string

#Biblioteca para Processamento de Linguagem natural
#Baixando os recursos necessários do NLTK
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

#Biblioteca para remover a acentuação
from unidecode import unidecode

#Vetorização e similaridade
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Interface Grafica - biblioteca Streamlit e configuração
import streamlit as st

st.set_page_config(page_title="ITEMM Chatbot", page_icon="🤖")
st.title("🤖 Assistente Emprensarial")


#Carregando o DataSet e realizando o pré-processamento e vetorização

@st.cache_resource
def carregar_dados():
    # Carregando o DataSet
    df = pd.read_csv(r'C:\Users\luanp\OneDrive\Documentos\ITEMM\dataset.csv', 
                      delimiter=';', 
                      quoting=csv.QUOTE_MINIMAL)
    
    # Pré-processamento da base
    df["Pergunta_Preprocessada"] = df["Pergunta"].apply(preprocessamento)
    
    # Vetorização
    vec = TfidfVectorizer()
    matrix = vec.fit_transform(df["Pergunta_Preprocessada"])
    return df, vec, matrix

# Função para remover pontuação
def remove_pontuacao(text):
    texto_limpo = ''
    for palavra in text:
      if palavra not in string.punctuation:
        texto_limpo += palavra
    return texto_limpo

# Função de pré-processamento do texto (remoção de pontuação, acentuação, stopwords e tokenização)
def preprocessamento(texto):
    texto = remove_pontuacao(texto)
    texto = unidecode(texto)
    texto = texto.lower()
    tokens = word_tokenize(texto)
    stop_words = stopwords.words('portuguese')
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

# Inicializa os dados e o modelo
dataset, vectorizer, tfidf_matrix = carregar_dados()

def obter_resposta(pergunta):
    pergunta_processada = preprocessamento(pergunta)
    pergunta_vector = vectorizer.transform([pergunta_processada])
    similaridades = cosine_similarity(pergunta_vector, tfidf_matrix)
    pergunta_index = similaridades.argmax()
    
    # Threshold de segurança: se a similaridade for muito baixa, avisa o usuário
    if similaridades[0][pergunta_index] < 0.2:
        return "Desculpe, não encontrei uma teoria específica para essa dúvida no meu banco de dados."
    
    return dataset["Resposta"].iloc[pergunta_index]

# Inicializa o histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada
if question := st.chat_input("Pergunte sobre Taylor, Fayol, Mayo..."):
    
    # Adiciona e exibe a pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Lógica de saída
    flags = ['Fechar', 'Sair', 'Tchau']
    if any(f.lower() in question.lower() for f in flags):
        answer = "Finalizando Chat. Até logo!"
    else:
        # Gera a resposta
        answer = obter_resposta(question)

        # Exibe e salva a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})