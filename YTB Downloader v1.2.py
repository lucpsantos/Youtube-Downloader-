import yt_dlp

def baixar_video(url): 
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', #melhor qualidade e melhor audio setado
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True #baixar apenas o video do link, ignorando se é playlist ou mix
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


print("=== Youtube Downloader ===")

nome = input("Digite seu nome: ")

while True:
    print(f"\nOlá {nome}! Como posso te ajudar hoje?")
    print("1 - Download do video")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo...")
        break

    elif opcao == "1":
        url = input("Insira o link do video que deseja baixar: ").strip()

        if "&" in url:
            url = url.split("&")[0]

        baixar_video(url)

    else: 
        print("Opção inválida.")
        #volta o loop
