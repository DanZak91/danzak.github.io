import streamlit as st
import streamlit.components.v1 as components
import codecs


def start_main():
    html_form = codecs.open('html_raz.html', encoding='UTF-8').read()
    st.markdown(html_form, unsafe_allow_html=True)
    styles_css = codecs.open('/app/danzak.github.io/css/style.css').read()
    st.markdown(f'<style>{styles_css}</style>', unsafe_allow_html=True)

    #часы
    styles_css_clock = codecs.open('/app/danzak.github.io/css/style_clock.css', encoding='UTF-8').read()
    js_clock = codecs.open('/app/danzak.github.io/js/js_clock.js', encoding='UTF-8').read()

    components.html(
        f"""<!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0" >
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
      <link rel="stylesheet" type="text/css" href="/app/danzak.github.io/css/style_clock.css">
      <style type="text/css">{styles_css_clock}</style>
      <title>Document</title>
    </head>
    <body>
    <div class="clock">
        <div id="Date"></div>
        <ul>
            <li id="hours"></li>
            <li id="point">:</li>
            <li id="min"></li>
            <li id="point">:</li>
            <li id="sec"></li>
        </ul>
    </div>
    <script type="text/javascript">{js_clock}</script>
    </body>
    </html>
    
            """
    )

    ##Гифка на прямую в stremlit
    # con = st.container()
    # lott = requests.get('https://assets10.lottiefiles.com/packages/lf20_dews3j6m.json').json()
    # con(st_lottie(lott, height=300))


if __name__ == '__main__':
    st.set_page_config(
        page_title="DASHBOARDS",
        page_icon="🥰",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    hide_menu_style = """
            <style>
            .css-79elbk  {display: none;}
            .css-1ck8f3p {visibility: hidden;}
            .css-hzzzp9  {display: none;}
            .css-1tipzh0  {display: none;}
            .css-1av10r7 {display: none;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    start_main()
