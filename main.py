from datetime import date
from datetime import datetime
from decimal import Decimal
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.pdf import BoletoPDF

def gerar_boleto_banco_do_brasil():
    data_vencimento = date.today()  # Data de vencimento
    valor = Decimal('1000.00')  # Valor do boleto

    boleto = BoletoBB(7, 2)  # Código do banco e código da moeda
    boleto.nosso_numero = '123456789'  # Seu número único
    boleto.numero_documento = '987654321'  # Número do documento
    boleto.convenio = '1234567'  # Número do convênio
    boleto.carteira = '18'  # Código da carteira
    boleto.agencia_cedente = '1234'  # Sua agência
    boleto.conta_cedente = '56789'  # Sua conta
    boleto.data_vencimento = data_vencimento
    boleto.valor_documento = valor
    boleto.cedente = 'Kevyn da Silveira de Fraga Martins'
    boleto.cedente_documento = '123.456.789-00'  # CPF ou CNPJ do cedente
    boleto.cedente_endereco = 'Endereço do Cedente'



    boleto.pagador = 'Nome do Pagador'
    boleto.pagador_documento = '987.654.321-00'  # CPF ou CNPJ do pagador
    boleto.pagador_endereco = 'Endereço do Pagador'

    boleto.instrucoes = [
        'Instrução 1: Não receber após o vencimento',
        'Instrução 2: Multa de 2% após o vencimento',
        'Instrução 3: Juros de mora de 1% ao mês',
        'Instrução 4: Cobrar valor adicional em caso de atraso',
        'Instrução 5: Em caso de dúvidas, entre em contato conosco'
    ]

    # Definir data_documento como um objeto datetime.date
    boleto.data_documento = date.today()

    # Definir mais informações do pagador
    boleto.pagador_telefone = '(12) 3456-7890'
    boleto.pagador_email = 'pagador@example.com'

    # Outras informações do cedente
    boleto.cedente_telefone = '(34) 5678-9012'
    boleto.cedente_email = 'cedente@example.com'
    boleto.cedente_endereco = "Neosul/palhoça"

    # Outros campos opcionais
    boleto.valor_cobrado = Decimal('1050.00')  # Valor total cobrado (incluindo multa e juros)
    boleto.percentual_multa = Decimal('2.00')  # Percentual de multa
    boleto.percentual_juros = Decimal('1.00')  # Percentual de juros ao mês

    # Criar um objeto BoletoPDF
    pdf = BoletoPDF("Boleto.pdf")

    # Chamar a função drawBoleto para desenhar o boleto no PDF
    pdf.drawBoleto(boleto)

    pdf.save()


# Chamar a função para gerar o boleto
gerar_boleto_banco_do_brasil()
