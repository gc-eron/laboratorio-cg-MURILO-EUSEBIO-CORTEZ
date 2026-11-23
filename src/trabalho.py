
import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title("Trabalho Final")

img = np.array(Image.open("imagens/foto.jpg").convert("RGB"))

tema = st.selectbox("Tema", ["Negativo", "Espelhamento", "Granulado", "Pixel Seal", "Pixel Art"])

resultado = img.copy()

if tema == "Negativo":
    resultado = 255 - img

elif tema == "Espelhamento":
    lado = st.selectbox("Espelhamento", ["Horizontal", "Vertical"])
    resultado = cv2.flip(img, 1 if lado == "Horizontal" else 0)

elif tema == "Granulado":
    intensidade = st.slider("Granulado", 0, 100, 30)
    ruido = np.random.randint(-intensidade, intensidade + 1, img.shape)
    resultado = np.clip(img.astype(int) + ruido, 0, 255).astype(np.uint8)

elif tema == "Pixel Seal":
    selo = np.array([
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 0],
        [1, 1, 2, 2, 2, 1, 1],
        [1, 2, 2, 3, 2, 2, 1],
        [1, 1, 2, 2, 2, 1, 1],
        [0, 1, 1, 2, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0]
    ])

    cores = np.array([
        [0, 0, 0],
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255]
    ], dtype=np.uint8)

    tamanho = st.slider("Tamanho do selo", 5, 30, 15)
    h, l = img.shape[:2]
    tamanho = min(tamanho, h // 7, l // 7)
    tamanho = max(1, tamanho)

    selo = cv2.resize(selo, (7 * tamanho, 7 * tamanho), interpolation=cv2.INTER_NEAREST)
    mask = selo > 0
    selo_rgb = cores[selo]

    x = st.slider("Posição X", 0, l - selo.shape[1], 0)
    y = st.slider("Posição Y", 0, h - selo.shape[0], 0)

    regiao = resultado[y:y + selo.shape[0], x:x + selo.shape[1]]
    regiao[mask] = selo_rgb[mask]

elif tema == "Pixel Art":
    tamanho = st.slider("Tamanho dos pixels", 2, 50, 10)
    cores = st.slider("Quantidade de cores", 2, 16, 6)
    h, l = img.shape[:2]
    pequena = cv2.resize(img, (l // tamanho, h // tamanho))
    resultado = cv2.resize(pequena, (l, h), interpolation=cv2.INTER_NEAREST)
    passo = 255 // (cores - 1)
    resultado = (resultado // passo) * passo

st.image(img, caption="Original")
st.image(resultado, caption="Resultado")
