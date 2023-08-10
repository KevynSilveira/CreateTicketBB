from datetime import date
from pyboleto.bank.bank_brasil import BoletoBB

def criar_boleto():
    d = BoletoBB()

    d.nosso_numero = '0000000001'
    d.numero_documento = '27.030195.10'

    d.data_vencimento = date(2023, 8, 15)
    d.data_documento = date(2023, 8, 10)
    d.data_processamento = date(2023, 8, 10)

    d.valor_documento = 250.50
    d.agencia_cedente = '00000'
    d.conta_cedente = '0000000'
    d.convenio = '1234567'

    d.carteira = '18'
    d.variacao_carteira = '019'

    d.cedente = 'Empresa Exemplo'
    d.cedente_documento = '12.345.678/0001-90'
    d.cedente_endereco = 'Rua Exemplo, 123 - Centro'
    d.cedente_uf = 'UF'
    d.cedente_cep = '12345-678'
    d.agencia_cedente_dv = '0'
    d.conta_cedente_dv = '0'

    d.sacado = 'Cliente Exemplo'
    d.sacado_documento = '123.456.789-01'
    d.sacado_endereco = 'Rua Cliente, 456 - Bairro'
    d.sacado_uf = 'Outra UF'
    d.sacado_cep = '98765-432'

    d.instrucoes = [
        "Sr. Caixa, não receber após o vencimento.",
        "Em caso de dúvidas, entre em contato conosco: telefone@example.com",
    ]

    pdf_filename = 'boleto_banco_do_brasil.pdf'
    d.save(pdf_filename)
    print(f"Boleto gerado e salvo como '{pdf_filename}'.")

# Chamando a função para gerar o boleto
criar_boleto()
