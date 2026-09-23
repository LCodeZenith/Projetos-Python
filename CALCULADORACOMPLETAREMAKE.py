import tkinter as tk
from tkinter import messagebox

# Messagebox é uma função dentro da biblioteca Tkinter que serve justamente para mostrar mensagens em
# janelas, uma função muito front-end

while True:

    somarsomar = input("Você deseja somar? y/n:")

    if somarsomar == "y":
        def somar_numeros():
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            resultado = num1 + num2
            messagebox.showinfo("Resultado", f"A soma dos números é: {resultado}")

        # aqui é criada a função somar_numeros() que será utilizada repetidamente pelo programa
        # São criadas duas variáveis de dados float, onde há duas variáveis dentro delas chamadas de entry
        # essas entry.get()) são as variáveis de número que o usuário irá digitar.

        janela = tk.Tk()
        janela.title("Calculadora de Soma")

        label_num1 = tk.Label(janela, text="Número 1:")
        label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # tk.label cria textos onde você não pode mexer, mas que estão presentes na janela.

        entry_num1 = tk.Entry(janela)
        entry_num1.grid(row=0, column=1, padx=10, pady=5)

        # tk.entry cria uma interface gráfica de input, isso torna a variável entry_num1 lá de cima sendo
        # algo com valor definido para a função de somar números.

        label_num2 = tk.Label(janela, text="Número 2:")
        label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        # obs: Sempre que for colocar um texto na janela, é necessário digitar text="str"

        entry_num2 = tk.Entry(janela)
        entry_num2.grid(row=1, column=1, padx=10, pady=5)

        botao_somar = tk.Button(janela, text="Somar", command=somar_numeros)
        botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)

        # tk.button é usado para criar um botão clicável com uma função imbutida
        # para definir a função de um tk.button, é necessário criar o text que será o nome e então
        # escrver command=função_algumacoisa

        janela.mainloop()

    elif somarsomar == "n":

        subtrairdef = input("Você deseja subtrair? y/n:")

        if subtrairdef == "y":

            def subtrair_numeros():
                num1 = float(entry_num1.get())
                num2 = float(entry_num2.get())
                resultado = num1 - num2
                messagebox.showinfo("Resultado", f"A subtração dos números é: {resultado}")

            # janela.mainloop é utilizado para manter a janela rodando sem fechar sozinha.

            janela = tk.Tk()
            janela.title("Calculadora de Subtração")

            label_num1 = tk.Label(janela, text="Número 1:")
            label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

            # tk.label cria textos onde você não pode mexer, mas que estão presentes na janela.

            entry_num1 = tk.Entry(janela)
            entry_num1.grid(row=0, column=1, padx=10, pady=5)

            # tk.entry cria uma interface gráfica de input, isso torna a variável entry_num1 lá de cima sendo
            # algo com valor definido para a função de somar números.

            label_num2 = tk.Label(janela, text="Número 2:")
            label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

            # obs: Sempre que for colocar um texto na janela, é necessário digitar text="str"

            entry_num2 = tk.Entry(janela)
            entry_num2.grid(row=1, column=1, padx=10, pady=5)

            botao_subtrair = tk.Button(
                janela,
                text="Subtrair",
                command=subtrair_numeros
            )
            botao_subtrair.grid(row=2, columnspan=2, padx=10, pady=5)

            # tk.button é usado para criar um botão clicável com uma função imbutida
            # para definir a função de um tk.button, é necessário criar o text que será o nome e então
            # escrver command=função_algumacoisa

            janela.mainloop()

        elif subtrairdef == "n":

            multiplicar = input("Você deseja multiplicar? y/n:")

            if multiplicar == "y":

                def multiplicar_numeros():
                    num1 = float(entry_num1.get())
                    num2 = float(entry_num2.get())
                    resultado = num1 * num2
                    messagebox.showinfo("Resultado", f"A multiplicação dos números é: {resultado}")

                # janela.mainloop é utilizado para manter a janela rodando sem fechar sozinha.

                janela = tk.Tk()
                janela.title("Calculadora de Multiplicação")

                label_num1 = tk.Label(janela, text="Número 1:")
                label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

                # tk.label cria textos onde você não pode mexer, mas que estão presentes na janela.

                entry_num1 = tk.Entry(janela)
                entry_num1.grid(row=0, column=1, padx=10, pady=5)

                # tk.entry cria uma interface gráfica de input, isso torna a variável entry_num1 lá de cima sendo
                # algo com valor definido para a função de somar números.

                label_num2 = tk.Label(janela, text="Número 2:")
                label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

                # obs: Sempre que for colocar um texto na janela, é necessário digitar text="str"

                entry_num2 = tk.Entry(janela)
                entry_num2.grid(row=1, column=1, padx=10, pady=5)

                botao_multiplicar = tk.Button(
                    janela,
                    text="Multiplicar",
                    command=multiplicar_numeros
                )
                botao_multiplicar.grid(row=2, columnspan=2, padx=10, pady=5)

                # tk.button é usado para criar um botão clicável com uma função imbutida
                # para definir a função de um tk.button, é necessário criar o text que será o nome e então
                # escrver command=função_algumacoisa

                janela.mainloop()

            elif multiplicar == "n":

                dividir = input("Você deseja dividir? y/n: ")

                if dividir == "y":

                    def dividir_numeros():
                        num1 = float(entry_num1.get())
                        num2 = float(entry_num2.get())

                        if num2 == 0:
                            messagebox.showerror(
                                "Erro",
                                "Não é possível dividir por zero!"
                            )
                        else:
                            resultado = num1 / num2
                            messagebox.showinfo(
                                "Resultado",
                                f"A divisão dos números é: {resultado}"
                            )

                    janela = tk.Tk()
                    janela.title("Calculadora de Divisão")

                    label_num1 = tk.Label(janela, text="Número 1:")
                    label_num1.grid(
                        row=0,
                        column=0,
                        padx=10,
                        pady=5,
                        sticky="e"
                    )

                    entry_num1 = tk.Entry(janela)
                    entry_num1.grid(
                        row=0,
                        column=1,
                        padx=10,
                        pady=5
                    )

                    label_num2 = tk.Label(janela, text="Número 2:")
                    label_num2.grid(
                        row=1,
                        column=0,
                        padx=10,
                        pady=5,
                        sticky="e"
                    )

                    entry_num2 = tk.Entry(janela)
                    entry_num2.grid(
                        row=1,
                        column=1,
                        padx=10,
                        pady=5
                    )

                    botao_dividir = tk.Button(
                        janela,
                        text="Dividir",
                        command=dividir_numeros
                    )
                    botao_dividir.grid(
                        row=2,
                        columnspan=2,
                        padx=10,
                        pady=5
                    )

                    janela.mainloop()

                else:

                    fechar = input("você deseja fechar o programa? y/n: ")

                    if fechar == "y":
                        input("Acabaram nossas opções, obrigado por testar o programa!")
                        break
                    else:
                        continue