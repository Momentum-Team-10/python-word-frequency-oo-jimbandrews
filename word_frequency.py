import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as opened_file:
            file_string = opened_file.read()
        return file_string


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        zero_punctuation = self.text.lower()
        punctuation = string.punctuation + "’" + "”" + "“"
        for char in punctuation:
            if char in zero_punctuation:
                zero_punctuation = zero_punctuation.replace(char, '')
        replace_whitespace = ["\n", "—", "  "]
        for char in replace_whitespace:
            if char in zero_punctuation:
                zero_punctuation = zero_punctuation.replace(char, " ")
        self.text = zero_punctuation.split(' ')

# do i want to keep sel.text as string or change to a list?
    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        if type(self.text) == str:
            return print("Please run extract_words first.")
        words_copy = self.text.copy()
        for word in words_copy:
            if word in STOP_WORDS:
                self.text.remove(word)

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        word_count = {}
        for word in self.text:
            if word == '':
                continue
            elif word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        max_length = max([len(word) for word in self.freqs])
        max_freq = max(self.freqs.values())
        frequency_groups = []
        while max_freq > 0:
            frequency_groups.append([])
            max_freq -= 1
        for word in self.freqs:
            frequency_groups[0-self.freqs[word]].append(word)
        list_count = 0
        for group in frequency_groups:
            group.sort()
            for word in group:
                freq = self.freqs[word]
                spaces = (max_length - len(word)) * " "
                if freq < 10:
                    stars = "  " + freq * "*"
                else:
                    stars = " " + freq * "*"
                print(f" {spaces}{word} | {freq}{stars}")
                list_count += 1
                if list_count == 25:
                    break
            if list_count == 25:
                break


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
