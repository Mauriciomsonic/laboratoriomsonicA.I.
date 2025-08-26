import cv2
import numpy as np
import sys

# Verificar se o OpenCV está instalado
try:
    # Carregar a imagem colorida
    img = cv2.imread('lena.jpg')
    
    # Verificar se a imagem foi carregada corretamente
    if img is None:
        raise FileNotFoundError("Erro: Imagem 'lena.jpg' não encontrada. Verifique o caminho.")
    
    # Converter para níveis de cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Binarizar a imagem (threshold = 160)
    _, img_bin = cv2.threshold(img_cinza, 160, 255, cv2.THRESH_BINARY)
    
    # Exibir resultados
    cv2.imshow('Imagem Original', img)
    cv2.imshow('Imagem em Escala de Cinza', img_cinza)
    cv2.imshow('Imagem Binaria (Preto e Branco)', img_bin)
    
    # Salvar resultados (opcional)
    cv2.imwrite('lena_cinza.jpg', img_cinza)
    cv2.imwrite('lena_binaria.jpg', img_bin)
    
    print("Processamento concluído! Pressione qualquer tecla para fechar as janelas.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    sys.exit(1)

    