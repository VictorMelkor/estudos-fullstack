// =======================================
// let e const - Declaração de variáveis
// =======================================

// Antes do ES6, usava-se 'var' para declarar variáveis.
// Problema: 'var' tem escopo de função e pode causar bugs.

// ES6 introduziu 'let' e 'const' com escopo de bloco, melhor controle.

// 'let' permite reatribuição, mas respeita escopo de bloco.
let idade = 25;
idade = 26; // ok

// 'const' cria uma constante - valor imutável (não pode reatribuir)
const PI = 3.1415;
// PI = 3.14; // ERRO!

// Mesmo assim, se o valor for um objeto ou array, seu conteúdo pode mudar.
const lista = [1, 2, 3];
lista.push(4); // ok - o array em si não mudou, só o conteúdo

console.log(lista); // [1, 2, 3, 4]

// Recomendação: use const sempre que possível e let quando for necessário reatribuir.
