# WHATSAPP BUSINESS API

## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/WHATSAPP-BUSINESS-API.git
```

### Variables de entorno

Al interior de la carpeta /Sripts debes crear un documento env.env el cual debe contener las siguiente variables:

```
PHONE_ID=
WSP_BUSINESS=
ACCESS_TOKEN=
```

### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
docker compose build
```

## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
docker compose run --rm scripts sh -c "python test.py"
```
