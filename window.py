import pywhatkit
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta

def btn_clicked():
    telefone = entry0.get().strip()  # Obtem o número de telefone
    mensagem = entry1.get("1.0", END).strip()  # Obtem a mensagem

    if not telefone or not mensagem:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return

    # Obtém o tempo atual e adiciona 2 minutos para o envio
    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute + 2

    if minuto >= 60:
        minuto -= 60
        hora += 1

    # Verifica se a hora está válida
    if hora > 23:
        hora = 0

    # Envia a mensagem
    try:
        pywhatkit.sendwhatmsg(telefone, mensagem, hora, minuto)
        messagebox.showinfo("Sucesso", f"Mensagem enviada para {hora}:{minuto}!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

window = Tk()

window.geometry("640x480")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# Campo para o número de telefone
entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    412.5, 159.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#fefdfd",
    highlightthickness=0)

entry0.place(
    x=281.0, y=139,
    width=263.0,
    height=38)

# Campo para a mensagem
entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    412.5, 299.5,
    image=entry1_img)

entry1 = Text(
    bd=0,
    bg="#fefdfd",
    highlightthickness=0)

entry1.place(
    x=281.0, y=255,
    width=263.0,
    height=87)

# Botão para enviar mensagem
img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=350, y=371,
    width=133,
    height=48)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    330.5, 240.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()