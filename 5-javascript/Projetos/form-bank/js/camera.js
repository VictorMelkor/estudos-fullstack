const botaoIniciarCamera = document.querySelector("[data-video-botao]");
const campoCamera = document.querySelector("[data-camera]");
const video = document.querySelector("[data-video]");
const botaoTirarFoto = document.querySelector("[data-tirar-foto]");
const canvas = document.querySelector("[data-video-canvas]");
const mensagem = document.querySelector("[data-mensagens]");
const botaoEnviarFoto = document.querySelector("[data-enviar]");

let imagemURL = "";

botaoIniciarCamera.addEventListener("click", async function () {
    try {
        const iniciarVideo = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        botaoIniciarCamera.style.display = "none";
        campoCamera.style.display = "block";

        video.srcObject = iniciarVideo;

    } catch (erro) {
        mensagem.textContent = "❌ Nenhuma câmera foi encontrada ou acesso negado.";
        console.error("Erro ao acessar a câmera:", erro);
    }
});

botaoTirarFoto.addEventListener("click", function() {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.clientWidth, canvas.heigth)

    imagemURL = canvas.toDataURL("image/jpeg");

    campoCamera.style.display = "none";
    mensagem.style.display = "block"
})

botaoEnviarFoto.addEventListener("click", () => {
    const receberDadosExistentes = localStorage.getItem("cadastro");
    const converteRetorno = JSON.parse(receberDadosExistentes);
    converteRetorno.imagem = imagemURL;

    localStorage.setItem('cadastro', JSON.stringify(converteRetorno));

    window.location.href = "./abrir-conta-form-3.html"
})