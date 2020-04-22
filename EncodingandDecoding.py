# Create a py file that encodes and decodes every individual line in textfile.txt
#DBES
#Decode bytes encode bytes
import sys
script, input_encoding, error = sys.argv


def main(textfile, encoding, errors):
    line = textfile.readline()
    if line:
        print_line(line, encoding, errors)
        return main(textfile, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    byte_string = next_lang.encode(encoding, errors=errors)
    utf_string = byte_string.decode(encoding, errors=errors)
    print(byte_string, "<====>", utf_string)

languages = open("textfile.txt", encoding="utf-8")
main(languages, input_encoding, error)
