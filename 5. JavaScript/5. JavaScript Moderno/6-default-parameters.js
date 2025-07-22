// =======================================
// Parâmetros padrão em funções
// =======================================

function saudacao(nome = "Visitante") {
  return `Olá, ${nome}!`;
}

console.log(saudacao());       // Olá, Visitante!
console.log(saudacao("Ana"));  // Olá, Ana!

// Útil para evitar erros quando parâmetro não é passado
