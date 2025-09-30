import streamlit as st

from crud import criar_aluno,listar_aluno, atualizar_alunos, deletar_aluno

st.set_page_config(page_title='gerenciamento de alunos', page_icon='😎')

st.title('sistema de alunos com postgreSQL')

menu = st.sidebar.radio("menu", ['criar', 'listar', 'atualizar', 'deletar'])

if menu == 'criar': 
    st.subheader('👀 criar aluno') 
    nome = st.text_input("nome")
    idade = st.number_input("idade", min_value=14, step=1)
    if st.button('cadastrar'):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"aluno {nome} foi cadastrado com sucesso!! ")
        else:
            st.warning('o campo nome nao pode estar vazio')
elif menu == "listar":
    st.subheader('lista de alunos')
    alunos = listar_aluno()
    if alunos:
        st.table(alunos)
else:
    st.info('nenhum aluno encontrado!')


