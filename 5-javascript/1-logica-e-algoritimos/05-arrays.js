// ==========================================
// ARRAYS (LISTAS) EM JAVASCRIPT
// ==========================================

// Arrays armazenam vários valores em uma única variável
let frutas = ["maçã", "banana", "uva"];

// Acessar elementos por índice (começa do zero)
console.log(frutas[0]); // "maçã"
console.log(frutas[1]); // "banana"

// Percorrer todos os itens com for...of
for (let fruta of frutas) {
  console.log("Fruta: " + fruta);
}

// Também pode usar for tradicional se quiser o índice
for (let i = 0; i < frutas.length; i++) {
  console.log("Fruta " + i + ": " + frutas[i]);
}
