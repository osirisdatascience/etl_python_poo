
import logging
import os

def configurar_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/execucao.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
