# 🧪 Testes do KaironDB

## 📋 Visão Geral

Este diretório contém todos os testes do KaironDB, incluindo testes unitários, de integração, de performance e comparativos.

## 🏗️ Estrutura dos Testes

```
tests/
├── 📄 test_real_databases.py      # Testes com bancos reais (PostgreSQL, SQL Server, MySQL)
├── 📄 test_benchmark_comparison.py # Testes comparativos de performance
├── 📄 test_bridge.py              # Testes do bridge principal
├── 📄 test_models.py              # Testes do sistema de modelos
├── 📄 test_query.py               # Testes de consultas
├── 📄 test_exceptions.py          # Testes de tratamento de erros
├── 📄 test_fields_advanced.py     # Testes de campos avançados
├── 📄 test_advanced_features.py   # Testes de funcionalidades avançadas
├── 📄 test_fase5_performance.py   # Testes de performance da Fase 5
├── 📄 test_logging.py             # Testes de logging
├── 📄 conftest.py                 # Configuração do pytest
├── 📄 __init__.py                 # Inicialização do pacote
└── 📄 README.md                   # Este arquivo
```

## 🚀 Como Executar os Testes

### 1. Preparação do Ambiente

```bash
# Instalar dependências
pip install -r requirements-benchmark.txt

# Configurar bancos de dados
python scripts/setup_databases.py

# Ou usar o script principal
python run_benchmarks.py
```

### 2. Executar Testes Específicos

```bash
# Todos os testes
python -m pytest tests/ -v

# Testes com bancos reais
python -m pytest tests/test_real_databases.py -v

# Testes de benchmark
python -m pytest tests/test_benchmark_comparison.py -v -s

# Testes específicos
python -m pytest tests/test_bridge.py::TestSQLBridge::test_connection -v
```

### 3. Executar com Cobertura

```bash
# Instalar pytest-cov
pip install pytest-cov

# Executar com cobertura
python -m pytest tests/ --cov=src/kairondb --cov-report=html
```

## 📊 Tipos de Testes

### 1. Testes Unitários
- **Arquivo**: `test_bridge.py`, `test_models.py`, `test_query.py`
- **Objetivo**: Testar componentes individuais
- **Cobertura**: Funções, métodos, classes isoladas

### 2. Testes de Integração
- **Arquivo**: `test_real_databases.py`
- **Objetivo**: Testar integração com bancos reais
- **Cobertura**: PostgreSQL, SQL Server, MySQL

### 3. Testes de Performance
- **Arquivo**: `test_benchmark_comparison.py`
- **Objetivo**: Comparar performance com outras bibliotecas
- **Cobertura**: AsyncPG, AioSQLite, aiomysql

### 4. Testes de Funcionalidades Avançadas
- **Arquivo**: `test_advanced_features.py`
- **Objetivo**: Testar cache, profiling, dashboard
- **Cobertura**: Funcionalidades não-básicas

## 🐳 Configuração Docker

### Bancos de Dados Suportados

#### PostgreSQL 15
```yaml
# docker-compose.yml
postgres:
  image: postgres:15-alpine
  environment:
    POSTGRES_DB: kairondb_test
    POSTGRES_USER: kairondb
    POSTGRES_PASSWORD: KaironDB123!
  ports:
    - "5432:5432"
```

#### SQL Server 2022
```yaml
# docker-compose.yml
sqlserver:
  image: mcr.microsoft.com/mssql/server:2022-latest
  environment:
    ACCEPT_EULA: Y
    SA_PASSWORD: KaironDB123!
  ports:
    - "1433:1433"
```

#### MySQL 8.0
```yaml
# docker-compose.yml
mysql:
  image: mysql:8.0
  environment:
    MYSQL_ROOT_PASSWORD: KaironDB123!
    MYSQL_DATABASE: kairondb_test
    MYSQL_USER: kairondb
    MYSQL_PASSWORD: KaironDB123!
  ports:
    - "3306:3306"
```

## 📈 Interpretando Resultados

### 1. Testes de Performance

```python
# Exemplo de resultado
{
    "library": "KaironDB",
    "operation": "Single Insert",
    "mean_time": 0.0023,
    "median_time": 0.0021,
    "min_time": 0.0018,
    "max_time": 0.0045,
    "std_dev": 0.0004,
    "iterations": 100
}
```

### 2. Comparação de Bibliotecas

```python
# Ranking de performance
1. AsyncPG: 0.0018s
2. KaironDB: 0.0023s (+28%)
3. AioSQLite: 0.0031s (+72%)
```

### 3. Análise de Gargalos

```python
# Identificação de problemas
{
    "bottleneck": "Python-Go Communication",
    "impact": "15-20% of total time",
    "solution": "Optimize JSON serialization"
}
```

## 🔧 Configuração Avançada

### 1. Variáveis de Ambiente

```bash
# Configurações de teste
export KAIRONDB_TEST_POSTGRES_HOST=localhost
export KAIRONDB_TEST_POSTGRES_PORT=5432
export KAIRONDB_TEST_POSTGRES_USER=kairondb
export KAIRONDB_TEST_POSTGRES_PASSWORD=KaironDB123!

export KAIRONDB_TEST_SQLSERVER_HOST=localhost
export KAIRONDB_TEST_SQLSERVER_PORT=1433
export KAIRONDB_TEST_SQLSERVER_USER=sa
export KAIRONDB_TEST_SQLSERVER_PASSWORD=KaironDB123!

export KAIRONDB_TEST_MYSQL_HOST=localhost
export KAIRONDB_TEST_MYSQL_PORT=3306
export KAIRONDB_TEST_MYSQL_USER=kairondb
export KAIRONDB_TEST_MYSQL_PASSWORD=KaironDB123!
```

### 2. Configuração do Pytest

```python
# conftest.py
import pytest
import asyncio

@pytest.fixture(scope="session")
def event_loop():
    """Cria um event loop para toda a sessão de testes"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def test_database():
    """Configuração do banco de teste"""
    return {
        "postgres": {
            "host": "localhost",
            "port": 5432,
            "database": "kairondb_test",
            "user": "kairondb",
            "password": "KaironDB123!"
        }
    }
```

## 🐛 Solução de Problemas

### 1. Erro de Conexão com Banco

```bash
# Verificar se containers estão rodando
docker-compose ps

# Verificar logs
docker-compose logs postgres
docker-compose logs sqlserver
docker-compose logs mysql

# Reiniciar containers
docker-compose restart
```

### 2. Erro de Importação

```bash
# Verificar se o path está correto
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Ou usar o script de teste
python run_benchmarks.py
```

### 3. Erro de Permissão

```bash
# Dar permissão de execução
chmod +x run_benchmarks.py
chmod +x scripts/setup_databases.py
```

## 📚 Documentação Adicional

- [BENCHMARK_RESULTS.md](../docs/BENCHMARK_RESULTS.md) - Resultados detalhados
- [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md) - Solução de problemas
- [API Reference](../docs/api-reference.md) - Documentação da API

## 🤝 Contribuindo

### 1. Adicionando Novos Testes

```python
# Exemplo de teste
class TestNewFeature:
    @pytest.mark.asyncio
    async def test_new_functionality(self):
        # Arrange
        bridge = SQLBridge(...)
        await bridge.connect()
        
        # Act
        result = await bridge.new_method()
        
        # Assert
        assert result is not None
        await bridge.close()
```

### 2. Executando Testes Antes do Commit

```bash
# Executar todos os testes
python -m pytest tests/ -v

# Verificar cobertura
python -m pytest tests/ --cov=src/kairondb --cov-report=term-missing

# Executar testes de performance
python -m pytest tests/test_benchmark_comparison.py -v -s
```

---

**Última Atualização**: 2025-01-27  
**Versão**: 1.0.1
