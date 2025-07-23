// =======================================
// Promises - Manipulação de operações assíncronas
// =======================================

// Promise representa uma operação que pode completar ou falhar no futuro

const promessa = new Promise((resolve, reject) => {
  let sucesso = true;

  setTimeout(() => {
    if (sucesso) {
      resolve("Deu certo!");
    } else {
      reject("Deu errado!");
    }
  }, 1000);
});

promessa
  .then(resultado => console.log(resultado)) // "Deu certo!" após 1s
  .catch(erro => console.error(erro));

// Isso ajuda a evitar "callback hell" e torna código assíncrono mais legível.
