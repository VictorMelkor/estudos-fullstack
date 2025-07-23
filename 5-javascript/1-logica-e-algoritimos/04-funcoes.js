// ==========================================
// FUNÇÕES EM JAVASCRIPT
// ==========================================

// Uma função é um bloco reutilizável de código

// Função tradicional com parâmetro e retorno
function saudacao(nome) {
  return "Olá, " + nome + "!";
}

console.log(saudacao("Victor")); // "Olá, Victor!"

// Função que retorna verdadeiro se o número for par
function ehPar(numero) {
  return numero % 2 === 0;
}

console.log(ehPar(4)); // true
console.log(ehPar(7)); // false
