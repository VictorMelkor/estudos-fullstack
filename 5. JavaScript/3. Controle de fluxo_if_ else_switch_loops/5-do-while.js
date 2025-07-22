// ==========================================
// DO...WHILE
// ==========================================

// Parecido com o while, mas garante que o bloco execute ao menos uma vez

let numero = 5;

do {
  console.log("Executando uma vez com número:", numero);
  numero++;
} while (numero < 3);

// Mesmo que a condição seja falsa, o bloco é executado uma vez.
