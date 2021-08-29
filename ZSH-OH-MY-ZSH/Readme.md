## Pasos para instalar Oh My ZSH

1. Instalar ZSH y git-core

```bash
sudo apt install zsh
sudo apt install git-core
```

2. Descargar el instalador de Oh My ZSH y ejecutarlo 

```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
```

3. Cambiar el shell a ZSH

```bash
chsh -s `which zsh`
```

4. Reiniciar consola

## Usar plugin

Oh My Zsh viene con un montón de complementos para que los aproveches. Puedes echar un vistazo [aquí](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins)

**habilitación de complementos**  

Ir al archivo **.zshrc**. Encontrará este archivo en su directorio $HOME. Lo abrimos con el editor de preferencia de la siguiente manera:  

```bash
nano ~/.zshrc
```

Buscamos la lista donde se enumeran los plugin habilitados se verá algo así(Estos son mis plugin yo tengo configurado), posiblemente solo tendrás git:

```bash
73. plugins=(
      git
      themes
      python
)
```
Tenga en cuenta que los plugin están separados por espacios en blanco pueden ser espacios, tabulaciones, nuevas líneas. *No use comas entre ellos o se rompera*.


**themes**

Este plugin me gusta porque te permite cambiar el tema de ZSH sobre la marcha.  

**USO**

Cambia a un tema específico.
```bash
theme <theme_name>
```

Cabia a un tema aleatorio
```bash
theme 
```

Lista de temas ZSH instalados.  
```bash
lstheme 
```


**python**

Este plugin agrega varios alias para comandos útiles de Python

**Alias**

|Comando|Descripción|
|-------|-----------|
|pyfind|Busca archivos .py en el directorio actual de manera recursiva|
|pygrep <texto\>| Busca el argumento <texto\> en archivos .py|


