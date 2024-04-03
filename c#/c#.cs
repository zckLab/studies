// Arquivo: Calculadora insana

using System;
// T
class Calculadora {
    public static void Main() {
        double number1 = Convert.ToDouble(Console.ReadLine());
        double number2 = Convert.ToDouble(Console.ReadLine());

        double result = number1 + number2;

        Console.WriteLine("Resultado: " + result);

        Console.ReadLine();
    }
}