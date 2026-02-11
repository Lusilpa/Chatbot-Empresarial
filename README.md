# 🤖 Chatbot Empresarial

Chatbot de suporte ao RH desenvolvido como base para o TCA para o curso de Jovem Aprendiz (ITEMM &amp; Tapajós). Focado na integração de novos colaboradores e documentação de processos, utiliza Python, Streamlit e Processamento de Linguagem Natural (NLP) com TF-IDF para automatizar respostas sobre leis trabalhistas, normas e processos internos.

📆 **Apresentação prevista do projeto: Abril/2026**

🧑‍💻 **Fase: projeto em desenvolvimento - Desenvolvedor: Luan Palma**

# 📈 Capítulo 1 - Objetivos
## 📌 Objetivo Geral
Criar uma aplicação real de Processamento de Linguagem Natural no contexto do departamento de Recursos Humanos, utilizando Python e Streamlit.

## 📌Objetivos Especificos

- Desenvolver habilidades com Python para desenvolvimento Full-Stack com foco em Ciência de Dados.
- Aplicar conceitos de Processamento de Linguagem Natural (NLP) para automação de FAQs empresariais.
- Otimizar o tempo de resposta do RH no atendimento a dúvidas frequentes de novos colaboradores (Onboarding).
- Estruturar uma base de dados (Dataset) voltada para a gestão de conhecimento organizacional.
- Garantir a conformidade com a LGPD no tratamento de informações e fluxos de dados do chatbot.

# ⚒️Tecnologias e Conceitos Utilizadas
## 🐍 Por que usar a linguagem Python?

A escolha do Python para o Chatbot Empresarial fundamenta-se em três pilares principais:

1. **Ecossistema Rico em NLP (Natural Language Processing)**
Diferente de linguagens como C ou Java, o Python possui bibliotecas prontas (como NLTK, Scikit-Learn e SpaCy) que permitem processar a linguagem humana com poucas linhas de código. No projeto, isso é essencial para que o bot entenda que "Férias" e "como tirar minhas férias?" pertencem ao mesmo contexto.

2. **Agilidade no Desenvolvimento (Prototipagem Rápida)**

O Python possui uma sintaxe clara e próxima da linguagem humana. Para um projeto de TCA, onde o tempo de desenvolvimento é precioso, o Python permite focar na lógica do negócio (RH) em vez de perder tempo com complexidades de gerenciamento de memória ou sintaxes verbosas.

3. **Integração com o Streamlit**

O Python permitiu o uso do Streamlit, que transforma scripts de dados em interfaces web de forma instantânea. Isso elimina a necessidade de aprender HTML/CSS/JavaScript avançado neste momento, garantindo uma ferramenta funcional e visualmente profissional para a apresentação final.

## 🛠️ Bibliotecas e Frameworks

- 💻 **Interface e Deploy**

Streamlit: Framework utilizado para transformar o script Python em uma aplicação web interativa. Ele permite a criação de dashboards e interfaces de chat de forma ágil, facilitando o acesso dos colaboradores do RH ao sistema sem a necessidade de instalação de ambientes de desenvolvimento.

- 📊 **Manipulação de Dados**

Pandas: Biblioteca fundamental para a análise de dados. No projeto, ela é responsável por carregar o arquivo dataset.csv, estruturar a base de conhecimentos em DataFrames e realizar operações de filtragem e mapeamento de respostas.

## 🧠 Processamento de Linguagem Natural (NLP)
O "coração" do chatbot utiliza técnicas de inteligência artificial clássica para compreender as intenções do usuário:

- NLTK (Natural Language Toolkit): Utilizada para a etapa de Tokenização (dividir o texto em unidades menores) e remoção de Stopwords (palavras como "de", "a", "o" que não agregam valor semântico à busca), tornando o processamento mais eficiente.

- Scikit-learn (TF-IDF): Implementa o algoritmo Term Frequency-Inverse Document Frequency. Ele transforma o texto em vetores numéricos, dando pesos maiores para palavras raras e importantes (ex: "FGTS", "Fayol") e pesos menores para palavras comuns.

- Similaridade de Cosseno: Técnica matemática utilizada para calcular o "ângulo" entre o vetor da pergunta do usuário e os vetores da base de dados. Quanto menor o ângulo, maior a similaridade e, portanto, mais precisa é a resposta entregue.

# ⚙️ Metodologia e Fluxo de Dados

O funcionamento do assistente segue um fluxo linear de processamento de dados, desde a entrada da pergunta do colaborador até a entrega da resposta fundamentada:

- Entrada: O usuário digita uma dúvida na interface Streamlit.
- Tratamento: O texto passa por limpeza (unidecode), tokenização e filtragem (NLTK).
- Vetorização: A pergunta tratada é convertida em um vetor numérico pelo modelo TF-IDF treinado no dataset.csv.
- Cálculo: A Similaridade de Cosseno identifica a linha do dataset com a maior pontuação de equivalência.
- Saída: Se a similaridade atingir o threshold mínimo, a resposta é exibida; caso contrário, o bot solicita mais informações.

# 🚀 Como executar o projeto

Para rodar este assistente localmente, siga os passos abaixo:

1. **Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
```

2. **Instalando dependências:**
```bash
pip install -r requirements.txt
```

3. **Inicie a aplicação:**
```bash
streamlit run app.py
```

# 📂 Estrutura de Arquivos

```markdown
Plaintext
├── dataset.csv          # Base de conhecimento (Perguntas/Respostas sobre TGS e TSA)
├── processador.py       # Script principal com lógica NLP e Interface
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependencias do Sistema
```

# 🗃️ Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018)

Todos os arquivos deste repositório utilizam dados sobre a Teoria dos Sistemas da Administração (TSA) e Teoria Geral dos Sistemas (TGS), reforçando o compromisso do autor sobre os dados privados das empresas que inspiraram o projeto.




