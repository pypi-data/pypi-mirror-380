# Changelog

Todas as mudanças notáveis neste projeto serão documentadas aqui.  
O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)  
e este projeto adere a [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

# Changelog

Todo o histórico de mudanças notáveis neste projeto será documentado neste ficheiro.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2025-10-01

### Added
- **Módulo de Dicionários (`dicts.py`):** Adicionado um toolkit completo para manipulação de dicionários, incluindo `deep_get`, `deep_set`, `merge_dicts`, `flatten_dict`, `unflatten_dict`, `dict_diff`, e mais.
- **Módulo de Formatação (`formatting.py`):**
    - Implementação de um formatador de tabelas (`print_table`) sem dependências externas, com suporte para alinhamento e bordas.
    - Adicionadas funções de UI de terminal com estética "hacker", como `print_table_hacker`, `ascii_banner_hacker`, `boxed_text_hacker`, `glitch_text`, e `matrix_rain_preview`.
    - Adicionada a função `to_markdown_table` para gerar tabelas em Markdown.
- **Módulo de I/O (`io.py`):**
    - Suporte transparente para compressão e descompressão de ficheiros **Gzip** (`.gz`).
    - Adicionada a função `backup_file` para criar backups rotativos de ficheiros.
    - Adicionada a função `stream_jsonl` para escrita eficiente de grandes volumes de dados.

### Changed
- **Arquitetura do Projeto:** O projeto foi refatorado para uma estrutura `src/` profissional, com o código organizado em sub-pacotes (`core`, `decorators`, `utils`) para melhor manutenibilidade e escalabilidade.
- **`@retry` Decorator:** Aprimorado para logar o sucesso (tanto na primeira tentativa como após retries) e permitir a configuração de quais exceções devem acionar uma nova tentativa.
- **`@timer` Decorator:** Aprimorado para incluir um timestamp (`{timestamp}`) na mensagem de log e permitir a personalização completa do template.
- **`setup_logging`:** Refatorado para ser compatível com `pytest` e mais robusto, usando `logging.basicConfig(force=True)`.
- **`slugify`:** Lógica melhorada para lidar corretamente com caracteres Unicode e outros casos extremos.
- **`snake_to_camel`:** Adicionado suporte para preservar acrónimos (ex: `api_id` -> `APIID`).
- **`extract_urls`:** Melhorada para remover pontuação final comum dos links extraídos.
- **`read_json`:** Aprimorado com type hints `@overload` para uma melhor experiência com análise estática de código.
- **Cobertura de Testes:** Aumentada para **+90%** em todo o projeto, com 100% de cobertura em vários módulos críticos.


## [0.4.0] - 2025-09-27
### Changed
- Renomeado o projeto de **pydevhelper** para **pybrige**.
- Nova identidade e branding.


## [0.3.1] - 2025-09-27
### Added
- Novo sistema de importação por namespaces (`text`, `io`, `robustness`, etc.).
- Mantida compatibilidade retroativa: `from dev_helper import slugify` ainda funciona.

### Changed
- `__init__.py` reestruturado para maior clareza e flexibilidade.


## [0.3.0] - 2025-09-27

### 🚀 Novidades
- **Módulo `text_utils`** adicionado com várias funções utilitárias:
  - `slugify` com suporte a **Unicode** (`allow_unicode=True`);
  - Conversores `camel_to_snake` e `snake_to_camel`;
  - `normalize_whitespace` para limpar espaços extras;
  - `remove_html_tags` para sanitização de strings;
  - Extratores `extract_emails` e `extract_urls`.
- **Módulo `config`** revisado e expandido:
  - Suporte a **esquema tipado** com `EnvSpec` e `VarSpec`;
  - Integração opcional com `.env` via `python-dotenv`;
  - Suporte a `parser` customizado e `validator` por variável;
  - Mensagens de erro claras e estruturadas via `MissingEnvVarsError`;
  - Suporte a prefixos (`prefix="APP_"`) para ambientes complexos.

### ✅ Melhorias na qualidade do projeto
- Testes unitários expandidos para `config`:
  - Verificação de variáveis obrigatórias ausentes;
  - Defaults aplicados corretamente;
  - Falha de **casting** (`int("not-a-number")`) devidamente sinalizada;
  - Validação customizada falhando;
  - Prefixos de variáveis.
- Cobertura de testes ampliada → **maior robustez e confiança**.

---

## [0.2.0] - 2025-09-26

### 🚀 Novidades
- **Decorator `@retry`** para reexecução automática de funções em caso de exceções.
  - Suporte a `tries`, `delay`, `backoff` exponencial;
  - Permite especificar exceções capturadas (`exceptions=(Exception,)`);
  - Possibilidade de injetar `sleep_func` para testes (sem atrasos reais);
  - Logging de falhas e sucessos.

---

## [0.1.1] - 2025-09-25

### 🚀 Novidades
- **Logger colorido** com `setup_logging(colors=True)`;
- **Timer** com suporte a timestamp e template customizado.

### ✅ Qualidade
- Cobertura de testes completa para `logging` e `timer`.

---

## [0.1.0] - 2025-09-24

### 🚀 Versão inicial
- `setup_logging` para configuração simples de logs.
- `require_vars` para validação de variáveis de ambiente.
- `@timer` decorator para medir tempo de execução.
- `print_table` para renderizar dados em tabela de terminal.
