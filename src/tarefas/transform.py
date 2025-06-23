import pandas as pd
import logging
from unidecode import unidecode
from src.task_pattern import ETLPattern
from utils.excecoes import ETLPipelineError


class Transform(ETLPattern):
    def __init__(self):
        super().__init__("Transform")

    def executar(self):
        logging.info("Iniciando tarefa: Transform")
        try:

            df = pd.read_feather("data/input_file.feather")

            df["nome"] = df["nome"].str.title()
            df["pais"] = df["pais"].str.capitalize()
            df["aniversario"] = pd.to_datetime(df["aniversario"]).dt.strftime("%d/%m/%Y")
            df["endereco"] = df["endereco"].apply(lambda x: unidecode(str(x)))

            df.to_csv("data/stage_file.csv", index=False)
            logging.info("Tarefa Transform finalizada sem erros.")

        except Exception as e:
            raise ETLPipelineError(f"Erro ao manipular arquivo raw_file.feather: {e}")
