# Text and Image Indexing
Nama : Muhammad Mulqan</br>
NIM  : 1708107010043

## A. Text Indexing dengan Swish-e
Membuat indexing text

```
swish-e -c indexing.conf
```
![Test Swish-e 0](screenshot/test-swish-e0.png)

Menguji index yang telah dibuat

```
swish-e -f hasil.index -m 5 -w “Macet”
```
![Test Swish-e 1](screenshot/test-swish-e1.png)


```
swish-e -f hasil.index -m 5 -w “Macet” and "jokowi"
```
![Test Swish-e 2](screenshot/test-swish-e2.png)


```
swish-e -f hasil.index -m 5 -w “Macet” or "jokowi"
```
![Test Swish-e 3](screenshot/test-swish-e3.png)

```
swish-e -f hasil.index -m 5 -w “Macet” not "jokowi"
```
![Test Swish-e 4](screenshot/test-swish-e4.png)

## B. Image Indexing dengan https://github.com/kudeh/image-search-engine
Menguji indexing gambar yang telah dibuat

![Test image indexing](screenshot/test-image-indexing.png)