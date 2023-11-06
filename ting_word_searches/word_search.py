def exists_word(word, instance):
    files = list()
    for index in range(len(instance)):
        ocorrencias = list()
        file = instance.search(index)
        ocorrencias = [
            {"linha": i + 1}
            for i, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()]
        if len(ocorrencias) > 0:
            files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return files


def search_by_word(word, instance):
    files = list()
    for index in range(len(instance)):
        ocorrencias = list()
        file = instance.search(index)
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": i + 1, "conteudo": line})
        if len(ocorrencias) > 0:
            files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return files
