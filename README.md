﻿# Computador Dual core


Trabalho realizado para melhor entendimento do funcionamento de threds e processos.

Há um processador com 2 núcleos e 7 processos a serem executados. Todos os processos tem mesma prioridade e basta haver um núcleo livre para que execute. Ao término de uma execução, os outros processos em espera são avisados e podem utilizar o núcleo vago. Cada processo leva uma quantidade de tempo X para executar por completo e o processador possui um quantum Q, que é o tempo que cada processo pode utilizar o processador. A cada execução do programa, é subtraído deseu tempo total de execução o valor do quantum e, caso o tempo restante para execução seja menor que esse quantum, o processo executa apenas pelo tempo que lhe resta.Desenvolva um programa que utilize threads para simular o comportamento desse sistema. O seu programa deve encerrar quando todos os processos terminarem suas execuções por completo e imprimir na tela o tempo que cada processo passou em espera e e também o tempo que cada núcleo passou
processando, ambos em ms. A entrada consistirá de um inteiro X que representará o quantum (em ms), seguido de 7 inteiros que serão os tempos de execução relativos a cada processo (também em ms). Ao executar em determinado núcleo, o processo deve imprimir na tela “Processo P executando no núcleo N” e permanecer no processador durante o seu tempo de execução.
