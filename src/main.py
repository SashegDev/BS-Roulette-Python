import pygame
from random import *
from os import system as sus
import time as t
from tkinter import messagebox as mb
from shotgun import *
pygame.mixer.init()
pygame.mixer.music.load("discl.mp3")
diskl = pygame.mixer.Sound("discl.mp3")
diskl.play(-1)
diskl.set_volume(0.1)
#pygame.mixer.music.load("dead.mp3")
items={
    0:'empty',
    1:'pivo',
    2:'handcuffs',
    3:'magnifying glass',
    4:'hand saw',
    5:'sigaratte'
}
ammo={
    0:'Blank',
    1:'Live',
}

TIME=1
rang=3

p_hp=2
d_hp=2
music=0

r_=1

u_input=0
u_items=[items[0]]
d_items=[]

gun=Shootgun(6)

sus("cls")
t.sleep(TIME)
print("Hi, this is Sasheg,\nI am wants to warn you that this game is gambling,\nAnd everything that happens in it does not need to be taken seriously.\nWell, it seems like the whole disclaimer,\nIf you want to start playing, write 'SHOOT'")
disc=input("\n>>> ")
if disc != 'SHOOT':
    exit
pygame.mixer.music.load("shoot.mp3")
shit = pygame.mixer.Sound("shoot.mp3")
shit.play(0)
shit.set_volume(0.5)
diskl.set_volume(0)
sus("cls")
pygame.mixer.music.load("menu.mp3")
back = pygame.mixer.Sound("menu.mp3")
back.play(-1)
back.set_volume(0.1)
name=input("\t\t\t   Welcome to Buckshot roulette,\n\n\tPlease, type your name in general release of liability to continue... \n\n>>> ")
name=name.upper()
if len(name) > 6:
    sus("cls")
    print("Welcome",name[:6])
elif name.lower() == 'god' or name.lower() == 'dealer':
    sus("cls")
    mb.showerror("Compile Error","Ti cho ebobo?\nDerji UserInputError #1")
    #mb.showinfo("Compile Error","ti cho ebobo? derji UserInputError #1")
    exit(1)
else:
    sus("cls")
    print("Welcome", name)
#mb.showinfo("HP Info",f"DEALER: {d_hp}\n{name}: {p_hp}")
t.sleep(TIME)
sus("cls")












def u_in():
    """u_in - это сокращение от user_input()\n
    Данная функция принимает значения от 1-7\n
    1 - выстрелить в диллера(если пустышка - ходит диллер)\n
    2 - выстрелить в себя(если пустышка пропуск хода диллера)\n
    3 - пиво(выброс патрона в патроннике) и продолжение данного хода\n
    (only dealer)4 - наручники(пропуск 2х ходов диллера)\n
    (no)5 - увеличительное стекло(при использовании ломается(удаляется) и показывает патрон в патроннике)\n
    (no)6 - ручная пила(срезает кусок ствола делая буквально из дробовика обрез, и делая х2 урон)\n
    (no)7 - пачка сигарет(добавляет 1 хп к тому кто ходит)\n
    """
    global TIME
    global ammo
    global gun
    global u_input
    global d_hp
    global p_hp
    global name

    if d_hp == 0:
        r()
    if p_hp ==0:
        mb.showerror("DEAD","You are dead.")
        exit(1)




    sus("cls")
    print(f"HP Info\nDEALER: {d_hp}\n{name}: {p_hp}\n")
    u_input=int(input("1 shot dealer\n2 shot yourself\n3 beer\nYour choise: "))

    if u_input == 1:
        shoot = gun.shoot()

        if shoot:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("shoot.mp3")
            shoot = pygame.mixer.Sound("shoot.mp3")
            shoot.play(0)
            shoot.set_volume(0.6)
            mb.showinfo("BOOM!","Dealer lost 1 HP!\nDealer turn")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            d_hp=d_hp-1
            dealer()

        else:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("cock.mp3")
            cock = pygame.mixer.Sound("cock.mp3")
            cock.play(0)
            cock.set_volume(0.6)
            mb.showerror("Oh....","Blank....\nDealer turn!")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            dealer()

    elif u_input == 2:
        shoot = gun.shoot()

        if shoot:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("shoot.mp3")
            shoot = pygame.mixer.Sound("shoot.mp3")
            shoot.play(0)
            shoot.set_volume(0.6)
            mb.showerror("BOOM!","You lost 1 HP!\nDealer turn")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            u_hp=u_hp-1
            dealer()

        else:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            cock = pygame.mixer.Sound("cock.mp3")
            cock.play(0)
            cock.set_volume(0.6)
            mb.showinfo("TICK!","It was blank.\nYour turn already :)")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            u_in()

    elif u_input == 3:
        shoot = gun.shoot()

        if shoot:
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            mb.showinfo("AMMO","It was live")
        else:
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            mb.showinfo("AMMO","It was blank")
        u_in()

    else:
        print("от 1 до 3 чё не ясно?")
        t.sleep(TIME)
        sus("cls")
        u_in()





def dealer():
    """ИИ диллера\n 
    dealer() - вызов 1 хода диллера
    """
    global TIME
    global gun
    global p_hp
    global d_hp
    if d_hp == 0:
        r()
    if p_hp == 0:
        mb.showerror("DEAD","You are dead.")
        exit(1)
    II = randint(1,3)
    t.sleep(TIME)
    if II == 1:
        mb.showinfo("SHOOT","Dealer want to try shoot you....")
        shoot = gun.shoot()
        if shoot:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("shoot.mp3")
            shoot = pygame.mixer.Sound("shoot.mp3")
            shoot.play(0)
            shoot.set_volume(0.6)
            mb.showerror("BOOM!","You lost 1 HP!\nYour turn")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            p_hp = p_hp - 1
            u_in()
        else:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("cock.mp3")
            cock = pygame.mixer.Sound("cock.mp3")
            cock.play(0)
            cock.set_volume(0.6)
            mb.showinfo("TICK!","It was blank!\nYour turn")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            u_in()
    elif II == 2:
        mb.showinfo("SHOOT","Dealer want to try shoot himself....")
        shoot = gun.shoot()
        if shoot:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("shoot.mp3")
            shoot = pygame.mixer.Sound("shoot.mp3")
            shoot.play(0)
            shoot.set_volume(0.6)
            mb.showinfo("BOOM!","Dealer lost 1 HP!\nYour turn")
            d_hp = d_hp-1
            u_in()
        else:
            mb.showinfo("Hmmmm","Hmmmmm")
            t.sleep(TIME)
            pygame.mixer.music.load("cock.mp3")
            cock = pygame.mixer.Sound("cock.mp3")
            cock.play(0)
            cock.set_volume(0.6)
            mb.showeinfo("TICK!","It was blank.\nDealer turn")
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            dealer()
    elif II == 3:
        shoot = gun.shoot()
        if shoot:
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            mb.showinfo("AMMO","It was live")
        else:
            pygame.mixer.music.load("rack.mp3")
            rack = pygame.mixer.Sound("rack.mp3")
            rack.play(0)
            rack.set_volume(0.3)
            mb.showinfo("AMMO","It was blank")
        dealer()
#   elif II == 4:
#       mb.showerror("USED ITEM","Dealer used handcuffs on you!")
#       II = randint(1,3)
#       if II == 1:
#           mb.showinfo("SHOOT","Dealer want to try shoot you....")
#           shoot = gun.shoot()
#           if shoot:
#               mb.showinfo("Hmmmm","Hmmmmm")
#               t.sleep(TIME)
#               mb.showinfo("BOOM!","You lost 1 HP!\nYour turn")
#               u_in()
#           else:
#               mb.showinfo("Hmmmm","Hmmmmm")
#               t.sleep(TIME)
#               mb.showinfo("TICK!","It was blank!\nYour turn")
#               u_in()
#       elif II == 2:
#           mb.showinfo("SHOOT","Dealer want to try shoot himself....")
#           shoot = gun.shoot()
#           if shoot:
#               mb.showinfo("Hmmmm","Hmmmmm")
#               t.sleep(TIME)
#               mb.showinfo("BOOM!","Dealer lost 1 HP!\nYour turn")
#               u_in()
#           else:
#               mb.showinfo("Hmmmm","Hmmmmm")
#               t.sleep(TIME)
#               mb.showinfo("TICK!","It was blank.\nDealer turn")
#               dealer()
#       elif II == 3:
#           mb.showinfo("BEER","Dealer skips current ammo....")
#           shoot = gun.shoot()
#           if shoot:
#               mb.showinfo("AMMO","It was live")
#           else:
#               mb.showinfo("AMMO","It was blank")
#           dealer()




def musicgame():
    pygame.mixer.music.load("game.mp3")
    au = pygame.mixer.Sound("game.mp3")
    au.play(-1)
    au.set_volume(0.1)
    r()

def game():
    global d_hp
    global p_hp
    global ammo
    global u_items
    global r_
    global rang
    global gun
    global u_in
    global back
    global music
    global au
    back.set_volume(0)
    if music == 0:
        au.set_volume(0)
        pygame.mixer.music.load("game.mp3")
        game = pygame.mixer.Sound("game.mp3")
        game.play(-1)
        game.set_volume(0.1)
    if r_ > 1:
        rang+=1
        u_items=[]
        u_items=u_items.append([items[random.randint(0,5)] for i in range(2)])
    #fill()
    gun.random_fill()
    pygame.mixer.music.load("load.mp3")
    load = pygame.mixer.Sound("load.mp3")
    load.play(6)
    load.set_volume(0.3)
    t.sleep(4)
    mb.showinfo("Ammo",gun.message_for_play())
    pygame.mixer.music.load("rack.mp3")
    rack = pygame.mixer.Sound("rack.mp3")
    rack.play(0)
    rack.set_volume(0.3)
    #mb.showinfo("Ammo",gun.message_for_dev())
    #mb.showinfo("Ammo",gun.message_for_play())
    print("Your items:\n",u_items)
    u_in()

def r():

    global back
    global r_
    global d_hp
    global p_hp
    global music
    music+=1
    if d_hp <= 0:
        r_+=1
        print("Round ended!\nStarting Round",r_)
        d_hp=2
        p_hp=2
        try:
            game()
        except NoAmmoException:
            r_+=1
            mb.showwarning("AMMO","Hmm\nNo ammo....\nHow unfortunate...")
            mb.showwarning("GAME","New ammos...")
            r()

    else:
        try:
            game()
        except NoAmmoException:
            r_+=1
            mb.showwarning("AMMO","Hmm\nNo ammo....\nHow unfortunate...")
            mb.showwarning("GAME","New ammos...")
            r()



musicgame()