from kivy import platform
from kivy.config import Config

Config.set('graphics', 'width', '1350')
Config.set('graphics', 'height', '600')

from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color, Line, Quad, Triangle
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
import time

Builder.load_file("menu.kv")

#glowne okno gry
class MainWidget(RelativeLayout):
    from transforms import transform, transform2DToPerspective, transformFromperspectiveTo2D
    from user_interactions import keyboardClosed, onKeyboardUp, onKeyboardDown, on_touch_down, on_touch_up
    from path_generation import generate_tiles_coordinates, pre_fill_tiles_coordinates
    from additionals import tileContainsPoint

    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    menu_widget = ObjectProperty()

    number_of_vertical_lines = 16
    vertical_lines_spacing = .4     # percentage of screen width
    vertical_lines = []

    number_of_horizontal_lines = 10
    horizontal_lines_spacing = .1  # percentage of screen height
    horizontal_lines = []
    #line indexes: first vertivcal line from the left index is -(numberOfLines/2)+1, horizontal lines are indexed from the bottom and first index is 0

    tiles = []
    number_of_tiles = 12
    tiles_coordinates = []

    current_offset_y = 0
    game_speed = 0.004

    turning_speed = 0.012
    current_turning_speed = 0
    current_offset_x = 0
    #turn_offset = 0

    current_loop = 0

    ship_width = .1
    ship_height = .04
    ship_offset_y = .2
    ship = None

    game_over_state = False
    game_started_state = False

    menu_title = StringProperty("G   A   L   A   X   Y")
    menu_button_title = StringProperty("START")

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.initVerticalLines()
        self.initHorizontalLines()
        self.initTiles()
        self.init_ship()
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()
        if self.isDesktop():
            self.keyboard = Window.request_keyboard(self.keyboardClosed, self)
            self.keyboard.bind(on_key_down=self.onKeyboardDown)
            self.keyboard.bind(on_key_up=self.onKeyboardUp)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def reset_game(self):
        self.current_offset_y = 0
        self.current_loop = 0
        self.current_turning_speed = 0
        self.current_offset_x = 0

        self.tiles_coordinates = []
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()
        self.game_over_state = False

    def isDesktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        else:
            return False

    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()

    def checkShipColision(self):
        #function checks if every of ship points is contained in any of three closest tiles
        ship_points = self.ship.points
        points_on_track = 0
        for tile in self.tiles[0:3]:
            if self.tileContainsPoint(tile.points, ship_points[0], ship_points[1]):
                points_on_track += 1
            if self.tileContainsPoint(tile.points, ship_points[2], ship_points[3]):
                points_on_track += 1
            if self.tileContainsPoint(tile.points, ship_points[4], ship_points[5]):
                points_on_track += 1

        if points_on_track < 3:
            return True
        return False

    def initVerticalLines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.number_of_vertical_lines):
                self.vertical_lines.append(Line())

    def initHorizontalLines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.number_of_horizontal_lines):
                self.horizontal_lines.append(Line())

    def initTiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.number_of_tiles):
                self.tiles.append(Quad())

    def getLineXFromIndex(self, index):
        central_x = self.perspective_point_x
        spacing = self.vertical_lines_spacing * self.width
        offset = index - 0.5
        return central_x + (spacing * offset) + self.current_offset_x

    def getLineYFromIndex(self, index):
        spacing = self.horizontal_lines_spacing * self.height
        return (index * spacing) - self.current_offset_y

    def getTileCoordinates(self, ti_x, ti_y):
        ti_y -= self.current_loop
        x = self.getLineXFromIndex(ti_x)
        y = self.getLineYFromIndex(ti_y)
        return x, y

    def updateShip(self):
        ship_width = self.ship_width * self.width
        ship_height = self.ship_height * self.height
        ship_offset_y = self.ship_offset_y * self.height
        self.ship.points = [(self.width-ship_width)/2, ship_offset_y, self.width/2, ship_height+ship_offset_y, (ship_width+self.width)/2, ship_offset_y]

    def updateVerticalLines(self):
        start_index = -int(self.number_of_vertical_lines/2) + 1
        for i in range(start_index, start_index + self.number_of_vertical_lines):
            line_x = self.getLineXFromIndex(i)

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)

            self.vertical_lines[i].points = [x1, y1, x2, y2]

    def updateHorizontalLines(self):
        start_index = -int(self.number_of_vertical_lines / 2) + 1
        end_index = start_index + self.number_of_vertical_lines - 1
        xmin = self.getLineXFromIndex(start_index)
        xmax = self.getLineXFromIndex(end_index)

        for i in range(self.number_of_horizontal_lines):
            line_y = self.getLineYFromIndex(i)

            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)

            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def updateTiles(self):
        for i in range(self.number_of_tiles):
            tile_coordinates = self.tiles_coordinates[i]
            xmin, ymin = self.getTileCoordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.getTileCoordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)
            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)
            self.tiles[i].points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def update(self, dt):
        offset_y = self.horizontal_lines_spacing * self.height
        self.perspective_point_x = self.width / 2
        self.perspective_point_y = self.height * 0.75
        time_factor = dt * 60   #dt - delta time tells us how much time really passed from last function call
                                #if function had waited longer than 1/60s horizontal line have to move more than regular offset
        self.updateVerticalLines()
        self.updateHorizontalLines()
        self.updateTiles()
        self.updateShip()
        if not self.game_over_state and self.game_started_state:
            self.current_offset_y += time_factor * self.game_speed * self.height
            while self.current_offset_y >= offset_y:
                self.current_offset_y -= offset_y
                self.current_loop += 1
                self.generate_tiles_coordinates()

            self.current_offset_x += time_factor * self.current_turning_speed

        if self.checkShipColision() and not self.game_over_state:
            self.game_over_state = True
            self.game_started_state = False
            self.menu_title = "G  A  M  E    O  V  E  R"
            self.menu_button_title = "RESTART"
            self.menu_widget.opacity = 1

        '''if self.turn_offset > 0:
            self.current_offset_x -= self.vertical_lines_spacing * self.width / 20
            self.turn_offset -= 1
        elif self.turn_offset < 0:
            self.current_offset_x += self.vertical_lines_spacing * self.width / 20
            self.turn_offset += 1'''

    def on_menu_button_click(self):
        self.game_started_state = True
        self.menu_widget.opacity = 0
        self.reset_game()

class GalaxyApp(App):
    pass
GalaxyApp().run()