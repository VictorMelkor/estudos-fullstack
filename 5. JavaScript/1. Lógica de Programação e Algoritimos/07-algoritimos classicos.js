// ==========================================
// ALGUNS ALGORITMOS CLÁSSICOS
// ==========================================

// Verifica se um número é primo
function ehPrimo(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
console.log("7 é primo?", ehPrimo(7)); // true

// Cálculo de fatorial com laço
function fatorialIterativo(n) {
  let resultado = 1;
  for (let i = 2; i <= n; i++) {
    resultado *= i;
  }
  return resultado;
}
console.log("Fatorial de 5:", fatorialIterativo(5)); // 120
