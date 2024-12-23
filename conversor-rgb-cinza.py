import cv2
import os

# Caminho para a imagem
image_path = 'assets/spacemarine2-2.webp'

# Verifica se a imagem existe
if not os.path.exists(image_path):
    print(f"Erro: A imagem não foi encontrada no caminho especificado: {image_path}")
else:
   # Carrega a imagem
   img = cv2.imread(image_path)

   # Verifica se a imagem foi carregada corretamente
   if img is None:
       print(f"Erro: Não foi possível carregar a imagem em: {image_path}")
   else:

       # Imprime a resolução original
       print(f"Resolução original: {img.shape}")

       # Converte a imagem para tons de cinza
       gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       # Imprime a resolução da imagem em tons de cinza
       print(f"Resolução após conversão: {gray_img.shape}")

       # Exibe a imagem (opcional)
       cv2.imshow("Imagem em tons de cinza", gray_img)
       cv2.waitKey(0)
       cv2.destroyAllWindows()