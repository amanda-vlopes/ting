from ting_file_management.file_management import txt_importer
# import sys


def process(path_file, instance):
    for index in range(len(instance)):
        file = instance.search(index)
        if file["nome_do_arquivo"] == path_file:
            return 'Nome do arquivo já existe no sistema'

    linhas_do_arquivo = txt_importer(path_file)

    save_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas":  len(linhas_do_arquivo),
        "linhas_do_arquivo": linhas_do_arquivo
    }

    instance.enqueue(save_file)
    print(save_file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
