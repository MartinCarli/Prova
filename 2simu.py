class ExamException(Exception):
    pass

class Diff():
    def __init__(self,ratio=1):

        if  not isinstance (ratio,int) and not isinstance(ratio,float):
            raise ExamException('Il numero deve essere di tipo float o int, got: {}'.format(type(ratio))
        if ratio<=0:
            raise ExamException('ATTENZIONE:  il ratio deve essere maggiore di 0, cambia valore')

        self.ratio=ratio
    def Computer(self,data):
        #alza l ecezione se data e una lista
        #alza un ecezione se data <2
        #alza un ecezione se i valori  di data sono di tipo int o float

        #creo una lista vuota
        #dopo si va lla funzione, non e complicata            