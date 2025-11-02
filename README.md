# 💧 Previsão da Qualidade da Água

Este projeto aplica **Machine Learning** para prever se a água é **potável (1)** ou **não potável (0)** com base em variáveis físico-químicas.  
O modelo foi desenvolvido em **Python**, utilizando algoritmos de **Decision Tree** e **Random Forest**.

---

## 📊 Objetivo

Analisar dados sobre a qualidade da água e criar um modelo capaz de classificar amostras como potáveis ou não, de acordo com as características medidas em laboratório.

---

## 🧩 Dataset

O conjunto de dados foi obtido no **Kaggle**, sob o nome **Water Potability Dataset**, e contém informações de diversas amostras de água, com atributos como:

- **pH** – nível de acidez
- **Hardness** – dureza da água
- **Solids** – sólidos dissolvidos
- **Chloramines** – presença de cloraminas
- **Sulfate**
- **Conductivity**
- **Organic_carbon**
- **Trihalomethanes**
- **Turbidity**
- **Potability** – variável-alvo (1 = potável, 0 = não potável)

---

## ⚙️ Etapas do Projeto

1. **Importação de bibliotecas**
   - `pandas`, `numpy`, `seaborn`, `matplotlib`, `sklearn`, `warnings`, `random`

2. **Análise exploratória dos dados (EDA)**
   - Estatísticas descritivas e gráficos de dispersão
   - Análise de correlações entre variáveis
   - Identificação e tratamento de valores ausentes

3. **Pré-processamento**
   - Normalização dos dados
   - Separação entre **treino** e **teste**

4. **Modelagem**
   - Treinamento com **Decision Tree** e **Random Forest**
   - Comparação de desempenho via **accuracy_score**

5. **Avaliação**
   - Cálculo da acurácia dos modelos
   - Visualização da importância das features
   - Interpretação dos resultados obtidos

---

## 📈 Resultados

O modelo apresentou resultados satisfatórios, com acurácia significativa na detecção de amostras potáveis.  
*(Substitua os valores abaixo pelos que aparecem no seu notebook)*

- **Decision Tree Accuracy:** Train: 97.04% , Test: 96.88%
- **Random Forest Accuracy:** 98.24%

O modelo **Random Forest** obteve o melhor desempenho geral.

---

## 🧠 Tecnologias Utilizadas

- **Python 3.x**
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **scikit-learn**

---

## 🚀 Próximos Passos

- Testar novos algoritmos (como SVM ou XGBoost)  
- Aplicar técnicas de otimização de hiperparâmetros (GridSearchCV)  
- Criar uma API ou aplicativo que use o modelo para prever a potabilidade da água em tempo real  

---

## 📚 Fonte

> Dataset: [Water Potability - Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

---

## ✍️ Autor

**Guilherme Costa**  
Estudante do Instituto Germinare Tech  
💼 Interesse em dados, IA e aplicações sustentáveis  
📅 2025
