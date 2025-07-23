// ==========================================
// VARIÁVEIS E OPERADORES EM JAVASCRIPT
// ==========================================

// Variáveis são usadas para armazenar dados temporariamente.

// 'let' declara uma variável que pode ser alterada depois
let idade = 25;

// 'const' declara uma constante, ou seja, um valor que não muda
const nome = "Victor";

// OPERADORES ARITMÉTICOS
// Servem para fazer contas matemáticas básicas

let soma = 2 + 3;          // adição → 5
let subtracao = 10 - 4;    // subtração → 6
let multiplicacao = 5 * 2; // multiplicação → 10
let divisao = 20 / 4;      // divisão → 5
let resto = 10 % 3;        // módulo (resto da divisão) → 1

// OPERADORES RELACIONAIS
// Comparam dois valores e retornam true ou false

console.log(idade > 18);       // true → maior que
console.log(idade === 25);     // true → igual (valor e tipo)
console.log(idade !== 30);     // true → diferente

// OPERADORES LÓGICOS
// Usados para combinar condições

let temCarteira = true;
let podeDirigir = idade >= 18 && temCarteira;
// && → E: ambas as condições precisam ser verdadeiras
console.log(podeDirigir); // true

let estaChovendo = false;
let vaiSair = idade > 18 || estaChovendo;
// || → OU: basta uma condição ser verdadeira
console.log(vaiSair); // true

console.log(!temCarteira); // false → ! inverte o valor lógico
