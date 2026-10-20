
import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Imagem como matriz")



bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

bandeira[:] = (0, 156, 59)

bandeira[0:1, 8:10] = (255, 223, 0)
bandeira[1:2, 6:12] = (255, 223, 0)
bandeira[2:3, 4:14] = (255, 223, 0)
bandeira[3:4, 3:15] = (255, 223, 0)
bandeira[4:8, 2:16] = (255, 223, 0)
bandeira[8:9, 3:15] = (255, 223, 0)
bandeira[9:10, 4:14] = (255, 223, 0)
bandeira[10:11, 6:12] = (255, 223, 0)
bandeira[11:12, 8:10] = (255, 223, 0)

bandeira[4:8, 6:12] = (0, 39, 118)
bandeira[5:6, 6:12] = (255, 255, 255)

st.image(ampliar(bandeira))

