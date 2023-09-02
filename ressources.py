# Ressources générales
import pygame


titleInit = f"\n\n" \
            f"██████  ██      ██ ███    ██ ██████  ███    ███ ██ ██   ██ ████████  █████  ██████  ███████ \n" \
            f"██   ██ ██      ██ ████   ██ ██   ██ ████  ████ ██  ██ ██     ██    ██   ██ ██   ██ ██      \n" \
            f"██████  ██      ██ ██ ██  ██ ██   ██ ██ ████ ██ ██   ███      ██    ███████ ██████  █████   \n" \
            f"██   ██ ██      ██ ██  ██ ██ ██   ██ ██  ██  ██ ██  ██ ██     ██    ██   ██ ██      ██      \n" \
            f"██████  ███████ ██ ██   ████ ██████  ██      ██ ██ ██   ██    ██    ██   ██ ██      ███████ \n" \
            f"                                                                                            " \
            f"                                                                                            "
version = 1.1

pygame.init()
background = "view/assets/windows/Window_10.png"
nunitoRegular = "view/assets/Nunito/static/Nunito-Bold.ttf"
BubbleFont = "view/assets/bubble3D.ttf"
blomberg = "view/assets/blomberg/Blomberg.otf"
blueButtonColor = "#007EC3"
greenButtonColor = "#6BBF00"
redButtonColor = "#C2181B"

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
# screen_width, screen_height = 1280, 720


def get_font(font, size):  # Fonction pour obtenir la police Press-Start-2P à la taille désirée
    return pygame.font.Font(font, size)


# Dico des playlists Deezer
playlistsDeezer = {
    "Actuel": 53362031,
    "FR 2022": 741188545,
    "FR 1980": 6025166364,
    "Afrobeat": 11272355264,    
    "Monde 2022": 10896810924,
    "Rap FR 2022": 10855125902,
    "Rock": 1306931615,
    "Pop": 1036183001,
    "Reggae": 2448918882,
    "Classique": 747148961,
    "Metal": 2655390504,
    "Disco": 2015058202,
    "K-pop": 873660353,
    "BMT": 11682866204,
    "Top 500 ever": 10295099302
}

largeurBoutons = screen_width * 0.039
hauteurBoutons = screen_height * 0.069
# Menu Principal

menuLogo = pygame.image.load("view/assets/logo.png")
menuGIF = [pygame.transform.scale(pygame.image.load(f"view/assets/GIF_dance/frame_{i}_delay-0.08s.gif"),
                                  (0.195 * screen_width, 0.374 * screen_height)) for i in range(18)]
menuPlayButton = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_14.png"),
                                         (0.185 * screen_width, 0.146 * screen_height))]
menuOptionButton = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_13.png"),
                                           (0.185 * screen_width, 0.146 * screen_height))]
menuQuitButton = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_15.png"),
                                         (0.185 * screen_width, 0.146 * screen_height))]

# Lobby

lobbyWindowOption1 = pygame.transform.scale(pygame.image.load("view/assets/windows/Window_24.png"),
                                            (0.370 * screen_width, 0.960 * screen_height))
lobbyWindowOption2 = pygame.transform.scale(pygame.image.load("view/assets/windows/Window_35.png"),
                                            (0.278 * screen_width, 0.164 * screen_height))
lobbyIconPlayers = pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_98.png"),
                                          (0.072 * screen_width, 0.123 * screen_height))
lobbyIconDifficulty = pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_29.png"),
                                             (0.072 * screen_width, 0.123 * screen_height))
lobbyIconRounds = pygame.transform.scale(pygame.image.load("view/assets/buttons/Button2_01.png"),
                                         (0.072 * screen_width, 0.123 * screen_height))
lobbyIconStyle = pygame.transform.scale(pygame.image.load("view/assets/buttons/Button2_09.png"),
                                        (0.072 * screen_width, 0.123 * screen_height))

lobbyButtonRight = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_46.png"),
                                           (largeurBoutons, hauteurBoutons))]
lobbyButtonLeft = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_62.png"),
                                          (largeurBoutons, hauteurBoutons))]

lobbyButtonPlus = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/plus/plus_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/plus/plus_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/plus/plus_3.png"), (largeurBoutons, hauteurBoutons))]

lobbyButtonMoins = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/moins/moins_1.png"),
                           (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/moins/moins_2.png"),
                           (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/moins/moins_3.png"),
                           (largeurBoutons, hauteurBoutons))]

lobbyButtonBack = [pygame.transform.scale(pygame.image.load("view/assets/buttons/home/home_1.png"),
                                          (0.065 * screen_width, 0.116 * screen_height)),
                   pygame.transform.scale(pygame.image.load("view/assets/buttons/home/home_2.png"),
                                          (largeurBoutons, hauteurBoutons)),
                   pygame.transform.scale(pygame.image.load("view/assets/buttons/home/home_3.png"),
                                          (largeurBoutons, hauteurBoutons))]

lobbyButtonPlay = [pygame.transform.scale(pygame.image.load("view/assets/buttons/play/play_1.png"),
                                          (0.185 * screen_width, 0.146 * screen_height)),
                   pygame.transform.scale(pygame.image.load("view/assets/buttons/play/play_2.png"),
                                          (largeurBoutons, hauteurBoutons)),
                   pygame.transform.scale(pygame.image.load("view/assets/buttons/play/play_3.png"),
                                          (largeurBoutons, hauteurBoutons))]

vignetteFond = pygame.transform.scale(pygame.image.load("view/assets/windows/Window_13.png"),
                                      (0.097 * screen_width, 0.174 * screen_height))

vignetteButtonCroix = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_23.png"),
                                              (0.020 * screen_width, 0.035 * screen_height))]

lobbyMute = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/Mute/Mute_1.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/Mute/Mute_2.png"), (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/Mute/Mute_3.png"), (largeurBoutons, hauteurBoutons))]

lobbySoundOn = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/SoundOn/SoundOn_1.png"),
                           (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/SoundOn/SoundOn_2.png"),
                           (largeurBoutons, hauteurBoutons)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/SoundOn/SoundOn_3.png"),
                           (largeurBoutons, hauteurBoutons))]

persos = [f"view/assets/perso/perso_{k}.png" for k in range(1, 21)]

# Play

playButtonPlayMusic = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_47.png"),
                                              (screen_width * 0.07, screen_width * 0.07))]
playButtonMuteMusic = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button2_35.png"),
                                              (screen_width * 0.07, screen_width * 0.07))]
playButtonMuteTest = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_46.png"),
                                             (screen_width * 0.07, screen_width * 0.07))]

# attrib

attributionPointsFond = "view/assets/windows/Window_28.png"
attributionPoints = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/attributionpoints/attributionpoints_1.png"),
                           (0.185 * screen_width, 0.146 * screen_height)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/attributionpoints/attributionpoints_2.png"),
                           (0.185 * screen_width, 0.146 * screen_height)),
    pygame.transform.scale(pygame.image.load("view/assets/buttons/attributionpoints/attributionpoints_3.png"),
                           (0.185 * screen_width, 0.146 * screen_height))]
attributionPointsBoutonCroix = [pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_23.png"),
                                                       (0.040 * screen_width, 0.070 * screen_height))]

attributionPointsPassButton = [
    pygame.transform.scale(pygame.image.load("view/assets/buttons/Button_15.png"),
                           (0.185 * screen_width, 0.146 * screen_height))]
