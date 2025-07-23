// ==========================================
// FUNÇÕES ANÔNIMAS E CALLBACKS
// ==========================================

// Funções anônimas → sem nome
const saudacao = function(nome) {
  return "Oi, " + nome;
};

console.log(saudacao("Lucas"));

// Callbacks → função passada como argumento
function executar(acao) {
  console.log("Início");
  acao(); // chama a função recebida
  console.log("Fim");
}

executar(function () {
  console.log("Executando callback...");
});
