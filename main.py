import sqlite3

class Gestao:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY,
                produto TEXT,
                quantidade INTEGER
             )
        ''')
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?, ?)", (produto, quantidade))
        self.conn.commit()
    
    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
    def remove_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
                cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?",
                                (estoque_atual - quantidade, produto))
                self.conn.commit()
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def consutar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0
    
    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto FROM estoque")
        produtos = cursor.fetchall()
        return [produto[0] for produto in produtos]

sistema = Gestao("estoque.db")

sistema.adicionar_produto("Chopp", 10)
sistema.adicionar_produto("Cerveja", 50)
sistema.adicionar_produto("Espetos", 100)
sistema.adicionar_produto("Refrigerante", 50)

estoque_chopp = sistema.consutar_estoque("Chopp")
print(f"Quantidade de Chopp em estoque: {estoque_chopp}")

estoque_cerveja = sistema.consutar_estoque("Cerveja")
print(f"Quantidade de Cerveja em estoque: {estoque_cerveja}")

estoque_espetos = sistema.consutar_estoque("Espetos")
print(f"Quantidade de Espetos em estoque: {estoque_espetos}")

estoque_refrigerante = sistema.consutar_estoque("Refrigerante")
print(f"Quantidade de Refrigerante em estoque: {estoque_refrigerante}")

sistema.remover_produto("Chopp", [0])
sistema.remover_produto("Cerveja", [0])
sistema.remover_produto("Espeto", [0])
sistema.remover_produto("Refrigerante", [0])

produtos_em_estoque = sistema.listar_produtos()
print(f"Produtos em estoque: {produtos_em_estoque}")