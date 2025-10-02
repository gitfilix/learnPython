def list_attributes(**kwargs):
    value_list = []
    for key, values in kwargs.items():
        print('values', values)
        value_list.append(values)

    return value_list


result = list_attributes(x='please', y='show', z='me', a='hi', b='there')
print('result', result)


def describe_person(name, **kwargs):
    print(f'Characteristics of {name}:')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


describe_person('Ash', eye_color="brown", hair_color="black")