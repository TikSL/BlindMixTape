from math import ceil

import pygame
import sys
from pygame import mixer, time, USEREVENT

import player
import ressources
from button import Button
from game_config import gameConfig
from mixtape import Mixtape
from vignette_joueur import VignetteJoueur
from volume_bar import VolumeBar


# screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen_width = 1280
screen_height = 720
print(screen_width, screen_height)


class GameState:
    def __init__(self):
        self.gameConf = gameConfig()
        mixer.music.unload()
        mixer.music.load("view/assets/AC theme.mp3")
        mixer.music.set_volume(0.1)
        time.set_timer(USEREVENT, 80)
        self.state = "main_menu"

    def _playAlignementJoueursBas_(self, nbrVignettes):
        total_width = screen_width * 0.097 * nbrVignettes
        espace_horizontal = (screen_width - total_width) / (nbrVignettes + 1)

        for index_vignette, vignette in enumerate(self.gameConf.listVignettes):
            position_x = espace_horizontal * (index_vignette + 1) + 0.097 * screen_width * index_vignette
            vignette.icon_croix = None
            vignette.setPos((position_x, screen_height - 0.24 * screen_height))

    def _attributionPointsAlignementJoueursMotif_(self, nbrVignettes):
        nbrVignettesHaut = ceil(nbrVignettes // 2)
        nbrVignettesBas = nbrVignettes - nbrVignettesHaut

        ecartVignettesHaut = (screen_width - nbrVignettesHaut * 0.097 * screen_width) / (nbrVignettesHaut + 1)
        ecartVignettesBas = (screen_width - nbrVignettesBas * 0.097 * screen_width) / (nbrVignettesBas + 1)

        for i, vignette in enumerate(self.gameConf.listVignettes):
            if i <= nbrVignettesHaut - 1:
                vignette.setPos(((0.097 * screen_width) * i + ecartVignettesHaut * (i + 1), 100))
            else:
                vignette.setPos(((0.097 * screen_width) * (i - nbrVignettesHaut) + ecartVignettesBas * (
                            i - nbrVignettesHaut + 1), 300))


    def main_menu(self):
        if not mixer.music.get_busy():
            mixer.music.play()

        current_image_index_floss = 0
        liste_image_floss = ressources.menuGIF

        elapsed_time1 = 0

        menuButtonPlay = Button(images=ressources.menuPlayButton, pos=(screen_width * 0.25, screen_height * 0.500),
                                text_input="PLAY",
                                font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
                                base_color="White",
                                hovering_color="#6DC300")

        menuButtonQuit = Button(images=ressources.menuQuitButton, pos=(screen_width * 0.250, screen_height * 0.700),
                                text_input="QUIT",
                                font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
                                base_color="White",
                                hovering_color="#CC191C")

        menuMousePosition = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(ressources.menuLogo,
                    (ressources.screen_width * 0.228, ressources.screen_height * 0.046))
        volume_bar.draw(screen)

        for button in [menuButtonPlay, menuButtonQuit]:
            button.changeColor(menuMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButtonPlay.checkForInput(menuMousePosition):
                    menuButtonPlay.press(screen)
                    self.state = "to_lobby"
                if menuButtonQuit.checkForInput(menuMousePosition):
                    menuButtonQuit.press(screen)
                    pygame.quit()
                    sys.exit()

            if event.type == USEREVENT:
                elapsed_time1 += 0.08
                if elapsed_time1 >= 15:
                    screen.blit(liste_image_floss[current_image_index_floss],
                                (screen_width * 0.571, screen_height * 0.400))
                    current_image_index_floss = (current_image_index_floss + 1) % 18

                pygame.display.flip()

            volume_bar.handle_event(event, mousePosition=menuMousePosition, screen=screen)

    def mainMenutoLobby(self):

        self.gameConf.listVignettes.append(VignetteJoueur(ressources.screen_width * 0.586, ressources.screen_height * 0.145))
        self.gameConf.listVignettes.append(VignetteJoueur(ressources.screen_width * 0.697, ressources.screen_height * 0.145))

        self.state = "lobby"

    def lobby(self):


        difficulty = ["FACILE", "MOYEN", "DIFFICILE"]

        lobbyTitreOption = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render("OPTIONS", True, "white")
        lobbyTitreOption_Rect = lobbyTitreOption.get_rect(
            center=(ressources.screen_width * 0.270, ressources.screen_height * 0.116))

        lobbyOptionButtonNbrJoueursPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.324),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonNbrJoueursMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.324),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonDiffPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.521),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonDiffMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.521),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonRoundPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, ressources.screen_height * 0.718),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonRoundMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, ressources.screen_height * 0.718),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyButtonBack = Button(
            images=ressources.lobbyButtonBack,
            pos=(ressources.screen_width * 0.052, ressources.screen_height * 0.920),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyButtonPlay = Button(
            images=ressources.lobbyButtonPlay,
            pos=(ressources.screen_width * 0.596, ressources.screen_height * 0.914),
            text_input="PLAY",
            font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.055)),
            base_color="White",
            hovering_color="#6DC300")


        lobbyMousePosition = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        volume_bar.draw(screen)

        num_players = len(self.gameConf.listVignettes)
        for i, vignette in enumerate(self.gameConf.listVignettes):
            vignette.afficher(screen)

        # Fenetre des options
        screen.blit(ressources.lobbyWindowOption1,
                    (ressources.screen_width * 0.091, ressources.screen_height * 0.058))

        # Titre

        screen.blit(lobbyTitreOption, lobbyTitreOption_Rect)

        # Options du nombre de joueurs
        screen.blit(ressources.lobbyWindowOption2,
                    (ressources.screen_width * 0.117, ressources.screen_height * 0.231))
        screen.blit(ressources.lobbyIconPlayers,
                    (ressources.screen_width * 0.124, ressources.screen_height * 0.249))
        lobbyTitreOptionNbrJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_height * 0.029)).render(
            f"Nombre de joueurs",
            True,
            "#CC191C")
        lobbyTitreOptionNbrJoueurs_Rect = lobbyTitreOptionNbrJoueurs.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.266))
        screen.blit(lobbyTitreOptionNbrJoueurs, lobbyTitreOptionNbrJoueurs_Rect)

        lobbyDataNombreJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                     round(ressources.screen_height * 0.029)).render(
            f"{num_players}",
            True,
            "#CC191C")
        lobbyDataNombreJoueurs_Rect = lobbyDataNombreJoueurs.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.324))
        screen.blit(lobbyDataNombreJoueurs, lobbyDataNombreJoueurs_Rect)

        # Option difficulté
        screen.blit(ressources.lobbyWindowOption2,
                    (ressources.screen_width * 0.117, ressources.screen_height * 0.428))
        screen.blit(ressources.lobbyIconDifficulty,
                    (ressources.screen_width * 0.124, ressources.screen_height * 0.446))

        lobbyTitreOptionDifficulte = ressources.get_font(ressources.nunitoRegular,
                                                         round(screen_height * 0.029)).render(
            f"Difficulté", True,
            "#CC191C")
        lobbyTitreOptionDifficulte_Rect = lobbyTitreOptionDifficulte.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.463))
        screen.blit(lobbyTitreOptionDifficulte, lobbyTitreOptionDifficulte_Rect)

        lobbyDataLvlDifficulte = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"{difficulty[self.gameConf.difficulty]}", True,

            "#CC191C")
        lobbyDataLvlDifficulte_Rect = lobbyDataLvlDifficulte.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.521))
        screen.blit(lobbyDataLvlDifficulte, lobbyDataLvlDifficulte_Rect)

        # Option nombres de rounds
        screen.blit(ressources.lobbyWindowOption2,
                    (ressources.screen_width * 0.117, ressources.screen_height * 0.625))
        screen.blit(ressources.lobbyIconRounds, (ressources.screen_width * 0.124, ressources.screen_height * 0.643))

        lobbyTitreOptionRounds = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"Nombre de manches", True,
            "#CC191C")
        lobbyTitreOptionRounds_Rect = lobbyTitreOptionRounds.get_rect(
            center=(ressources.screen_width * 0.286, ressources.screen_height * 0.660))
        screen.blit(lobbyTitreOptionRounds, lobbyTitreOptionRounds_Rect)

        lobbyDataRounds = ressources.get_font(ressources.nunitoRegular, round(screen_height * 0.029)).render(
            f"{self.gameConf.numRounds}", True,
            "#CC191C")
        lobbyDataRounds_Rect = lobbyDataRounds.get_rect(
            center=(ressources.screen_width * 0.293, ressources.screen_height * 0.718))
        screen.blit(lobbyDataRounds, lobbyDataRounds_Rect)

        for button in [lobbyButtonBack, lobbyButtonPlay,
                       lobbyOptionButtonRoundMoins, lobbyOptionButtonRoundPlus,
                       lobbyOptionButtonDiffMoins, lobbyOptionButtonDiffPlus,
                       lobbyOptionButtonNbrJoueursPlus, lobbyOptionButtonNbrJoueursMoins]:
            button.changeColor(lobbyMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for vignette in self.gameConf.listVignettes:
                vignette.text.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for vignette in self.gameConf.listVignettes:

                    if vignette.icon_croix.checkForInput(lobbyMousePosition) and len(self.gameConf.listVignettes) > 2:
                        index_suppr = self.gameConf.listVignettes.index(vignette)
                        self.gameConf.listVignettes.remove(vignette)
                        for k in range(0, len(self.gameConf.listVignettes)):
                            if k >= index_suppr:
                                self.gameConf.listVignettes[k].realigner(k)

                    if vignette.personnage_image.checkForInput(lobbyMousePosition):
                        if event.button == 3:
                            vignette.changer_personnageAvant()
                        elif event.button == 1:
                            vignette.changer_personnageApres()

                if lobbyButtonBack.checkForInput(lobbyMousePosition):
                    self.gameConf.listVignettes = []
                    self.state = "main_menu"

                if lobbyButtonPlay.checkForInput(lobbyMousePosition):
                    for vignette in self.gameConf.listVignettes:
                        self.gameConf.listPlayers.append(player.Player(vignette.text))
                    self.state = "to_round"

                if lobbyOptionButtonNbrJoueursPlus.checkForInput(lobbyMousePosition):
                    if len(self.gameConf.listVignettes) < 9:
                        lobbyOptionButtonNbrJoueursPlus.press(screen)
                        nouvelle_vignette = VignetteJoueur(ressources.screen_width * 0.586 + (
                                len(self.gameConf.listVignettes) % 3) * ressources.screen_width * 0.111,
                                                           ressources.screen_height * 0.145 + (
                                                                   len(self.gameConf.listVignettes) // 3) * ressources.screen_height * 0.231)
                        self.gameConf.listVignettes.append(nouvelle_vignette)

                if lobbyOptionButtonNbrJoueursMoins.checkForInput(lobbyMousePosition):
                    if len(self.gameConf.listVignettes) > 2:
                        lobbyOptionButtonNbrJoueursMoins.press(screen)
                        self.gameConf.listVignettes.pop()

                if lobbyOptionButtonDiffPlus.checkForInput(lobbyMousePosition):
                    if self.gameConf.difficulty < 2:
                        lobbyOptionButtonDiffPlus.press(screen)
                        self.gameConf.difficulty += 1
                if lobbyOptionButtonDiffMoins.checkForInput(lobbyMousePosition):
                    if self.gameConf.difficulty > 0:
                        lobbyOptionButtonDiffMoins.press(screen)
                        self.gameConf.difficulty -= 1

                if lobbyOptionButtonRoundPlus.checkForInput(lobbyMousePosition):
                    if self.gameConf.numRounds < 5:
                        lobbyOptionButtonRoundPlus.press(screen)
                        self.gameConf.numRounds += 1

                if lobbyOptionButtonRoundMoins.checkForInput(lobbyMousePosition):
                    if self.gameConf.numRounds > 1:
                        lobbyOptionButtonRoundMoins.press(screen)
                        self.gameConf.numRounds -= 1

            volume_bar.handle_event(event, mousePosition=lobbyMousePosition, screen=screen)

        pygame.display.flip()


    def toRound(self):
        self.gameConf.currentRound += 1
        self.gameConf.listMixtapes.append(Mixtape())
        self.gameConf.dspInfos()
        self.state = "round_play"

    def roundListening(self):

        self._playAlignementJoueursBas_(len(self.gameConf.listVignettes))

        playButtonMusic = Button(
            images=ressources.playButtonPlayMusic,
            pos=(screen_width * 0.5, screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        playButtonBack = Button(
            images=ressources.lobbyButtonBack,
            pos=(screen_width * 0.948, screen_height * 0.08),
            text_input=None, font=None, base_color=None, hovering_color=None)


        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()
        for i, vignette in enumerate(self.gameConf.listVignettes):
            vignette.afficher(screen)

        for button in [playButtonBack, playButtonMusic]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonBack.checkForInput(playMousePosition):
                    self.gameConf.listVignettes = []
                    self.state = "main_menu"
                if playButtonMusic.checkForInput(playMousePosition):
                    if playSoundOn:
                        playButtonMusic.setImages(ressources.playButtonMuteMusic)
                        pygame.mixer.music.pause()
                        self.state = "round_paused"

        pygame.display.flip()

    def roundPaused(self):

        playButtonMusic = Button(
            images=ressources.playButtonMuteMusic,
            pos=(screen_width * 0.5, screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        playButtonTest = Button(
            images=ressources.playButtonMuteMusic,
            pos=(screen_width * 0.5, screen_height * 0.5),
            text_input=None, font=None, base_color=None, hovering_color=None)


        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()

        for button in [playButtonMusic, playButtonTest]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonMusic.checkForInput(playMousePosition):
                    if playSoundOn:
                        playButtonMusic.setImages(ressources.playButtonMuteMusic)
                        pygame.mixer.music.unpause()
                        self.state = "round_play"

                if playButtonTest.checkForInput(playMousePosition):
                    self.state = "round_attrib"


        pygame.display.flip()

    def attributionPoints(self):
        attributionPointsTitre = Button(images=ressources.attributionPoints,
                                        pos=(screen_width * (3 / 12), screen_height * 0.880),
                                        text_input="Titre",
                                        font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.035)),
                                        base_color="White",
                                        hovering_color="#2F6DC7")

        attributionPointsGroupe = Button(images=ressources.attributionPoints,
                                         pos=(screen_width * (6 / 12), screen_height * 0.880),
                                         text_input="Groupe",
                                         font=ressources.get_font(ressources.nunitoRegular,
                                                                  round(screen_width * 0.035)),
                                         base_color="White",
                                         hovering_color="#2F6DC7")

        attributionPointsTitreEtGroupe = Button(images=ressources.attributionPoints,
                                                pos=(screen_width * (9 / 12), screen_height * 0.880),
                                                text_input="Titre+Groupe",
                                                font=ressources.get_font(ressources.nunitoRegular,
                                                                         round(screen_width * 0.026)),
                                                base_color="White",
                                                hovering_color="#2F6DC7")

        attributionPointsCroix = Button(images=ressources.attributionPointsBoutonCroix,
                                        pos=(screen_width * 0.92, screen_height * (1 / 8)),
                                        text_input=None, font=None, base_color=None, hovering_color=None)
        self._attributionPointsAlignementJoueursMotif_(len(self.gameConf.listVignettes))

        screen.blit(fond_attribution, (screen_width * 0.02, (1 / 25) * screen_height))
        menuMousePosition = pygame.mouse.get_pos()

        for i, vignette in enumerate(self.gameConf.listVignettes):
            vignette.afficher(screen)
        for button in [attributionPointsTitreEtGroupe, attributionPointsGroupe, attributionPointsTitre,
                       attributionPointsCroix]:
            button.changeColor(menuMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if attributionPointsGroupe.checkForInput(menuMousePosition):
                    attributionPointsGroupe.press(screen)
                    self.state = "round_play"
                if attributionPointsTitre.checkForInput(menuMousePosition):
                    attributionPointsTitre.press(screen)
                    self.state = "round_play"
                if attributionPointsTitreEtGroupe.checkForInput(menuMousePosition):
                    attributionPointsTitreEtGroupe.press(screen)
                    self.state = "round_play"
                if attributionPointsCroix.checkForInput(menuMousePosition):
                    self.state = "round_paused"
        pygame.display.flip()

    def interRounds(self):
        pass

    def end(self):
        pass

    def stateManager(self):
        if self.state == "main_menu":
            self.main_menu()
        elif self.state == "to_lobby":
            self.mainMenutoLobby()
        elif self.state == "lobby":
            self.lobby()
        elif self.state == "to_round":
            self.toRound()
        elif self.state == "round_play":
            self.roundListening()
        elif self.state == "round_paused":
            self.roundPaused()
        elif self.state == "round_attrib":
            self.attributionPoints()
        elif self.state == "inter_rounds":
            self.interRounds()
        elif self.state == "end_game":
            self.end()


pygame.init()
gameState = GameState()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("BlindMixTape")


background = pygame.transform.scale(pygame.image.load(ressources.background), (screen_width, screen_height))
volume_bar = VolumeBar(screen_width * 0.805, screen_height * 0.884, screen_width * 0.130, screen_height * 0.035)
fond_attribution = pygame.transform.scale(pygame.image.load(ressources.attributionPointsFond),
                                          (screen_width * 0.96, (16 / 17) * screen_height))


while True:
    gameState.stateManager()
    clock.tick(60)