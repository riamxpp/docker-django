import os
import sys
import django

# Configuração necessária para rodar o script fora do servidor web
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.db import connection
from core.models import Projeto, Alocacao, Empregado

def questao_3_sql_puro():
    print("\n--- Executando Questão 3 (SQL Puro) ---")
    with connection.cursor() as cursor:
        # 1. Inserir uma atividade (Alocação)
        cursor.execute('INSERT INTO core_alocacao (horas, matric_id, "codProj_id") VALUES (15.0, 9491, 2)')
        
        # 2. Atualizar líder
        cursor.execute('UPDATE core_projeto SET lider_id = 9495 WHERE id = 2')
        
        # 3. Listar
        cursor.execute('SELECT p.nome, a.horas FROM core_projeto p JOIN core_alocacao a ON p.id = a."codProj_id"')
        for row in cursor.fetchall():
            print(f"Projeto: {row[0]} | Horas: {row[1]}")

def questao_4_orm():
    print("\n--- Executando Questão 4 (ORM Django) ---")
    # 1. Inserir atividade
    Alocacao.objects.create(horas=20.0, matric_id=9492, codProj_id=1)
    
    # 2. Atualizar líder
    novo_lider = Empregado.objects.get(matricula=9493)
    Projeto.objects.filter(id=1).update(lider=novo_lider)
    
    # 3. Listar
    projetos = Projeto.objects.all()
    for p in projetos:
        atividades = Alocacao.objects.filter(codProj_id=p.id)
        print(f"Projeto: {p.nome}")
        for atv in atividades:
            print(f"  - Atividade (Horas): {atv.horas}")

if __name__ == "__main__":
    questao_3_sql_puro()
    questao_4_orm()
