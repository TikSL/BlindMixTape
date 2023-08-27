from math import ceil

import pygame
import sys
from pygame import mixer, time, USEREVENT

from player import Player
import ressources
from button import Button
from game_config import gameConfig
from mixtape import Mixtape
from vignette_joueur import VignetteJoueur
from volume_bar import VolumeBar


# screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen_width = 1280
screen_height = 720
print(f"Affichage : {screen_width} x {screen_height}")


class GameState:
    def __init__(self):
        self.gameConf = gameConfig()
        mixer.pre_init(44100, 16, 2, 4096)
        mixer.music.unload()
        mixer.music.load("view/assets/AC theme.mp3")
        mixer.music.set_volume(0.2)
        time.set_timer(USEREVENT, 80)
        self.state = "main_menu"
        self.premierPassagePlay = True

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

        self.premierPassagePlay = True
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


        difficulty = ["FACILE", "MOYEN", "DIFFICILE", "PROGRES."]

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
                    pygame.mixer.music.stop()
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
                    if self.gameConf.difficulty < 3:
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
        if self.gameConf.currentRound == 1:
            for vignette in self.gameConf.listVignettes:
                self.gameConf.listPlayers.append(Player(vignette.text.text_input, vignette))
            for player in self.gameConf.listPlayers:
                player.vignette.setScore(player.score)
        if self.gameConf.difficulty == 0:
            diff = [0, 0, 0, 0, 0, 0]
        elif self.gameConf.difficulty == 1:
            diff = [0, 0, 0, 1, 1, 1]
        elif self.gameConf.difficulty == 2:
            diff = [0, 0, 1, 1, 2, 2]
        elif self.gameConf.difficulty == 3:
            ratio = self.gameConf.currentRound // self.gameConf.numRounds
            if ratio <= 0.5:
                diff = [0, 0, 0, 0, 0, 0]
            elif ratio > 0.5 and ratio <= 0.75:
                diff = [0, 0, 0, 1, 1, 1]
            else:
                diff = [0, 0, 1, 1, 2, 2]
        self.gameConf.listMixtapes.append(Mixtape(diff))
        self.gameConf.dspInfos()
        self.state = "round_play"

    def roundListening(self):

        self._playAlignementJoueursBas_(len(self.gameConf.listVignettes))

        if self.premierPassagePlay:
            playSonAJouer = []
            for song in self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver:
                if not song.found:
                    playSonAJouer.append(pygame.mixer.Sound(f"game/{song.id}.mp3"))

            for song in playSonAJouer:
                song.play()
            self.premierPassagePlay = False


        playButtonMusic = Button(
            images=ressources.playButtonPlayMusic,
            pos=(screen_width * 0.5, screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        button_positions = [
            (screen_width * 0.10, screen_height * 0.30),
            (screen_width * 0.40, screen_height * 0.30),
            (screen_width * 0.70, screen_height * 0.30),
            (screen_width * 0.10, screen_height * 0.58),
            (screen_width * 0.40, screen_height * 0.58),
            (screen_width * 0.70, screen_height * 0.58)
        ]

        playListButtonCover = []
        playListTitles = []
        playListArtists = []
        playListFounder = []

        for song in self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver:
            playListButtonCover.append(
                Button(
                    images=[pygame.transform.scale(pygame.image.load(song.cover),
                                                   (0.146 * screen_width, 0.146 * screen_width))],
                    pos=button_positions[song.id],
                    text_input=None, font=None, base_color=None, hovering_color=None
                )
            )
            if song.found:
                playListFounder.append((pygame.transform.scale(pygame.image.load(song.founder.vignette.bufferPerso),(0.065 * ressources.screen_width, 0.116 * ressources.screen_height)),button_positions[song.id]))


        for id, song in enumerate(self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver):
            if song.found:
                color = "grey"
            else:
                color = "black"
            left = button_positions[id][0] + 0.09 * screen_width
            playTitreSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.title, True, color)
            playTitreSon_Rect = playTitreSon.get_rect(left=left, top=button_positions[id][1] - 0.05 * screen_width)

            playArtistSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.artist, True, color)
            playArtistSon_Rect = playArtistSon.get_rect(left=left, top=button_positions[id][1] - 0.02 * screen_width)

            playListTitles.append((playTitreSon, playTitreSon_Rect))
            playListArtists.append((playArtistSon, playArtistSon_Rect))


        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()
        for i, vignette in enumerate(self.gameConf.listVignettes):
            vignette.afficher(screen)

        for button in [playButtonMusic] + playListButtonCover:
            button.update(screen)

        for infos in playListArtists + playListTitles + playListFounder:
            screen.blit(infos[0], infos[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonMusic.checkForInput(playMousePosition):
                    if playSoundOn:
                        playButtonMusic.setImages(ressources.playButtonMuteMusic)
                        # pygame.mixer.music.pause()
                        pygame.mixer.stop()
                        self.state = "round_paused"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.stop()
                    self.state = "round_paused"

        pygame.display.flip()

    def roundPaused(self):
        self.premierPassagePlay = True
        playButtonMusic = Button(
            images=ressources.playButtonMuteMusic,
            pos=(screen_width * 0.5, screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        playListButtonCover = []
        playListTitles = []
        playListArtists = []
        playListFounder = []
        button_positions = [
            (screen_width * 0.10, screen_height * 0.35),
            (screen_width * 0.42, screen_height * 0.35),
            (screen_width * 0.74, screen_height * 0.35),
            (screen_width * 0.10, screen_height * 0.75),
            (screen_width * 0.42, screen_height * 0.75),
            (screen_width * 0.74, screen_height * 0.75)
        ]

        for song in self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver:
            playListButtonCover.append(
                Button(
                    images=[pygame.transform.scale(pygame.image.load(song.cover),
                                                   (0.146 * screen_width, 0.146 * screen_width))],
                    pos=button_positions[song.id],
                    text_input=None, font=None, base_color=None, hovering_color=None
                )
            )
            if song.found:
                playListFounder.append((pygame.transform.scale(pygame.image.load(song.founder.vignette.bufferPerso), (
                0.065 * ressources.screen_width, 0.116 * ressources.screen_height)), button_positions[song.id]))

        for id, song in enumerate(self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver):
            if song.found:
                color = "grey"
            else:
                color = "black"
            left = button_positions[id][0] + 0.09 * screen_width
            playTitreSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.title, True, color)
            playTitreSon_Rect = playTitreSon.get_rect(left=left, top=button_positions[id][1] - 0.05 * screen_width)

            playArtistSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.artist, True, color)
            playArtistSon_Rect = playArtistSon.get_rect(left=left, top=button_positions[id][1] - 0.02 * screen_width)

            playListTitles.append((playTitreSon, playTitreSon_Rect))
            playListArtists.append((playArtistSon, playArtistSon_Rect))

        playButtonPass = Button(images=ressources.menuPlayButton, pos=(screen_width * 0.85, screen_height * 0.12),
                                text_input="PASSER",
                                font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.045)),
                                base_color="White",
                                hovering_color="#6DC300")

        screen.blit(background, (0, 0))
        playMousePosition = pygame.mouse.get_pos()

        for button in [playButtonMusic, playButtonPass] + playListButtonCover:
            button.update(screen)

        for info in playListTitles + playListArtists + playListFounder:
            screen.blit(info[0], info[1])

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
                        pass
                if playButtonPass.checkForInput(playMousePosition):
                    self.state = "inter_rounds"
                    pass
                for id, button in enumerate(playListButtonCover):
                    if button.checkForInput(playMousePosition) and not self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver[id].found:
                        self.gameConf.sonSelectionne = id
                        self.state = "round_attrib"
                        pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.unpause()
                    self.state = "round_play"
                    pass

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
            if self.gameConf.joueurSelectionne:
                button.changeColor(menuMousePosition)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.gameConf.joueurSelectionne:

                    for button in [attributionPointsTitreEtGroupe, attributionPointsGroupe, attributionPointsTitre]:

                        if button.checkForInput(menuMousePosition):

                            button.press(screen)
                            for vignette in self.gameConf.listVignettes:
                                vignette.selected = False

                            for player in self.gameConf.listPlayers:
                                if player.name == self.gameConf.joueurSelectionne.text_input:
                                    if button == attributionPointsTitreEtGroupe:
                                        player.score += 3
                                    else:
                                        player.score += 1
                                    self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver[self.gameConf.sonSelectionne].found = True
                                    self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver[self.gameConf.sonSelectionne].founder = player

                                    player.vignette.setScore(player.score)
                            self.gameConf.joueurSelectionne = None

                            count_found = 0

                            for song in self.gameConf.listMixtapes[self.gameConf.currentRound-1].listeATrouver:
                                if song.found:
                                    count_found += 1

                            if count_found == 6:
                                self.state = "inter_rounds"
                            else:
                                self.state = "round_play"

                if attributionPointsCroix.checkForInput(menuMousePosition):
                    self.state = "round_paused"

                for vignette in self.gameConf.listVignettes:
                    if vignette.personnage_image.checkForInput(menuMousePosition):
                        if vignette.rect.collidepoint(menuMousePosition):
                            for other_vignette in self.gameConf.listVignettes:
                                if other_vignette != vignette:
                                    other_vignette.selected = False
                            vignette.selected = not vignette.selected
                            if self.gameConf.joueurSelectionne == vignette.text:
                                self.gameConf.joueurSelectionne = None
                            else:
                                self.gameConf.joueurSelectionne = vignette.text

        pygame.display.flip()

    def interRounds(self):

        if self.gameConf.currentRound == self.gameConf.numRounds :
            self.state = "end_game"
            pass
        screen.blit(background, (0, 0))
        interRoundsTitre = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render(f"Fin du round {self.gameConf.currentRound}", True, "white")
        interRoundsTitre_Rect = interRoundsTitre .get_rect(
            center=(ressources.screen_width * 0.50, ressources.screen_height * 0.116))
        players_sorted = sorted(self.gameConf.listPlayers, key=lambda player: player.score, reverse=True)
        screen.blit(interRoundsTitre, interRoundsTitre_Rect)
        for i, vignette in enumerate(players_sorted):
            if i==0:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.45,
                                                   ressources.screen_height * 0.2))
            if i==1:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.25,
                                                   ressources.screen_height * 0.26))
            if i==2:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.65,
                                                   ressources.screen_height * 0.32))
            if i>=3:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.01 +(i-2)*0.15*ressources.screen_width, ressources.screen_height*0.7))
            players_sorted[i].vignette.afficher(screen)

        playButtonPass = Button(images=ressources.menuPlayButton, pos=(screen_width * 0.85, screen_height * 0.12),
                                text_input="PASSER",
                                font=ressources.get_font(ressources.nunitoRegular, round(screen_width * 0.045)),
                                base_color="White",
                                hovering_color="#6DC300")

        playButtonPass.update(screen)

        menuMousePosition = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonPass.checkForInput(menuMousePosition):
                    self.state = "to_round"


        pygame.display.flip()

    def end(self):

        screen.blit(background, (0, 0))

        playButtonBack = Button(
            images=ressources.lobbyButtonBack,
            pos=(screen_width * 0.948, screen_height * 0.08),
            text_input=None, font=None, base_color=None, hovering_color=None)

        interRoundsTitre = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render("FIN DU JEU", True, "white")
        interRoundsTitre_Rect = interRoundsTitre.get_rect(
            center=(ressources.screen_width * 0.50, ressources.screen_height * 0.116))
        players_sorted = sorted(self.gameConf.listPlayers, key=lambda player: player.score, reverse=True)
        screen.blit(interRoundsTitre, interRoundsTitre_Rect)
        for i, vignette in enumerate(players_sorted):
            if i == 0:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.45,
                                                   ressources.screen_height * 0.2))
                players_sorted[i].vignette.setScore(players_sorted[i].score, "Gold")
                players_sorted[i].vignette.text.update_text_surface(color="Gold")
            if i == 1:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.25,
                                                   ressources.screen_height * 0.26))
                players_sorted[i].vignette.setScore(players_sorted[i].score, "Silver")
                players_sorted[i].vignette.text.update_text_surface(color="Silver")
            if i == 2:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.65,
                                                   ressources.screen_height * 0.32))
                players_sorted[i].vignette.setScore(players_sorted[i].score, "Peru")
                players_sorted[i].vignette.text.update_text_surface(color="Peru")
            if i >= 3:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.01 + (
                            i - 2) * 0.15 * ressources.screen_width, ressources.screen_height * 0.7))
            players_sorted[i].vignette.afficher(screen)

        for button in [playButtonBack]:
            button.update(screen)

        playMousePosition =  pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if playButtonBack.checkForInput(playMousePosition):
                self.gameConf.listVignettes = []
                pygame.mixer.stop()
                self.gameConf = gameConfig()
                self.state = "main_menu"

        pygame.display.flip()

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