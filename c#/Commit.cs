//Estrutura do programa C#
 
//Usando um namespace
using System;
 
//Namespace
namespace MeuNamespace                                      
{
    //Classe
    public class MinhaAplicacao                               
    {
        //Comentários de linhas múltiplas
        /*Este programa                                     
         exibe no prompt
         um cálculo de soma*/
 
        static void Main(string[] args)
        //Início de bloco
        {
            MinhaClasse m = new MinhaClasse();
            Console.WriteLine(m.Soma(100, 10));
        //Fim de bloco
        }
 
        //Comentário XML
        ///<summary>        
        ///Minha Classe Math                               
        ///</summary>
 
        public class MinhaClasse
        {
            //Método
            public int Soma(int a, int b) {return a + b;}   
        }
    }
}