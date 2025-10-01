# #########################################
# Programa que utiliza as Classes  
# cPontoCor e cCor
# #########################################

import cPonto
import random

class setor:
    def __init__(self, x, y, largura, altura)
        self.ponto_a = cPonto.cPonto(x, y)
        self.ponto_b = Ponto.cPonto(x + largura, y)   
        self.ponto_c = Ponto.cPonto(x + largura, y + altura)
        self.ponto_d = Ponto.cPonto(x, y + altura)
        self.largura = largura
        self.altura = altura
        self.perimetro = 2 * (largura + altura)
        self.area = largura * altura

    def get_perimetro(self):
        return self.perimetro

    def get_area(self):
        return self.area

    def get_dimensoes(self):
        return (self.largura, self.altura)
    
    def get_localizacao(self):
        return (self.ponto_a, self.ponto_b, self.ponto_c, self.ponto_d)
    
    def ajustar_largura(self, nova_largura):
        self.largura = nova_largura
        self.perimetro = 2 * (self.largura + self.altura)
        self.area = self.largura * self.altura
        self.ponto_b.setX(self.ponto_a.getX() + nova_largura)
        self.ponto_c.setX(self.ponto_a.getX() + nova_largura)

    def ajustar_altura(self, nova_altura):
        self.altura = nova_altura
        self.perimetro = 2 * (self.largura + self.altura)
        self.area = self.largura * self.altura
        self.ponto_c.setY(self.ponto_a.getY() + nova_altura)
        self.ponto_d.setY(self.ponto_a.getY() + nova_altura)

    def ajustar_localizacao_x(self, novo_x):
        self.ponto_a.setX(novo_x)
        self.ponto_b.setX(novo_x + self.largura)
        self.ponto_c.setX(novo_x + self.largura)
        self.ponto_d.setX(novo_x)

    def ajustar_localizacao_y(self, novo_y):
        self.ponto_a.setY(novo_y)
        self.ponto_b.setY(novo_y)
        self.ponto_c.setY(novo_y + self.altura)
        self.ponto_d.setY(novo_y + self.altura)
        
    
    def sobreposicao(self,outro_setor):
        


    

ponto = cPonto.__init__(1.0, 2.0)
print(ponto)
