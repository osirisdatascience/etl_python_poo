from src.pipeline import Pipeline
from tarefas.extract import Extract
from tarefas.transform import Transform
from tarefas.load import Load
from utils.logger import configurar_logger

if __name__ == "__main__":
    configurar_logger()

    pipeline = Pipeline([Extract(), Transform(), Load()])

    pipeline.executar()
