# 🏆 Challenge: Wydajność wyszukiwania w SQLAlchemy

W tym ćwiczeniu zobaczysz, jak sposób zapisu zapytania w SQLAlchemy wpływa na jego czas wykonania,  
i jak w pewnych przypadkach można przyspieszyć wyszukiwanie.

---

##  Cel

- Uruchomić zapytanie z filtrem `LIKE` w SQLAlchemy.
- Zmierzyć czas działania zapytania.
- Zrozumieć, dlaczego niektóre wzorce `LIKE` działają wolniej.
- Przygotować eksperyment, który można łatwo powtórzyć.

---

## Przygotowanie środowiska

1. **Stwórz wirtualne środowisko i zainstaluj zależności**
  ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
  ```

2. **Utwórz tabele w bazie**
  W katalogu głównym projektu jest plik `init_db.py`:

  Uruchom go raz aby utworzyć tabele:

  ```bash
   python init_db.py
  ```

3. **Zasil bazę danymi (seed)**
  W katalogu projektu jest plik `seed.py`, który generuje dużą liczbę klientów.
  Uruchom:

  ```bash
  python seed.py
  ```

  Po wykonaniu w bazie powinno być dużo rekordów — to ważne, aby test wydajności miał sens.

---

## Eksperyment z wyszukaniem

W katalogu projektu jest plik `test_like.py`:

Uruchom:

```bash
python test_like.py
```

Zapisz wynik — to będzie Twój punkt odniesienia.

---

## Co dalej?

* Spróbuj zmienić wzorzec wyszukiwania na:

  ```python
  term_prefix = "Jan%"
  ```

  i porównaj czas działania.
  W niektórych bazach (np. PostgreSQL) taki zapis pozwala skorzystać z indeksu, co znacząco przyspiesza zapytanie.

* Możesz utworzyć indeks na kolumnie `name`:

  ```sql
  CREATE INDEX idx_customers_name ON customers (name);
  ```

  i ponownie zmierzyć czasy działania.

* Jeśli używasz PostgreSQL, sprawdź, jak zapytanie jest wykonywane:

  ```sql
  EXPLAIN ANALYZE SELECT * FROM customers WHERE name LIKE '%Jan%';
  ```

  Dokumentacja:

  * [`EXPLAIN` w PostgreSQL](https://www.postgresql.org/docs/current/using-explain.html)
  * [`EXPLAIN QUERY PLAN` w SQLite](https://www.sqlite.org/eqp.html)


## Dlaczego `%Jan%` jest wolniejsze?

* Wzorzec zaczynający się od `%` wymusza **skan sekwencyjny** (Sequential Scan) — baza musi sprawdzić każdy wiersz.
* Wzorzec prefiksowy (`Jan%`) pozwala użyć indeksu, jeśli taki istnieje, i pominąć większość wierszy.
* Przy dużych tabelach różnica w czasie może być ogromna.

## Materiały dodatkowe – optymalizacja baz danych i zapytań

-  **Use the Index, Luke!**  
  https://use-the-index-luke.com/  
  Darmowy, praktyczny przewodnik po indeksach w SQL.  
  
-  **Mode: SQL Optimization Basics**  
  https://mode.com/sql-tutorial/sql-performance-tuning 
  Tłumaczy podstawy optymalizacji
  
-  **Why SELECT * is Bad for Performance**  
  https://tanelpoder.com/posts/reasons-why-select-star-is-bad-for-sql-performance/ 
  Krótkie, praktyczne uzasadnienie, dlaczego warto wybierać tylko potrzebne kolumny.

-  **EXPLAIN QUERY PLAN**  
  https://medium.com/geekculture/how-to-read-postgresql-query-plan-df4b158781a1 
  Krótki i konkretny przewodnik po planach zapytań.

- **SQLAlchemy Core Tutorial (Real Python)**  
  https://realpython.com/python-sqlalchemy/#working-with-core  
  Wprowadzenie do pracy z SQLAlchemy bez ORM. Budowanie zapytań `select()`, `where()`, `order_by()`, `text()` itd.

## 🔎 Zadanie dodatkowe — samodzielne pogłębienie wiedzy

Poszukaj samodzielnie informacji na poniższe tematy:

- **Jak działa `EXPLAIN` i `ANALYZE` w PostgreSQL?**  
  Dowiedz się, jak PostgreSQL planuje i wykonuje zapytania oraz jak interpretować wynik `EXPLAIN ANALYZE`.

- **Czym jest `Sequential Scan`, `Index Scan` i `Bitmap Index Scan`?**  
  Poznaj różne sposoby odczytu danych z tabeli i dowiedz się, kiedy baza wybiera który z nich.

- **Jak działają indeksy w bazach danych (np. B-tree)?**  
  Zrozum podstawy działania indeksów, ich strukturę i wpływ na wydajność zapytań.

- **W jaki sposób można zoptymalizować zapytania `LIKE`?**  
  Przykłady użycia prefiksów, pełnotekstowego wyszukiwania i indeksów typu GIN w PostgreSQL.

- **Jakie są dobre praktyki projektowania zapytań w SQL?**  
  Dowiedz się, jak pisać czytelne i szybkie zapytania: unikać `SELECT *`, używać indeksów, ograniczać zbędne złączenia itd.
