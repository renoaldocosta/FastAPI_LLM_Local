---
noteId: "8e6fb090a82711efa557f9dca5bcd96a"
tags: []

---

# FastAPI_LLM_Local

---

# API de LLMs com FastAPI

Esta é uma API desenvolvida com **FastAPI** que oferece funcionalidades de geração e tradução de texto utilizando modelos de linguagem pré-treinados, como GPT-2 e o modelo de tradução da Helsinki-NLP.

## Índice

- [FastAPI\_LLM\_Local](#fastapi_llm_local)
- [API de LLMs com FastAPI](#api-de-llms-com-fastapi)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
    - [1. Clone o Repositório](#1-clone-o-repositório)
    - [2. Navegue até o Diretório do Projeto](#2-navegue-até-o-diretório-do-projeto)
    - [3. Crie um Ambiente Virtual](#3-crie-um-ambiente-virtual)
    - [4. Instale as Dependências](#4-instale-as-dependências)
  - [Configuração](#configuração)
  - [Executando a Aplicação](#executando-a-aplicação)
  - [Endereços da API](#endereços-da-api)
    - [Geração de Texto com GPT-2](#geração-de-texto-com-gpt-2)
    - [Tradução de Inglês para Francês](#tradução-de-inglês-para-francês)
  - [Exemplos de Uso](#exemplos-de-uso)
    - [Geração de Texto](#geração-de-texto)
    - [Tradução de Texto](#tradução-de-texto)
  - [Documentação Interativa](#documentação-interativa)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Contribuição](#contribuição)

## Visão Geral

Esta API permite aos usuários gerar texto com base em prompts fornecidos e traduzir textos do inglês para o francês. Utiliza modelos avançados de processamento de linguagem natural (NLP) para fornecer respostas eficientes e precisas.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

## Instalação

### 1. Clone o Repositório

Primeiro, clone este repositório para a sua máquina local usando o Git:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Substitua `seu-usuario` e `seu-repositorio` pelo seu nome de usuário e nome do repositório correspondentes.

### 2. Navegue até o Diretório do Projeto

```bash
cd seu-repositorio
```

### 3. Crie um Ambiente Virtual

É recomendado criar um ambiente virtual para gerenciar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **No Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **No macOS e Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

## Configuração

Certifique-se de que o arquivo `requirements.txt` inclua todas as bibliotecas necessárias. Um exemplo de `requirements.txt` para este projeto pode ser:

```
fastapi
uvicorn
transformers
torch
```

Caso necessite de outras dependências, adicione-as ao arquivo `requirements.txt`.

## Executando a Aplicação

Para iniciar a aplicação FastAPI, utilize o seguinte comando:

```bash
uvicorn main:app --reload
```

**Detalhes do Comando:**

- `main`: Refere-se ao arquivo `main.py`.
- `app`: Refere-se à instância da aplicação FastAPI dentro de `main.py`.
- `--reload`: Habilita o recarregamento automático da aplicação sempre que houver alterações no código, útil durante o desenvolvimento.

Após executar o comando, a aplicação estará disponível em `http://127.0.0.1:8000`.

## Endereços da API

A API possui os seguintes endpoints:

### Geração de Texto com GPT-2

- **URL:** `/gpt2/generate_text`
- **Método:** `POST`
- **Descrição:** Gera texto com base em um prompt fornecido utilizando o modelo GPT-2.
- **Parâmetros:**
  - `text` (string): O prompt de texto para gerar a continuação.
- **Resposta:**
  - `text` (string): O texto gerado.

### Tradução de Inglês para Francês

- **URL:** `/gpt2/translate`
- **Método:** `POST`
- **Descrição:** Traduz um texto do inglês para o francês utilizando o modelo Helsinki-NLP.
- **Parâmetros:**
  - `text` (string): O texto em inglês a ser traduzido.
- **Resposta:**
  - `text_translated` (string): O texto traduzido para o francês.

## Exemplos de Uso

### Geração de Texto

**Requisição:**

```bash
POST /gpt2/generate_text
Content-Type: application/json

{
  "text": "Era uma vez em uma terra distante,"
}
```

**Resposta:**

```json
{
  "text": "Era uma vez em uma terra distante, um jovem príncipe que sonhava em explorar o mundo além das montanhas. Ele embarcou em uma jornada épica para descobrir novos horizontes e enfrentar desafios desconhecidos..."
}
```

### Tradução de Texto

**Requisição:**

```bash
POST /gpt2/translate
Content-Type: application/json

{
  "text": "The quick brown fox jumps over the lazy dog."
}
```

**Resposta:**

```json
{
  "text_translated": "A rápida raposa marrom pula sobre o cachorro preguiçoso."
}
```

## Documentação Interativa

FastAPI fornece uma interface de documentação interativa automaticamente gerada. Você pode acessá-la navegando para:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Estas interfaces permitem testar os endpoints diretamente do navegador.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e de alto desempenho para construir APIs com Python.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI rápido e leve para Python.
- **[Transformers](https://huggingface.co/transformers/):** Biblioteca para processamento de linguagem natural com modelos pré-treinados.
- **[Torch](https://pytorch.org/):** Biblioteca para computação científica e aprendizado de máquina.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

1. Fork o projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request



