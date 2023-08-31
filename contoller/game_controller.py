from typing import re

import pygame
import sys
from pygame import mixer, time, USEREVENT
from math import ceil

from player import Player
import ressources
from button import Button
from game_config import GameConfig
from mixtape import Mixtape
from vignette_joueur import VignetteJoueur
from volume_bar import VolumeBar


def messageInit():
    print(ressources.titleInit)
    print(f"\n"
          f"Crée par TikSl avec l'aide de HageshiiYagi.\n"
          f"Jeu basé sur les blindtests de Navo dans le podcast \"Un Bon Moment\" de Kyan Khojandi et Navo.\n"
          f"Lien du podcast : https://www.youtube.com/playlist?list=PLSkidoCR8oB3HDB-QSDlwGYbjeb5Ra4wG \n"
          f"Lien GitHub : https://github.com/TikSL/BlindMixTape\n"
          f"Version {ressources.version}\n")

    print(f"Affichage : {ressources.screen_width} x {ressources.screen_height}")

def decouper_phrase(phrase, paquet_max_length= 8):
    liste_paquets = []
    paquet = []
    mots = phrase.split()
    if len(mots) == 1:
        return mots
    for mot in mots:
        if len(' '.join(paquet + [mot])) <= paquet_max_length:
            paquet.append(mot)
        else:
            liste_paquets.append(' '.join(paquet))
            paquet = [mot]
    if paquet:
        liste_paquets.append(' '.join(paquet))
    return liste_paquets


class GameState:
    def __init__(self):
        messageInit()
        self.gameConf = GameConfig()
        mixer.pre_init(44100, 16, 2, 4096)
        mixer.music.unload()
        mixer.music.load("view/assets/AC theme.mp3")
        volume = 0.3
        mixer.music.set_volume(volume)
        self.volume_bar = VolumeBar(ressources.screen_width * 0.805, ressources.screen_height * 0.884,
                               ressources.screen_width * 0.130, ressources.screen_height * 0.035,
                               volume = volume)
        time.set_timer(USEREVENT, 80)
        self.state = "main_menu"
        self.premierPassagePlay = True

    def _playAlignementJoueursBas_(self, nbrVignettes):
        total_width = ressources.screen_width * 0.097 * nbrVignettes
        espace_horizontal = (ressources.screen_width - total_width) / (nbrVignettes + 1)

        for index_vignette, vignette in enumerate(self.gameConf.listVignettes):
            position_x = espace_horizontal * (index_vignette + 1) + 0.097 * ressources.screen_width * index_vignette
            vignette.icon_croix = None
            vignette.setPos((position_x, ressources.screen_height - 0.24 * ressources.screen_height))

    def _attributionPointsAlignementJoueursMotif_(self, nbrVignettes):
        nbrVignettesHaut = ceil(nbrVignettes // 2)
        nbrVignettesBas = nbrVignettes - nbrVignettesHaut

        ecartVignettesHaut = (ressources.screen_width - nbrVignettesHaut * 0.097 * ressources.screen_width) / (nbrVignettesHaut + 1)
        ecartVignettesBas = (ressources.screen_width - nbrVignettesBas * 0.097 * ressources.screen_width) / (nbrVignettesBas + 1)

        for i, vignette in enumerate(self.gameConf.listVignettes):
            if i <= nbrVignettesHaut - 1:
                vignette.setPos(((0.097 * ressources.screen_width) * i + ecartVignettesHaut * (i + 1), 100))
            else:
                vignette.setPos(((0.097 * ressources.screen_width) * (i - nbrVignettesHaut) + ecartVignettesBas * (
                        i - nbrVignettesHaut + 1), 400))

    def main_menu(self):

        self.premierPassagePlay = True
        if not mixer.music.get_busy():
            mixer.music.play()

        current_image_index_floss = 0
        liste_image_floss = ressources.menuGIF

        elapsed_time1 = 0

        menuButtonPlay = Button(images=ressources.menuPlayButton, pos=(ressources.screen_width * 0.25, ressources.screen_height * 0.40),
                                text_input="PLAY",
                                font=ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_width * 0.035)),
                                base_color="#6BBF00",
                                hovering_color="white")

        menuButtonOption = Button(images = ressources.menuOptionButton, pos=(ressources.screen_width*0.25, ressources.screen_height*0.57),
                                  text_input="OPTIONS",
                                  font=ressources.get_font(ressources.nunitoRegular,
                                                           round(ressources.screen_width * 0.035)),
                                  base_color="#007EC3",
                                  hovering_color="white")

        menuButtonQuit = Button(images=ressources.menuQuitButton, pos=(ressources.screen_width * 0.25, ressources.screen_height * 0.74),
                                text_input="QUIT",
                                font=ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_width * 0.035)),
                                base_color="#C2181B",
                                hovering_color="white")

        menuMousePosition = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(ressources.menuLogo,
                    (ressources.screen_width * 0.292, ressources.screen_height * 0.046))
        self.volume_bar.draw(screen)

        for button in [menuButtonPlay, menuButtonOption, menuButtonQuit]:
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
                                (ressources.screen_width * 0.571, ressources.screen_height * 0.400))
                    current_image_index_floss = (current_image_index_floss + 1) % 18

                pygame.display.flip()

            self.volume_bar.handle_event(event, mousePosition=menuMousePosition, screen=screen)

    def mainMenutoLobby(self):

        self.gameConf.listVignettes.append(
            VignetteJoueur(ressources.screen_width * 0.586, ressources.screen_height * 0.145))
        self.gameConf.listVignettes.append(
            VignetteJoueur(ressources.screen_width * 0.697, ressources.screen_height * 0.145))

        self.state = "lobby"

    def lobby(self):

        difficulty = ["FACILE", "MOYEN", "DIFFICILE", "PROGRES."]

        lobbyTitreOption = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render("OPTIONS", True, "white")
        lobbyTitreOption_Rect = lobbyTitreOption.get_rect(
            center=(ressources.screen_width * 0.270, ressources.screen_height * 0.085))

        pos_y = ressources.screen_height * 0.298
        lobbyOptionButtonNbrJoueursPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonNbrJoueursMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        pos_y += 0.166 * ressources.screen_height
        lobbyOptionButtonDiffPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonDiffMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        pos_y += 0.166 * ressources.screen_height
        lobbyOptionButtonRoundPlus = Button(
            images=ressources.lobbyButtonPlus,
            pos=(ressources.screen_width * 0.358, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonRoundMoins = Button(
            images=ressources.lobbyButtonMoins,
            pos=(ressources.screen_width * 0.228, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        pos_y += 0.166 * ressources.screen_height
        lobbyOptionButtonPlaylistPlus = Button(
            images=ressources.lobbyButtonRight,
            pos=(ressources.screen_width * 0.358, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyOptionButtonPlaylistMoins = Button(
            images=ressources.lobbyButtonLeft,
            pos=(ressources.screen_width * 0.228, pos_y),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyButtonBack = Button(
            images=ressources.lobbyButtonBack,
            pos=(ressources.screen_width * 0.052, ressources.screen_height * 0.910),
            text_input=None, font=None, base_color=None, hovering_color=None)

        lobbyButtonPlay = Button(
            images=ressources.lobbyButtonPlay,
            pos=(ressources.screen_width * 0.596, ressources.screen_height * 0.904),
            text_input="PLAY",
            font=ressources.get_font(ressources.nunitoRegular, round(ressources.screen_width * 0.035)),
            base_color="#6BBF00",
            hovering_color="white")

        lobbyMousePosition = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        self.volume_bar.draw(screen)

        num_players = len(self.gameConf.listVignettes)
        for i, vignette in enumerate(self.gameConf.listVignettes):
            vignette.afficher(screen)

        # Fenetre des options
        screen.blit(ressources.lobbyWindowOption1,
                    (ressources.screen_width * 0.085, ressources.screen_height * 0.030))

        # Titre

        screen.blit(lobbyTitreOption, lobbyTitreOption_Rect)
        pos_y = ressources.screen_height * 0.205
        # Options du nombre de joueurs
        screen.blit(ressources.lobbyWindowOption2,
                    (ressources.screen_width * 0.117, pos_y))
        screen.blit(ressources.lobbyIconPlayers,
                    (ressources.screen_width * 0.130, pos_y + ressources.screen_height * 0.015))
        lobbyTitreOptionNbrJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_height * 0.029)).render(
            f"Nombre de joueurs",
            True,
            "#CC191C")
        lobbyTitreOptionNbrJoueurs_Rect = lobbyTitreOptionNbrJoueurs.get_rect(
            center=(ressources.screen_width * 0.286, pos_y + ressources.screen_height * 0.036))
        screen.blit(lobbyTitreOptionNbrJoueurs, lobbyTitreOptionNbrJoueurs_Rect)

        lobbyDataNombreJoueurs = ressources.get_font(ressources.nunitoRegular,
                                                     round(ressources.screen_height * 0.029)).render(
            f"{num_players}",
            True,
            "#CC191C")
        lobbyDataNombreJoueurs_Rect = lobbyDataNombreJoueurs.get_rect(
            center=(ressources.screen_width * 0.293, pos_y + ressources.screen_height * 0.094))
        screen.blit(lobbyDataNombreJoueurs, lobbyDataNombreJoueurs_Rect)

        # Option difficulté
        pos_y = pos_y + ressources.screen_height * 0.166
        screen.blit(ressources.lobbyWindowOption2,
                    (ressources.screen_width * 0.117, pos_y))
        screen.blit(ressources.lobbyIconDifficulty,
                    (ressources.screen_width * 0.130, pos_y + ressources.screen_height * 0.015))

        lobbyTitreOptionDifficulte = ressources.get_font(ressources.nunitoRegular,
                                                         round(ressources.screen_height * 0.029)).render(
            f"Difficulté", True,
            "#CC191C")
        lobbyTitreOptionDifficulte_Rect = lobbyTitreOptionDifficulte.get_rect(
            center=(ressources.screen_width * 0.286, pos_y + ressources.screen_height * 0.036))
        screen.blit(lobbyTitreOptionDifficulte, lobbyTitreOptionDifficulte_Rect)

        lobbyDataLvlDifficulte = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.029)).render(
            f"{difficulty[self.gameConf.difficulty]}", True,

            "#CC191C")
        lobbyDataLvlDifficulte_Rect = lobbyDataLvlDifficulte.get_rect(
            center=(ressources.screen_width * 0.293, pos_y + ressources.screen_height * 0.094))
        screen.blit(lobbyDataLvlDifficulte, lobbyDataLvlDifficulte_Rect)

        # Option nombres de rounds
        pos_y = pos_y + ressources.screen_height * 0.166
        screen.blit(ressources.lobbyWindowOption2, (ressources.screen_width * 0.117, pos_y))
        screen.blit(ressources.lobbyIconRounds, (ressources.screen_width * 0.130, pos_y + ressources.screen_height * 0.015))

        lobbyTitreOptionRounds = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.029)).render(
            f"Nombre de manches", True,
            "#CC191C")
        lobbyTitreOptionRounds_Rect = lobbyTitreOptionRounds.get_rect(
            center=(ressources.screen_width * 0.286, pos_y + ressources.screen_height * 0.036))
        screen.blit(lobbyTitreOptionRounds, lobbyTitreOptionRounds_Rect)

        lobbyDataRounds = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.029)).render(
            f"{self.gameConf.numRounds}", True,
            "#CC191C")
        lobbyDataRounds_Rect = lobbyDataRounds.get_rect(
            center=(ressources.screen_width * 0.293, pos_y + ressources.screen_height * 0.094))
        screen.blit(lobbyDataRounds, lobbyDataRounds_Rect)

        # Option style de playlist
        pos_y = pos_y + ressources.screen_height * 0.166
        screen.blit(ressources.lobbyWindowOption2, (ressources.screen_width * 0.117, pos_y))
        screen.blit(ressources.lobbyIconStyle,
                    (ressources.screen_width * 0.130, pos_y + ressources.screen_height * 0.015))

        lobbyTitreOptionStyle = ressources.get_font(ressources.nunitoRegular,
                                                     round(ressources.screen_height * 0.029)).render(
            f"Style de playlist", True,
            "#CC191C")
        lobbyTitreOptionStyle_Rect = lobbyTitreOptionStyle.get_rect(
            center=(ressources.screen_width * 0.286, pos_y + ressources.screen_height * 0.036))
        screen.blit(lobbyTitreOptionStyle, lobbyTitreOptionStyle_Rect)

        liste_texte = []
        texte = decouper_phrase(self.gameConf.style)
        for i, mot in enumerate(texte) :

            lobbyDataStyle = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.029)).render(
                f"{mot}", True,
                "#CC191C")
            if len(texte) > 1:
                lobbyDataStyle_Rect = lobbyDataStyle.get_rect(
                    center=(ressources.screen_width * 0.293, pos_y + ressources.screen_height * 0.084 + ressources.screen_height * 0.025 * i))
                liste_texte.append((lobbyDataStyle, lobbyDataStyle_Rect))
            else :
                lobbyDataStyle_Rect = lobbyDataStyle.get_rect(
                    center=(ressources.screen_width * 0.293, pos_y + ressources.screen_height * 0.094))
                liste_texte.append((lobbyDataStyle, lobbyDataStyle_Rect))

        for (mot_infos, mot_infos_rect) in liste_texte:
            screen.blit(mot_infos, mot_infos_rect)

        for button in [lobbyButtonBack, lobbyButtonPlay,
                       lobbyOptionButtonRoundMoins, lobbyOptionButtonRoundPlus,
                       lobbyOptionButtonDiffMoins, lobbyOptionButtonDiffPlus,
                       lobbyOptionButtonNbrJoueursPlus, lobbyOptionButtonNbrJoueursMoins,
                       lobbyOptionButtonPlaylistPlus, lobbyOptionButtonPlaylistMoins]:
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

                if lobbyOptionButtonPlaylistPlus.checkForInput(lobbyMousePosition):
                    self.gameConf.updateStyle(1)
                if lobbyOptionButtonPlaylistMoins.checkForInput(lobbyMousePosition):
                    self.gameConf.updateStyle(-1)

            self.volume_bar.handle_event(event, mousePosition=lobbyMousePosition, screen=screen)

        pygame.display.flip()

    def toRound(self):
        self.gameConf.currentRound += 1
        if self.gameConf.currentRound == 1:
            for vignette in self.gameConf.listVignettes:
                self.gameConf.listPlayers.append(Player(vignette.text.text_input, vignette))
            for player in self.gameConf.listPlayers:
                player.vignette.setScore(player.score)
        diff = [0, 0, 0, 0, 0, 0]
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
        id_playlist = ressources.playlistsDeezer[self.gameConf.style]
        print(f"Round {self.gameConf.currentRound}\n"
              f"Génération Mixtape - {self.gameConf.style} - Id playlist Deezer {id_playlist}")
        self.gameConf.listMixtapes.append(Mixtape(diff, playlist=id_playlist))
        self.gameConf.dspInfos()
        self.state = "round_play"

    def roundListening(self):

        self._playAlignementJoueursBas_(len(self.gameConf.listVignettes))

        if self.premierPassagePlay:
            playSonAJouer = []
            for song in self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver:
                if not song.found:
                    playSonAJouer.append(pygame.mixer.Sound(f"game/{song.id}.mp3"))

            for song in playSonAJouer:
                song.play()
            self.premierPassagePlay = False

        playButtonMusic = Button(
            images=ressources.playButtonPlayMusic,
            pos=(ressources.screen_width * 0.5, ressources.screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        button_positions = [
            (ressources.screen_width * 0.10, ressources.screen_height * 0.30),
            (ressources.screen_width * 0.40, ressources.screen_height * 0.30),
            (ressources.screen_width * 0.70, ressources.screen_height * 0.30),
            (ressources.screen_width * 0.10, ressources.screen_height * 0.58),
            (ressources.screen_width * 0.40, ressources.screen_height * 0.58),
            (ressources.screen_width * 0.70, ressources.screen_height * 0.58)
        ]

        playListButtonCover = []
        playListTitles = []
        playListArtists = []
        playListFounder = []

        for song in self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver:
            playListButtonCover.append(
                Button(
                    images=[pygame.transform.scale(pygame.image.load(song.cover),
                                                   (0.146 * ressources.screen_width, 0.146 * ressources.screen_width))],
                    pos=button_positions[song.id],
                    text_input=None, font=None, base_color=None, hovering_color=None
                )
            )
            if song.found:
                playListFounder.append((pygame.transform.scale(pygame.image.load(song.founder.vignette.bufferPerso), (
                0.065 * ressources.screen_width, 0.116 * ressources.screen_height)), button_positions[song.id]))

        for id, song in enumerate(self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver):
            if song.found:
                color = "grey"
            else:
                color = "black"
            left = button_positions[id][0] + 0.09 * ressources.screen_width
            playTitreSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.title, True, color)
            playTitreSon_Rect = playTitreSon.get_rect(left=left, top=button_positions[id][1] - 0.05 * ressources.screen_width)

            playArtistSon = ressources.get_font(ressources.nunitoRegular,
                                                round(ressources.screen_height * 0.02)).render(
                song.artist, True, color)
            playArtistSon_Rect = playArtistSon.get_rect(left=left, top=button_positions[id][1] - 0.02 * ressources.screen_width)

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
            pos=(ressources.screen_width * 0.5, ressources.screen_height * 0.1),
            text_input=None, font=None, base_color=None, hovering_color=None)
        playSoundOn = True

        playListButtonCover = []
        playListTitles = []
        playListArtists = []
        playListFounder = []
        button_positions = [
            (ressources.screen_width * 0.10, ressources.screen_height * 0.35),
            (ressources.screen_width * 0.42, ressources.screen_height * 0.35),
            (ressources.screen_width * 0.74, ressources.screen_height * 0.35),
            (ressources.screen_width * 0.10, ressources.screen_height * 0.75),
            (ressources.screen_width * 0.42, ressources.screen_height * 0.75),
            (ressources.screen_width * 0.74, ressources.screen_height * 0.75)
        ]

        for song in self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver:
            playListButtonCover.append(
                Button(
                    images=[pygame.transform.scale(pygame.image.load(song.cover),
                                                   (0.146 * ressources.screen_width, 0.146 * ressources.screen_width))],
                    pos=button_positions[song.id],
                    text_input=None, font=None, base_color=None, hovering_color=None
                )
            )
            if song.found:
                playListFounder.append((pygame.transform.scale(pygame.image.load(song.founder.vignette.bufferPerso), (
                    0.065 * ressources.screen_width, 0.116 * ressources.screen_height)), button_positions[song.id]))

        for id, song in enumerate(self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver):
            if song.found:
                color = "grey"
            else:
                color = "black"
            left = button_positions[id][0] + 0.09 * ressources.screen_width
            playTitreSon = ressources.get_font(ressources.nunitoRegular, round(ressources.screen_height * 0.02)).render(
                song.title, True, color)
            playTitreSon_Rect = playTitreSon.get_rect(left=left, top=button_positions[id][1] - 0.05 * ressources.screen_width)

            playArtistSon = ressources.get_font(ressources.nunitoRegular,
                                                round(ressources.screen_height * 0.02)).render(
                song.artist, True, color)
            playArtistSon_Rect = playArtistSon.get_rect(left=left, top=button_positions[id][1] - 0.02 * ressources.screen_width)

            playListTitles.append((playTitreSon, playTitreSon_Rect))
            playListArtists.append((playArtistSon, playArtistSon_Rect))

        playButtonPass = Button(images=ressources.menuPlayButton, pos=(ressources.screen_width * 0.85, ressources.screen_height * 0.12),
                                text_input="PASSER",
                                font=ressources.get_font(ressources.nunitoRegular, round(ressources.screen_width * 0.045)),
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
                    if button.checkForInput(playMousePosition) and not \
                    self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver[id].found:
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
                                        pos=(ressources.screen_width * (3 / 12), ressources.screen_height * 0.880),
                                        text_input="Titre",
                                        font=ressources.get_font(ressources.nunitoRegular, round(ressources.screen_width * 0.035)),
                                        base_color="White",
                                        hovering_color="#2F6DC7")

        attributionPointsGroupe = Button(images=ressources.attributionPoints,
                                         pos=(ressources.screen_width * (6 / 12), ressources.screen_height * 0.880),
                                         text_input="Groupe",
                                         font=ressources.get_font(ressources.nunitoRegular,
                                                                  round(ressources.screen_width * 0.035)),
                                         base_color="White",
                                         hovering_color="#2F6DC7")

        attributionPointsTitreEtGroupe = Button(images=ressources.attributionPoints,
                                                pos=(ressources.screen_width * (9 / 12), ressources.screen_height * 0.880),
                                                text_input="Titre+Groupe",
                                                font=ressources.get_font(ressources.nunitoRegular,
                                                                         round(ressources.screen_width * 0.026)),
                                                base_color="White",
                                                hovering_color="#2F6DC7")

        attributionPointsCroix = Button(images=ressources.attributionPointsBoutonCroix,
                                        pos=(ressources.screen_width * 0.92, ressources.screen_height * (1 / 8)),
                                        text_input=None, font=None, base_color=None, hovering_color=None)

        self._attributionPointsAlignementJoueursMotif_(len(self.gameConf.listVignettes))

        screen.blit(fond_attribution, (ressources.screen_width * 0.02, (1 / 25) * ressources.screen_height))
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
                                    self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver[
                                        self.gameConf.sonSelectionne].found = True
                                    self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver[
                                        self.gameConf.sonSelectionne].founder = player

                                    player.vignette.setScore(player.score)
                            self.gameConf.joueurSelectionne = None

                            count_found = 0

                            for song in self.gameConf.listMixtapes[self.gameConf.currentRound - 1].listeATrouver:
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

        if self.gameConf.currentRound == self.gameConf.numRounds:
            self.state = "end_game"
            pass
        screen.blit(background, (0, 0))
        interRoundsTitre = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render(
            f"Fin du round {self.gameConf.currentRound}", True, "white")
        interRoundsTitre_Rect = interRoundsTitre.get_rect(
            center=(ressources.screen_width * 0.50, ressources.screen_height * 0.116))
        players_sorted = sorted(self.gameConf.listPlayers, key=lambda player: player.score, reverse=True)
        screen.blit(interRoundsTitre, interRoundsTitre_Rect)
        for i, vignette in enumerate(players_sorted):
            if i == 0:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.45,
                                                   ressources.screen_height * 0.2))
            if i == 1:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.25,
                                                   ressources.screen_height * 0.26))
            if i == 2:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.65,
                                                   ressources.screen_height * 0.32))
            if i >= 3:
                players_sorted[i].vignette.setPos((ressources.screen_width * 0.01 + (
                            i - 2) * 0.15 * ressources.screen_width, ressources.screen_height * 0.7))
            players_sorted[i].vignette.afficher(screen)

        playButtonPass = Button(images=ressources.menuPlayButton, pos=(ressources.screen_width * 0.85, ressources.screen_height * 0.12),
                                text_input="PASSER",
                                font=ressources.get_font(ressources.nunitoRegular, round(ressources.screen_width * 0.045)),
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
            pos=(ressources.screen_width * 0.948, ressources.screen_height * 0.08),
            text_input=None, font=None, base_color=None, hovering_color=None)

        interRoundsTitre = ressources.get_font(ressources.nunitoRegular,
                                               round(ressources.screen_height * 0.052)).render("FIN DU JEU", True,
                                                                                               "white")
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

        playMousePosition = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButtonBack.checkForInput(playMousePosition):
                    self.gameConf.listVignettes = []
                    pygame.mixer.stop()
                    self.gameConf = GameConfig()
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
screen = pygame.display.set_mode((ressources.screen_width, ressources.screen_height))

pygame.display.set_caption("BlindMixTape")

background = pygame.transform.scale(pygame.image.load(ressources.background), (ressources.screen_width, ressources.screen_height))

fond_attribution = pygame.transform.scale(pygame.image.load(ressources.attributionPointsFond),
                                          (ressources.screen_width * 0.96, (16 / 17) * ressources.screen_height))

while True:
    gameState.stateManager()
    clock.tick(60)
