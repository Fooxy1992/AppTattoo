from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from ttkthemes import ThemedTk
from tkcalendar import Calendar

# Adicione o código das classes e funções que já criamos aqui
import os
from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta

@dataclass
class TattooIdea:
    image_path: str
    description: str
    size: float
    colors: bool
    body_part: str

@dataclass
class TattooArtist:
    name: str

@dataclass
class Customer:
    name: str

@dataclass
class PerfilTatuador:
    tatuador: TattooArtist
    sobre_mim: str
    estilos: List[str]

def enviar_ideia_tatuagem(cliente: Customer, ideia_tatuagem: TattooIdea):
    return f"{cliente.name} enviou uma ideia de tatuagem: {ideia_tatuagem.description}"

def comentario_tatuador(tatuador: TattooArtist, comment: str, price_range: str):
    return f"{tatuador.name} comentou: {comment}. Preço estimado: {price_range}"

def exibir_conversa(conversa: list):
    for mensagem in conversa:
        print(mensagem)

def adicionar_imagem(cliente: Customer, caminho_imagem: str):
    return f"{cliente.name} adicionou uma imagem: {caminho_imagem}"

def adicionar_descricao(cliente: Customer, descricao: str):
    return f"{cliente.name} adicionou uma descrição: {descricao}"

def solicitar_alteracao(cliente: Customer, solicitacao: str):
    return f"{cliente.name} solicitou uma alteração: {solicitacao}"

def concordar_com_alteracao(tatuador: TattooArtist):
    return f"{tatuador.name} concordou com a alteração."

def sugerir_novo_preco(tatuador: TattooArtist, nova_faixa_preco: str):
    return f"{tatuador.name} sugeriu um novo preço: {nova_faixa_preco}"

def exibir_tatuadores_disponiveis(tatuadores: List[PerfilTatuador]):
    print("Tatuadores disponíveis:")
    for perfil in tatuadores:
        print(f"Nome: {perfil.tatuador.name}")
        print(f"Sobre mim: {perfil.sobre_mim}")
        print(f"Estilos dominados: {', '.join(perfil.estilos)}")
        print()

def agendar_tatuagem(cliente: Customer, data_agendamento: datetime):
    return f"{cliente.name} solicitou agendamento para: {data_agendamento.strftime('%d/%m/%Y')}"

def resposta_agendamento(tatuador: TattooArtist, resposta: str, data_sugerida: datetime = None):
    if data_sugerida:
        return f"{tatuador.name} {resposta} o agendamento e sugeriu uma nova data: {data_sugerida.strftime('%d/%m/%Y')}"
    return f"{tatuador.name} {resposta} o agendamento"

def alterar_agendamento(cliente: Customer, nova_data: datetime):
    return f"{cliente.name} alterou o agendamento para: {nova_data.strftime('%d/%m/%Y')}"

def cancelar_agendamento(cliente: Customer):
    return f"{cliente.name} cancelou o agendamento"

def verificar_prazo_cancelamento(data_agendamento: datetime) -> bool:
    prazo_cancelamento = data_agendamento - timedelta(days=2)
    return datetime.now() <= prazo_cancelamento
if __name__ == "__main__":
    tatuador1 = TattooArtist("Fernanda")
    perfil_tatuador1 = PerfilTatuador(tatuador1, "Especialista em tatuagens realistas.", ["Realismo", "Retratos"])

    tatuador2 = TattooArtist("Carlos")
    perfil_tatuador2 = PerfilTatuador(tatuador2, "Amo criar tatuagens geométricas.", ["Geométricas", "Pontilhismo"])

    tatuadores_disponiveis = [perfil_tatuador1, perfil_tatuador2]
    
    exibir_tatuadores_disponiveis(tatuadores_disponiveis)

    ideia_tatuagem = TattooIdea("imagem.jpg", "Leão", 15, False, "Braço")
    cliente = Customer("João")
    tatuador = TattooArtist("Fernanda")

    conversa = []
    conversa.append(enviar_ideia_tatuagem(cliente, ideia_tatuagem))
    conversa.append(comentario_tatuador(tatuador, "Podemos adicionar mais detalhes no rosto do leão.", "R$ 800 - R$ 1000"))

    exibir_conversa(conversa)

    data_agendamento = datetime(2023, 4, 25)
    conversa.append(agendar_tatuagem(cliente, data_agendamento))
    conversa.append(resposta_agendamento(tatuador, "aceitou"))

    exibir_conversa(conversa)

    if verificar_prazo_cancelamento(data_agendamento):
        conversa.append(alterar_agendamento(cliente, datetime(2023, 4, 26)))
        conversa.append(resposta_agendamento(tatuador, "aceitou"))
        exibir_conversa(conversa)
    else:
        print("Prazo para cancelamento ou alteração expirado.")

# ...

# Funções da interface gráfica

def anexar_imagem():
    global caminho_imagem
    caminho_imagem = filedialog.askopenfilename(filetypes=[("Arquivos de imagem", "*.jpg;*.jpeg;*.png"), ("Todos os arquivos", "*.*")])
    if caminho_imagem:
        extensao = caminho_imagem.split(".")[-1].lower()
        if extensao in ["jpg", "jpeg", "png"]:
            imagem_label.config(text=caminho_imagem)
        else:
            messagebox.showerror("Erro", "Por favor, selecione uma imagem nos formatos JPEG, JPG ou PNG.")

def enviar_ideia_tatuagem_gui():
    ideia_descricao = ideia_entry.get()
    regiao_corpo = regiao_combobox.get()
    if caminho_imagem and regiao_corpo:
        ideia_tatuagem = TattooIdea(caminho_imagem, ideia_descricao, 10, True, regiao_corpo)
        conversa.append(enviar_ideia_tatuagem(cliente, ideia_tatuagem))
        messagebox.showinfo("Tatuagem", f"Ideia de tatuagem enviada: {ideia_descricao}")
    else:
        messagebox.showerror("Erro", "Por favor, anexe uma imagem e selecione a região do corpo antes de enviar a ideia de tatuagem.")
    
def on_calendario_selecionado(date):
    data_entry.delete(0, END)
    data_entry.insert(0, date.strftime('%d/%m/%Y'))
    
def selecionar_data():
    top = Toplevel(app)
    cal = Calendar(top, font="Arial 14", selectmode='day', year=2023, month=3, day=21)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Selecionar", command=lambda: on_calendario_selecionado(cal.selection_get())).pack()


def solicitar_agendamento_gui():
    data_agendamento_str = data_entry.get()
    if data_agendamento_str:
        data_agendamento = datetime.strptime(data_agendamento_str, '%d/%m/%Y')
        messagebox.showinfo("Agendamento", "Agendamento solicitado")
    else:
        messagebox.showerror("Erro", "Por favor, selecione a data do agendamento.")

app = ThemedTk(theme="adapta")
app.title("Estúdio de tatuagem")

frame = ttk.Frame(app, padding="10")
frame.grid(column=0, row=0, sticky=(N, S, E, W))

ttk.Label(frame, text="Ideia da tatuagem:").grid(column=0, row=0, sticky=W)
ideia_entry = ttk.Entry(frame, width=40)
ideia_entry.grid(column=1, row=0, sticky=(W, E))

ttk.Label(frame, text="Região do corpo:").grid(column=0, row=1, sticky=W)
regiao_combobox = ttk.Combobox(frame, values=["Braço", "Perna", "Costas", "Peito", "Pé", "Mão"], state="readonly")
regiao_combobox.grid(column=1, row=1, sticky=(W, E))

ttk.Label(frame, text="Data do agendamento (dd/mm/aaaa):").grid(column=0, row=6, sticky=W)
data_entry = ttk.Entry(frame, width=10)
data_entry.grid(column=1, row=6, sticky=W)
data_selecionar_button = ttk.Button(frame, text="Selecionar", command=selecionar_data)
data_selecionar_button.grid(column=2, row=6, sticky=W)

anexar_imagem_button = ttk.Button(frame, text="Anexar Imagem", command=anexar_imagem)
anexar_imagem_button.grid(column=1, row=2, sticky=E)

enviar_ideia_button = ttk.Button(frame, text="Enviar Ideia", command=enviar_ideia_tatuagem_gui)
enviar_ideia_button.grid(column=1, row=4, sticky=E)
enviar_ideia_button.configure(style='Blue.TButton')

imagem_label = ttk.Label(frame, text="")
imagem_label.grid(column=0, row=5, columnspan=2, sticky=W)

ttk.Label(frame, text="Data do agendamento (dd/mm/aaaa):").grid(column=0, row=6, sticky=W)
data_entry = ttk.Entry(frame, width=10)
data_entry.grid(column=1, row=6, sticky=W)
data_selecionar_button = ttk.Button(frame, text="Selecionar", command=selecionar_data)
data_selecionar_button.grid(column=2, row=6, sticky=W)

solicitar_agendamento_button = ttk.Button(frame, text="Solicitar Agendamento", command=solicitar_agendamento_gui)
solicitar_agendamento_button.grid(column=1, row=8, sticky=E)
solicitar_agendamento_button.configure(style='Green.TButton')

ttk.Separator(frame, orient=HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky=(W,E))

ttk.Label(frame, text="Conversa com o tatuador:").grid(column=0, row=10, sticky=W)
conversa_text = Text(frame, height=10, width=40, state="disabled")
conversa_text.grid(column=1, row=10, sticky=(W, E))

ttk.Label(frame, text="Digite sua mensagem:").grid(column=0, row=11, sticky=W)
mensagem_entry = ttk.Entry(frame, width=40)
mensagem_entry.grid(column=1, row=11, sticky=(W, E))

enviar_mensagem_button = ttk.Button(frame, text="Enviar Mensagem")
enviar_mensagem_button.grid(column=1, row=12, sticky=E)
enviar_mensagem_button.configure(style='Blue.TButton')

frame.columnconfigure(1, weight=1)

app.mainloop()