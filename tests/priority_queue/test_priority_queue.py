from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    file1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ['linha1', 'linha2', 'linha3', 'linha4']
    }
    priority_queue.enqueue(file1)
    assert len(priority_queue) == 1

    file2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo":
            [
                'ola',
                'como vai',
                'teste',
                'projeto',
                'TING',
                'requisito6',
                'queue',
            ]
    }
    priority_queue.enqueue(file2)
    assert len(priority_queue) == 2

    assert priority_queue.is_priority(file1) is True
    assert priority_queue.is_priority(file2) is False

    assert priority_queue.search(1) == file2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-1)

    assert priority_queue.dequeue() == file1
