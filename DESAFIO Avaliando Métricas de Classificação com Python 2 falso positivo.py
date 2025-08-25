import sys

def main():
    try:
        # Lê a quantidade de matrizes da entrada padrão
        n = int(sys.stdin.readline().strip())
    except:
        # Se falhar, tenta ler do input normal (para teste local)
        n = int(input().strip())
    
    best_fpr = float('inf')  # Inicializa com um valor infinito
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
        
        # Calcula a Taxa de Falsos Positivos (FPR)
        # FPR = FP / (FP + TN)
        if (fp + tn) > 0:
            fpr = fp / (fp + tn)
        else:
            fpr = 0.0  # Evita divisão por zero
        
        # Atualiza a menor FPR, se necessário
        if fpr < best_fpr:
            best_fpr = fpr
            best_index = idx
    
    # Formata a FPR para duas casas decimais e remove zeros finais
    fpr_str = f"{best_fpr:.2f}"
    fpr_str = fpr_str.rstrip('0').rstrip('.') if '.' in fpr_str else fpr_str
    
    # Imprime o resultado
    print(f"Index: {best_index}")
    print(f"FPR: {fpr_str}")

if __name__ == '__main__':
    main()