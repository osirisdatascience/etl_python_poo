from faker import Faker
import pandas as pd
import logging
from src.task_pattern import ETLPattern


class Extract(ETLPattern):

    def __init__(self):
        super().__init__("Extract")

    def executar(self):

        logging.info("Iniciando tarefa: Extract")
        fake = Faker("pt_BR")
        dados = []

        try:

            for i in range(11000):
                dados.append(
                    {
                        "id": i,
                        "nome": fake.name(),
                        "email": fake.email(),
                        "pais": fake.country(),
                        "aniversario": fake.date_of_birth(),
                        "endereco": fake.address(),
                    }
                )

            df = pd.DataFrame(dados)
            df.reset_index(drop=True).to_feather("data/input_file.feather")
            logging.info("Tarefa Extract finalizada sem erros.")

        except Exception as e:

            logging.info(f"Erro ao extrair (gerar) dados {e}")
