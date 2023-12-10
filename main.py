import kivy
kivy.require('1.0.7')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def animate(self, instance):

        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))
        animation.start(instance)

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = Button(size_hint=(None, None), text='plop',
                        on_press=self.animate)
        return button


if __name__ == '__main__':
    TestApp().run()