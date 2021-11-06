import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import AutoModelWithLMHead, AutoTokenizer

# zaczynamy od zaimportowania bibliotek

st.success('Witam w mojej aplikacji. Nazywam się Michał Melaniuk a to jest moje ćwiczenie z biblioteki Streamlit')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Zajęcia 1. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji
st.header("Moja aplikacja oferuje dwie możliwości.")
# st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader ("1. Emocjonalny wydzwięk tekstu 'ENG' ")
st.subheader ("2. Translator z ENG na GER")
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit


# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('1) Dzięki opcji pierwszej sprawdzisz jaki wydzięk emocjonalny ma twój tekst w języku angielskim')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.write('2) Dzięki opcji drugiej dokonasz tłumaczenia tekstu z języka angielskiego na język niemiecki')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

df = pd.read_csv("cwiczenie_1.csv", sep = ';')
st.dataframe(df)
# musimy tylko pamiętaćo właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Translator z języka angielskiego na niemiecki')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "1. Wydźwięk emocjonalny tekstu (eng)",
        
        "2. Translator z ENG na GER"
    ],
)

if option == "1. Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst po angielsku")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
        st.success('I jak? Zadowolony z wyniku?)')
        
if option == "2. Translator z ENG na GER":
    text = st.text_area(label="Wpisz tekst po angielsku")
    if text:
        translator = pipeline ("translation_en_to_de")
        ans = translator(text)
        st.write(ans)
        st.success('Udało się przetłumaczyć. Gratulacje! :)')  
       
st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')


st.success('Michał Melaniuk - S19713')