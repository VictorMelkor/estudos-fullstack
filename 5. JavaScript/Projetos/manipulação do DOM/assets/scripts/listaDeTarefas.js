
const btnNovoItem = document.querySelector(".form-button");
const listaDeTarefas = document.querySelector(".list");

const criarTarefa = (evento) => {
    evento.preventDefault();

    const inputTexto = document.querySelector(".form-input");
    const novoInput = inputTexto.value;
    inputTexto.value = ""
    
    const novoItem  = document.createElement("li");
    const texto = document.createElement("p");

    novoItem.classList.add("task")
    texto.classList.add("content");

    if (novoInput != "") {
        texto.textContent = novoInput
        novoItem.appendChild(texto)
        listaDeTarefas.appendChild(novoItem)
    }

}

btnNovoItem.addEventListener("click", criarTarefa)