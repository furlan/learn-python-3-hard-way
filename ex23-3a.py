from os import write
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, output_file, errors):
  line = language_file.readline()  # return one line (file position )

  if line:
    print_line(line, encoding, errors)
    output_line = line.strip().encode(encoding, errors=errors)
    output_file.write(output_line)
    return main(language_file, encoding, output_file, errors)


def print_line(line, encoding, errors):
  next_lang = line.strip()  # remove the white spaces
  raw_bytes = next_lang.encode(encoding, errors=errors)
  cooked_string = raw_bytes.decode(encoding, errors=errors)

  print(raw_bytes, " <==> ", cooked_string)


languages = open("languages.txt", encoding="utf-8")
output = open("languages_output.enc", 'wb')

main(languages, input_encoding, output, error)
output.close()
