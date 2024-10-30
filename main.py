import os
import img2pdf

ALLOWED_IMAGE_EXTENSIONS = ("png", "jpg", "jpeg")

if __name__ == "__main__":
    images_path = input("Type images path: ")
    images_path = images_path.replace('"', "").replace("'", "")

    extension = input(f"Type extension {ALLOWED_IMAGE_EXTENSIONS}: ").lower()

    if os.path.exists(images_path):
        if extension in ALLOWED_IMAGE_EXTENSIONS:
            image_files = [
                os.path.join(images_path, i)
                for i in os.listdir(images_path)
                if i.lower().endswith(f".{extension}")
            ]

            if not image_files:
                print("Nenhuma imagem encontrada!")
            else:
                output_pdf_path = os.path.join(images_path, "output.pdf")
                with open(output_pdf_path, "wb") as f:
                    f.write(img2pdf.convert(image_files))
                print(
                    f"PDF gerado com sucesso! O arquivo foi salvo em: {output_pdf_path}"
                )
        else:
            print("Extensão inválida! Selecione uma das opções aceitas.")
    else:
        print("O caminho informado não existe!")
