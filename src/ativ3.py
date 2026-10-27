
import numpy as np
import streamlit as st


def tom_pixel(x, y, k):
    return (x * y + k * (x + y)) % 256


def gerar_imagem(k):
    imagem = np.zeros((64, 64), dtype=np.uint8)

    for y in range(64):
        for x in range(64):
            imagem[y, x] = tom_pixel(x, y, k)

    return imagem


st.title("Atividade 3 - Imagem como matriz")

k = st.slider(
    "Controle k",
    min_value=0,
    max_value=255,
    value=10
)

imagem = gerar_imagem(k)

st.image(imagem, clamp=True, width=512)
