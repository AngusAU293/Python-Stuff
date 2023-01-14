from ursina import *
from tkinter import messagebox
def crash():
    app.destroy()
    messagebox.showerror("Crash","Game crashed manually")
def main():
    app = Ursina()
    camera.fov = 70
    Text.size = 0.05
    Text.default_resolution = 1080 * Text.size
    stext = Text(text="Chase Clicker (click green square to start)")
    stext.x = -0.5
    stext.y = -0.27
    stext.background = False
    stext.visible = True
    Text.size = 0.03
    qText = Text(text="X")
    qText.x = 0.86
    qText.y = 0.5
    qText.background = False
    qText.visible = True
    window.borderless = True
    window.fps_counter.enabled = False
    window.fullscreen = True
    def start():
        stext.visible = False
        def kwinner():
            Text.size = 0.05
            Text.default_resolution = 1080 * Text.size
            kwtext = Text(text="Caught!")
            kwtext.x = 0
            kwtext.y = 0
            kwtext.background = False
            destroy(p)
            kwtext.visible = True
        destroy(e)
        p = Entity(model="sphere", scale=(1,1,1), collider="sphere", on_click=kwinner)
        p.color = color.blue
        p.position = Vec2(0.7,0.7)
        def update():
            p.x += held_keys['d'] * 0.21
            p.x -= held_keys['a'] * 0.21
            p.y += held_keys['w'] * 0.21
            p.y -= held_keys['s'] * 0.21
        p.update = update
    def quitGame():
        MsgBox = messagebox.askquestion("Exit","Are you sure you want to exit?", icon = 'warning')
        if MsgBox == "yes":
            app.destroy()
        else:
            start()
    e = Entity(model="cube", scale=(5,5), collider="box", on_click=start)
    e.color = color.green
    e.position = Vec2(0,0)
    q = Entity(model="cube", scale=(0.7,0.6,0), collider="box", on_click=quitGame)
    q.color = color.red
    q.position = Vec2(13.7,7.7)
    app.run()
main()
