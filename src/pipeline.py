
import logging

class Pipeline:
    def __init__(self, tarefas):
        self.tarefas = tarefas

    def executar(self):
        for tarefa in self.tarefas:
            try:
                tarefa.executar()
            except Exception as e:
                logging.error(f"Erro na tarefa {tarefa.nome}: {e}")
                break
