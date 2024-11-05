import logging
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.parse
import requests
from typing import List, Optional, Tuple
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# Configuração do logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


selectors = {
    'no_results': '/html/body/section/div[4]/div/section/section/form/div/span',
    'total_results': '//div[@class="col-sm-6 no-padding"]/span',
    'max_items_dropdown': '//*[@id="itensPagina_chosen"]/a',
    'max_items_option': '//*[@id="itensPagina_chosen"]/div/ul/li[text()="50"]',
    'article_link': './/h3/a'
}


def get_total_results(driver: webdriver.Chrome) -> int:
    """Obtém o número total de resultados encontrados na página."""
    try:
        no_results_element = driver.find_element(
            By.XPATH, selectors['no_results'])
        if no_results_element and "Nenhum resultado encontrado" in no_results_element.text:
            logging.info("Nenhum resultado encontrado na pesquisa.")
            return 0

        total_results_text = driver.find_element(
            By.XPATH, selectors['total_results']).text
        total_results = int(total_results_text.split()[0])
        logging.info(
            "Número total de resultados encontrados: %s", total_results)
        return total_results
    except Exception as e:
        logging.error("Erro ao obter o número total de resultados: %s", e)
        return 0


def setup_driver(download_dir: str) -> webdriver.Chrome:
    """Configura o driver do Selenium com diretório de download."""
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=3')
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def send_email_notification(downloaded_files: List[Tuple[str, str]], start_date: str, end_date: str):
    """Envia um e-mail notificando sobre os documentos encontrados e baixados."""

    # Configurações de e-mail
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = 587
    smtp_user = sender_email
    smtp_password = os.getenv("EMAIL_PASSWORD")

    # Criação da mensagem
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Documentos CVM encontrados de {
        start_date} a {end_date}"

    # Corpo do e-mail
    body = f"Documentos foram encontrados e baixados para o período de {
        start_date} a {end_date}.\n\n"
    body += "Arquivos baixados e links correspondentes:\n"
    for file_path, pdf_link in downloaded_files:
        body += f"{os.path.basename(file_path)}: {pdf_link}\n"

    message.attach(MIMEText(body, "plain"))

    # Envio do e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Segurança (TLS)
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            logging.info("E-mail de notificação enviado com sucesso.")
    except Exception as e:
        logging.error("Erro ao enviar e-mail de notificação: %s", e)


def select_max_items_per_page(driver: webdriver.Chrome, max_attempts: int = 5) -> None:
    """Tenta expandir o dropdown personalizado e selecionar o valor máximo de itens por página (50) até ter sucesso."""
    attempts = 0
    while attempts < max_attempts:
        try:
            wait = WebDriverWait(driver, 10)
            dropdown = wait.until(EC.element_to_be_clickable(
                (By.XPATH, selectors['max_items_dropdown'])))
            current_value = dropdown.find_element(By.TAG_NAME, 'span').text
            if current_value == "50":
                logging.info(
                    "O valor máximo de itens por página já está selecionado: 50")
                return

            dropdown.click()
            logging.info("Dropdown expandido.")

            option_50 = wait.until(EC.element_to_be_clickable(
                (By.XPATH, selectors['max_items_option'])))
            option_50.click()
            logging.info("Selecionado o máximo de itens por página: 50")
            return
        except Exception as e:
            attempts += 1
            logging.error(
                "Erro ao tentar selecionar o número máximo de itens por página (tentativa %s/%s): %s", attempts, max_attempts, e)
            time.sleep(2)

    logging.error(
        "Falha ao selecionar o número máximo de itens por página após várias tentativas.")
    driver.quit()
    raise ValueError(
        "Não foi possível selecionar o número máximo de itens por página.")


def generate_url(start_date: datetime, end_date: datetime) -> str:
    """Gera a URL com os parâmetros de data e categorias."""
    base_url = "https://conteudo.cvm.gov.br/legislacao/index.html?"
    params = {
        "numero": "",
        "lastNameShow": "",
        "lastName": "",
        "filtro": "todos",
        "dataInicio": start_date.strftime('%d/%m/%Y'),
        "dataFim": end_date.strftime('%d/%m/%Y'),
        "categoria0": "/legislacao/instrucoes/",
        "categoria1": "/legislacao/pareceres-orientacao/",
        "categoria2": "/legislacao/deliberacoes/",
        "categoria3": "/legislacao/decisoesconjuntas/",
        "categoria4": "/legislacao/oficios-circulares/",
        "categoria5": "/legislacao/leis-decretos/",
        "categoria6": "/legislacao/notas-explicativas/",
        "buscado": "false",
        "contCategoriasCheck": "7"
    }
    return base_url + "&".join([f"{key}={value}" for key, value in params.items()])


def get_pdf_link(article_link: str) -> Optional[List[str]]:
    """Converte o link do artigo no link direto para o PDF, tentando múltiplas opções."""
    parsed_url = urllib.parse.urlparse(article_link)
    path_parts = parsed_url.path.split('/')
    category = path_parts[2]
    subfolder = path_parts[3]
    filename = path_parts[4].replace('.html', '')

    pdf_links = []

    if category == 'oficios-circulares':
        if "snc-sep" in subfolder:
            pdf_filename = filename.replace('_', '')
            pdf_links.append(f"https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/{
                             category}/{subfolder}/anexos/{pdf_filename}.pdf")
        elif "sse1" in subfolder:
            pdf_links.append(f"https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/{
                             category}/{subfolder}/anexos/{filename}-.pdf")
            pdf_links.append(f"https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/{
                             category}/{subfolder}/anexos/oc-sse-{filename[-4:]}.pdf")
        else:
            pdf_links.append(f"https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/{
                             category}/{subfolder}/anexos/{filename}.pdf")
    elif category == 'deliberacoes':
        subfolder_num = subfolder[4:]
        pdf_links.append(f"https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/{
                         category}/anexos/{subfolder_num}/{filename}.pdf")
    else:
        logging.error("Categoria %s não reconhecida para o link: %s",
                      category, article_link)
        return None

    return pdf_links


def download_pdf(pdf_urls: List[str], save_path: str, downloaded_files: List[Tuple[str, str]], failed_files: List[str]) -> None:
    """Faz o download do PDF e salva no caminho especificado."""
    for pdf_url in pdf_urls:
        try:
            response = requests.get(pdf_url, timeout=10)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                file.write(response.content)
            logging.info(
                "PDF baixado e salvo em: %s usando o link: %s", save_path, pdf_url)
            # Armazena o caminho e o link
            downloaded_files.append((save_path, pdf_url))
            return
        except requests.exceptions.HTTPError as http_err:
            logging.error(
                "Erro HTTP ao baixar o PDF: %s - Link tentado: %s", http_err, pdf_url)
        except Exception as e:
            logging.error("Erro ao baixar o PDF: %s", e)

    failed_files.append(pdf_urls[0])


def click_and_download_pdfs(driver: webdriver.Chrome, download_dir: str) -> List[Tuple[str, str]]:
    """Encontra os artigos, gera o link do PDF e faz o download."""
    downloaded_files = []
    failed_files = []

    try:
        total_results = get_total_results(driver)
        if total_results == 0:
            logging.info("Nenhum documento disponível para download.")
            return downloaded_files

        select_max_items_per_page(driver)

        processed_results = 0

        while processed_results < total_results and processed_results < 50:
            articles = driver.find_elements(By.TAG_NAME, 'article')

            if not articles:
                logging.info("Nenhum artigo encontrado para processar.")
                break

            for article in articles:
                attempts = 0
                max_attempts = 2  # Número máximo de tentativas para lidar com stale element
                while attempts < max_attempts:
                    try:
                        link = article.find_element(
                            By.XPATH, selectors['article_link'])
                        article_url = link.get_attribute('href')
                        logging.info("Processando artigo: %s", article_url)

                        pdf_links = get_pdf_link(article_url)
                        if not pdf_links:
                            failed_files.append(article_url)
                            break

                        logging.info("Links de PDF gerados: %s", pdf_links)
                        pdf_filename = os.path.basename(pdf_links[0])
                        save_path = os.path.join(download_dir, pdf_filename)

                        driver.get(pdf_links[0])
                        time.sleep(2)

                        download_pdf(pdf_links, save_path,
                                     downloaded_files, failed_files)

                        driver.back()
                        time.sleep(2)

                        processed_results += 1

                        if processed_results >= total_results or processed_results >= 50:
                            logging.info(
                                "Número máximo de resultados processados ou limite atingido.")
                            break
                        else:
                            break

                    except Exception as article_exception:
                        attempts += 1
                        logging.error(
                            "Erro ao processar artigo na tentativa %s: %s", attempts, article_exception)
                        time.sleep(2)

                        if "stale element reference" in str(article_exception).lower():
                            articles = driver.find_elements(
                                By.TAG_NAME, 'article')
                        else:
                            failed_files.append(article_url)
                            break

    except Exception as e:
        logging.error("Erro ao encontrar artigos: %s", e)

    retry_failed_downloads(failed_files, download_dir, downloaded_files)

    success_files = set(downloaded_files)
    logging.info("Total de arquivos baixados com sucesso: %s",
                 len(success_files))
    logging.info("Total de arquivos com falha no download: %s",
                 len(failed_files))
    logging.info("Arquivos baixados:")
    for file_path, pdf_link in downloaded_files:
        logging.info(f"{file_path}: {pdf_link}")
    logging.info("Arquivos que falharam:")
    for file in failed_files:
        logging.info(file)

    return downloaded_files


def retry_failed_downloads(failed_files: List[str], download_dir: str, downloaded_files: List[Tuple[str, str]]) -> List[str]:
    """Tenta novamente baixar os PDFs diretamente usando as URLs dos artigos que falharam."""
    logging.info("Tentando baixar novamente os arquivos que falharam...")
    still_failed_files = []

    for article_url in failed_files:
        if "export/sites" in article_url:
            logging.error("URL incorreta para retry: %s", article_url)
            still_failed_files.append(article_url)
            continue

        pdf_links = get_pdf_link(article_url)
        if not pdf_links:
            logging.error(
                "Não foi possível gerar o link do PDF para: %s", article_url)
            still_failed_files.append(article_url)
            continue

        pdf_filename = os.path.basename(pdf_links[0])
        save_path = os.path.join(download_dir, pdf_filename)
        download_pdf(pdf_links, save_path,
                     downloaded_files, still_failed_files)

    logging.info("Total de arquivos que ainda falharam após o retry: %s", len(
        still_failed_files))
    for file in still_failed_files:
        logging.info(file)

    return still_failed_files


def main() -> None:
    """Função principal para executar o script de web scraping."""
    download_dir = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    driver = setup_driver(download_dir)

    try:
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() - timedelta(days=1)

        logging.info("Data de início: %s", start_date.strftime('%d/%m/%Y'))
        logging.info("Data final: %s", end_date.strftime('%d/%m/%Y'))

        url = generate_url(start_date, end_date)
        logging.info("Acessando URL: %s", url)

        driver.get(url)
        logging.info("Página da CVM acessada com parâmetros.")

        downloaded_files = click_and_download_pdfs(driver, download_dir)

        if downloaded_files:
            send_email_notification(downloaded_files, start_date.strftime(
                '%d/%m/%Y'), end_date.strftime('%d/%m/%Y'))

    finally:
        driver.quit()
        logging.info("Driver encerrado.")


if __name__ == "__main__":
    main()
