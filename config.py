#Cluster0luster0 Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8269134466:AAFv2KK3a0MFkzFyotbaLMOdDNNKlvnydUE")
APP_ID = int(os.environ.get("APP_ID", "25926022")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "30db27d9e56d854fb5e943723268db32") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003161888858")) #Your db channel Id
OWNER = os.environ.get("OWNER", "ZeeXDevBot") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "8140299716")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tgbot:4KzEdxEl4YldwwFR@tg.vr8ef.mongodb.net/?retryWrites=true&w=majority&appName=Tg")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "840"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/BTZF_CHAT")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://ibb.co/qLMmwR0y")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/qLMmwR0y")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>Besoin d'aide ?</blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ Ceci est un bot OpenSource qui vous offre des fichiers de Films/Series inédite</blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>Salut {first}\n\n<blockquote>Bienvenue sur l'un des meilleures plateformes de diffusion sur Télégram.\n\nTout les films et Séries  disponibles💥\n\n<a href='https://t.me/posterserie'>𝙿𝙾𝚂𝚃𝙴𝚁𝚂 𝚂𝙴𝚁𝙸𝙴𝚂</a>\n<a href='https://t.me/motiveflix'>𝐏𝐎𝐒𝐓𝐄𝐑𝐒 𝐅𝐈𝐋𝐌𝐒</a>\n\n😍 Abonnez-vous ici ! et partager pour pouvoir Télécharger 👌.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Salut {first}\n\n<b>Ɑνᥲᥒt Ꮷᥱ ρoυνoιɾ tᥱ́ᥣᥱ́ᥴhᥲɾɡᥱɾ νotɾᥱ 𝖿ιᥴhιᥱɾ, Vᥱυιᥣᥣᥱᴢ Ꮷ'ᥲᑲoɾᏧ ɾᥱȷoιᥒᏧɾᥱ ɱᥱs ᥴᥲᥒᥲυx.\n\nSᥱυᥣᥱs ᥣᥱs ρᥱɾsoᥒᥒᥱs ᥲᑲoᥒᥒᥱ́ᥱs ᥲ̀ ɱᥱs ᥴᥲᥒᥲυx o𝖿𝖿ιᥴιᥱᥣs ᥴι-Ꮷᥱssoυs ρᥱυνᥱᥒt ᥱ𝖿𝖿ᥱᥴtυᥱɾ Ꮷᥱs tᥱ́ᥣᥱ́ᥴhᥲɾɡᥱɱᥱᥒts..</b>")

CMD_TXT = """<blockquote><b>» Commandes administrateur :</b></blockquote>

<b>›› /dlt_time :</b> Définir le temps de suppression automatique
<b>›› /check_dlt_time :</b> Vérifier le temps de suppression actuel
<b>›› /dbroadcast :</b> Diffuser un document/vidéo
<b>›› /ban :</b> Bannir un utilisateur
<b>›› /unban :</b> Débannir un utilisateur
<b>›› /banlist :</b> Obtenir la liste des utilisateurs bannis
<b>›› /addchnl :</b> Ajouter un canal d'abonnement obligatoire
<b>›› /delchnl :</b> Supprimer un canal d'abonnement obligatoire
<b>›› /listchnl :</b> Voir les canaux ajoutés
<b>›› /fsub_mode :</b> Activer/désactiver le mode abonnement obligatoire
<b>›› /pbroadcast :</b> Envoyer une photo à tous les utilisateurs
<b>›› /add_admin :</b> Ajouter un administrateur
<b>›› /deladmin :</b> Supprimer un administrateur
<b>›› /custom_batch : </b> Batch personnalisée</b>
<b>›› /pbroadcast : pour envoyer un message à épinglé
<b>›› /dbroadcast : pour envoyer un message éphémere aux utilisateurs
<b>›› /admins :</b> Obtenir la liste des administrateurs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) #Définissez votre légende personnalisée ici, mettez None pour désactiver
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #Mettez True si vous voulez empêcher le transfert de fichiers depuis le bot
#--------------------------------------------
#Mettez True si vous voulez désactiver le bouton de partage des posts du canal
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False'
#--------------------------------------------
BOT_STATS_TEXT = "<b>TEMPS DE FONCTIONNEMENT DU BOT</b>\n{uptime}"
USER_REPLY_TEXT = "Impossible d'utilisé ! Vous n'êtes pas un administrateur !!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
