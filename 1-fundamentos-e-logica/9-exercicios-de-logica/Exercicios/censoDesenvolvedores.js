/*
🧠 EXERCÍCIO DE LÓGICA: Censo dos Desenvolvedores

Você está ajudando a organizar um CENSO DE DESENVOLVEDORES.
Dado um conjunto de respostas com o nome do dev e as tecnologias que ele usa,
crie um programa que:
1. Conte quantos devs usam cada tecnologia
2. Mostre um ranking decrescente de tecnologias mais populares
*/

// 🎯 ENTRADA SIMULADA
const respostas = [
  { nome: "Alice", tecnologias: ["Python", "JavaScript"] },
  { nome: "Bob", tecnologias: ["Python", "C#"] },
  { nome: "Carol", tecnologias: ["JavaScript", "HTML", "CSS"] },
  { nome: "David", tecnologias: ["Python", "HTML"] },
  { nome: "Eve", tecnologias: ["C#", "JavaScript"] }
];

// 🔢 Criamos um objeto para contar quantos devs usam cada tecnologia
const contagem = {};

// 🔄 Iteramos por cada resposta da lista
respostas.forEach((resposta) => {
  resposta.tecnologias.forEach((tec) => {
    if (contagem[tec]) {
      contagem[tec]++;
    } else {
      contagem[tec] = 1;
    }
  });
});

// 🧮 Transformamos o objeto em um array de pares [tecnologia, quantidade]
const ranking = Object.entries(contagem).sort((a, b) => b[1] - a[1]);

// 📊 Exibimos o ranking
console.log("Ranking de tecnologias mais populares:");
ranking.forEach(([tecnologia, quantidade], index) => {
  console.log(`${index + 1}. ${tecnologia} - ${quantidade} devs`);
});

/*
🧠 CONCEITOS APLICADOS:
- Objetos (object): usados para contar ocorrências de cada tecnologia
- Array.forEach(): percorre listas e listas internas
- Condicional if/else: verifica se a tecnologia já foi contada
- Object.entries(): converte o objeto em array de pares [chave, valor]
- Array.sort(): ordena o array com base no número de devs
- Array destructuring: usamos para pegar chave e valor diretamente no forEach
- console.log(): imprime os resultados formatados no navegador

💡 EXPANSÕES POSSÍVEIS:
- Coletar dados de um formulário HTML
- Exibir o ranking em uma tabela no DOM
- Salvar e recuperar do LocalStorage
- Gerar gráficos com Chart.js
*/
