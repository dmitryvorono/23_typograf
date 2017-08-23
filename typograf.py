import re


def typographical_text(text):
    regexp_for_replace = {' {2,}': ' ',
                          r'\t{2,}': r'\t',
                          '\(c\)': '&copy;',
                          r'\b(\w+)(\b[ \t]+\b\1\b)*': delete_double_words,
                          r'\b(\w+)\b([ \t]+)\b(а|но)\b': add_comma_before_conjuction,
                          r'\b(\w+)\b([ \t]+)\b(то|либо|нибудь|ка|де|кась|таки)\b': add_hyphen_before_postfix,
                          r'\b(кое|кой)\b([ \t]+)\b(\w{2,})\b': add_hyphen_after_postfix,
                          r'(\W)\1': delete_double_symbols,
                          r'([^\w]+)(-+)[ \t]+': change_hyphen_to_mdash,
                          r'\b(\w+)\b([ \t]+)([.,:\!\?]+)': delete_spaces_before_punctuation,
                          r'([.,:\!\?]+)(\w+)': add_space_after_punctuation,
                          r'[ \t]+%': '%',
                          r'\([ \t]+': '(',
                          r'[ \t]+\)': ')',
                          r'\b(\w+)\b(\()': add_space_before_bracket,
                          r'[ \t]("|\')': ' &laquo;',
                          r'(\w+)("|\')': change_right_quotes_to_raquo,
                          r'\b(\w{1,3})\b([ \t]+)': bind_small_word_to_next_word,
                          r'[\d\+]{1,}[\d\-]{3,15}': change_hyphen_to_ndash,
                          r'([\d]+)([ \t])(\w+)': bind_digit_to_next_word}
    for pattern, repl in regexp_for_replace.items():
        text = re.sub(pattern, repl, text)
    return text


def delete_double_words(match):
    return match.group(1)


def add_comma_before_conjuction(match):
    return ''.join([match.group(1), ',', match.group(2), match.group(3)])


def add_hyphen_before_postfix(match):
    return ''.join([match.group(1), '-', match.group(3)])


def add_hyphen_after_postfix(match):
    return ''.join([match.group(1), '-', match.group(3)])


def delete_double_symbols(match):
    return match.group(1)


def delete_spaces_before_punctuation(match):
    return ''.join([match.group(1), match.group(3)])


def add_space_after_punctuation(match):
    return ''.join([match.group(1), ' ', match.group(2)])


def add_space_before_bracket(match):
    return ''.join([match.group(1), ' ', match.group(2)])


def change_hyphen_to_mdash(match):
    return ''.join([match.group(1), '&nbsp;&mdash;&nbsp;'])


def bind_small_word_to_next_word(match):
    return ''.join([match.group(1), '&nbsp;'])


def change_right_quotes_to_raquo(match):
    return ''.join([match.group(1), '&raquo;'])


def change_hyphen_to_ndash(match):
    return re.sub('-', '&ndash;', match.group(0))


def bind_digit_to_next_word(match):
    return ''.join([match.group(1), '&nbsp;', match.group(3)])


if __name__ == '__main__':
    pass
