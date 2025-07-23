// ==========================
// TYPEOF E COERÇÃO DE TIPOS
// ==========================

let x = "10";
let y = 10;

console.log(typeof x); // string
console.log(typeof y); // number

// Coerção implícita: o JS tenta "converter" automaticamente
console.log(x + y); // "1010" → string (concatenação)
console.log(x * y); // 100 → number (conversão implícita)

// Coerção explícita (forçar a conversão)
let numero = Number(x);
console.log(numero + y); // 20

let texto = String(y);
console.log(texto + " anos"); // "10 anos"
