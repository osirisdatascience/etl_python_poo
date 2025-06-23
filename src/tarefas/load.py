import logging
import pandas as pd
from src.task_pattern import ETLPattern
from utils.excecoes import ETLPipelineError


class Load(ETLPattern):

    def __init__(self):
        super().__init__("load")

    def executar(self):

        logging.info("Iniciando tarefa: load")

        try:

            df = pd.read_csv("data/stage_file.csv")
            df_final = df[["id", "nome", "email", "pais", "aniversario"]]
            df_final.to_csv("data/output_file.csv", index=False)
            logging.info("Tarefa load finalizada sem erros.")

        except Exception as e:
            raise ETLPipelineError(f"Erro ao load arquivo stage_file.csv: {e}")
