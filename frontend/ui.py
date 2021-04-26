import PySimpleGUI as sg

from readData import readJSON
from readData import getGuildName

# define the window's content
layout = [[sg.Text("쿠키런: 킹덤 길드 관리")],
          ]

# window creator
def createWindow():
    sg.Window(title="CKR Guild Management", layout=layout, margins=(500,300)).read()

if __name__ == '__main__':
    createWindow()
    data = readJSON()
    guildName = getGuildName(data)
