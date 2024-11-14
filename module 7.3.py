class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        listofsigns = [',', '.', '=', '!', '?', ';', ':']
        all_words = {}
        for i in range(len(self.file_names)):
            line_fixed = []
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                for line in file:
                    k = 0
                    while (' - ' or ' — ') in line:
                        k += 1
                        line = line.replace(' - ', ' ', k)
                    while ' — ' in line:
                        k += 1
                        line = line.replace(' — ', ' ', k)
                    line = line.lower()
                    line = line.replace('\n', '', 1)
                    for char in range(len(line)):
                        for j in listofsigns:
                            if line[char] != j:
                                continue
                            else:
                                line = line[:char] + '' + line[char + 1:] + ' '
                    line = line.split(' ')
                    line = [i for i in line if i]
                    for z in range(len(line)):
                        line_fixed.append(line[z])
            all_words.update({self.file_names[i] : line_fixed})
        return all_words
    def find(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word not in words:
                continue
            return {name: words.index(word) + 1}
    def count(self, word):
        word = word.lower()
        for name, words in self.get_all_words().items():
            return {name: words.count(word)}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
