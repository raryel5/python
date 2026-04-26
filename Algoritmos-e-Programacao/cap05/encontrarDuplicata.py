a = [1, 2, 3, 5]

def containsDuplicate(vetor):
    tabelaHash = set()

    for item in vetor:
        if item in tabelaHash:
            return True
        
        tabelaHash.add(item)
    return False

print(containsDuplicate(a))