import re


def typographical_text(text):
    return replace_substring(text)

def replace_substring(text):
    regexp_for_replace = {' {2,}': ' ',
                          r'\t{2,}': r'\t',
                          '\(c\)': '&copy;',
                          r'\b(\w+)(\b[ \t]+\b\1\b)*': delete_double_words,
                          r'\b(\w+)\b([ \t]+)\b(а|но)\b': add_comma_before_conjuction}
    for pattern, repl in regexp_for_replace.items():
        text = re.sub(pattern, repl, text)
    return text


def delete_double_words(match):
    return match.group(1)


def add_comma_before_conjuction(match):
    return ''.join([match.group(1), ',', match.group(2), match.group(3)])


if __name__ == '__main__':
    pass
