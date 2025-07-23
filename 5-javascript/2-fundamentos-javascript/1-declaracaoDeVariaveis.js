// ==========================
// DECLARAÇÃO DE VARIÁVEIS
// ==========================

// var → escopo de função (evite)
var nome1 = "João";

// let → escopo de bloco (preferido para valores mutáveis)
let nome2 = "Maria";

// const → escopo de bloco e valor constante (imutável)
const PI = 3.14;

// let permite reatribuição
let idade = 25;
idade = 26; // ok

// const não permite reatribuição
const cpf = "123.456.789-00";
// cpf = "000.000.000-00"; // ❌ erro
