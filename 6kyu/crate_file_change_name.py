
qq = print

init_filename = input('Enter a file name: ')
end_filename = init_filename.lower().replace(' ', '_') + '.py'
with open('C:/Users/misha/PycharmProjects/pythonProject/pythonProject/6kyu/' + end_filename, 'w') as file:
    qq(f'{end_filename}     file has been created!')
