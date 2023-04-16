def sentences(sentence: str):
    return f"- {sentence}"


input_sentences = input().split(". ")
sentences_rows = map(sentences, input_sentences)
print('\n'.join(sentences_rows))

