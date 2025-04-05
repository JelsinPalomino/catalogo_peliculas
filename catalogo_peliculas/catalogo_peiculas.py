import tkinter as tk
from client.gui_app import Frame

def main():
    root = tk.Tk()
    root.title('Catalogo de Películas')
    root.iconbitmap('catalogo_peliculas\img\cp-logo.ico')
    root.resizable(0,0)

    app = Frame(root=root)

    app.mainloop()



if __name__ == '__main__':
    main()