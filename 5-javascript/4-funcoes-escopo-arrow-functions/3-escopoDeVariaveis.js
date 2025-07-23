// ==========================================
// ESCOPO DE VARIÁVEIS
// ==========================================

// Escopo global: disponível em todo o script
let nome = "Maria";

function mostrarNome() {
  // Escopo de função: só existe dentro da função
  let idade = 30;
  console.log(nome);  // acessa variável global
  console.log(idade); // acessa variável local
}

mostrarNome();
// console.log(idade); // ❌ erro → idade só existe dentro da função

// Escopo de bloco (usando let ou const)
if (true) {
  let cor = "azul";
  console.log(cor); // "azul"
}
// console.log(cor); // ❌ erro → escopo de bloco
