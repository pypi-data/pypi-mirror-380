import socket
import sys
import logging
import hashlib

# Configuration du logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class celyatrix_ami:
    def __init__(self, host, port, username, password, nivdebug=3):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.nivdebug = nivdebug
        self.sock = None

    def connect(self):
        """
        Se connecte à Asterisk AMI et s'authentifie.
        """
        try:
            # Création de la socket TCP
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))

            challenge_response = self.send_action(f"Action: Challenge\r\nAuthType: MD5")

            if challenge_response and "Response: Success" in challenge_response:
                # Récupérer le challenge
                challenge = self.parse_response(challenge_response)['Challenge']
           #     sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ  Valeur challenge : "+str(type(challenge))+"\n")
                m = hashlib.md5()
                m.update(challenge.encode())
                m.update(self.password.encode())
                self.key = m.hexdigest()
               # sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ  Valeur challenge : "+self.key+"\n")

                login_response = self.send_action(f"Action: Login\r\nUsername: {self.username}\r\nAuthType: MD5\r\nSecret: {self.password}\r\nKey: {self.key}\r\n")
               # sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n" + "login_response " + "\n")
                if 'Response: Success' in login_response:
                    logger.info("Authentification réussie avec AMI.")
                    return True
                else:
                    logger.error("Échec de l'authentification AMI.")
                    self.sock.close()
                    return False
            else:
                logger.error("Problème lors de la récupération du challenge AMI.")
                self.sock.close()
        except Exception as e:
            logger.error(f"Erreur lors de la connexion : {e}")
            if self.sock:
                self.sock.close()


    def Challenge(self, auth_type="MD5"):

        # Envoyer la commande Challenge avec le type d'authentification
        challenge_action = f"Action: Challenge\r\nAuthType: {auth_type}\r\n\r\n"

        try:
            self.sock.sendall(challenge_action.encode())
        except Exception as e:
            sys.stderr.write(f"Erreur lors de l'envoi de la commande Challenge: {e}\n")
            return None

        # Lire la réponse
        try:
            response = b""
            while True:
                data = self.sock.recv(1024)
                response += data
                if b'\r\n\r\n' in response:  # Fin de la réponse AMI
                    break

            response = response.decode()
            sys.stderr.write(f"Réponse au challenge: {response}\n")
        except Exception as e:
            sys.stderr.write(f"Erreur lors de la réception de la réponse: {e}\n")
            return None

        # Traiter la réponse pour extraire le challenge
        if "Challenge" in response:
            parsed_response = self.parse_response(response)
            challenge_value = parsed_response.get("Challenge")
            #sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZz Valeur du challenge : " + challenge_value + "\n")
            return challenge_value
        else:
            sys.stderr.write(f"Erreur Challenge incorrect  \n")
            return None

    def send_action(self, Action):
        """
        Envoie une commande AMI au serveur Asterisk et retourne la réponse.
        """
        try:
            # Envoie de la commande
            self.sock.sendall(f"{Action}\r\n\r\n".encode())
            response = b""
            while True:
                data = self.sock.recv(1024)
                if not data:
                    break
                response += data
                if b'\r\n\r\n' in response:
                    break

            return response.decode()
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de la commande : {e}")
            return None



    def monitor_connection(self):
        """
        Vérifie si la connexion AMI est active.
        """
        try:
            response = self.send_action({'Action': 'Ping'})
            if 'Response: Success' in response:
                logger.info("Connexion AMI active.")
             #   sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZ CONNEXION AMI REUSSI \n ")
            else:
              #  sys.stderr.write("ZZZZZZZZZZZZZZZZZZZZZZ CONNEXION AMI FAIL \n ")
                logger.info("Connexion AMI fail.")
        except Exception as e:
            logger.error(f"Erreur lors de la vérification dela connexion : {e}")

    def monitor_channel(self, channel, id_com):
        """
        Active l'enregistrement (Monitor) d'un canal spécifique.
        """
        try:
            if self.nivdebug >= 1:
                logger.info(f"{id_com} : Activation du monitor sur la CHANNEL : {channel} pour l'ID_COM : {id_com}")

            response = self.send_action(f"Action: Monitor\r\nChannel: {channel}\r\nFile: /var/spool/asterisk/monitor/record_{id_com}")
            if 'Response: Success' in response:
                logger.info(f"Monitor activé sur le canal {channel} pour l'ID_COM {id_com}.")
            else:
                logger.error(f"Échec de l'activation du monitor sur le canal {channel} pour l'ID_COM {id_com}.")
        except Exception as e:
            logger.error(f"Erreur lors de l'activation du monitor : {e}")
    
    def Monitor(self, FILENAME):
        sys.stdout.write("MONITOR %s\n" % (FILENAME))
        sys.stdout.flush()


    def parse_response(self, response):
        """
        Parse une réponse AMI en dictionnaire.
        """
        lines = response.strip().split("\r\n")
        response_dict = {}
        for line in lines:
            if ": " in line:
                key, value = line.split(": ", 1)
                response_dict[key] = value
        return response_dict

    def close(self):
        """
        Ferme la connexion AMI.
        """
        if self.sock:
            self.send_action({'Action': 'Logoff'})
            self.sock.close()
            logger.info("Déconnexion d'Asterisk AMI réussie.")
