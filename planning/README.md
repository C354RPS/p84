# LiteLLM

O LiteLLM é uma aplicação que funciona como um proxy para modelos de LLM, de *embeddings* e de geração de imagens, permitindo o acesso através de uma API padronizada. Assim, independentemente do provedor do modelo (OpenAI, AWS, etc.), o formato das mensagens é o mesmo.

O uso do LiteLLM é opcional para a maioria das APIs, e o acesso direto aos modelos através das APIs independentes continua disponível no Hub de Modelos. Uma exceção é o acesso aos modelos de geração de imagem, que no momento só pode ser feito através do LiteLLM.

Nem todos os modelos disponíveis no Hub estão disponíveis no LiteLLM. Consulte a lista abaixo.

Este diretório contém um exemplo de uso de modelos através do LiteLLM. O acesso requer uma chave de API para o produto `modelos-ia-texto`. Caso não possua, [siga as instruções aqui](../../README.md).

## Modelos disponíveis no LiteLLM

Para acessar estes modelos através do LiteLLM, confira o [exemplo](./exemplo_litellm.ipynb). Você também pode acessá-los diretamente, através das APIs Azure OpenAI e AWS Bedrock. [Confira mais informações aqui](../../).

### LLM:

* claude-instant-v1
* claude-v2
* claude-v2.1
* claude-v3-haiku
* claude-v3-sonnet
* claude-v35-sonnet
* command-light-v14
* command-r
* command-r-plus
* command-v14
* gpt-35-turbo-16k
* gpt-4o
* gpt-4o-mini
* llama3-70b-instruct
* llama3-8b-instruct
* llama3-1-8b-instruct-v1
* llama3-1-70b-instruct-v1
* llama3-1-405b-instruct-v1
* mistral-7b-instruct
* mistral-large
* mistral-small
* mixtral-8x7b-instruct

### Embeddings

* text-embedding-3-large
* text-embedding-3-small
* embedding-amazon-titan-image-v1
* embedding-amazon-titan-v2
* embedding-cohere-english-v3
* embedding-cohere-multilingual-v3
* embedding-openai-ada-002

### Geração de imagens

* stable-diffusion-xl-v1
* dall-e-3
