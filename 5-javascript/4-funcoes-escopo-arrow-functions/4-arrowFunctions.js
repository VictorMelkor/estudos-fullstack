// ==========================================
// ARROW FUNCTIONS (FUNÇÕES DE FLECHA)
// ==========================================

// Sintaxe reduzida para funções anônimas

// Forma tradicional
function quadrado(n) {
  return n * n;
}

// Arrow function equivalente
const quadradoArrow = (n) => {
  return n * n;
};

console.log(quadrado(3));       // 9
console.log(quadradoArrow(3));  // 9

// Versão reduzida (quando tem só 1 parâmetro e 1 linha de retorno)
const dobro = x => x * 2;

console.log(dobro(5)); // 10

// Arrow function NÃO tem 'this' próprio (importante para DOM depois)
