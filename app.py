import streamlit as st
from crud import criar_aluno, listar_aluno, atualizar_alunos, deletar_aluno

# Configuração da página
st.set_page_config(page_title="Gerenciamento de Alunos", page_icon="🎓")

st.title("🎓 Sistema de Gerenciamento de Alunos (PostgreSQL)")

# Menu lateral
menu = st.sidebar.radio("Menu", ["📥 Criar", "📋 Listar", "✏️ Atualizar", "❌ Deletar"])

# ---------------------
# Função: Criar Aluno
# ---------------------
if menu == "📥 Criar":
    st.subheader("Cadastrar novo aluno")

    nome = st.text_input("Nome do aluno")
    idade = st.number_input("Idade", min_value=14, max_value=100, step=1)

    if st.button("Cadastrar"):
        if nome.strip():
            criar_aluno(nome, idade)
            st.success(f"✅ Aluno **{nome}** cadastrado com sucesso!")
        else:
            st.warning("⚠️ O campo **Nome** não pode estar vazio.")

# ---------------------
# Função: Listar Alunos
# ---------------------
elif menu == "📋 Listar":
    st.subheader("Lista de Alunos")

    alunos = listar_aluno()
    if alunos:
        st.table(alunos)
    else:
        st.info("ℹ️ Nenhum aluno encontrado.")

# ---------------------
# Função: Atualizar Aluno
# ---------------------
elif menu == "✏️ Atualizar":
    st.subheader("Atualizar idade do aluno")

    alunos = listar_aluno()
    if alunos:
        alunos_dict = {f"{linha[1]} (ID: {linha[0]})": linha[0] for linha in alunos}
        aluno_selecionado = st.selectbox("Escolha o aluno", list(alunos_dict.keys()))
        id_aluno = alunos_dict[aluno_selecionado]

        nova_idade = st.number_input("Nova idade", min_value=14, max_value=100, step=1)

        if st.button("Atualizar"):
            atualizar_alunos(id_aluno, nova_idade)
            st.success(f"✅ Idade do aluno **{aluno_selecionado}** atualizada com sucesso!")
    else:
        st.info("ℹ️ Nenhum aluno disponível para atualizar.")

# ---------------------
# Função: Deletar Aluno
# ---------------------
elif menu == "❌ Deletar":
    st.subheader("Deletar aluno")

    alunos = listar_aluno()
    if alunos:
        alunos_dict = {f"{linha[1]} (ID: {linha[0]})": linha[0] for linha in alunos}
        aluno_selecionado = st.selectbox("Escolha o aluno para deletar", list(alunos_dict.keys()))
        id_aluno = alunos_dict[aluno_selecionado]

        if st.button("Deletar"):
            deletar_aluno(id_aluno)
            st.success(f"🗑️ Aluno **{aluno_selecionado}** deletado com sucesso!")
    else:
        st.info("ℹ️ Nenhum aluno disponível para deletar.")
