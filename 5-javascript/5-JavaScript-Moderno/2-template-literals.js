// =======================================
// Template Literals - Strings multilinha e interpolação
// =======================================

// Antes do ES6, para concatenar strings:
let nome = "Ana";
let mensagem = "Olá, " + nome + "! Seja bem-vinda.";
console.log(mensagem);

// Template literals usam crases (` `) e permitem:
// 1) Interpolação com ${expressão}
// 2) Strings multilinha naturalmente

let mensagem2 = `Olá, ${nome}!
Seja bem-vinda ao curso de JavaScript.`;
console.log(mensagem2);
