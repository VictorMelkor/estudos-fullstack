
const btnNovoItem = document.querySelector(".form-button");
const listaDeTarefas = document.querySelector(".list");

const criarTarefa = (evento) => {
    evento.preventDefault();

    const inputTexto = document.querySelector(".form-input");
    const novoInput = inputTexto.value;
    inputTexto.value = ""

    const novoItem = document.createElement("li");
    const texto = document.createElement("p");

    novoItem.classList.add("task")
    texto.classList.add("content");

    if (novoInput != "") {
        texto.textContent = novoInput
        novoItem.appendChild(texto)
        novoItem.appendChild(ConcluirTarefa())
        novoItem.appendChild(DeletarTarefa())
        listaDeTarefas.appendChild(novoItem)
    }
}

const ConcluirTarefa = () => {
    const btnConcluirTarefa = document.createElement("button");
    btnConcluirTarefa.classList.add("check-button");
    btnConcluirTarefa.innerText = "concluir"

    btnConcluirTarefa.addEventListener("click", (evento) => {
        evento.preventDefault();
        const li = evento.target.parentElement;
        li.classList.add("done")
    })

    return btnConcluirTarefa
}

const DeletarTarefa = () => {
    const btnDeletar = document.createElement("button");
    btnDeletar.classList.add("delete-button");
    btnDeletar.innerText = "deletar"

    btnDeletar.addEventListener ("click", (evento) => {
        evento.preventDefault();
        const li = evento.target.parentElement;
        li.remove()
    })

    return btnDeletar
}

btnNovoItem.addEventListener("click", criarTarefa)