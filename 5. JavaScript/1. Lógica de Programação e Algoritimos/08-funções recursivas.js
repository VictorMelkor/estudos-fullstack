// ==========================================
// FUNÇÕES RECURSIVAS
// ==========================================

// Recursão é quando uma função chama a si mesma

// Exemplo: fatorial recursivo
function fatorial(n) {
  if (n === 0) return 1; // caso base
  return n * fatorial(n - 1); // chamada recursiva
}
console.log("Fatorial de 5:", fatorial(5)); // 120

// Sequência de Fibonacci com recursão
function fibonacci(n) {
  if (n <= 1) return n; // casos base: fib(0)=0, fib(1)=1
  return fibonacci(n - 1) + fibonacci(n - 2); // chamada recursiva
}
console.log("Fibonacci(6):", fibonacci(6)); // 8
