4. Considere o formato de imagem NetPBM:

**Qual a diferença entre os números mágicos P1, P2, P3, P4, P5 e P6?**

Os números mágicos servem para identificar o tipo do arquivo e sua codificação.
Os 3 primeiros números mágicos são de codificação ASCII, os 3 restantes são de codificação binário.
P1 e P4 são do formato `.pbm`, P2 e P5 são `.pgm` e P3 e P6 são `.ppm`.

**Converta a mesma imagem para PBM (binário) e para PPM (binário). Compare o tamanho dos 4 arquivos de imagem.**

| Imagem | Tamanho |
| ------ | ------- |
| bash_logo.jpg | 43987 B |
| bash_logo_pbm_ascii.pbm | 1297212 B |
| bash_logo_pbm_binary.pbm | 81012 B |
| bash_logo_ppm_binary.ppm | 1944016 B |

A imagem original é a mais leve das quatro.
O PBM binário saiu mais leve que o PBM ASCII,
ocupando apenas aproximadamente 62,45% do tamanho do PBM ASCII.
O PPM binário saiu muito mais grande que o PBM binário, quase 2400 vezes maior.

**Por que o formato binário ocupa menos espaço que o formato ASCII?**

O formato ASCII é légival ao olho humano, utiliza-se a tabela ASCII para codificar os pixels e gasta muito espaço de memória.
O formato binário gasta apenas 1 bit por pixel, o que é uma economia muito grande se comparado ao formato ASCII.

**Por que o formato PPM binário ocupa mais espaço que o formato PBM binário?**

O formato PBM binário gasta apenas 1 bit por pixel, enquanto o formato PPM gasta 24 bits por pixel (8 para cada camada de cor).
