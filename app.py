import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Meu Executor de Algoritmos", page_icon="🖥️", layout="centered")

# Título do Aplicativo
st.title("🖥️ Aplicativo Multiferramentas de Algoritmos")
st.write("Selecione um algoritmo na barra lateral para interagir com a interface visível.")

# Menu de seleção na barra lateral
opcao = st.sidebar.selectbox(
    "Escolha o Algoritmo:",
    [
        "Selecionar...",
        "1. Celsius para Kelvin",
        "2. Polegadas para Milímetros",
        "3. Cálculo de Potência Mecânica",
        "4. Área de um Trapézio"
    ]
)

# -------------------------------------------------------------------------
# ALGORITMO 1: Celsius para Kelvin
# -------------------------------------------------------------------------
if opcao == "1. Celsius para Kelvin":
    st.header("🌡️ Conversor de Celsius para Kelvin")
    st.write("Este algoritmo converte uma temperatura de graus Celsius para Kelvin.")
    
    # Campo visual para entrada de dados (Substitui o input())
    celsius = st.number_input("Digite a temperatura em graus Celsius (°C):", value=0.0, step=0.1)
    
    # Processamento interno (Escondido do usuário)
    kelvin = celsius + 273
    
    # Botão para calcular
    if st.button("Calcular Temperatura"):
        st.success(f"**Resultado:** {celsius}°C equivale a **{kelvin:.2f} K**.")

# -------------------------------------------------------------------------
# ALGORITMO 2: Polegadas para Milímetros
# -------------------------------------------------------------------------
elif opcao == "2. Polegadas para Milímetros":
    st.header("📏 Conversor de Polegadas para Milímetros")
    st.write("Este algoritmo converte um comprimento de polegadas para milímetros.")
    
    # Campo visual para entrada de dados
    polegadas = st.number_input("Digite o comprimento em polegadas (\"): ", value=0.0, step=0.1)
    
    # Processamento interno
    milimetros = polegadas * 25.4
    
    if st.button("Calcular Medida"):
        st.info(f"**Resultado:** {polegadas}\" equivalem a **{milimetros:.2f} mm**.")

# -------------------------------------------------------------------------
# ALGORITMO 3: Cálculo de Potência Mecânica
# -------------------------------------------------------------------------
elif opcao == "3. Cálculo de Potência Mecânica":
    st.header("⚡ Cálculo de Potência Mecânica")
    st.write("Este algoritmo calcula a potência a partir da força e da velocidade.")
    
    # Campos de entrada
    forca = st.number_input("Digite a força F aplicada (em Newtons):", value=0.0, step=1.0)
    velocidade = st.number_input("Digite a velocidade V do corpo (em m/s):", value=0.0, step=0.1)
    
    # Processamento
    potencia = forca * velocidade
    
    if st.button("Calcular Potência"):
        st.warning(f"**Resultado:** A potência calculada é de **{potencia:.2f} W**.")

# -------------------------------------------------------------------------
# ALGORITMO 4: Área de um Trapézio
# -------------------------------------------------------------------------
elif opcao == "4. Área de um Trapézio":
    st.header("📐 Área de um Trapézio")
    st.write("Este algoritmo calcula a área de um trapézio usando as suas dimensões.")
    
    # Campos de entrada
    base_maior = st.number_input("Digite o valor da Base Maior (B):", value=0.0, step=0.1)
    base_menor = st.number_input("Digite o valor da Base Menor (b):", value=0.0, step=0.1)
    altura = st.number_input("Digite o valor da Altura (h):", value=0.0, step=0.1)
    
    # Processamento com proteção para evitar divisões incorretas
    area = ((base_maior + base_menor) * altura) / 2
    
    if st.button("Calcular Área"):
        st.success(f"**Resultado:** A área total do trapézio é de **{area:.2f} unidades de área**.")

else:
    st.info("👈 Escolha uma das opções no menu ao lado para começar a usar o sistema.")
