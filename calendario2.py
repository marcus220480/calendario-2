import streamlit as st
import datetime
import calendar
import ephem

st.set_page_config(page_title="Calendário e Relógio com Fases da Lua")
st.title("Calendário e Relógio com Fases da Lua")

def get_moon_phase(date):
    moon = ephem.Moon(date)
    phase = moon.phase
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

def display_calendar(year):
    st.subheader(f"Calendário do Ano {year} com Fases da Lua")
    for i in range(1, 13, 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j <= 12:
                month = i + j
                month_name = calendar.month_name[month]
                with cols[j]:
                    st.write(f"### {month_name}")
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

year = st.number_input("Digite o ano:", min_value=1, max_value=9999, value=datetime.datetime.now().year, step=1)

if st.button("Atualizar Calendário"):
    display_calendar(int(year))

# Exibe o horário atual
st.subheader("Hora Atual")
clock_placeholder = st.empty()
current_time = datetime.datetime.now().strftime("%H:%M:%S")
clock_placeholder.write(current_time)
