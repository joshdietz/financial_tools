import pandas as pd

def testCSV():
    file = input('File name: ')
    #C:/Users/jacob/Downloads/Checking1.csv

    #reads csv
    df = pd.read_csv(file, sep=',', header=None)
    read_num_columns = len(df.axes[1])
    print('Read {} columns'.format(read_num_columns))

    #names columns 
    #num_columns = int(input('Number of columns: ')) 
    columns = [] 

    for i in range(read_num_columns):
        columns.append(input('Column {} name: '.format(i+1)))
        print(columns)

    #names csv columns 
    df.columns = columns

    #choose which colums print
    to_print = []

    for i in range(read_num_columns):
        if columns[i] == '':
            to_print_columns.append(columns[i])
        else:
            to_print.append(input('Print column {}? (y/n) '.format(i+1)))
        print(to_print)

    to_print_columns = []
    for i in range(read_num_columns):
        if to_print[i] == 'y':
            to_print_columns.append(columns[i])

    #prints csv
    print('\n')
    print('File: {}'.format(file))
    print(df[to_print_columns])