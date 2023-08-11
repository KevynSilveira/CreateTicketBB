from datetime import date
from datetime import datetime
from decimal import Decimal
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.pdf import BoletoPDF

def gerar_boleto_banco_do_brasil():
    data_vencimento = date.today()  # Data de vencimento
    valor = Decimal('100.00')  # Valor do boleto

    boleto = BoletoBB(7, 2)  # Código do banco e código da moeda
    boleto.nosso_numero = '123456789'  # Seu número único
    boleto.numero_documento = '123456789'  # Número do documento
    boleto.convenio = '1234567'  # Número do convênio
    boleto.carteira = '18'  # Código da carteira
    boleto.agencia_cedente = '1234'  # Sua agência
    boleto.conta_cedente = '56789'  # Sua conta
    boleto.data_vencimento = data_vencimento
    boleto.valor_documento = valor
    boleto.cedente = 'Nome do Cedente'
    boleto.cedente_documento = '123.456.789-00'  # CPF ou CNPJ do cedente
    boleto.cedente_endereco = 'Endereço do Cedente'

    boleto.pagador = 'Nome do Pagador'
    boleto.pagador_documento = '987.654.321-00'  # CPF ou CNPJ do pagador
    boleto.pagador_endereco = 'Endereço do Pagador'

    boleto.instrucoes = [
        'Não receber após o vencimento',
        'Multa de 2% após o vencimento',
        'Juros de mora de 1% ao mês',
        'Cobrar valor adicional em caso de atraso',
        'Em caso de dúvidas, entre em contato conosco'
    ]

    # Definir data_documento como um objeto datetime.date
    boleto.data_documento = datetime.now().date()

    # Criar um objeto BoletoPDF
    pdf = BoletoPDF("Boleto.pdf")

    # Chamar a função drawBoleto para desenhar o boleto no PDF
    pdf.drawBoleto(boleto)

    pdf.save()


# Chamar a função para gerar o boleto
gerar_boleto_banco_do_brasil()
