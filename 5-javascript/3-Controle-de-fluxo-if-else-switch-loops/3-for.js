// ==========================================
// LAÇO FOR
// ==========================================

// Ideal quando você sabe quantas vezes quer repetir algo

for (let i = 1; i <= 5; i++) {
  console.log("Contando: " + i);
}

// Estrutura: for (início; condição; incremento)
// Exemplo prático: somar os números de 1 a 10

let soma = 0;
for (let i = 1; i <= 10; i++) {
  soma += i;
}
console.log("Soma total:", soma);
