
# Projeto de Pipeline de Dados

Este é um projeto acadêmico desenvolvido em Python para simular uma pipeline de dados com foco em boas práticas de engenharia de software.

## 📁 Estrutura do Projeto

projeto_dados/
├── data/ # Arquivos de entrada, transformação e saída
│ ├── input_file.feather
│ ├── stage_file.csv
│ └── output_file.csv
├── env/ # Ambiente Virtual
├── logs/ # Registro de execuções e erros
│ └── execucao.log
├── src/ # Código-fonte principal
│ ├── main.py
│ ├── pipeline.py
│ └── tarefas/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
└── README.md
└── requirements.txt

## 🛠️ Funcionalidades

- Geração de dados simulados com `Faker`
- Transformações e limpeza (ex: formatação de datas, remoção de acentos)
- Escrita em múltiplos formatos (Feather, CSV)
- Estrutura orientada a objetos
- Logging detalhado

## ▶️ Como executar

Instale as dependências:
bash / powershell
pip install -r requirements.txt

Execute o pipeline:

bash / powershell
python src/main.py
Obs.: certifique-se de estar na raiz do projeto.

📋 Requisitos
Python 3.10+
Pandas
Faker
PyArrow
Unidecode