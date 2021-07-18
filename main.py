# Creating the App

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.camera import Camera
from opencv_cam import CamApp

# declare screens
class PreLoadScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class RememberScreen(Screen):
    pass

class RecogniseScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass


# App class
class iKnowU(MDApp):

    dialog = None
    cam_app = CamApp()

    def build(self):
        buildkv = Builder.load_file("main.kv")
        return buildkv

    def popup_msg(self):
        if not self.dialog:
            self.dialog = MDDialog(text="This person has been saved.",
                                   buttons = [
                                       MDRectangleFlatButton(text="Close", on_press=self.close_popup)])
        self.dialog.open()

    def close_popup(self,obj):
        self.dialog.dismiss()

    def load_facial(self):
        self.cam_app.run()

    def stop_facial(self):
        self.cam_app.my_camera.stop()

if __name__ == "__main__":
    iKnowU().run()



