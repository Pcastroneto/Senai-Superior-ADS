'''
SQLAlchemy é o kit de ferramentas Python SQL e Object Relational Mapper que oferece o poder e flexibilidade do SQL.
Prefiro não procurar um banco de dados como exemplo então esse é meio que uma 'base':


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando uma conexão com o banco de dados
engine = create_engine('sqlite:///exemplo.db')

# Criando uma classe base para as tabelas
base = declarative_base()

# Definindo uma classe para uma tabela
class Pessoa(base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo dados na tabela
pessoa1 = Pessoa(nome='João', idade=30)
pessoa2 = Pessoa(nome='Maria', idade=25)
session.add_all([pessoa1, pessoa2])
session.commit()

# Fazendo uma consulta na tabela
pessoas = session.query(Pessoa).all()
print(pessoas)

# Atualizando um registro na tabela
pessoa1.idade = 31
session.commit()

# Removendo um registro da tabela
session.delete(pessoa2)
session.commit()

# Encerrando a sessão
session.close()


"Nesse exemplo, estamos criando uma tabela Pessoa com as colunas id, nome e idade. 
Depois, inserimos duas pessoas na tabela, fazemos uma consulta para recuperar todas as pessoas, atualizamos a idade de uma delas e removemos a outra. 
Por fim, encerramos a sessão."
'''