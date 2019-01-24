class Neurônio(object):

    def __init__(self, entrada):
        self.entrada = entrada;
        self.peso = [0.8, -0.5];

    def somatório(self):
        s = 0;
        for k,c in enumerate(self.entrada):
            s += (c * self.peso[k]);
        return s;

    def funçãoDeAtivação(self, valor):
        if valor < 0:
            return 0;
        else:
            return 1;

    def atualizaPeso(self, tx, e):
        for k, p in enumerate(self.peso):
            self.peso[k] = p + (tx * e * self.entrada[k]);



