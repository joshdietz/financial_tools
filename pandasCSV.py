import csv
import pandas as pd

def getProfile(x):
    profile = 'ProfileWF.csv'
    Pre_name = []
    Pre_print = []
    i = 0

    #reads preset.csv
    with open(profile, 'r') as csv_file:
        preset = csv.reader(csv_file)
        for row in preset:
            if i == 0:
                Pre_name = row
                i += 1
            if i == 1:
                Pre_print = row

        if x == 0:
            print('name')
            print(Pre_name)
            return Pre_name

        if x == 1:
            print('print')
            print(Pre_print)
            return Pre_print  

def makeProfile(x, columns, to_print, read_num_columns):

    #column names
    if x == 0:
    
        for i in range(read_num_columns):
            columns.append(input('Column {} name: '.format(i+1)))
            print(columns)

        return columns

    #columns to print 
    if x == 1:

        for i in range(read_num_columns):
           
            if columns[i] != to_print[i]:
                to_print[i] = input('Print column {}? (y/n) '.format(i+1))
            print(to_print)

        return to_print

def trimCSV():
    #calls getProfile or makeProfile to get column names and define columns to print

    #file = input('File name: ')
    file = 'C:/Users/jacob/Downloads/Checking1.csv'

    #reads csv
    df = pd.read_csv(file, sep=',', header=None)
    read_num_columns = len(df.axes[1])
    
    #print all rows 
    pd.set_option('display.max_rows', None)

    preset = 0

    #asks if column names have been created
    columns = [] 
    if input('Have you created column names? (y/n) ') == 'y':
        preset = 1
        columns = getProfile(0)
        df.columns = columns
    
    else:

        #names columns and uses makeProfile method
        print('Read {} columns'.format(read_num_columns))                
        df.columns = makeProfile(0, columns, 0 ,read_num_columns)

    #asks if column names have been created
    to_print_columns = []
    if preset == 1:
        
        to_print = getProfile(1)

    else:
        #choose which colums print 
        to_print = []
        for i in range(len(columns)):
            to_print.append('')
           
        #calls makeProfile method
        to_print = makeProfile(1, columns, to_print, read_num_columns)

    #creats new list of columns to print
    for i in range(len(columns)):
        if to_print[i] == 'y':
            to_print_columns.append(columns[i])
        
    trimed_CSV = df[to_print_columns]

    #prints trimed csv
    print('\n')
    print('File: {}'.format(file))
    print(trimed_CSV)


    #groups by date and calls groupByDate method
    date = df[columns[0]]
    columns_no_date = []
    for i in range(read_num_columns):
        if i == 0:
            continue
        if columns[i] == '':
            continue
        else:
            columns_no_date.append(columns[i])
    
    groupByDate(df, columns[0], date, to_print, trimed_CSV, columns_no_date)

def groupByDate(df, columns, date, to_print, trimed_CSV, columns_no_date):
    input()
    df['YearMonth'] = pd.to_datetime(date).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))
    
    print(df['YearMonth'])
    print(columns_no_date)
    input()
    res = df.groupby('YearMonth')[columns_no_date].nunique()
    
    print(res)
    
def combineCSV():
    pass

def reorderCSV():
    pass

def classifyCSV(trimed_CSV):
    
    #add column to trimed_CSV
    trimed_CSV['Class'] = ''
    trimed_CSV['Vendor'] = ''

    print(trimed_CSV)


if __name__ == '__main__':

    trimCSV() 