import streamlit as st
import pandas as pd
import altair as alt
import altair_viewer
import plotly_express as px
import codecs

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def sales():
    st.write('### Отчет по продажам')
    style_h1_sales = codecs.open('/app/danzak.github.io/css/style_h1_sales.css').read()
    st.markdown(f'<style>{style_h1_sales}</style>', unsafe_allow_html=True)

    dataset = pd.DataFrame(pd.read_excel('Датасет.xlsx', sheet_name=0))
    # Добавил столбец, месяц + год
    # dataset['Месяц_год'] = dataset['День'].dt.strftime('%Y, %B')
    dataset['Месяц_год'] = dataset["День"].dt.to_period("M")

    years_filter = st.sidebar.multiselect(
        'ГОД',
        dataset['Год'].unique(),
        dataset['Год'].unique())
    manager_filter = st.sidebar.multiselect(
        'МЕНЕДЖЕР',
        dataset['Менеджер'].unique(),
        dataset['Менеджер'].unique())
    customer_filter = st.sidebar.multiselect(
        'ЗАКАЗЧИК',
        dataset['Заказчик'].unique(),
        dataset['Заказчик'].unique())
    vegetables_filter = st.sidebar.multiselect(
        'НАИМЕНОВАНИЕ',
        dataset['Наименование'].unique(),
        dataset['Наименование'].unique())
    # print(data.head().to_markdown())

    # with st.sidebar:
    #     st.button('EXIT')

    # ЭТО СВЯЗКА ФИЛЬТРОВ и ТАБЛИЦЫ (ДАТАФРЕЙИМА)
    data_selection = dataset.query(
        'Год == @years_filter and Менеджер == @manager_filter and Заказчик == @customer_filter and Наименование == '
        '@vegetables_filter'
    )
    # st.dataframe(data_selection)
    st.markdown('---')

    # ------Общие показатели--------
    col1, col2, col3 = st.columns(3)
    with col1:
        sale_sum = int(data_selection['Продажи(тыс.руб)'].sum() / 1000)
        st.metric(label="Продажи, млн руб.", value=sale_sum)
    with col2:
        mean_check = int(round(data_selection['Продажи(тыс.руб)'].mean(), 1))
        st.metric(label="Средний чек, руб.", value=mean_check)
    with col3:
        count_sales = int(len(data_selection['Продажи(тыс.руб)']))
        st.metric(label="Количество продаж", value=count_sales)
    st.markdown('---')

    # -----График:Динамика продаж, млн руб.----#
    ss3 = (data_selection.groupby([data_selection["День"].dt.to_period("M")]).sum()[['Продажи(тыс.руб)']] / 1000).round(
        1)
    fig_prod_sales_grafik = px.line(
        ss3,
        y='Продажи(тыс.руб)',
        x=ss3.index.to_timestamp(),
        text='Продажи(тыс.руб)',
        labels={'Продажи(тыс.руб)': 'Продажи (млн.руб)'},
        title='Динамика продаж, млн руб.'
    )

    fig_prod_sales_grafik.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        # title_font_family='Source Sans Pro',
        title_font_size=20,
        height=300
    )
    st.plotly_chart(fig_prod_sales_grafik, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        # ------Горизонтальная(линейчатая) гистограмма: Продажи по товарам, млн руб.------#
        sss = (data_selection.groupby("Наименование")[["Продажи(тыс.руб)"]].sum() / 1000).round(1).sort_values(
            'Продажи(тыс.руб)')
        fig_prod_sales = px.bar(
            sss,
            x='Продажи(тыс.руб)',
            y=sss.index,
            orientation='h',
            template='plotly_dark',
            text_auto=True,
            title='Продажи по товарам, млн.руб',
            # height=700,
            color='Продажи(тыс.руб)',
            labels={'Продажи(тыс.руб)': 'Продажи (млн.руб)'}
        )

        fig_prod_sales.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            # title_font_family='Source Sans Pro',
            title_font_size=20
        )
        st.plotly_chart(fig_prod_sales, use_container_width=True)

    with col2:
        # ------Кольцевая диаграмма: Продажи по городам------#
        sdsd = data_selection.groupby(["Склад"]).sum()[['Продажи(тыс.руб)']] / 1000
        fig_prod_sales_okr = px.pie(
            sdsd,
            values='Продажи(тыс.руб)',
            names=sdsd.index,
            title='Продажи по городам',
            opacity=0.9,
            hole=0.5,
            labels={'Продажи(тыс.руб)': 'Продажи (млн.руб)'}
        )

        fig_prod_sales_okr.update_layout(
            title_font_size=20
        )
        st.plotly_chart(fig_prod_sales_okr)


if __name__ == '__main__':
    st.set_page_config(
        page_title="SALES",
        page_icon="🥰",
        layout="wide",
        initial_sidebar_state="auto"
    )

    hide_menu_style = """
            <style>
            .css-wjbhl0 li:nth-child(2) {display: none;}
            .css-wjbhl0 li:nth-child(3) {display: none;}
            .css-wjbhl0 li:nth-child(4) {display: none;}
            .css-wjbhl0 li:nth-child(1) svg {display: none;}
            
            .css-1ck8f3p {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    sales()

    # hide_menu_style = """
    #         <style>
    #         .css-79elbk  {display: none;}
    #         .css-1ck8f3p {visibility: hidden;}
    #         </style>
    #         """
    # st.markdown(hide_menu_style, unsafe_allow_html=True)

    ### sss2 = (data_selection.groupby(["Наименование", 'Склад'])[["Продажи(тыс.руб)"]].sum() / 1000).round(1)

    # ------Горизонтальная гистограмма: Продажи по товарам, млн руб.------ALTAIR
    # sss4 = (data_selection.groupby("Наименование")[["Продажи(тыс.руб)"]].sum() / 1000).round(1).reset_index()
    # s = alt.Chart(sss4).mark_bar().encode(
    #     x=alt.X('Продажи(тыс\\.руб):Q', title='Продажи (млн.руб)', sort='ascending'),
    #     y=alt.Y('Наименование:N'),
    #     color=alt.Color('Продажи(тыс\\.руб):Q', sort='ascending', title='Продажи (млн.руб)')
    # )
    # s_text = s.mark_text(
    #     align='left',
    #     baseline='middle',
    #     dx=3
    # ).encode(text=alt.Text('Продажи(тыс\\.руб):Q'))
    # st.altair_chart(s + s_text.interactive(), use_container_width=True)
