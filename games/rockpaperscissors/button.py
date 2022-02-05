import pygame


class Button(object):
    def __init__(self, image_path, name, size, position):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = pygame.Rect(position, size)
        self.position = position
        self.name = name
        self.chosen = False

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    print("chosen")
                    self.chosen = True
                else:
                    self.chosen = False

class ButtonText(object):
    def __init__(self, name, position, font_type, font_size, text_colour, bg_colour):
        self.name = name
        self.position = position
        self.fontType = font_type
        self.textColour = text_colour
        self.bgColour = bg_colour
        self.font = pygame.font.SysFont(self.fontType, font_size)
        self.text = self.font.render(self.name, True, self.textColour, self.bgColour)
        self.rect = self.text.get_rect()
        self.rect.topright = position
        self.chosen = False

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.chosen = True
                else:
                    self.chosen = False
