import pygame
import os #Importar os så att jag kan hitta bilderna i assets-mappen


#Fixa så att man flyttar flera kort när man flyttar högsta
#Fixa så att korten inte hamnar på varandra
#fixa så att man kan lägga kungen på en tom yta
#Fixa bugg där man kan klicka på två kort samtidigt --> inget flyttar sig
#Man kan klicka på ett kort genom ett annat

#Fixa blandad kortlek, viktigt, svårt att göra


WIDTH, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Patiens") #Namnet på fönstret
fps = 240 #240Hz, snabba grejer
CARD_WIDTH, CARD_HEIGHT = 80, 120


ROW1 = 200
ROW2 = 350
ROW3 = 500
ROW4 = 650
ROW5 = 800

#är läser jag in alla bilder och gör om deras storlek
BACKGROUND = pygame.image.load(
    os.path.join('Assets', 'background.jpg')
)
RESIZED_BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RKUNG = pygame.image.load(
    os.path.join('Assets', 'ruterkung.png')
)
RESIZED_RKUNG = pygame.transform.scale(RKUNG, (80, 120))


HDAM = pygame.image.load(
    os.path.join('Assets', 'hdam.png')
)
RESIZED_HDAM = pygame.transform.scale(HDAM, (80, 120))

AXEL = pygame.image.load(
    os.path.join('Assets', 'axel.png')
)
RESIZED_AXEL = pygame.transform.scale(AXEL, (CARD_WIDTH, CARD_HEIGHT))

UPSIDE_DOWN_CARD = pygame.image.load(
    os.path.join('Assets', 'upside_down_card.png')
)
UPSIDE_DOWN_CARD_RESIZED = pygame.transform.scale(UPSIDE_DOWN_CARD, (CARD_WIDTH, CARD_HEIGHT))

K2 = pygame.image.load(
    os.path.join('Assets', 'klover_tva.png')
)
K2_RESIZED = pygame.transform.scale(K2, (CARD_WIDTH, CARD_HEIGHT))

H3 = pygame.image.load(
    os.path.join('Assets', 'hjarter_tre.png')
)
H3_RESIZED = pygame.transform.scale(H3, (CARD_WIDTH, CARD_HEIGHT))

R4 = pygame.image.load(
    os.path.join('Assets', 'ruter_fyra.png')
)
R4_RESIZED = pygame.transform.scale(R4, (CARD_WIDTH, CARD_HEIGHT))

#Skapar min klass Kort där jag kan skriva in kortets färg, om kortet är svart/rött, vilket värde kortet har, kortets koordinater och själva bilden som kortet använder
class Kort:
    def __init__(self, farg, sr_farg, varde, xpos, ypos, image):
        self.farg = farg
        self.varde = varde
        self.xpos = xpos
        self.ypos = ypos
        self.sr_farg = sr_farg
        self.image = image

#Skapar 6 kort
CARD1 = Kort("spader", "röd", 14, ROW4, 20, RESIZED_AXEL)
CARD2 = Kort("ruter", "svart", 13, ROW2, 20, RESIZED_RKUNG)
CARD3 = Kort("hjarter", "röd", 12, ROW3, 20, RESIZED_HDAM)
CARD4 = Kort("ruter", "röd", 4, ROW5, 20, R4_RESIZED)
CARD5 = Kort("hjarter", "röd", 3, ROW5, 50, H3_RESIZED)
CARD6 = Kort("klover", "svart", 2, ROW1, 20, K2_RESIZED)

#En array som innehåller alla korten. Typ som en kortlek
LIST_OF_CARDS = [CARD1, CARD2, CARD3, CARD4, CARD5, CARD6]

#Funktionen ritar alla kort samt bakgrunden
#Tar inte in några argument
#Returnerar inget
#Inga specialfall
#By: Oskar Skiöld Lundquist
#Date: 2022-05-30
def draw_window():
    WIN.blit(RESIZED_BACKGROUND, (0, 0))
    i = 0
    while i < len(LIST_OF_CARDS):
        current_card = LIST_OF_CARDS[i]
        WIN.blit(UPSIDE_DOWN_CARD_RESIZED, (current_card.xpos, current_card.ypos-10))
        i += 1

    i = 0
    while i < len(LIST_OF_CARDS):
        current_card = LIST_OF_CARDS[i]
        WIN.blit(current_card.image, (current_card.xpos, current_card.ypos))
        i += 1

    pygame.display.update()

#Funktionen flyttar ett kort till ett ställe under det andra
#Argument 1, card: Är det Kort som ska flyttas
#Argument 2, parent_card: Är det Kort som card ska flyttas till
#Funktionen returnar inget utan ändrar istället värdena på cards x- och ypos
#By: Oskar Skiöld Lundquist
#Date: 2022-05-30
def move_card(card, parent_card):
    card.xpos = parent_card.xpos
    card.ypos = parent_card.ypos + 30


#Denna funktionen kollar om ett visst kort går att flytta
#Argument 1, card: Det Kort som funktionen kollar om det är möjligt att flytta
#Argument2, list_of_cards: En array som innehåller alla kort.
#Return: Indexet för det Kort i list_of_cards som card kan flyttas till, finns inget kort returneras None
#By: Oskar Skiöld Lundquist
#Date: 2022-05-30
def is_moveable(card, list_of_cards):
    i = 0
    while i < len(list_of_cards):
        if list_of_cards[i].sr_farg != card.sr_farg and list_of_cards[i].varde == card.varde + 1 and list_of_cards[i].xpos != card.xpos:
            global parent_card
            parent_card = list_of_cards[i]
            return list_of_cards[i]

        i += 1

#Funktionen kollar om spelaren klickade på ett kort eller inte genom att skapa en rektangel för varje kort och sedan använde collidepoint för att kolla om spelaren klickade inom rektangeln.
#Argument 1, mousepos: Detta är musens position inom spelfönstret, beskrivs av python som (x, y).
#Return: Det kort som spelaren klickade på. Klickade spelaren inte på något kort returneras None.
#By: Oskar Skiöld Lundquist
#Date: 2022-05-30
def clicked_on_card(mousepos):
    i = 0
    while i < len(LIST_OF_CARDS):
        card_rect = pygame.Rect(LIST_OF_CARDS[i].xpos, LIST_OF_CARDS[i].ypos, CARD_WIDTH, CARD_HEIGHT)
        if card_rect.collidepoint(mousepos):
            return LIST_OF_CARDS[i]
        i += 1

#Main-funktionen. Härifrån går jag in i alla andra funktioner. Denna funktionen är också ansvarig för att stänga ner spelet om användaren trycker på krysset.
#Tar inte in några argument
#Returnerar inget
#By: Oskar Skiöld Lundquist
#Date: 2022-05-30
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                mousepos = pygame.mouse.get_pos()
                clicked_card = clicked_on_card(mousepos)
                if clicked_card is not None and is_moveable(clicked_card, LIST_OF_CARDS) is not None:
                    move_card(clicked_card, parent_card)

        draw_window()
    pygame.quit()


main()
