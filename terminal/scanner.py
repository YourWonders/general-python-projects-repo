import sys, logging


lg = logging.basicConfig(level=logging.INFO,
                         format="""
LEVEL => %(levelname)s
INFORMATION => %(message)s
TIME OF INCIDENT => %(asctime)s
"""
)

LOW_WARNING = 25
logging.addLevelName(LOW_WARNING, 'LOW WARNING')


try:

    s1 = sys.argv[1]
    cmd = {'read_file':'-rd',
        'write_file':'-wr',
        'csv_read':'-csv--read'}
    
except IndexError:

    print("Missing commands")

# ------------------------------------------------

key_words = ['cookie','cookies','Cookie','Cookies','browser','ip','isp']

# ------------------------------------------------
def readFunction():

    path_arg = sys.argv[2]


    with open(path_arg,'r') as flr:

        data = flr.readlines()

        def searchFunction(k,p):

            for i in k:
                for j in p:

                    if i in j:

                        logging.log(LOW_WARNING, f'keyword "{i}" has been found')

                    else:
                        continue

        searchFunction(key_words,data)


        flr.close()

# ----- read function ends here -----------


def writeFunction():

    path_write = sys.argv[2]

    with open(path_write, '+a') as wrfl:

        while 1:

            user_input = input('[WRITE] ')
            wrfl.writelines(user_input + '\n')

            if user_input == '#':
                wrfl.close()
                break




# ----- write function ends here -----------


def csvReadFunction():

    print('[WARNING] you must have make a CSV file or atleast make one\n')

    csv_read = sys.argv[2]

    with open(csv_read, 'r') as csvFileR:

        data = csvFileR.readlines()

        for i in data:

            print(i)

        csvFileR.close()

# ----- csv read function ends here -----------

if s1 == cmd['read_file']:

    readFunction()

elif s1 == cmd['write_file']:

    writeFunction()


elif s1 == cmd['csv_read']:

    csvReadFunction()


elif s1 == 'help':

    print("Current commands")

    for key, itm in cmd.items():

        print(key,itm,sep=' -> ')

else:

    print(f'command {s1} does not exist')