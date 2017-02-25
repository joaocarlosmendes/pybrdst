PyBrDST
========

Um simples calculador das datas de início e fim do horário de verão brasileiro a partir de um ano especificado.

## Instalando

```bash
pip install pybrdst
```

## Como usar ##

#### Obtendo o início e fim do horário de verão:

```python
from pybrdst.pybrdst import PyBrDST
dst = PyBrDST()
start, end = dst.get_dst(2017)
print(start)
2017-10-15 00:00:00
print(end)
2018-02-18 00:00:00
```

#### Obtendo somente o início do horário de verão:

```python
from pybrdst.pybrdst import PyBrDST
dst = PyBrDST()
start = dst.begin_dst(2017)
print(start)
2017-10-15 00:00:00
```


#### Obtendo somente o fim do horário de verão:
Observe que a data informada será o fim que ocorreu ou ocorrerá no ano informado e não no ano seguinte

```python
from pybrdst.pybrdst import PyBrDST
dst = PyBrDST()
end = dst.end_dst(2017)
print(end)
2017-02-19 00:00:00
```

#### Obtendo a data do Páscoa:

```python
from pybrdst.pybrdst import PyBrDST
dst = PyBrDST()
easter_date = dst.easter_date(2017)
print(easter_date)
2017-04-16 00:00:00
```

#### Obtendo a data do carnaval:

```python
from pybrdst.pybrdst import PyBrDST
dst = PyBrDST()
carnival_date = dst.carnival_date(dst.easter_date(2017))
print(carnival_date)
2017-02-28 00:00:00
```
Todos os retornos são do tipo `datetime.datetime`
