import os
import time
import requests
from dhooks import Webhook
import discord
import colorama
import asyncio


os.system("title Webhook Deleter - github.com/jayshimself")


def deletewebhook():
    delete = input("Webhook?: ")
    webhook = Webhook(delete)
    webhook.send("@everyone jays#0023")
    requests.delete(delete)

def delete():
    print(" [>] Completed Webhook Deletion + Sent message")
    asyncio.sleep(2)
    os.system("exit")



deletewebhook()
delete()
