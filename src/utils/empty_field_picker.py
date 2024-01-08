import random


def fill_form_with_empty_random_field(form_fields, number_of_fields):
    no_fill_num = random.randint(1, number_of_fields)
    for i in range(1, number_of_fields + 1):
        if i == no_fill_num:
            continue
        else:
            field, value = form_fields[i]
            field.send_text(value)
    return no_fill_num
