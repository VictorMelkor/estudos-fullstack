import api from "./api.js"

const ui = {

    async preencherFormulario(pensamentoId) {
        const pensamento = await api.buscarPensamentoPorId(pensamentoId)
        document.getElementById("pensamento-id").value = pensamento.id
        document.getElementById("pensamento-conteudo").value = pensamento.conteudo
        document.getElementById("pensamento-autoria").value = pensamento.autoria
        document.getElementById("pensamento-data").value = pensamento.data.toISOString().split("T")[0]
        document.getElementById('form-container').scrollIntoView()
    },

    limparFormulario() {
        document.getElementById("pensamento-form").reset();
    },

    async renderizarPensamentos(pensamentosFiltrados = null) {
        const listaPensamentos = document.getElementById('lista-pensamentos');
        const mensagemVazia = document.getElementById("mensagem-vazia")
        listaPensamentos.innerHTML = ""

        try {
            let pensamentosParaRenderizar

            if (pensamentosFiltrados) {
                pensamentosParaRenderizar = pensamentosFiltrados
            } else {
                pensamentosParaRenderizar = await api.buscarPensamentos()
            }


            if (pensamentosParaRenderizar.length === 0) {
                mensagemVazia.style.display = "block";
            } else {
                mensagemVazia.style.display = "none"
                pensamentosParaRenderizar.forEach(ui.adicionarPensamentoNaLista)
            }
        }
        catch {
            alert('Pensamento não encontrado')
        }
    },

    adicionarPensamentoNaLista(pensamento) {
        const listaPensamentos = document.getElementById('lista-pensamentos');
        const li = document.createElement("li");

        li.setAttribute("data-id", pensamento.id)
        li.classList.add("li-pensamento")

        const iconeAspas = document.createElement("img")
        iconeAspas.src = "assets/imagens/aspas-azuis.png"
        iconeAspas.alt = "Aspas azuis"
        iconeAspas.classList.add("icone-aspas")

        const pensamentoConteudo = document.createElement("div")
        pensamentoConteudo.textContent = pensamento.conteudo
        pensamentoConteudo.classList.add("pensamento-conteudo")

        const pensamentoAutoria = document.createElement("div")
        pensamentoAutoria.textContent = pensamento.autoria
        pensamentoAutoria.classList.add("pensamento-autoria")

        let options = {
            weekday: `long`,
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            timeZone: 'UTC'
        }

        const pensamentoData = document.createElement("div")
        const dataFormatada = pensamento.data.toLocaleDateString(`pt-BR`, options)
        const dataComRegex = dataFormatada.replace(/^(\w)/, (match) => match.toUpperCase())

        pensamentoData.textContent = dataComRegex
        pensamentoData.classList.add("pensamento-data")

        const botaoFavorito = document.createElement("button")
        botaoFavorito.classList.add("botao-favorito")
        botaoFavorito.onclick = async () => {
            try {
                await api.atualizarFavorito(pensamento.id, !pensamento.favorito)
                ui.renderizarPensamentos
            } catch (error) {
                alert("Erro ao atualizar pensamento")
            }
        }

        const botaoEditar = document.createElement("button")
        botaoEditar.classList.add("botao-editar")
        botaoEditar.onclick = () => {
            ui.preencherFormulario(pensamento.id)
        }

        const iconeFavorito = document.createElement("img")
        iconeFavorito.src = pensamento.favorito ? "assets/imagens/icone-favorito.png" : "assets/imagens/icone-favorito_outline.png"

        iconeFavorito.alt = "Icone de favorito"
        botaoFavorito.appendChild(iconeFavorito)


        const iconeEdicao = document.createElement("img")
        iconeEdicao.src = "assets/imagens/icone-editar.png"
        iconeEdicao.alt = "Icone de edição"
        botaoEditar.appendChild(iconeEdicao)

        const botaoExcluir = document.createElement("button")
        botaoExcluir.classList.add("botao-excluir")
        botaoExcluir.onclick = async () => {
            try {
                await api.excluirPensamento(pensamento.id)
                ui.renderizarPensamentos
            } catch (error) {
                alert("Erro ao excluir pensamento")
            }
        }

        const iconeExcluir = document.createElement("img")
        iconeExcluir.src = "assets/imagens/icone-excluir.png"
        iconeExcluir.atl = "Icone de Excluir"
        botaoExcluir.appendChild(iconeExcluir)

        const icones = document.createElement("div")
        icones.classList.add("icones")
        icones.appendChild(botaoFavorito)
        icones.appendChild(botaoEditar)
        icones.appendChild(botaoExcluir)




        li.appendChild(iconeAspas)
        li.appendChild(pensamentoConteudo)
        li.appendChild(pensamentoAutoria)
        li.appendChild(pensamentoData)
        li.appendChild(icones)


        listaPensamentos.appendChild(li)
    },


}





export default ui