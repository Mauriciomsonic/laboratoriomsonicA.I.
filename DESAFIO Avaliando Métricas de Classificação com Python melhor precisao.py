import sys

def main():
    try:
        # Lê a quantidade de matrizes da entrada padrão
        n = int(sys.stdin.readline().strip())
    except:
        # Se falhar, tenta ler do input normal (para teste local)
        n = int(input().strip())
    
    best_precision = -1.0  # Inicializa com valor baixo
    best_index = -1
    
    # Percorre cada matriz
    for idx in range(n):
        try:
            # Tenta ler da entrada padrão
            data = sys.stdin.readline().strip().split(',')
        except:
            # Se falhar, tenta ler do input normal
            data = input().strip().split(',')
        
        tp = int(data[0])
        fp = int(data[1])
        fn = int(data[2])
        tn = int(data[3])
        
        # Calcula a precisão
        # precision = TP / (TP + FP)
        denominator = tp + fp
        if denominator > 0:
            precision = tp / denominator
        else:
            precision = 0.0  # Evita divisão por zero
        
        # Atualiza a maior precisão, se necessário
        if precision > best_precision:
            best_precision = precision
            best_index = idx
    
    # Formata a precisão para duas casas decimais e remove zeros finais
    precision_str = f"{best_precision:.2f}"
    precision_str = precision_str.rstrip('0').rstrip('.') if '.' in precision_str else precision_str
    
    # Imprime o resultado
    print(f"Index: {best_index}")
    print(f"Precision: {precision_str}")

if __name__ == '__main__':
    main()
    