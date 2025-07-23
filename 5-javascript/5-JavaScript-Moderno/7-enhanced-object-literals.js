// =======================================
// Objetos Literais Aprimorados (ES6)
// =======================================

const nome = "Carlos";
const idade = 30;

// Antes, era necessário escrever assim:
const pessoa1 = {
  nome: nome,
  idade: idade
};

// Agora, pode simplificar quando nome da propriedade é igual à variável:
const pessoa2 = {
  nome,
  idade
};

console.log(pessoa2);

// Também é possível definir métodos de forma mais simples
const pessoa3 = {
  nome,
  idade,
  saudacao() {
    console.log(`Olá, eu sou ${this.nome}`);
  }
};

pessoa3.saudacao();
