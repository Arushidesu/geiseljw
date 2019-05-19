from django.db import models


class Local(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Publicador(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=1)
    local = models.OneToOneField(Local, on_delete=models.SET_NULL, blank=True, null=True)
    superior = models.ForeignKey(Publicador, on_delete=models.CASCADE, related_name='superior')
    assistente = models.ForeignKey(Publicador, on_delete=models.CASCADE, related_name='assistente')
    publicadores = models.ManyToManyField(Publicador, related_name='publicadores')

    def __str__(self):
        return self.nome


class Limpeza(models.Model):
    dia = models.DateField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Dia: {self.dia}\nGrupo: {self.grupo}'


class Indicador(models.Model):
    dia = models.DateField()
    indicador1 = models.ForeignKey(Publicador, on_delete=models.CASCADE, related_name='indicador1')
    indicador2 = models.ForeignKey(Publicador, on_delete=models.CASCADE, related_name='indicador2')

    def __str__(self):
        return f'Dia: {self.dia}\nIndicadores: {self.indicador1} e {self.indicador2}'

class Congregacao(models.Model):
    DIA_ESCOLHA = (
        ('0', 'Domingo'),
        ('1', 'Segunda'),
        ('2', 'Terça'),
        ('3', 'Quarta'),
        ('4', 'Quinta'),
        ('5', 'Sexta'),
        ('6', 'Sábado'),
    )

    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    dia_meio = models.CharField(max_length=1, choices=DIA_ESCOLHA)
    hora_meio = models.TimeField()
    dia_fim = models.CharField(max_length=1, choices=DIA_ESCOLHA)
    hora_fim = models.TimeField()

    def __str__(self):
        return self.nome


class ConferenciaPublica(models.Model):
    dia = models.DateField()
    orador = models.ForeignKey(Publicador, on_delete=models.CASCADE)
    esboco = models.CharField(max_length=3)
    congregacao = models.ForeignKey(Congregacao, on_delete=models.CASCADE)
    horario = models.TimeField()

    def __str__(self):
        return f'Dia e hora: {self.dia} às {self.horario}\nOrador: {self.orador}\nEsboço: {self.esboco}\nCongregação: {self.congregacao}'


class ConferenciaOutra(models.Model):
    dia = models.DateField()
    titulo = models.CharField(max_length=80)
    orador = models.CharField(max_length=40)
    Congregacao = models.ForeignKey(Congregacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Campo(models.Model):
    DIA_ESCOLHA = (
        ('0', 'Domingo'),
        ('1', 'Segunda'),
        ('2', 'Terça'),
        ('3', 'Quarta'),
        ('4', 'Quinta'),
        ('5', 'Sexta'),
        ('6', 'Sábado'),
    )

    dia = models.CharField(max_length=1, choices=DIA_ESCOLHA)
    hora = models.TimeField()
    dirigente = models.ForeignKey(Publicador, on_delete=models.SET_NULL, blank=True, null=True)
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Dia e hora: {self.dia} às {self.hora}\nDirigente: {self.dirigente}\nLocal: {self.local}'
