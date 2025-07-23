// ==========================================
// BREAK E CONTINUE
// ==========================================

// break → interrompe o loop
// continue → pula para a próxima iteração

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    console.log("Pulei o 3");
    continue; // não executa o restante do bloco quando i === 3
  }

  if (i === 5) {
    console.log("Saindo no 5");
    break; // encerra o loop completamente
  }

  console.log("Valor:", i);
}
