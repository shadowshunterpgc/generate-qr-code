import segno


def main():
    creating_qrcode("https://www.linkedin.com/in/pablogomezcorrea/")


def creating_qrcode(link):
    video = segno.make(link)
    video.save("profile.png", dark="black")


if __name__ == '__main__':
    main()