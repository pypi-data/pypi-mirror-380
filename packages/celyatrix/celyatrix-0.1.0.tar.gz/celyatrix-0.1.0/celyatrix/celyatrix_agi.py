import sys
import re
import time
import random
import socket

ami_credentials = {'host': '127.0.0.1', 'port': 5038, 'username': 'admin', 'password': 'password'}

class celyatrix_agi:
    def __init__(self):  # Read and ignore AGI environment (read until blank line)
        self.ReadAgi()

    def ReadAgi(self):
        self.env = {}
        tests = 0;

        while 1:
            line = sys.stdin.readline().strip()

            if line == '':
                break
            key,data = line.split(':')
            if key[:4] != 'agi_':
                #skip input that doesn't begin with agi_
                sys.stderr.write("Did not work!\n");
                sys.stderr.flush()
                continue
            key = key.strip()
            data = data.strip()
            if key != '':
                self.env[key] = data

       # sys.stderr.write("AGI Environment Dump:\n");
       # sys.stderr.flush()
       # for key in self.env.keys():
        #    sys.stderr.write(" -- %s = %s\n" % (key, self.env[key]))
         #   sys.stderr.flush()
        # return env

    def Exec(self, command):
        sys.stdout.write("EXEC %s\n" % command)
        sys.stdout.flush()

        response = sys.stdin.readline().strip()
        sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ " + response + "\n")
        

    def execute(self, command):
        sys.stdout.write("EXEC %s\n" % command)
        sys.stdout.flush()
        response = sys.stdin.readline().strip()

    def SetVariable(self, VARIABLENAME, VALUE):
        sys.stdout.write(f'SET VARIABLE {VARIABLENAME} "{VALUE}"\n')
        sys.stdout.flush()
        response = sys.stdin.readline().strip()      

    def GetVariable(self, VARIABLENAME):
        # Envoie la commande pour obtenir la variable
        sys.stdout.write("GET VARIABLE %s\n" % VARIABLENAME)
        sys.stdout.flush()

        # Lis la réponse depuis stdin
        response = sys.stdin.readline().strip()
        analyseResponse = re.search(r'\(([^)]+)\)', response)

        if analyseResponse:
            if type(analyseResponse.group(1)) != "NoneType":
                finalResponse = analyseResponse.group(1)
            else:
                finalResponse = None
        else:
            finalResponse = None

        # On peut s'attendre à ce que la réponse soit au format "VALUE: <value>"
        # Traite la réponse
        if finalResponse:
            return finalResponse  # Retourne la valeur sans espaces
        else: 
            return None  # Retourne None si la réponse n'est pas valide


    def StreamFile(self, FILENAME ):
        #sys.stdout.write('STREAM FILE %s "" \n' % (FILENAME))
        sys.stderr.write("JPR " + f"STREAM FILE {FILENAME} \"\" \n")
        sys.stdout.write(f"STREAM FILE {FILENAME} \"\" \n")
        sys.stdout.flush()
        response = sys.stdin.readline().strip() 
        analyseResponse = re.search(r'\(([^)]+)\)', response)
        if analyseResponse:
            if type(analyseResponse.group(1)) != "NoneType":
                finalResponse = analyseResponse.group(1)
            else:
                finalResponse = None
        else:
            finalResponse = None
     #   if finalResponse:
   #         return finalResponse
    #    else:
    #        return None
          
    def Login(self, USERNAME, SECRET):
        sys.stdout.write("LOGIN %s %s\n" % (USERNAME, SECRET))
        sys.stdout.flush()
        response = sys.stdin.readline().strip()

    def Monitor(self, FILENAME):
        sys.stdout.write("MONITOR %s\n" % (FILENAME))
        sys.stdout.flush()
        response = sys.stdin.readline().strip()

    def get_environment(self):
        return self.env
