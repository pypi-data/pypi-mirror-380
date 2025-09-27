# IlyasFamily Python Implementation
**IlyasFamily** adalah format pertukaran dan penyimpanan data alternatif, seperti JSON tetapi lebih kaya tipe data.

Ekstensi resmi: `.ifamily`.

Repositori ini berisi **implementasi Python** dari spesifikasi [IlyasFamily](https://github.com/aflacake/ilyasfamily-spec).

## Instalasi
```bash
pip install ilyasfamily-py
```

## Contoh Pemakaiaan
```python
from ilyasfamily import Node, dump_file, load_file

person = Node("Person", {"Name": "Budi", "Age": 21})
dump_file(person, "person.ifamily")
loaded = load_file("person_family")

print(loaded)
```

### Menguji
Uji dengan **pytest** atau jalankan manual. Namun kali ini dengan pytest karena untuk uji coba cepat. Anda bisa mengedit kode `test/test.py` untuk uji coba manual.
1. Instal pytest
   ```
   pip install pytest
   ```
2. Jalankan dari root
   ```
   pytest
   ```
   atau jalur spesifik:
   ```
   pytest tests/test.py -v
   ```

Apa bila pytest tidak menemukan package ilyasfamily karena struktur repositori memakai `src/` layout.

Instal lokal dahulu
```
pip install -e .
```
Lalu coba lagi
```
pytest tests/test.py -v
```

## Lisensi
[Apache-2.0](https://github.com/aflacake/ilyasfamily-py/?tab=Apache-2.0-1-ov-file)
