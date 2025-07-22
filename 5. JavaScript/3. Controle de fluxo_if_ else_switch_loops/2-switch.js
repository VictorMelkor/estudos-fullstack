// ==========================================
// SWITCH
// ==========================================

// Útil quando você quer testar um único valor com várias possibilidades

let dia = 3;

switch (dia) {
  case 1:
    console.log("Domingo");
    break;
  case 2:
    console.log("Segunda");
    break;
  case 3:
    console.log("Terça");
    break;
  default:
    console.log("Dia inválido");
}

// 'break' impede que os outros cases sejam executados em sequência.
