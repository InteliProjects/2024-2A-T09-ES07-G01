import nltk
import re
import pickle
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError  
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import unittest
import os
import time
import matplotlib.pyplot as plt


nltk.download('stopwords')
nltk.download('punkt')

# Função para extrair texto de um PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para preprocessar o texto
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('portuguese')]
    return ' '.join(tokens)


def carrega_modelo():
    
    # Caminhos dos arquivos
    model_path = '../model/model.pkl'
    vectorizer_path = '../model/vectorizer.pkl'
    mbl_path = '../model/mlb.pkl'

    # Verifica se os arquivos existem
    if not os.path.exists(model_path):
        raise FileNotFoundError(f'File {model_path} not found')

    if not os.path.exists(vectorizer_path):
        raise FileNotFoundError(f'File {vectorizer_path} not found')

    if not os.path.exists(mbl_path):
        raise FileNotFoundError(f'File {mbl_path} not found')


    # Carrega o modelo, vetorizador e classes
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    with open(vectorizer_path, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    with open(mbl_path, 'rb') as mlb_file:
        mlb_classes = pickle.load(mlb_file)

    return model, vectorizer, mlb_classes

# Função para configurar o TestRunner para um teste específico
def run_specific_test(clase_teste, nome_teste=None):
  loader = unittest.TestLoader()
  if nome_teste:
    # Carregar teste específico
    suite = loader.loadTestsFromName(f'{clase_teste.__name__}.{nome_teste}', clase_teste)
  else:
    # Carregar todos os testes da classe
    suite = loader.loadTestsFromTestCase(clase_teste)

  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite)

class TesteExtracaoDeTextoPDF(unittest.TestCase):

    # Configuração inicial
    def setUp(self):
        self.pdf_path = r"../../../data/raw/oc-sep-0522.pdf"
        self.expected_text = """COMISSÃO DE VALORES MOBILIÁRIOS Rua Sete de Setembro, 111/2-5º e 23-34º Andares, Centro, Rio de Janeiro/RJ – CEP: 20050-901 – Brasil - Tel.: (21) 3554-8686 Rua Cincinato Braga, 340/2º, 3º e 4º Andares, Bela Vista, São Paulo/ SP – CEP: 01333-010 – Brasil - Tel.: (11) 2146- 2000 SCN Q.02 – Bl. A – Ed. Corporate Financial Center, S.404/4º Andar, Brasília/DF – CEP: 70712-900 – Brasil -Tel.: (61) 3327-2030/2031 www.cvm.gov.br Ofício Circular nº 5/2022-CVM/SEP Rio de Janeiro, 23 de novembro 2022. Assunto: Relato Integrado - Resolução CVM n° 14/20. Senhor Diretor de Relações com Investidores/Representante Legal, 1 . O presente Ofício Circular tem como objetivo informar às companhias abertas e estrangeiras sobre a criação de uma categoria especíﬁca no Sistema Empresas.NET (E-NET) para envio do Relato Integrado previsto na Resolução CVM n° 14/20. 2 . A Resolução CVM n° 14/20 tornou obrigatória para as companhias abertas, quando da decisão de elaboração e divulgação do Relato Integrado, a Orientação CPC 09 – Relato Integrado, emitida pelo Comitê de Pronunciamentos Contábeis - CPC (Correlação à Estrutura Conceitual Básica do Relato Integrado, elaborada pelo Internacional Integrated Reporting Council - IIRC) e determinou que o Relato Integrado deve ser objeto de asseguração limitada por auditor independente registrado na CVM. 3 . As Companhias vêm utilizando outras categorias já existentes no E-NET para envio do Relato Integrado, como, por exemplo, a categoria "Relatório de Sustentabilidade". 4 . A partir desta data, o Relato Integrado previsto na referida Resolução deverá ser encaminhado por meio da categoria “Relato Integrado”. 5 . Por sua vez, outros relatórios ou documentos especíﬁcos relacionados às questões ASG, podem continuar a ser divulgados como anteriormente. 6 . Importa salientar, ainda, que, no âmbito do Relato Integrado, a companhia deve deixar claro ao usuário da informação (i) que o documento segue a estrutura conceitual prevista na Orientação CPC 09 e (ii) que isso está compreendido no escopo dos trabalhos de asseguração limitada pelo auditor independente registrado na CVM. 7 . Informamos que dúvidas referentes à instalação, utilização e Ofício-Circular 5 (1651789) SEI 19957.014264/2022-93 / pg. 1funcionamento do Sistema Empresas.NET, assim como o relato de problemas ou diﬁculdades no envio de documentos, devem ser encaminhadas para a Superintendência de Emissores da B3. 8 . O contato com a Superintendência de Emissores pode ser feito pelo telefone (11) 2565-5063 ou por e-mail: emissores.empresas@b3.com.br: a ) Atendimento Normal: nos dias úteis, das 8h às 20h, pelo e-mail ou pelo telefone. b ) Plantão de Atendimento: nos dias úteis, após às 20h ou em finais de semana e feriados, exclusivamente por meio do e-mail. 9 . As questões recebidas após às 20h dos dias úteis e em ﬁnais de semana e feriados serão tratadas após às 8h do dia útil seguinte, exceto as relacionadas à disponibilidade do sistema para o recebimento de informações, as quais serão tratadas imediatamente. Atenciosamente, FERNANDO SOARES VIEIRA Superintendente de Relações com Empresas Documento assinado eletronicamente por Fernando Soares Vieira , Superintendente , em 23/11/2022, às 12:37, com fundamento no art. 6º do Decreto nº 8.539, de 8 de outubro de 2015. A autenticidade do documento pode ser conferida no site https://super.cvm.gov.br/conferir_autenticidade , informando o código verificador 1651789 e o código CRC AAF68AC0 . This document's authenticity can be verified by accessing https://super.cvm.gov.br/conferir_autenticidade , and typing the "Código Verificador" 1651789 and the "Código CRC" AAF68AC0 . Referência: Processo nº 19957.014264/2022-93 Documento SEI nº 1651789 Ofício-Circular 5 (1651789) SEI 19957.014264/2022-93 / pg. 2"""
        self.maxDiff = None

    # Função para formatar o texto esperado pelo teste
    def formatar_texto(self, texto):
        texto = re.sub(r'\s+', ' ', texto).strip()  
        return texto

    # Teste para verificar se o texto extraído do PDF corresponde ao esperado
    def teste_extracao_texto_pdf(self):
        try:
            texto_extraido = extract_text_from_pdf(self.pdf_path)
            texto_formatado = self.formatar_texto(texto_extraido)
            texto_esperado_formatado = self.formatar_texto(self.expected_text)

            self.assertEqual(texto_formatado, texto_esperado_formatado, "O texto extraído não corresponde ao esperado.")
        except FileNotFoundError:
            self.fail(f"Arquivo PDF não encontrado: {self.pdf_path}")
        except Exception as e:
            self.fail(f"Erro inesperado durante o teste: {str(e)}")

run_specific_test(TesteExtracaoDeTextoPDF)