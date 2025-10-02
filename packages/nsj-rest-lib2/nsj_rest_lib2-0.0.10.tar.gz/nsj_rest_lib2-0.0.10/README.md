# nsj_rest_lib2

Biblioteca para permitir a distribuição de rotas dinâmicas numa API, configuradas por meio de EDLs declarativos (em formato JSON).

## TODO
* Colocar tempo para recarregamento das entidades (para checar, no redis, se mudou o hash.)
* Unificar o arquivo redis_config.py
* Usar pydantic, ou similar, para transformar a configuração das entidades, no redis, num objeto
* Rever modo de usar o InjectFactory (talvez dando ciência, ao RestLib, do padrão multibanco)