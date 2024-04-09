programa {
      funcao inicio() {
		real media
		real nota_um
		real nota_dois
		real nota_tres
		media = 7

          escreva("Digite a nota 1:")
          leia(nota_um)
          
          escreva("Digite a nota 2:")
          leia(nota_dois)
          
          escreva("Digite a nota 3:")
          leia(nota_tres)
          
          se(media >= 7){
		escreva("Aluno aprovado!")
		} senao {
		escreva("Aluno reprovado")
	}
  escreva("\nMedias verificadas com sucesso!!!")
  }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 151; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */