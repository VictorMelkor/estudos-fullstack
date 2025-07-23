// =======================================
// Destructuring - Extrair dados de arrays e objetos facilmente
// =======================================

// Destructuring de array
const numeros = [10, 20, 30];

// Extrai elementos para variáveis
const [primeiro, segundo, terceiro] = numeros;

console.log(primeiro);  // 10
console.log(segundo);   // 20

// Você pode ignorar valores
const [, , ultimo] = numeros;
console.log(ultimo);    // 30

// Destructuring de objeto
const pessoa = {
  nome: "João",
  idade: 28,
  cidade: "SP"
};

const { nome, idade } = pessoa;

console.log(nome);  // João
console.log(idade); // 28

// Pode renomear variáveis
const { cidade: cidadeNatal } = pessoa;
console.log(cidadeNatal); // SP

// Pode usar valores padrão
const { estado = "SP" } = pessoa;
console.log(estado); // SP (porque não existia no objeto)
