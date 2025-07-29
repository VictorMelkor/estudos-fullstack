using System;

public class Desafio
{
    public static void Main()
    {
        // Lê os valores de Entrada:
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());

        float valorImposto = 0;

        if (valorSalario >= 0 && valorSalario <= 1100)
        {
            // Atribui a alíquota de 5% mediante o salário:
            valorImposto = 0.05F * valorSalario;
        }
        else if (valorSalario <= 2500)
        {
            // Alíquota de 10% para salários entre 1100.01 e 2500
            valorImposto = 0.10F * valorSalario;
        }
        else
        {
            // Alíquota de 15% para salários acima de 2500
            valorImposto = 0.15F * valorSalario;
        }

        // Calcula e imprime a Saída (com 2 casas decimais):
        float saida = valorSalario - valorImposto + valorBeneficios;
        Console.WriteLine(saida.ToString("0.00"));
    }
}
