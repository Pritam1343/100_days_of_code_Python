def format_string(f_name,l_name):
    """This take first name and last name and converts
    into the title case with the new version of the input string""" #This is Docstring
    formated_f=f_name.title()
    formated_l=l_name.title()
    return f"{formated_f} {formated_l}"

print(format_string("PRITAM","mOGAL"))