def calcular_acuracia(tp, fp, fn, tn):
    """Calcula a acurácia a partir dos componentes da matriz de confusão"""
    return (tp + tn) / (tp + fp + fn + tn)

def main():
    # Lê o número de matrizes
    n = int(input().strip())
    
    melhor_acuracia = -1
    melhor_indice = 0
    acuracias = []
    
    # Processa cada matriz
    for i in range(n):
        # Lê os quatro valores da matriz de confusão
        dados = input().split()
        if len(dados) < 4:
            continue
            
        tp = int(dados[0])
        fp = int(dados[1])
        fn = int(dados[2])
        tn = int(dados[3])
        
        # Calcula a acurácia
        acc = calcular_acuracia(tp, fp, fn, tn)
        acuracias.append(acc)
        
        # Atualiza a melhor acurácia
        if acc > melhor_acuracia:
            melhor_acuracia = acc
            melhor_indice = i
    
    # Formata a saída conforme especificado
    print(f"Index: {melhor_indice}")
    print(f"Accuracy: {melhor_acuracia:.2f}".rstrip('0').rstrip('.') if melhor_acuracia % 1 else f"Accuracy: {int(melhor_acuracia)}")

if __name__ == "__main__":
    main()
    