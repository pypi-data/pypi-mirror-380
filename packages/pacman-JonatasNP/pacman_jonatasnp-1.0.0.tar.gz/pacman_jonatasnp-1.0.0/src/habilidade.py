import constantes
import time
from spritebase import SpriteBase

#PARA AS POSSÍVEIS PRÓXIMAS VERSÕES
class Habilidade(SpriteBase):
    def __init__(self, nome, cooldown, duracao=None):
        self.nome = nome
        self.image = constantes.SKILL_IMAGE.get(nome)
        self.cooldown = cooldown
        self.duracao = duracao
        self.ultimo_uso = 0
        self.ativa_ate = 0


    def pode_ativar(self):
        return time.time() - self.ultimo_uso >= self.cooldown


    def ativar(self):
        if self.pode_ativar():
            self.ultimo_uso = time.time()
            if self.duracao:
                self.ativa_ate = self.ultimo_uso + self.duracao
            return True
        return False


    def ta_ativa(self):
        return self.duracao is not None and time.time() < self.ativa_ate

