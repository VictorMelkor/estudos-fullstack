// ==========================================
// ESTRUTURAS DE REPETIÇÃO (LOOPS)
// ==========================================

// FOR → Quando se sabe quantas vezes repetir
for (let i = 1; i <= 5; i++) {
  console.log("Contando: " + i);
}

// i = 1 → valor inicial
// i <= 5 → condição para continuar
// i++ → incremento por repetição

// WHILE → Repete enquanto a condição for verdadeira
let contador = 0;
while (contador < 3) {
  console.log("while: " + contador);
  contador++;
}

// DO...WHILE → Sempre executa pelo menos uma vez
let numero = 0;
do {
  console.log("do...while: " + numero);
  numero++;
} while (numero < 2);
