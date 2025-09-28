#!/usr/bin/env python3
"""
Testes comparativos de performance entre KaironDB e outras bibliotecas
"""

import pytest
import asyncio
import time
import sys
import os
import statistics
from typing import Dict, List, Any

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from kairondb.bridge import SQLBridge

# Tentar importar outras bibliotecas para comparação
try:
    import asyncpg
    HAS_ASYNCPG = True
except ImportError:
    HAS_ASYNCPG = False

try:
    import aiosqlite
    HAS_AIOSQLITE = True
except ImportError:
    HAS_AIOSQLITE = False

try:
    import aiomysql
    HAS_AIOMYSQL = True
except ImportError:
    HAS_AIOMYSQL = False

try:
    import aioodbc
    HAS_AIODBC = True
except ImportError:
    HAS_AIODBC = False

class BenchmarkResult:
    """Classe para armazenar resultados de benchmark"""
    
    def __init__(self, library_name: str, operation: str, times: List[float], success: bool = True, error: str = None):
        self.library_name = library_name
        self.operation = operation
        self.times = times
        self.success = success
        self.error = error
        self.mean_time = statistics.mean(times) if times else 0
        self.median_time = statistics.median(times) if times else 0
        self.min_time = min(times) if times else 0
        self.max_time = max(times) if times else 0
        self.std_dev = statistics.stdev(times) if len(times) > 1 else 0

class DatabaseBenchmark:
    """Classe base para benchmarks de banco de dados"""
    
    def __init__(self):
        self.results: List[BenchmarkResult] = []
    
    async def benchmark_operation(self, operation_func, operation_name: str, iterations: int = 10) -> BenchmarkResult:
        """Executa um benchmark de uma operação"""
        times = []
        success = True
        error = None
        
        for i in range(iterations):
            try:
                start_time = time.time()
                await operation_func()
                end_time = time.time()
                times.append(end_time - start_time)
            except Exception as e:
                success = False
                error = str(e)
                break
        
        return BenchmarkResult(operation_name, operation_name, times, success, error)
    
    def add_result(self, result: BenchmarkResult):
        """Adiciona um resultado ao benchmark"""
        self.results.append(result)
    
    def get_summary(self) -> Dict[str, Any]:
        """Retorna um resumo dos resultados"""
        summary = {}
        for result in self.results:
            if result.success:
                summary[result.library_name] = {
                    "mean": result.mean_time,
                    "median": result.median_time,
                    "min": result.min_time,
                    "max": result.max_time,
                    "std_dev": result.std_dev,
                    "iterations": len(result.times)
                }
            else:
                summary[result.library_name] = {
                    "error": result.error
                }
        return summary

class TestKaironDBBenchmark:
    """Benchmarks do KaironDB"""
    
    @pytest.fixture
    def kairondb_bridge(self):
        """Bridge do KaironDB para PostgreSQL"""
        return SQLBridge(
            driver="postgres",
            server="localhost",
            db_name="kairondb_test",
            user="kairondb",
            password="KaironDB123!"
        )
    
    @pytest.mark.asyncio
    async def test_kairondb_insert_performance(self, kairondb_bridge):
        """Testa performance de inserção do KaironDB"""
        await kairondb_bridge.connect()
        
        # Criar tabela
        await kairondb_bridge.create_table("benchmark_test", {
            "id": "SERIAL PRIMARY KEY",
            "name": "VARCHAR(100)",
            "value": "INTEGER",
            "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        })
        
        benchmark = DatabaseBenchmark()
        
        # Benchmark de inserção única
        async def single_insert():
            await kairondb_bridge.insert("benchmark_test", {
                "name": f"Test {time.time()}",
                "value": int(time.time())
            })
        
        result = await benchmark.benchmark_operation(single_insert, "KaironDB Single Insert", 100)
        benchmark.add_result(result)
        
        # Benchmark de inserção em lote
        async def batch_insert():
            data = []
            for i in range(100):
                data.append({
                    "name": f"Batch Test {i}",
                    "value": i
                })
            await kairondb_bridge.batch_insert("benchmark_test", data)
        
        result = await benchmark.benchmark_operation(batch_insert, "KaironDB Batch Insert", 10)
        benchmark.add_result(result)
        
        # Benchmark de consulta
        async def select_query():
            await kairondb_bridge.select("benchmark_test")
        
        result = await benchmark.benchmark_operation(select_query, "KaironDB Select", 100)
        benchmark.add_result(result)
        
        # Benchmark de consulta com WHERE
        async def select_where():
            await kairondb_bridge.select("benchmark_test", {"value": 50})
        
        result = await benchmark.benchmark_operation(select_where, "KaironDB Select WHERE", 100)
        benchmark.add_result(result)
        
        await kairondb_bridge.close()
        
        # Imprimir resultados
        summary = benchmark.get_summary()
        print("\n📊 KAIRONDB BENCHMARK RESULTS:")
        print("=" * 50)
        for operation, stats in summary.items():
            if "error" not in stats:
                print(f"{operation}:")
                print(f"  Mean: {stats['mean']:.4f}s")
                print(f"  Median: {stats['median']:.4f}s")
                print(f"  Min: {stats['min']:.4f}s")
                print(f"  Max: {stats['max']:.4f}s")
                print(f"  Std Dev: {stats['std_dev']:.4f}s")
                print(f"  Iterations: {stats['iterations']}")
            else:
                print(f"{operation}: ERROR - {stats['error']}")
        
        return summary

class TestAsyncPGBenchmark:
    """Benchmarks do AsyncPG (PostgreSQL)"""
    
    @pytest.mark.skipif(not HAS_ASYNCPG, reason="AsyncPG não está instalado")
    @pytest.mark.asyncio
    async def test_asyncpg_performance(self):
        """Testa performance do AsyncPG"""
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="kairondb",
            password="KaironDB123!",
            database="kairondb_test"
        )
        
        # Criar tabela
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS asyncpg_benchmark (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                value INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        benchmark = DatabaseBenchmark()
        
        # Benchmark de inserção única
        async def single_insert():
            await conn.execute(
                "INSERT INTO asyncpg_benchmark (name, value) VALUES ($1, $2)",
                f"Test {time.time()}", int(time.time())
            )
        
        result = await benchmark.benchmark_operation(single_insert, "AsyncPG Single Insert", 100)
        benchmark.add_result(result)
        
        # Benchmark de inserção em lote
        async def batch_insert():
            data = [(f"Batch Test {i}", i) for i in range(100)]
            await conn.executemany(
                "INSERT INTO asyncpg_benchmark (name, value) VALUES ($1, $2)",
                data
            )
        
        result = await benchmark.benchmark_operation(batch_insert, "AsyncPG Batch Insert", 10)
        benchmark.add_result(result)
        
        # Benchmark de consulta
        async def select_query():
            await conn.fetch("SELECT * FROM asyncpg_benchmark")
        
        result = await benchmark.benchmark_operation(select_query, "AsyncPG Select", 100)
        benchmark.add_result(result)
        
        # Benchmark de consulta com WHERE
        async def select_where():
            await conn.fetch("SELECT * FROM asyncpg_benchmark WHERE value = $1", 50)
        
        result = await benchmark.benchmark_operation(select_where, "AsyncPG Select WHERE", 100)
        benchmark.add_result(result)
        
        await conn.close()
        
        # Imprimir resultados
        summary = benchmark.get_summary()
        print("\n📊 ASYNCPG BENCHMARK RESULTS:")
        print("=" * 50)
        for operation, stats in summary.items():
            if "error" not in stats:
                print(f"{operation}:")
                print(f"  Mean: {stats['mean']:.4f}s")
                print(f"  Median: {stats['median']:.4f}s")
                print(f"  Min: {stats['min']:.4f}s")
                print(f"  Max: {stats['max']:.4f}s")
                print(f"  Std Dev: {stats['std_dev']:.4f}s")
                print(f"  Iterations: {stats['iterations']}")
            else:
                print(f"{operation}: ERROR - {stats['error']}")
        
        return summary

class TestAioSQLiteBenchmark:
    """Benchmarks do AioSQLite (SQLite)"""
    
    @pytest.mark.skipif(not HAS_AIOSQLITE, reason="AioSQLite não está instalado")
    @pytest.mark.asyncio
    async def test_aiosqlite_performance(self):
        """Testa performance do AioSQLite"""
        db_path = "benchmark_test.db"
        
        async with aiosqlite.connect(db_path) as db:
            # Criar tabela
            await db.execute("""
                CREATE TABLE IF NOT EXISTS aiosqlite_benchmark (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    value INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            await db.commit()
            
            benchmark = DatabaseBenchmark()
            
            # Benchmark de inserção única
            async def single_insert():
                await db.execute(
                    "INSERT INTO aiosqlite_benchmark (name, value) VALUES (?, ?)",
                    (f"Test {time.time()}", int(time.time()))
                )
                await db.commit()
            
            result = await benchmark.benchmark_operation(single_insert, "AioSQLite Single Insert", 100)
            benchmark.add_result(result)
            
            # Benchmark de inserção em lote
            async def batch_insert():
                data = [(f"Batch Test {i}", i) for i in range(100)]
                await db.executemany(
                    "INSERT INTO aiosqlite_benchmark (name, value) VALUES (?, ?)",
                    data
                )
                await db.commit()
            
            result = await benchmark.benchmark_operation(batch_insert, "AioSQLite Batch Insert", 10)
            benchmark.add_result(result)
            
            # Benchmark de consulta
            async def select_query():
                await db.execute("SELECT * FROM aiosqlite_benchmark")
                await db.fetchall()
            
            result = await benchmark.benchmark_operation(select_query, "AioSQLite Select", 100)
            benchmark.add_result(result)
            
            # Benchmark de consulta com WHERE
            async def select_where():
                await db.execute("SELECT * FROM aiosqlite_benchmark WHERE value = ?", (50,))
                await db.fetchall()
            
            result = await benchmark.benchmark_operation(select_where, "AioSQLite Select WHERE", 100)
            benchmark.add_result(result)
        
        # Limpar arquivo
        if os.path.exists(db_path):
            os.remove(db_path)
        
        # Imprimir resultados
        summary = benchmark.get_summary()
        print("\n📊 AIOSQLITE BENCHMARK RESULTS:")
        print("=" * 50)
        for operation, stats in summary.items():
            if "error" not in stats:
                print(f"{operation}:")
                print(f"  Mean: {stats['mean']:.4f}s")
                print(f"  Median: {stats['median']:.4f}s")
                print(f"  Min: {stats['min']:.4f}s")
                print(f"  Max: {stats['max']:.4f}s")
                print(f"  Std Dev: {stats['std_dev']:.4f}s")
                print(f"  Iterations: {stats['iterations']}")
            else:
                print(f"{operation}: ERROR - {stats['error']}")
        
        return summary

class TestPerformanceComparison:
    """Testes comparativos de performance"""
    
    @pytest.mark.asyncio
    async def test_comprehensive_benchmark(self):
        """Executa benchmark abrangente comparando todas as bibliotecas"""
        print("\n🚀 INICIANDO BENCHMARK ABRANGENTE")
        print("=" * 60)
        
        results = {}
        
        # KaironDB
        try:
            kairondb_test = TestKaironDBBenchmark()
            kairondb_bridge = kairondb_test.kairondb_bridge()
            kairondb_results = await kairondb_test.test_kairondb_insert_performance(kairondb_bridge)
            results["KaironDB"] = kairondb_results
        except Exception as e:
            results["KaironDB"] = {"error": str(e)}
        
        # AsyncPG
        if HAS_ASYNCPG:
            try:
                asyncpg_test = TestAsyncPGBenchmark()
                asyncpg_results = await asyncpg_test.test_asyncpg_performance()
                results["AsyncPG"] = asyncpg_results
            except Exception as e:
                results["AsyncPG"] = {"error": str(e)}
        else:
            results["AsyncPG"] = {"error": "AsyncPG não instalado"}
        
        # AioSQLite
        if HAS_AIOSQLITE:
            try:
                aiosqlite_test = TestAioSQLiteBenchmark()
                aiosqlite_results = await aiosqlite_test.test_aiosqlite_performance()
                results["AioSQLite"] = aiosqlite_results
            except Exception as e:
                results["AioSQLite"] = {"error": str(e)}
        else:
            results["AioSQLite"] = {"error": "AioSQLite não instalado"}
        
        # Análise comparativa
        print("\n📈 ANÁLISE COMPARATIVA:")
        print("=" * 60)
        
        operations = ["Single Insert", "Batch Insert", "Select", "Select WHERE"]
        
        for operation in operations:
            print(f"\n🔍 {operation}:")
            print("-" * 30)
            
            operation_results = {}
            for library, library_results in results.items():
                if operation in library_results and "error" not in library_results[operation]:
                    operation_results[library] = library_results[operation]["mean"]
                else:
                    operation_results[library] = None
            
            # Ordenar por performance (menor tempo = melhor)
            sorted_results = sorted(
                [(lib, time) for lib, time in operation_results.items() if time is not None],
                key=lambda x: x[1]
            )
            
            if sorted_results:
                best_library, best_time = sorted_results[0]
                print(f"🏆 Melhor: {best_library} ({best_time:.4f}s)")
                
                for i, (library, time) in enumerate(sorted_results[1:], 2):
                    slowdown = (time / best_time - 1) * 100
                    print(f"   {i}º: {library} ({time:.4f}s, +{slowdown:.1f}%)")
            else:
                print("❌ Nenhum resultado válido encontrado")
        
        return results
