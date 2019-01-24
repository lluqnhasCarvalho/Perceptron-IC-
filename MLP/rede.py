from MLP.neurônio import Neurônio;

class MLP(object):

    def __init__(self,base, desejadas):
        self.base = base
        self.desejadas = desejadas;
        self.taxa = 0.5;
        self.neuronio = None;

    def erro(self, i, e):
        return self.desejadas[i] - e;

    def treinamento(self):
        self.neuronio = Neurônio(self.base[0]);
        i=0;
        cont = 4;

        while True:
            y = self.neuronio.funçãoDeAtivação(self.neuronio.somatório());
            e = self.erro(i,y);
            i += 1;

            if i == 4:
                i = 0;


            if e != 0:
                self.neuronio.atualizaPeso(self.taxa, e);
                cont = 4;
            else:
                cont -= 1;

            if cont != 0:
                self.neuronio.entrada = self.base[i];
            else:
                break;

    def testeRede(self, entrada):
        self.neuronio.entrada = entrada;
        y = self.neuronio.funçãoDeAtivação(self.neuronio.somatório());
        print(f'A saída para a entrada inserida é {y}');