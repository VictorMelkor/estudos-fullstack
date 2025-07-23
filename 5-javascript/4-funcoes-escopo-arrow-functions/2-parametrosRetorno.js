// ==========================================
// PARÂMETROS E RETORNO
// ==========================================

// Parâmetros são dados que você passa para a função
// Return é o valor que a função devolve

function soma(a, b) {
  return a + b;
}

let resultado = soma(3, 7);
console.log("Resultado da soma:", resultado);

// Funções podem retornar qualquer tipo: número, string, boolean, etc.
function saudacao(nome) {
  return "Olá, " + nome + "!";
}

console.log(saudacao("Victor"));
