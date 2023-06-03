## Projeto: `Algorithms`

- Nesse projeto foi solicitado a criação de métodos com seu nível de complexidade mesurado, exigindo um patamar máximo, medindo tempo e método usando recursividade.

## Seção: 

- Durante essa seção foi apresentada a ideia de complexidade assintótica com Big O, complexidades logaritmicas, quadraticas, cubicas, linearitmicas, etc...
- Busca linear e binária
- Ordenações e suas diferentes formas como, merge, quick, bubble, insertion e selection.
- A necessidade de alternar entre uma e outra dependendo da necessidade do projeto.
- Métodos recursivos vs iterativos, suas vantagens e diferenças.
<details>
  <summary>
    <strong>
      :telescope: Métodos criados no projeto:
    </strong>
  </summary>

  
# Challenge Study Schedule

Método para identificar em uma lista de tuplas onde é definido cada aluno seu inicio e fim de estudos, em qual mais alunos estudam no mesmo horario, onde é defino um algo.

<details>
  <summary>
  Exemplo(Retirado do README da trybe):
  </summary>

```
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```

</details>

# Test encrypt

Criação de um teste, usando pytest, onde o método recebe uma `message` e um inteiro `key`, onde:

- Se `key` e `message` não possuírem os tipos corretos, uma exceção deve ser lançada
- Se`key`não for um índice positivo válido de `message`, retorna a string `message` invertida
- Se`key`for ímpar:
divide `message` no índice`key` inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas
- Se`key`for par:
divide `message` no índice`key` inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas

<details>
  <summary>
  Exemplo(Retirado do README da trybe):
  </summary>

```
message = "AABBCC"
key = 3
# saída: "BAA_CCB"

message = "ABBCCA"
key = 4
# saída: "AC_CBBA"

message = "AABBCC"
key = -1
# saída: "CCBBAA"
```

O teste deve garantir que o método funciona como explicado.

</details>

# Challenge Palindrome Recursivo

Criação de um método, que identifica se uma palavra é um palindrome, retornando True quando sim, e False, quando negativo. 
Usando Recursividade.

> Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`. 

# Challenge Anagrams

Fornecendo duas palavras é analisado se uma palavra é anagrama da outra, retornando ambas com uma reordenação de palavras de forma alfabética, e com True ou False, se elas são anagramas.

> "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

# Challenge Find the duplicate

Dada uma lista de números inteiros positivos sem ordem, identifica o primeiro número que está duplicado na lista, retornando o mesmo, e caso não exista um número repetido ou tenha um número negativo ou string, retorna `False`
# Challenge Palindrome Iterative

Versão iterativa, para identificar se uma palavra é palindrome.


</details>

#

# Tecnologias e ferramentas usadas 🛠

![Python](https://img.shields.io/badge/-Python-%23F7DF1C?style=flat-square&logo=python)
![Pytest](https://img.shields.io/badge/-Pytest-fff?style=flat-square&logo=pytest)


# Desafios

- Não pensar em somente fazer funcionar o método mas ter um capricho na parte de complexidade de tempo e espaço(espaço não foi o foco no projeto), pensar melhor nas melhores opções quando abordando soluções de escalas maiores e menores.

# Conclusão

- Como sempre na área de desenvolvimento, existem N formas de resolver desafios, agora mais uma forma foi adiciona ao meu vocabulário, recursividade e complexidade de tempo e espaço, não existe um dia, que eu não aprenda algo novo.

<details>
  <summary>
    <strong>
      ⚠️ Configurações mínimas para execução do projeto
    </strong>
  </summary>

   - Sistema Operacional Distribuição Unix
 - Python versão >= 3.8.10 

</details>

</details>

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos solicitados durante o desenvolvimento do projeto
    </strong>
  </summary>

 
### Resultado por requisito
*Nome* | *Avaliação*
--- | :---:
1.1 - Retorne, para uma entrada específica, a quantidade de estudantes presentes | :heavy_check_mark:
1.2 - Retorne `None` se em `permanence_period` houver alguma entrada inválida | :heavy_check_mark:
1.3 - Retorne `None` se  `target_time` recebe um valor vazio | :heavy_check_mark:
1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear | :heavy_check_mark:
2 - Implementar adequadamente o teste para a função `encrypt_message` | :heavy_check_mark:
3.1 - Retorne `True` se a palavra passada por parâmetro for um palíndromo | :heavy_check_mark:
3.2 - Retorne `False` se a palavra passada por parâmetro não for um palíndromo | :heavy_check_mark:
3.3 - Retorne `False` se nenhuma palavra for passada por parâmetro | :heavy_check_mark:
4.1 - Retorne `True` se as palavras passadas forem anagramas | :heavy_check_mark:
4.2 - Retorne `False` se as palavras passadas por parâmetro não forem anagramas | :heavy_check_mark:
3.3 - Retorne `false` se alguma das palavras passadas por parâmetro for uma string vazia | :heavy_check_mark:
4.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica | :heavy_check_mark:
4.5 - Retorne `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas | :heavy_check_mark:
5.1 - Retorne o número repetido se a função receber, como parâmetro, uma lista com números repetidos | :heavy_check_mark:
5.2 - Retorne `False` se a função não receber nenhum parâmetro | :heavy_check_mark:
5.3 - Retorne `False` se a função receber, como parâmetro, uma string | :heavy_check_mark:
5.4 - Retorne `False` se a função receber, como parâmetro, uma lista sem números repetidos | :heavy_check_mark:
5.5 - Retorne `False` se a função receber, como parâmetro, apenas um valor | :heavy_check_mark:
5.6 - Retorne `False` se a função receber, como parâmetro, um número negativo | :heavy_check_mark:
5.7 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica. | :heavy_check_mark:
6.1 - Retorne `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa | :heavy_check_mark:
6.2 - Retorne `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa | :heavy_check_mark:
6.3 - Retorne `False` se nenhuma palavra for passada como parâmetro, executando uma função iterativa | :heavy_check_mark:
6.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear. | :heavy_check_mark:


</details>
