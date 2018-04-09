import scrapy


class RistoMejide(scrapy.Spider):
    name = "risto"

    def start_requests(self):
        urls = [
            'https://ristomejide.com/2016/07/25/fuera-de-cobertura/',
            'https://ristomejide.com/2016/07/21/el-mundo-se-va-a-la-mierda/',
            'https://ristomejide.com/2016/07/14/we-try-harder/',
            'https://ristomejide.com/2016/07/11/que-has-hecho-conmigo/',
            'https://ristomejide.com/2016/07/18/9-80665-ms2/',
            'https://ristomejide.com/2016/07/07/que/',
            'https://ristomejide.com/2016/06/30/carta-abierta-\
            al-votante-del-pp/',
            'https://ristomejide.com/2016/07/04/el-rabillo/',
            'https://ristomejide.com/2016/06/27/mejor-asi-mejor-ahora/',
            'https://ristomejide.com/2016/06/23/nadie-deberia-\
            votar-en-verano/',
            'https://ristomejide.com/2016/06/16/atascame-otra-vez/',
            'https://ristomejide.com/2016/06/20/la-tristeza-se-\
            acumula-la-felicidad-no/',
            'https://ristomejide.com/2016/06/13/los-idus-de-junio/',
            'https://ristomejide.com/2016/06/09/fe-relevancia-y-calidad/',
            'https://ristomejide.com/2016/06/02/la-suerte-no-existe/',
            'https://ristomejide.com/2016/06/06/soy-de-letras/',
            'https://ristomejide.com/2016/05/30/alguien-decidio-no-quererte/',
            'https://ristomejide.com/2016/05/26/pasa-o-pistacho/',
            'https://ristomejide.com/2016/05/19/senoiccele/',
            'https://ristomejide.com/2016/05/23/elige-un-problema/',
            'https://ristomejide.com/2016/05/16/que-falta/',
            'https://ristomejide.com/2016/05/09/manifiesto-becario/',
            'https://ristomejide.com/2016/05/02/mujer-sin-paraguas/',
            'https://ristomejide.com/2016/05/05/logistica-emocional/',
            'https://ristomejide.com/2016/04/28/voten-ustedes/',
            'https://ristomejide.com/2016/04/25/existe/',
            'https://ristomejide.com/2016/04/21/se-acabo-lo-que-se-acababa/',
            'https://ristomejide.com/2016/04/18/no-se-lo-que-no-se/',
            'https://ristomejide.com/2016/04/14/hipocrates-en-panama/',
            'https://ristomejide.com/2016/04/11/me-puede/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
