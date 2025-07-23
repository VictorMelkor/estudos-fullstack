// ==========================================
// CONDICIONAIS EM JAVASCRIPT
// ==========================================

// Condicionais são usadas para tomar decisões baseadas em condições

let idade = 16;

// Estrutura if/else if/else
if (idade < 12) {
  console.log("Criança");
} else if (idade < 18) {
  console.log("Adolescente");
} else {
  console.log("Adulto");
}

// A estrutura é sempre:
// if (condição) { ... } else if (outra condição) { ... } else { ... }

// SWITCH
// Outra forma de tomar decisões, ideal quando se testa um valor específico

let cor = "azul";

switch (cor) {
  case "vermelho":
    console.log("Cor quente");
    break;
  case "azul":
    console.log("Cor fria");
    break;
  default:
    console.log("Cor indefinida");
}

// O switch compara valor exato (===) com cada "case"
// 'break' evita que o código continue executando os próximos cases
