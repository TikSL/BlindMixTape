# Ressources générales
import pygame

pygame.init()
background = "vue/assets/windows/Window_10.png"
nunitoRegular = "vue/assets/Nunito/static/Nunito-Bold.ttf"
BubbleFont = "vue/assets/bubble3D.ttf"
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen_width = 1280
screen_height = 720


def get_font(font, size):  # Fonction pour obtenir la police Press-Start-2P à la taille désirée
    return pygame.font.Font(font, size)


largeurBoutons = screen_width * 0.039
hauteurBoutons = screen_height * 0.069
# Menu Principal

menuLogo = pygame.image.load("vue/assets/logo.png")
menuGIF = [pygame.transform.scale(pygame.image.load(f"vue/assets/GIF_dance/frame_{i}_delay-0.08s.gif"),
                                  (0.195 * screen_width, 0.374 * screen_height)) for i in range(18)]
menuPlayButton = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_14.png"),
                                         (0.185 * screen_width, 0.146 * screen_height))]
menuQuitButton = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_15.png"),
                                         (0.185 * screen_width, 0.146 * screen_height))]

# Lobby

lobbyWindowOption1 = pygame.transform.scale(pygame.image.load("vue/assets/windows/Window_24.png"),
                                            (0.358 * screen_width, 0.868 * screen_height))
lobbyWindowOption2 = pygame.transform.scale(pygame.image.load("vue/assets/windows/Window_35.png"),
                                            (0.278 * screen_width, 0.164 * screen_height))
lobbyIconPlayers = pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_98.png"),
                                          (0.072 * screen_width, 0.123 * screen_height))
lobbyIconDifficulty = pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_29.png"),
                                             (0.072 * screen_width, 0.123 * screen_height))
lobbyIconRounds = pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button2_01.png"),
                                         (0.072 * screen_width, 0.123 * screen_height))

lobbyButtonPlus = [
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/plus/plus_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/plus/plus_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/plus/plus_3.png"), (largeurBoutons, hauteurBoutons))]

lobbyButtonMoins = [
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/moins/moins_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/moins/moins_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/moins/moins_3.png"), (largeurBoutons, hauteurBoutons))]

lobbyButtonBack = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/home/home_1.png"),
                                          (0.065 * screen_width, 0.116 * screen_height)),
                   pygame.transform.scale(pygame.image.load("vue/assets/buttons/home/home_2.png"),
                                          (largeurBoutons, hauteurBoutons)),
                   pygame.transform.scale(pygame.image.load("vue/assets/buttons/home/home_3.png"),
                                          (largeurBoutons, hauteurBoutons))]

lobbyButtonPlay = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/play/play_1.png"),
                                          (0.185 * screen_width, 0.146 * screen_height)),
                   pygame.transform.scale(pygame.image.load("vue/assets/buttons/play/play_2.png"),
                                          (largeurBoutons, hauteurBoutons)),
                   pygame.transform.scale(pygame.image.load("vue/assets/buttons/play/play_3.png"),
                                          (largeurBoutons, hauteurBoutons))]

vignetteFond = pygame.transform.scale(pygame.image.load("vue/assets/windows/Window_13.png"),
                                      (0.097 * screen_width, 0.174 * screen_height))

vignetteButtonCroix = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_23.png"),
                                              (0.020 * screen_width, 0.035 * screen_height))]

lobbyMute = [
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/Mute/Mute_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/Mute/Mute_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/Mute/Mute_3.png"), (largeurBoutons, hauteurBoutons))]

lobbySoundOn = [
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/SoundOn/SoundOn_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/SoundOn/SoundOn_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/SoundOn/SoundOn_3.png"), (largeurBoutons, hauteurBoutons))]

persos = [f"vue/assets/perso/perso_{k}.png" for k in range(1, 21)]

# Play

playButtonPlayMusic = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_47.png"),
                                              (screen_width * 0.07, screen_width * 0.07))]
playButtonMuteMusic = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button2_35.png"),
                                              (screen_width * 0.07, screen_width * 0.07))]
playButtonMuteTest = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_46.png"),
                                             (screen_width * 0.07, screen_width * 0.07))]

# attrib

attributionPointsFond = "vue/assets/windows/Window_28.png"
attributionPoints = [
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/attributionpoints/attributionpoints_1.png"),
                           (0.185 * screen_width, 0.146 * screen_height)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/attributionpoints/attributionpoints_2.png"),
                           (0.185 * screen_width, 0.146 * screen_height)),
    pygame.transform.scale(pygame.image.load("vue/assets/buttons/attributionpoints/attributionpoints_3.png"),
                           (0.185 * screen_width, 0.146 * screen_height))]
attributionPointsBoutonCroix = [pygame.transform.scale(pygame.image.load("vue/assets/buttons/Button_23.png"),
                                                       (0.040 * screen_width, 0.070 * screen_height))]
