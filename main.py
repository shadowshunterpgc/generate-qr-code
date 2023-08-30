import segno
from segno import helpers

from usuario import Usuario


def main():
    usuario = Usuario()
    usuario.setNome("Pablo")
    usuario.setLink("https://www.linkedin.com/in/pablogomezcorrea")
    usuario.setEmail("pablogomezcorrea@gmail.com")
    creating_qrcode(usuario)


def creating_qrcode(usuario):
    qr = helpers.make_mecard(name=usuario.nome, email=usuario.email, url=usuario.link)
    qr.save("profile.png", dark="black", scale=10)


if __name__ == '__main__':
    main()
