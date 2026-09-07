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



s1 = sys.argv[1]
cmd = {'read_file':'-rd'}

# ------------------------------------------------

key_words = ['cookies','ip']

# ------------------------------------------------
def function():

    path_arg = sys.argv[2]


    with open(path_arg,'r') as flr:

        data = flr.readlines()

        def searchFunction(k,p):

            for i in k:
                for j in p:

                    if i in j:

                        logging.log(LOW_WARNING, f'key word "{i}" has been found')

                    else:
                        continue
            

        searchFunction(key_words,data)


        flr.close()


if s1 == cmd['read_file']:

    function()

