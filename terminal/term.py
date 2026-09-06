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
def function():

    path_arg = sys.argv[2]


    with open(path_arg,'r') as flr:

        data = flr.readlines()

        for info in data:

            print(info)

        flr.close()


if s1 == cmd['read_file']:

    function()

# gonna fix up some ideas later...