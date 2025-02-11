import tkinter as tk
from tkinter import ttk, messagebox


class Processo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.bloco_alocado = None

    def desalocar(self):
        self.bloco_alocado = None


class GerenciadorMemoriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Memória")
        self.root.configure(bg='black')  # Cor de fundo preta
        self.centralizar_janela()
        self.processos = []
        self.espaco_livre = 100  # Inicialmente, todo o espaço está livre

        self.criar_interface()

    def centralizar_janela(self):
        largura_janela = 890
        altura_janela = 670
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    def criar_interface(self):
        estilo = ttk.Style()
        estilo.configure("TButton", padding=(10, 5), font=('Arial', 12))
        estilo.configure("TLabel", font=('Arial', 12))
        estilo.configure("Horizontal.TProgressbar", thickness=20, troughcolor='#D9D9D9', bordercolor='#D9D9D9',
                         background='#D9D9D9')

        quadro_externo = tk.Frame(self.root, bg='#282828')
        quadro_externo.pack(expand=True, fill='both')

        quadro = tk.Frame(quadro_externo, bg='#282828')
        quadro.place(relx=0.5, rely=0.5, anchor='center')

        self.quadros = []
        for i in range(1, 11):
            linha = []
            for j in range(1, 11):
                label = tk.Label(quadro, width=9, height=2, bg='#121212', borderwidth=1, relief="solid")
                label.grid(row=i - 1, column=j - 1, padx=2, pady=2)
                linha.append(label)
            self.quadros.append(linha)

        botao_quadro = tk.Frame(self.root, bg='#282828')
        botao_quadro.pack(side='bottom', pady=20)
        self.criar_controles(botao_quadro)
        quadro_barra_progresso = tk.Frame(self.root, bg='#000000')
        quadro_barra_progresso.pack(side='top', fill='x', padx=10, pady=10)

        self.barra_progresso = ttk.Progressbar(quadro_barra_progresso, style="Horizontal.TProgressbar", length=300,
                                               mode='determinate', maximum=100)
        self.barra_progresso.pack(side='bottom')

        quadro_botoes = tk.Frame(self.root, bg='#282828')
        quadro_botoes.pack(side='top', padx=0, pady=0)

        self.label_contador = ttk.Label(quadro_barra_progresso, text="Espaço Restante: 100 blocos livres",
                                        style="TLabel")
        self.label_contador.pack(fill='y')

        estilo.configure("EstiloRotulo.TLabel", background='#000000', foreground='white', font=('Arial', 11))
        self.label_contador.config(style="EstiloRotulo.TLabel")

    def criar_controles(self, botao_quadro):
        estilo = ttk.Style()
        estilo.configure("TButton", padding=6, relief="flat", background="#ccc")
        estilo.configure("TEntry", padding=6, relief="flat")

        self.entry_nome = ttk.Entry(botao_quadro, width=10)
        self.entry_tamanho = ttk.Entry(botao_quadro, width=5)
        self.button_adicionar = ttk.Button(botao_quadro, text="Adicionar Processo", command=self.adicionar_processo)
        self.button_desalocar = ttk.Button(botao_quadro, text="Desalocar", command=self.desalocar_processo)
        self.button_realocar_processos = ttk.Button(botao_quadro, text='Realocar', command=self.realocar_processos)
        self.button_mostrar_ajuda = ttk.Button(botao_quadro, text='Ajuda', command=self.mostrar_ajuda)
        self.button_liberar_memoria = ttk.Button(botao_quadro, text='Liberar Memória', command=self.liberar_memoria)

        self.label_erro = tk.Label(botao_quadro, text="", fg="red", bg='#282828')

        self.entry_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_tamanho.grid(row=0, column=1, padx=5, pady=5)
        self.button_adicionar.grid(row=0, column=2, padx=5, pady=5)
        self.button_desalocar.grid(row=0, column=3, padx=5, pady=5)
        self.button_realocar_processos.grid(row=0, column=4, padx=5, pady=5)
        self.button_mostrar_ajuda.grid(row=0, column=5, padx=5, pady=5)
        self.button_liberar_memoria.grid(row=0, column=6, padx=5, pady=5)
        self.label_erro.grid(row=1, column=0, columnspan=4, pady=5)

    def adicionar_processo(self):
        nome = self.entry_nome.get()
        tamanho = int(self.entry_tamanho.get())

        if tamanho <= self.espaco_livre:
            processo = Processo(nome, tamanho)
            self.processos.append(processo)

            if not self.alocar_processo(processo):
                self.label_erro.config(text=f'Não foi possível alocar o Processo {processo.nome}')
        else:
            self.label_erro.config(text=f'Espaço insuficiente para alocar o Processo {nome}')

    def alocar_processo(self, processo):
        melhor_ajuste = None
        linha_inicial = -1

        espaco_disponivel = 0
        inicio_linha = -1
        for i in range(len(self.quadros)):

            for j in range(len(self.quadros[i])):
                if self.quadros[i][j].cget("text") == "":
                    if linha_inicial == -1: linha_inicial = i
                    if espaco_disponivel == 0:
                        inicio_linha = j
                    espaco_disponivel += 1

                    if espaco_disponivel >= processo.tamanho:
                        melhor_ajuste = (linha_inicial, inicio_linha, i)
                        break
                else:
                    espaco_disponivel = 0  # Reinicia ao encontrar um bloco ocupado
                    linha_inicial = -1

            if melhor_ajuste:
                break  # Interrompe o loop externo se encontrar um ajuste

        if melhor_ajuste:
            tamanho_alocado = processo.tamanho

            indice_linha_inicial = melhor_ajuste[1]
            for i in range(melhor_ajuste[0], melhor_ajuste[2] + 2):

                for j in range(indice_linha_inicial, 10):
                    if tamanho_alocado == 0: break
                    tamanho_alocado -= 1
                    quadro = self.quadros[i][j]
                    quadro.config(text=processo.nome, bg='white')
                indice_linha_inicial = 0

                if tamanho_alocado == 0: break

            self.atualizar_barra_progresso()
            return True

        return False

    def desalocar_processo(self):
        desalocar_nome = self.entry_nome.get()
        tamanho_processo = 0
        for i in range(len(self.quadros)):

            for j in range(len(self.quadros[i])):
                quadro = self.quadros[i][j]
                if quadro.cget('text') == desalocar_nome:
                    quadro.config(text="", bg='#121212')
                    tamanho_processo += 1

        if tamanho_processo > 0:
            self.label_erro.config(text=f'Processo {desalocar_nome} desalocado')
            self.espaco_livre += tamanho_processo  # Atualiza o espaço livre

        else:
            self.label_erro.config(text=f'O Processo {desalocar_nome} não está atualmente alocado.')

    def liberar_memoria(self):
        for i in range(len(self.quadros)):

            for j in range(len(self.quadros[i])):
                quadro = self.quadros[i][j]
                quadro.config(bg='#121212', text = '')
        self.atualizar_barra_progresso()

    def atualizar_barra_progresso(self):
        espaco_total = 100  # Total de espaços de memória
        espaco_ocupado = 0

        for i in range(len(self.quadros)):
            espaco_disponivel = 0
            for j in range(len(self.quadros[i])):
                if self.quadros[i][j].cget("text") != "":
                    espaco_disponivel += 1

            espaco_ocupado += espaco_disponivel

        self.espaco_livre = espaco_total - espaco_ocupado  # Atualiza a variável do espaço livre
        valor_progresso = (espaco_ocupado / espaco_total) * 100
        self.barra_progresso['value'] = valor_progresso
        # Atualize o texto do rótulo de contador
        self.label_contador.config(text=f'Espaço Restante: {self.espaco_livre} blocos livres')

    def realocar_processos(self):

        # 1 Passo: Criar uma lista de controle/copia
        lista_controle = []
        quantidade_letras = []
        # 2 Passo: Percorrer as linhas da lista de processos
        for i in range(len(self.quadros)):

            for j in range(len(self.quadros[i])):
                quadro = self.quadros[i][j]
                letra_atual = quadro.cget('text')
                # 3 Passo: Fazer leitura/contador de processos na lista
                if letra_atual != '': # 4 Passo: Verificar se o outro valor existente é diferente, se sim guardar o processo.
                    lista_controle.append(letra_atual)

        print(lista_controle)

        # 5 Passo: Separar a quantidade de cada processo
        letra_anterior = -1
        for letra in lista_controle:
            if letra_anterior == -1:
                letra_anterior = letra

            elif letra != letra_anterior:
                quantidade_letras.append(Processo(letra_anterior,lista_controle.count(letra_anterior)))
                letra_anterior = letra
        quantidade_letras.append(Processo(letra_anterior, lista_controle.count(letra_anterior)))

        print(quantidade_letras)

        self.liberar_memoria()
        # 6 Passo: Adicionar cada processo individualmente na lista principal.
        for processo in quantidade_letras:
            self.alocar_processo(processo)
        self.atualizar_barra_progresso()

    def mostrar_ajuda(self):
        mensagem_ajuda = (
            "Este é um projeto de exemplo que demonstra um alocador de memória Best Fit. "
            "Quando você inserir um processo, o algoritmo procurará o melhor espaço para ele.\n\n"
            "Instruções:\n"
            "1. Insira o nome e o tamanho do processo nos campos apropriados.\n"
            "2. Clique no botão 'Inserir' para alocar o processo.\n"
            "3. Clique no botão 'Desalocar' para liberar espaço ocupado por um processo, para isso basta fornecer "
            "apenas o nome do seu processo.\n"
            "4. Clique no botão 'Realocar' para desalocar e realocar um processo.\n"
            "5. A barra de progresso mostra o espaço ocupado na memória.\n"
            "6. O rótulo 'Espaço Restante' exibe a quantidade restante de espaço na memória.\n"
            "7. Use o botão de ajuda para obter mais informações sobre o projeto. \n"
            "8. Use o botão de Liberar memória caso queira começar novamente, assim ele liberara todo espaço "
            "novamente. \n"
            "\n"
            "Você terá um total de 100 espaços de memória, aproveite ;)"
        )
        messagebox.showinfo("Ajuda", mensagem_ajuda)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorMemoriaApp(root)
    root.mainloop()