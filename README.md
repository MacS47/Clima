# Clima ☀🌙

<div style="display:flex; flex-wrap:wrap">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat" alt="License Shield" style="padding:2px">
  <img src="https://img.shields.io/badge/python-v.310-blue?style=flat&logo=" alt="Language and version" style="padding:2px">
</div>

## 🎯 Propósito

O objetivo desse projeto foi desenvolver um aplicação capaz de obter dados climáticos em tempo real, toda vez que o usuário desejar.

## 🧠 Experiência/Motivação

Conheci a API da [OpenWeather]("https://openweathermap.org/" "OpenWeather") por meio de um curso de JavaScript. Em meio a dias quentes de verão... e pensando em como cruzar o que havia aprendido em JS e o Python, me desafiei a criar uma aplicação de desktop que utilizasse o módulo [Tkinter]("https://docs.python.org/3/library/tkinter.html" "Link para documentação do módulo Python Tkinter") para exibir a temperatura da região onde moro.

### Status

O projeto está concluído. _Até o momento..._


## ✍ Como começar

Antes de começar de fato,  garanta que os módulos `requests` e `tkinter` estão instalados na sua máquina. Além disso é preciso abrir o arquivo `info.py` e informar uma credencial válida para utilizar a API da [OpenWeather]("https://openweathermap.org/" "OpenWeather"). É possível gerar uma chave, ao realizar cadastro no site da companhia, sendo que há um plano gratuito com limite de chamadas à API.

<div align="center">
    <img src="screenshots/001.png" alt="Imagem detalhando local a ser informada a credencial." style="display: block; margin-left: auto; margin-right: auto; border-radius: 15px"><br>
</div>

Após informar a sua chave, basta executar o arquivo `main.py`. Se tudo correr conforme esperado, a seguinte janela abaixo será exibida:

<div align="center">
    <img src="screenshots/002.png" alt="Imagem da janela da aplicação Clima, exibindo a temperatura" style="display: block; margin-left: auto; margin-right: auto; border-radius: 15px"><br>

O projeto ainda conta com o botão atualizar, para buscar os dados recentes.

</div>

Lembre-se que a região exibida pode ser alterada. Para isso vá até o arquivo `main.py` e altere o valor da variável `city`:

<div align="center">
    <img src="screenshots/003.png" alt="Imagem da janela da aplicação Clima, exibindo a temperatura" style="display: block; margin-left: auto; margin-right: auto; border-radius: 15px"><br>
</div>

