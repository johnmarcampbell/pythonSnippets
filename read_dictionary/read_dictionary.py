import ast

def read_dictionary(dictionary_file):
    """ Reads a file containing a dictionary and returns that dictionary.
        This function ignores text outside of the curly braces, so that
        space may be used for comments.
    """

    nesting_level = 0
    dictionary_string = ''

    with open(dictionary_file) as f:
        for line in f:
            nesting_level += line.count('{')
            if nesting_level >= 1:
                dictionary_string += line
            nesting_level -= line.count('}')

    dictionary = ast.literal_eval(dictionary_string)
    return dictionary
