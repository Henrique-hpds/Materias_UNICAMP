class Ponto:
    
    def __init__(self, x:float, y:float, ddp:float) -> None:
        self.coordenada = {"x": x, "y": y}
        self.ddp = ddp
    
    @property
    def ddp(self) -> float:
        return self._ddp
    
    @ddp.setter
    def ddp(self, ddp:float) -> None:
        if -100 < ddp < 100:
            self._ddp = ddp
        else:
            raise ValueError("ddp inválida!")
        
    @property
    def coordenada(self) -> dict:
        return self._coordenada
    
    @coordenada.setter
    def coordenada(self, coord):
        if isinstance(coord, list):
            self._coordenada = {"x": coord[0], "y": coord[1]} 
        else:
            self._coordenada = coord
    
    def printar(self) -> None:
        print("[", self.coordenada["x"], ",", self.coordenada["y"], "] -> ", self.ddp, "V")
    
    
# o ponto possui um dicionário com as coordenadas x e y, além de uma ddp associada a elas

def printar_pontos(pontos:list) -> None:
    for atual in pontos:
        atual.printar()