// =======================================
// Arrow Functions (funções de flecha) detalhadas
// =======================================

// Sintaxe curta para funções anônimas

// Tradicional
function soma(a, b) {
  return a + b;
}

// Arrow function equivalente
const somaArrow = (a, b) => a + b;

console.log(soma(2, 3));      // 5
console.log(somaArrow(2, 3)); // 5

// Mais de um parâmetro precisa de parênteses, zero ou um parâmetro pode omitir parênteses

const dizerOla = () => "Olá!";
const quadrado = x => x * x;

console.log(dizerOla());
console.log(quadrado(5));

// Diferença importante: Arrow functions não possuem seu próprio this,
// herdando o this do escopo pai.
