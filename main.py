import customtkinter as ctk
import yt_dlp

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AppDescargador(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mi Descargador Pro")
        self.geometry("500x350")

        # Elementos de la interfaz
        self.label = ctk.CTkLabel(self, text="Pega el enlace de YouTube:", font=("Arial", 16))
        self.label.pack(pady=20)

        self.url_entry = ctk.CTkEntry(self, width=400, placeholder_text="https://www.youtube.com/watch?v=...")
        self.url_entry.pack(pady=10)

        self.res_label = ctk.CTkLabel(self, text="Selecciona la resolución:")
        self.res_label.pack(pady=5)

        self.res_option = ctk.CTkOptionMenu(self, values=["720p", "480p", "360p", "Lo mejor disponible"])
        self.res_option.pack(pady=10)

        self.download_btn = ctk.CTkButton(self, text="Descargar ahora", command=self.descargar)
        self.download_btn.pack(pady=30)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def descargar(self):
        url = self.url_entry.get()
        res_elegida = self.res_option.get()

        if not url:
            self.status_label.configure(text="¡Error: Pega un link!", text_color="red")
            return

        # Mapeo de resolución para yt-dlp
        # format_str buscará la resolución elegida o la más cercana hacia abajo
        res_map = {
            "720p": "best[height<=720]",
            "480p": "best[height<=480]",
            "360p": "best[height<=360]",
            "Lo mejor disponible": "best"
        }

        ydl_opts = {
            'format': res_map.get(res_elegida, 'best'),
            'outtmpl': '%(title)s.%(ext)s',
        }

        try:
            self.status_label.configure(text="Descargando...", text_color="yellow")
            self.update()  # Refresca la interfaz para mostrar el texto

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.status_label.configure(text="¡Completado con éxito!", text_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)[:30]}...", text_color="red")


if __name__ == "__main__":
    app = AppDescargador()
    app.mainloop()