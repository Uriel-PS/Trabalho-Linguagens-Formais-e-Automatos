
"""
Simulador de Máquina de Mealy que gera imagem PPM (P1).
Uso:
   >python3 mealy.py MM.txt w16.txt saida.ppm
"""

import sys

# Leitura de argumentos de linha de comando
mm_file, word_file, output_file = sys.argv[1:]

lines = []  # cria uma lista vazia para armazenar as linhas úteis
with open(mm_file, encoding="utf-8") as arquivo:
    for line in arquivo:
        # remove espaços e quebras de linha
        line = line.strip()
        
        # ignora linhas vazias
        if line == "":
            continue
        
        lines.append(line)


initial_state = lines[1]

# Dicionário de transições: (estado, símbolo) -> (próximo, saída)
transitions = {}

# Cada linha a partir da sexta contém uma transição
for line in lines[5:]:
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        continue  # ignora linhas incompletas
    state_from, symbol, state_to, output = parts

    if output.lower() in ['ε', 'eps', 'e']:
        output = ''

    output = output.replace('\\n', '\n')

    # Armazena a transição
    transitions[(state_from, symbol)] = (state_to, output)

# Remove quebras de linha (\n) e retornos de carro (\r)
word = open(word_file, encoding="utf-8").read().replace('\r', '').replace('\n', '')

# Simulação da máquina de Mealy
state = initial_state
output_text = ''

for c in word:
    key = (state, c)
    if key not in transitions:
        print(f"Sem transição definida para ({state}, '{c}') — parada.")
        break
    state, out = transitions[key]
    output_text += out


# Divide o texto de saída em várias linhas,
all_lines = output_text.split('\n')

# Cria uma nova lista contendo apenas as linhas não vazias
lines = []
for line in all_lines:
    if line != '':
        lines.append(line)


if len(lines) > 0:
    # A largura é o tamanho da linha mais comprida
    comprimentos = []
    for line in lines:
        comprimentos.append(len(line))
    width = max(comprimentos)

    # A altura é o número total de linhas
    height = len(lines)
else:
    width = 0
    height = 0


with open(output_file, 'w', encoding="utf-8") as f:
    f.write(f"P1\n{width} {height}\n")
    for line in lines:
        f.write(line.ljust(width, '0') + '\n')

print(f"PPM gerado com sucesso: {output_file} ({width}x{height})")
