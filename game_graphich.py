import pygame as pg
import pygame_gui as pgui
import game_core as gc

class Graphich:
    def __init__(self):
        """
        Инициализирует все переменные, необходимые для работы класса,
        такие как экран, дисплей, шрифт, менеджер GUI.
        """
        pg.init()
        pg.display.set_caption('Виселица')
        self.screen_size = (800, 600)
        self.game = gc.GameCore()
        self.done = True
        self.screen = pg.display.set_mode(self.screen_size)
        self.manager = pgui.UIManager(self.screen_size)
        self.font = pg.font.Font(None, 36)
        self.clock = pg.time.Clock()

    def draw_text(self, text: str, x: int, y: int, color):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def draw_image(self, image: pg.Surface, x: int, y: int):
        pass

    def draw_textbox(self, x: int, y: int, width: int, height: int):

        if self.manager is None:
            raise ValueError("Manager is not initialized")

        text_box = pgui.elements.UITextBox(
            relative_rect=pg.Rect((x, y), (width, height)),
            manager=self.manager
        )
        try:
            text_box.update(1 / 60)
            text_box.draw_ui(self.screen)
        except pg.error as e:
            print(f"Failed to draw text box: {e}")

        return text_box.get_text()

Graphich().draw_textbox(0, 0, 100, 100)