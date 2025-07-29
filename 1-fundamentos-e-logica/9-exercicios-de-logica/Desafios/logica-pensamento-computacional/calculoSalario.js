// Desafios JavaScript tem funções "get" e "print" acessíveis globalmente:
//- "gets": Lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

// Lê os valores de entrada:
const valorSalario = parseFloat(gets());
const valorBeneficios = parseFloat(gets());

// Calcula o imposto através da função "calcularImposto":
const valorImposto = calcularImposto(valorSalario);
// Calcula e imprime a saída (com 2 casas decimais):
const saida = valorSalario - valorImposto + valorBeneficios;
print(saida.toFixed(2));

// função útil para o calculo do imposto (baseado nas aliquotas):
function calcularImposto(salario) {
    let aliquota;
    if (salario >= 0 && salario <= 1100) {
        aliquota = 0.05;
    } else if ( salario >= 1100.1 && salario <= 2500) {
        aliquota = 0.10;
    } else {
        aliquota = 0.15;
    }

    return aliquota * salario;
    
}