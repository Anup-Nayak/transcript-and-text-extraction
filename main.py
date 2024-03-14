import assemblyai as aai
import PyPDF2
import time
# from pikepdf import Pdf,Name, PdfImage
# import fitz
# import os
# from PIL import Image
# from pytesseract import pytesseract

def transcribeAV(av, file_name):
    aai.settings.api_key = "ccfbc0fa60344b068ec8629016103a87"
    transcriber = aai.Transcriber()
    if av == "video":
        transcript = transcriber.transcribe(file_name)
    else:
        transcript = transcriber.transcribe(file_name)

    formatted_transcript = ".\n".join(transcript.text.split(". "))

    with open('transcript.txt', "w") as output_file:
            output_file.write(formatted_transcript)

    print(f"Transcript written to transcript.txt")
    output_file.close()
    # print(transcript.text)

def extractPdf(file_name):
    with open(file_name,'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf,strict = False)
        pdf_text = []
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
               
    with open('transcript.txt', "w") as output_file:
        for text in pdf_text:
            formatted_transcript = ".\n".join(text.split(". "))

            output_file.write(formatted_transcript)

    print(f"Transcript written to transcript.txt")
    output_file.close()
    
    # pdf_file = fitz.open(file_name) 
    
    # if not os.path.exists("images"):
    #     os.makedirs("images")

    
    # for page_index in range(len(pdf_file)): 
    #     page = pdf_file[page_index]
    
    #     for img_index, img in enumerate(page.get_images()):
    #         xref = img[0] 
    
    #         # extract the image bytes 
    #         base_image = pdf_file.extract_image(xref)
    #         image_name = os.path.join("images", f"{img_index + 1}.png")
    #         with open(image_name, "wb") as fp:
    #                 fp.write(base_image["image"])
            
            
if __name__ == "__main__":
    
    file_type = int(input("1 for video, 2 for audio, 3 for pdf: "))
    file_name = input("Enter the file name you want to transcribe: ")
    
    stime = time.time()
    if file_type == 1 :
        transcribeAV("video",file_name)
    elif file_type == 2:
        transcribeAV("audio",file_name)
    else:
        extractPdf(file_name)
    etime = time.time()
    
    time = etime-stime
    print(time)