import smach
from robot import *

krakudo = Robot()
krakudo.set_motors()

class Explorar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['tarefa1', 'tarefa2'])

    def execute(self, userdata):
        # Criando a submáquina de estados
        if (userdata['inicio']):
            my_initial_state = 'GIRAR_45_POS'
        else:
            my_initial_state =
        sub_sm = smach.StateMachine(outcomes=['done'],
                        initial_state='GIRAR_45_POS')

        # Adicionando os estados à submáquina de estados
        with sub_sm:
            smach.StateMachine.add('ANDAR_1S', Andar1Segundo(),
                                   transitions={'n90':'GIRAR_90_NEG', 'p90':'GIRAR_90_POS'})
            smach.StateMachine.add('GIRAR_90_NEG', Girar90Neg(),
                                   transitions={'done':'ANDAR_1S'})
            smach.StateMachine.add('GIRAR_90_POS', Girar90Pos(),
                                   transitions={'done':'ANDAR_1S'})
            smach.StateMachine.add('GIRAR_45_POS', Girar45Pos(),
                                   transitions={'done':'ANDAR_1S'})
        sub_sm.execute()

        # verificando se algum objeto foi encontrado
        if objeto_encontrado:
            if objeto == 'objeto1':
                return 'tarefa1'
            else:
                return 'tarefa2'
        else:
            return 'explorar'

class Tarefa1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['explorar'])

    def execute(self, userdata):
        # código para executar a tarefa1
        return 'explorar'

class Tarefa2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['explorar'])

    def execute(self, userdata):
        # código para executar a tarefa2
        return 'explorar'

class Andar1Segundo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['n90', 'p90'])

    def execute(self, userdata):
        # código para andar 1 segundo
        krakudo.forward()
        if (userdata['inicio'] or userdata['ultimo_return'] == 'p90'):
            return 'n90'
        elif (userdata['ultimo_return'] == 'n90'):
            return 'p90'

class Girar90Neg(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])

    def execute(self, userdata):
        # código para girar -90 graus
        krakudo.left()
        return 'done'

class Girar90Pos(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])

    def execute(self, userdata):
        # código para girar +90 graus
        krakudo.right('90')
        return 'done'

class Girar45Pos(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])

    def execute(self, userdata):
        # código para girar +45 graus
        krakudo.right('45')
        return 'done'

# Criando uma máquina de estados
sm = smach.StateMachine(outcomes=['done'])

# Adicionando os estados à máquina de estados
with sm:
    smach.StateMachine.add('EXPLORAR', Explorar(),
                           transitions={'tarefa1':'TAREFA1', 'tarefa2':'TAREFA2'})
    smach.StateMachine.add('TAREFA1', Tarefa1(),
                           transitions={'explorar':'EXPLORAR'})
    smach.StateMachine.add('TAREFA2', Tarefa2(),
                           transitions={'explorar':'EXPLORAR'})

# Executando a máquina de estados
outcome = sm.execute()
Neste exemplo, o estado Explorar é iniciado primeiro e pode transitar para os estados Tarefa1 ou Tarefa2, dependendo da condição. Os estados Tarefa1 e Tarefa2 podem transitar de volta para o estado Explorar quando completos.
