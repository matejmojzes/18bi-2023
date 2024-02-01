import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def intro():
    st.title("Analýza léků z prodeje z lékárny/FN")
    st.write("Tato aplikace dává vhled k analýze dat týkající se používání léků, jak volně prodejných tak na předpis. ")
    st.write("Pro jednotlivé rozebírané kategorie prosím volte z menu vlevo. V každé naleznete rychlou analýzu dat z databáze, jejíž struktura je taktéž k nahlédnutí.")

    st.subheader("Databaze léků")
    medication_data = pd.read_csv('./sukl_meds_all.csv', sep=';', dtype={'your_column_name': str})

    st.dataframe(medication_data)


def medicaments():
    st.title("Volně prodejné léky")
    st.write("V této sekci se věnujeme analýze prodeje volně dostupných léků.")
    df2 = pd.read_csv('./medication_usage_summary.csv', sep=';')
    bins = [0, 5, 10, 15, 20, float('inf')]
    labels = ['1-5', '6-10', '11-15', '16-20', '20+']
    df2['category'] = pd.cut(df2['No. users taking'], bins=bins, labels=labels, right=False)

    category_counts = df2.groupby('category', observed=True)['Medication Name'].count()

    fig, ax = plt.subplots(figsize=(10, 6))
    category_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Number of Users')
    ax.set_ylabel('Number of Medication Names')
    ax.set_title('Number of Medication Names by User Count Categories')

    # plt.show()
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    st.pyplot(fig)
    st.write("""
        Tento graf znázorňuje, že pouhé jedno procento léků je běžně používáno velkou skupinou lidí 
        """)

def prescriptions():
    st.title("Léky na předpis a jednotliví doktoři")
    st.write("V této kapitole je rozebráno jaké léky se předepisují nejčastěji. Taktéž je zde pracovní analýza jednotlivých doktorů.")

    st.write("Seznam doktorů a počty předepsaných léků")
    df = pd.read_csv('./doctor_prescription_counts.csv', sep=';')
    st.write(df)

    # jsi lína píča, pracuj!!!
    st.write("""
            Druhý koláčový graf říká, že 98% procent lidí má doma v průměru 20-25 léků, pouhá dvě procenta mají doma léků výrazně méně.
            """)
    df3 = pd.read_csv('./medicament_count_graph.csv', sep=';')
    df3 = df3[df3['count'] > 0]
    category_counts3 = df3.set_index('category')['count']
    fig3, ax3 = plt.subplots()
    ax3.pie(category_counts3, labels=category_counts3.index, autopct='%1.1f%%', startangle=0)
    ax3.axis('equal')
    st.pyplot(fig3)

    # mrdko

def database_overview():
    st.write("Zde můžete vidět veškeré věci co se týkají databáze")
    if os.path.isfile('./IMG_2488.png'):
        st.image('./IMG_2488.png', caption='Schéma databáze')
    else:
        st.write(f"Error: file path  {'./IMG_2488.png'} neexistuje")




st.sidebar.title("Menu")
page = st.sidebar.radio("Zvolne stránku:", ('Úvod', 'Volně prodejné léky', 'Léky na předpis', 'Databáze'))

if page == 'Úvod':
    intro()
elif page == 'Volně prodejné léky':
    medicaments()
elif page == 'Léky na předpis':
    prescriptions()
elif page == 'Databáze':
    database_overview()




