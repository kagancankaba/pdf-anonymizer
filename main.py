import re
import spacy
import pypdf
from pypdf import PdfReader, PdfWriter

# spaCy'nin İngilizce dil modeli yükleniyor
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """PDF dosyasından metni çıkartır"""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def anonymize_text(text):
    """Metindeki özel isimleri (kişiler, organizasyonlar) anonimleştirir"""
    doc = nlp(text)
    anonymized_text = text
    
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE"]:  # Kişi, organizasyon ve yer isimleri
            anonymized_text = re.sub(rf'\b{re.escape(ent.text)}\b', '****', anonymized_text)

    return anonymized_text

def write_anonymized_pdf(input_pdf, output_pdf):
    """Anonimleştirilmiş metinle yeni PDF oluşturur"""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            anon_text = anonymize_text(text)
            writer.add_page(page)  # Orijinal sayfayı ekle
            writer.pages[-1].annotations = None  # Ek açıklamaları temizle (güvenlik için)
        else:
            writer.add_page(page)  # Eğer metin yoksa sayfayı olduğu gibi ekle

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Kullanım örneği
input_pdf_path = "makale.pdf"  # Orijinal PDF dosyan
output_pdf_path = "anonim_makale.pdf"  # Çıktı PDF dosyan

write_anonymized_pdf(input_pdf_path, output_pdf_path)
print(f"Anonimleştirilmiş PDF oluşturuldu: {output_pdf_path}")
