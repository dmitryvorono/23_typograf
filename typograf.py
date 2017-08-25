import re
import collections


def typographical_text(text):
    regexp_for_replace = collections.OrderedDict()
    regexp_for_replace[' {2,}'] = ' '
    regexp_for_replace[r'\t{2,}'] = r'\t'
    regexp_for_replace['\(c\)'] = '&copy;'
    regexp_for_replace[r'\b(\w+)(\b[ \t]+\b\1\b)*'] = delete_double_words
    regexp_for_replace[r'\b(\w+)\b([ \t]+)\b(а|но)\b'] = add_comma_before_conjuction
    regexp_for_replace[r'\b(\w+)\b([ \t]+)\b(то|либо|нибудь|ка|де|кась|таки)\b'] = add_hyphen_before_postfix
    regexp_for_replace[r'\b(кое|кой)\b([ \t]+)\b(\w{2,})\b'] = add_hyphen_after_postfix
    regexp_for_replace[r'(\W)\1'] = delete_double_symbols
    regexp_for_replace[r'([^\w]+)(-+)[ \t]+'] = change_hyphen_to_mdash
    regexp_for_replace[r'\b(\w+)\b([ \t]+)([.,:\!\?]+)'] = delete_spaces_before_punctuation
    regexp_for_replace[r'([.,:\!\?]+)(\w+)'] = add_space_after_punctuation
    regexp_for_replace[r'[ \t]+%'] = '%'
    regexp_for_replace[r'\([ \t]+'] = '('
    regexp_for_replace[r'[ \t]+\)'] = ')'
    regexp_for_replace[r'\b(\w+)\b(\()'] = add_space_before_bracket
    regexp_for_replace[r'[ \t]("|\')'] = ' &laquo;'
    regexp_for_replace[r'(\w+)("|\')'] = change_right_quotes_to_raquo
    regexp_for_replace[r'\b(\w{1,3})\b([ \t]+)'] = bind_small_word_to_next_word
    regexp_for_replace[r'[\d\+]{1,}[\d\-]{3,15}'] = change_hyphen_to_ndash
    regexp_for_replace[r'([\d]+)([ \t])(\w+)'] = bind_digit_to_next_word
    for pattern, repl in regexp_for_replace.items():
        text = re.sub(pattern, repl, text)
    return text


def delete_double_words(match):
    one_word = 1
    return match.group(one_word)


def add_comma_before_conjuction(match):
    word = 1
    spaces = 2
    conjuction = 3
    return ''.join([match.group(word), ',', match.group(spaces), match.group(conjuction)])


def add_hyphen_before_postfix(match):
    word = 1
    postfix = 3
    return ''.join([match.group(word), '-', match.group(postfix)])


def add_hyphen_after_postfix(match):
    postfix = 1
    word = 3
    return ''.join([match.group(postfix), '-', match.group(word)])


def delete_double_symbols(match):
    one_symbol = 1
    return match.group(one_symbol)


def delete_spaces_before_punctuation(match):
    word = 1
    punctuation = 3
    return ''.join([match.group(word), match.group(punctuation)])


def add_space_after_punctuation(match):
    punctuation = 1
    word = 2
    return ''.join([match.group(punctuation), ' ', match.group(word)])


def add_space_before_bracket(match):
    word = 1
    bracket = 2
    return ''.join([match.group(word), ' ', match.group(bracket)])


def change_hyphen_to_mdash(match):
    hyphen = 1
    return ''.join([match.group(hyphen), '&nbsp;&mdash;&nbsp;'])


def bind_small_word_to_next_word(match):
    small_word = 1
    return ''.join([match.group(small_word), '&nbsp;'])


def change_right_quotes_to_raquo(match):
    word = 1
    return ''.join([match.group(word), '&raquo;'])


def change_hyphen_to_ndash(match):
    telephone_number = 0
    return re.sub('-', '&ndash;', match.group(telephone_number))


def bind_digit_to_next_word(match):
    word = 1
    digit = 3
    return ''.join([match.group(word), '&nbsp;', match.group(digit)])


if __name__ == '__main__':
    pass
