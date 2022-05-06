def cutoff(X, y, token_length):
    '''Remove samples from X an y where y has a token length > 150.'''
    removed = []
    for idx in reversed(range(len(y))):
        if len(y[idx]) > token_length:
            print(idx)
            removed.append((X[idx], y[idx]))
    return removed

def clean(dataset, vocab):
    '''Remove samples for which there is a token not included in the vocabulary.'''
    tokens = dataset[2]
    removed = []
    vocab = set(vocab)
    print(len(dataset[0]))
    for idx in reversed(range(len(tokens))):
        for token in tokens[idx].split():
            if not token in vocab:
                print(idx, token)
                removed.append(tuple(dataset[i].pop(idx) for i in range(4)))
                
    print(len(dataset[0]))
    return removed, dataset
                           
rem_cleaned, dataset = clean(dataset, vocab=vocab)