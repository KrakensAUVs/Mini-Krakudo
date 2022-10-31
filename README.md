# Mini-Krakudo
Projeto piloto para testar os módulos da arquitetura de software projetada para o submarino. 
## Módulos
#### 1. Localizer 
Módulo responsável por estimar a pose do Krakudo no ambiente real a partir da leitura dos sensores. Para localizar o Krak no mapa exportado pelo módulo cartógrafo, ele requisita aos sensores a leitura das movimentações feitas pelo robô. A estimativa é armazenada e disponibilizada aos outros módulos, atualizando de tempo em tempo.
#### 2. Cartográfico
Este módulo mapeia o ambiente utilizando a posição do Krakudo exportada pelo módulo Localizer e leituras do sensor de distância e objeto detectado exportado pelo módulo Perception. O módulo é responsável por manter atualizado um mapa global com o tipo, posição e pose do objeto detectado. Aqui pode ser usado o método SLAM clássico ou com visão.
#### 3. Planejamento
O módulo Planejamento é responsável por determinar as ações necessárias pelo Krak para realizar uma dada tarefa. Para determinar as ações necessárias ele se utiliza de a posição global fornecida pelo módulo Localizer, o mapa global fornecido pelo módulo Cartográfico e as informações fornecidas pelo módulo de Percepção.
Além disso, o módulo também é responsável por gerar um conjunto de pontos que levem o Krak ao destino que se deseja atingir, gerado pelo submódulo Navegador. Os movimentos necessários para cada tarefa será armazenada neste módulo, e junto com as informações sobre a posição, gera uma sequência de pontos a serem passados para o Executor.
#### 4. Executor
Este módulo tem a função de executar a trajetória proveniente do módulo Planejamento. Para isto ele passa as referências sincronamente ao controlador que controla os servo motores nas rodas. Ele também possui um submódulo desviador de obstáculos. Seu papel é evitar que o Krakudo colida com algum obstáculo. O robô possui motores diferenciais, o que implica que seu movimento de rotação se da a partir da diferença de velocidade entre as rodas. 
#### 5. Percepção
O módulo de Percepção é responsável por reconhecer objetos e mandar para o módulo cartográfico e planejador. Se usarmos o SLAM com visão, vamos ter que identificar os pontos neste módulo também e fazer o acompanhamento deles. 

#### TODO list
### 1° etapa (2 semanas) 06/11?
- [ ] Acionar os motores dc com a Jetson Nano.
- [ ] Calcular a distância de objetos com o sensor ultrasônico.
- [ ] Montar um ciruito onde o Krak terá que buscar por tarefas e a realizar quando encontrar. 
- [ ] Coletar imagens com a camera direto na Jetson Nano. 

### 2° etapa
- [ ] Andar em linha reta. 08/11?
- [ ] Identificar o movimento do Krakudo através de enconders ou outra forma.
- [ ] Dar comandos em centímetros para o Krakudo andar em linha reta com precisão (translação). 
- [ ] Coletar imagens dos objetos do circuito com o próprios Krakudo, e treinar o modelo de visão computacional para identificar objetos. 

### 3° etapa 19/11?
- [ ] Identificar graficamente em um mundo global o movimento do Krak com o auxílio de algum simulador (MATLAB).
- [ ] Dar comandos em graus para o Krak rotacionar com precição (rotação). 
- [ ] Calcular e executar trajetorias fazendo curvas.
- [ ] Executar movimentos em linha reta, fazendo curva, ré, etc.

### 4° etapa 26/11?
- [ ] Usar o Krakudo para identificar um objeto, posiciona-lo centralizado ao sensor ultrasônico e calcular a distância do objeto.
- [ ] Usar a informação do objeto detectado e da distância coletada para montar um mapa global do objeto e do Krakudo.
- [ ] Realizar a parte reativa do Krakudo, desviar de objetos e voltar à trajetória. Com o auxílio do sensor de distância. 

### 5° etapa 03/12?
- [ ] Fazer uma máquina de estado com os movimentos necessários para a realização de cada tarefa individualmente. 
- [ ] Juntar todas as máquinas de estados em uma única máquina de estado para planejar as missões e execuções do Krak. 
- [ ] #TESTARTUDOJUNTO
