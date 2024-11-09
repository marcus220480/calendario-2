import streamlit as st
import datetime
import calendar
import ephem  # Biblioteca para cálculos astronômicos
import time

# Configurações da página
st.set_page_config(page_title="Calendário e Relógio com Fases da Lua")
st.title("Calendário e Relógio com Fases da Lua")

# Função para obter a fase da lua para uma data específica
def get_moon_phase(date):
    moon = ephem.Moon(date)
    phase = moon.phase  # Fase da lua (0 a 100)
    if phase < 1.5:
        return "🌑 Nova"
    elif 1.5 <= phase < 25:
        return "🌒 Crescente"
    elif 25 <= phase < 50:
        return "🌓 Quarto Crescente"
    elif 50 <= phase < 75:
        return "🌔 Gibosa Crescente"
    elif 75 <= phase < 99.9:
        return "🌕 Cheia"
    elif 99.9 <= phase < 100:
        return "🌖 Gibosa Minguante"
    elif 50 < phase <= 75:
        return "🌗 Quarto Minguante"
    else:
        return "🌘 Minguante"

# Função para mostrar o relógio em tempo real
def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state['time'] = current_time

# Função para mostrar o calendário do ano com fases da lua
def display_calendar(year):
    st.subheader(f"Calendário do Ano {year} com Fases da Lua")
    
    # Loop pelos meses em grupos de 3
    for i in range(1, 13, 3):
        cols = st.columns(3)  # Cria 3 colunas para cada linha
        
        # Mostra o calendário de 3 meses lado a lado
        for j in range(3):
            if i + j <= 12:  # Para evitar indexação além de dezembro
                month = i + j
                month_name = calendar.month_name[month]
                
                # Exibe o nome e o calendário do mês com as fases da lua
                with cols[j]:
                    st.write(f"### {month_name}")
                    
                    # Exibe cada dia com sua fase da lua
                    month_days = calendar.monthcalendar(year, month)
                    month_text = ""
                    for week in month_days:
                        week_text = ""
                        for day in week:
                            if day == 0:
                                week_text += "   "
                            else:
                                date = datetime.date(year, month, day)
                                moon_phase = get_moon_phase(date)
                                week_text += f"{day:2} {moon_phase}  "
                        month_text += week_text + "\n"
                    st.text(month_text)

# Entrada do usuário para escolher o ano
year = st.number_input("Digite o ano:", min_value=1, max_value=9999, value=datetime.datetime.now().year, step=1)

# Atualiza o calendário quando o botão é pressionado
if st.button("Atualizar Calendário"):
    display_calendar(int(year))

# Exibe o relógio em tempo real
if 'time' not in st.session_state:
    st.session_state['time'] = datetime.datetime.now().strftime("%H:%M:%S")

st.subheader("Hora Atual")
clock_placeholder = st.empty()

# Loop para atualizar o relógio
while True:
    update_clock()
    clock_placeholder.write(st.session_state['time'])
    time.sleep(1)
