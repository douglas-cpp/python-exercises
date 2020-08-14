# Creating your own iterators: https://www.youtube.com/watch?v=C3Z9lJXI6Qw
class SentenceToWords:
    def __init__(self, sentence: str):
        self.words: list = sentence.split()
        self.counter: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.words):
            raise StopIteration
        counter = self.counter
        self.counter += 1
        return self.words[counter]


def sentence_to_words(sentence: str):
    for word in sentence.split():
        yield word


if __name__ == "__main__":
    s = sentence_to_words('This is a test')
    for word in s:
        print(word)

    s = SentenceToWords('This is a test')
    for word in s:
        print(word)
