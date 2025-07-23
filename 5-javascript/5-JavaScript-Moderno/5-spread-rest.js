// =======================================
// Spread (...) e Rest (...) operators
// =======================================

// Spread (espalhar elementos de arrays ou objetos)

const arr1 = [1, 2, 3];
const arr2 = [4, 5];

// Combinar arrays com spread
const combinado = [...arr1, ...arr2];
console.log(combinado); // [1, 2, 3, 4, 5]

// Copiar array
const copia = [...arr1];

// Spread com objetos
const obj1 = { a: 1, b: 2 };
const obj2 = { b: 3, c: 4 };

// Combinar objetos (propriedades do segundo sobrescrevem do primeiro)
const combinadoObj = { ...obj1, ...obj2 };
console.log(combinadoObj); // { a:1, b:3, c:4 }

// Rest (juntar parâmetros ou propriedades restantes)

function somaTudo(...numeros) {
  return numeros.reduce((acc, n) => acc + n, 0);
}

console.log(somaTudo(1, 2, 3, 4)); // 10

const { a, ...resto } = combinadoObj;
console.log(a);      // 1
console.log(resto);  // { b: 3, c: 4 }
