from kivy.uix.relativelayout import RelativeLayout


def keyboardClosed(self):
    self.keyboard.unbind(on_key_down=self.onKeyboardDown)
    self.keyboard.unbind(on_key_up=self.onKeyboardUp)
    self.keyboard = None

def on_touch_down(self, touch):
    if not self.game_over_state and self.game_started_state:
        if touch.x > self.width / 2:
            self.current_turning_speed = -self.turning_speed * self.width
            # self.turn_offset = 20
        else:
            self.current_turning_speed = self.turning_speed * self.width
            # self.turn_offset = -20
    super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    self.current_turning_speed = 0


def onKeyboardDown(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'right':
        self.current_turning_speed = -self.turning_speed * self.width
    elif keycode[1] == 'left':
        self.current_turning_speed = self.turning_speed * self.width


def onKeyboardUp(self, keyboard, keycode):
    self.current_turning_speed = 0