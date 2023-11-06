def exists_word(word, instance):
    files = list()
    for index in range(len(instance)):
        ocorrencias = list()
        file = instance.search(index)
        ocorrencias = [
            {"linha": i + 1}
            for i, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if len(ocorrencias) > 0:
            files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return files


instance = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['hello', 'henrique', 'how are you?']
    },
    {
        "nome_do_arquivo": "arquivo_teste2.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['hi', 'amanda', 'how are you?']
    },
    {
        "nome_do_arquivo": "arquivo_teste3.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ['hey', 'you', 'how are you?', 'he is fine']
    }
]

# print(exists_word('he', instance))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
