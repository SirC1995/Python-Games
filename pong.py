from livewires import games, color


games.init(screen_width = 1152, screen_height = 648, fps = 50)

# Tworzenie klasy Bat
class Bat(games.Sprite):
    """ Paletka sterowana przez gracza do odbijania piłeczki """

    image = games.load_image("paletka.png")


    def __init__(self):
        """ Inicjalizacja paletki i tworzenie licznika odbić """

        super(Bat, self).__init__(image = Bat.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)

        self.score = games.Text(value = 0, size = 25, color = color.white,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzedną x myszy. """

        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_bounce()


    def check_bounce(self):
        """ Sprawdź czy piłka została odbita. """

        for ball in self.overlapping_sprites:
            self.score.value += 1
            self.score.right = games.screen.width - 10
            ball.ball_bounce()
            if self.score.value % 5 == 0:
                ball.ball_speed()
                ball.ball_bounce()



# Tworzenei klasy Ball
class Ball(games.Sprite):
    """ Piłka odbijana od paletki i trzech scian. """

    image = games.load_image("pilka.png")
    speed = 1

    def __init__(self, y = 30):
        """ Inicjalizacja piłki. """

        super(Ball, self).__init__(image = Ball.image,
                                   x = games.screen.width/2, y = y,
                                   dy = Ball.speed,
                                   dx = Ball.speed)

    def update(self):
        """ Zmiana kierunku lotu piłki po dotknieciu ścian. """

        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.top < 0:
            self.dy = -self.dy

        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def ball_bounce(self):
        """ Odbicie piłki po zetknięciu z paletką. """

        self.dy = -self.dy

    def ball_speed(self):
        Ball.speed += 1
        self.dy = Ball.speed
        self.dx = Ball.speed


    def end_game(self):
        """ Zakończ grę."""

        end_message = games.Message(value = "Koniec gry!!",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)



def main():
    """ Uruchom grę. """

    court_image = games.load_image("tlo.jpg", transparent = False)
    games.screen.background = court_image

    ball = Ball()
    games.screen.add(ball)

    bat = Bat()
    games.screen.add(bat)

    games.mouse.is_visible = True

    games.screen.event_grab = True
    games.screen.mainloop()

# wystartowanie gry
main()
