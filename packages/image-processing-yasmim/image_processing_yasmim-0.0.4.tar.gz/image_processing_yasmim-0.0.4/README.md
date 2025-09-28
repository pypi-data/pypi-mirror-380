# 📷 image-processing

![PyPI Version](https://img.shields.io/pypi/v/image-processing-yasmim?style=flat-square)  
![Downloads](https://img.shields.io/pypi/dm/image-processing-yasmim?style=flat-square)  
![License](https://img.shields.io/pypi/l/image-processing-yasmim?style=flat-square)  

📌 Descrição
O pacote image-processing fornece ferramentas para processamento e análise de imagens, incluindo técnicas avançadas como histogram matching e comparação de similaridade estrutural, além de utilitários úteis para manipulação e visualização de imagens.

### Funcionalidades principais:

* **Histogram Matching** — iguala o histograma de uma imagem a outro para uniformizar aparência e iluminação.
* **Structural Similarity (SSIM)** — compara a similaridade estrutural entre duas imagens.
* **Redimensionamento de imagens** — ajusta o tamanho de imagens mantendo qualidade.

### Utilitários adicionais:

* **Leitura de imagens.**
* **Salvamento de imagens.**
* **Exibição de imagens.**
* **Plotagem de resultados.**
* **Plotagem de histogramas.**

---

### 💿 Instalação

Você pode instalar diretamente pelo PyPI usando o pip:

```bash
pip install image-processing-yasmim

---

### 🚀 Exemplo de Uso

# Importa a classe principal do seu pacote
from image_processing import ImageProcessor

# Inicializa o processador de imagens
processor = ImageProcessor()

# Ler a imagem de um arquivo
imagem = processor.read_image("exemplo.jpg")

# Redimensionar a imagem para um tamanho específico
imagem_redimensionada = processor.resize_image(imagem, width=500, height=500)

# Salvar a imagem processada em um arquivo
processor.save_image(imagem_redimensionada, "saida.jpg")

# Exibir a imagem na tela
processor.plot_image(imagem_redimensionada)

---

### 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do projeto.

### 👤 Autora

Yasmim Freitas


