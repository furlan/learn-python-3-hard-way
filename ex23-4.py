import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
  line = language_file.readline()  # return one line (file position )

  if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
  raw_bytes = line
  next_lang = raw_bytes.decode(encoding, errors=errors)
  cooked_string = next_lang.encode(encoding, errors=errors)

  print(raw_bytes, " | ", next_lang, " <==> ", cooked_string)


languages = open("languages_byte.txt", 'r')

main(languages, input_encoding, error)
