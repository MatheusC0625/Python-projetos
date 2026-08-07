alunos = {
    "João": {"Média": "10", "Ano Escolar": "1EM"},
    "Maria": {"Média": "8.75", "Ano Escolar": "1EM"},
    "Elizabeth Alexandra Mary Windsor": {"Média": "10", "Ano Escolar": "3EM"}
}

for aluno in alunos: #a cada aluno daquela lista de cima ele vai dar print neles
    print(aluno) #Os alunos já estão definidos como "aluno" por conta do for in
    print(alunos[aluno]["Média"])
    print(alunos[aluno]["Ano Escolar"])