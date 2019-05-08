# -*- coding: utf-8 -*-
import scrapy
import json


class DiputadoSpider(scrapy.Spider):
    name = 'diputado'

    allowed_domains = ['elecciones.santafe.gov.ar']
    urls = ['https://elecciones.santafe.gov.ar/mesa/diputado/%s/E' %
            #rosario
            #(i) for i in range(3687, 6343)]

            #pueblo esther
            #(i) for i in range(6463, 6486)]

            #toda la provincia
            (i) for i in range(1, 7910)]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, headers={'Referer': 'https://elecciones.santafe.gov.ar/', 'X-Requested-With': 'XMLHttpRequest'}, callback=self.parse)

    def parse(self, response):
        r = json.loads(response.body_as_unicode())
        partido = ''
        for d in r['detalle']:
            if d['tipo'] == 'P':
                partido = d['nombre']
                continue
            o = {}
            o['mesa'] = r['cabecera'][0]['mesa']
            o['asistencia'] = r['cabecera'][0]['asistencia']
            o['departamento'] = r['cabecera'][0]['departamento']
            o['estadoMesa'] = r['cabecera'][0]['estadoMesa']
            o['fechaHoraInformacion'] = r['cabecera'][0]['fechaHoraInformacion']
            o['intervinoTribunal'] = r['cabecera'][0]['intervinoTribunal']
            o['local'] = r['cabecera'][0]['local']
            o['localidad'] = r['cabecera'][0]['localidad']
            o['mesasDesestimadas'] = r['cabecera'][0]['mesasDesestimadas']
            o['mesasIngresadas'] = r['cabecera'][0]['mesasIngresadas']
            o['mesasNoComputadas'] = r['cabecera'][0]['mesasNoComputadas']
            o['mesasNoRecibidas'] = r['cabecera'][0]['mesasNoRecibidas']
            o['nombreArchivoFax'] = r['cabecera'][0]['nombreArchivoFax']
            o['porcentajeMesas'] = r['cabecera'][0]['porcentajeMesas']
            o['porcentajeMesasNoComputadas'] = r['cabecera'][0]['porcentajeMesasNoComputadas']
            o['porcentajeParticipacion'] = r['cabecera'][0]['porcentajeParticipacion']
            o['seccional'] = r['cabecera'][0]['seccional']
            o['totalElectores'] = r['cabecera'][0]['totalElectores']
            o['totalMesas'] = r['cabecera'][0]['totalMesas']
            o['totalMesasExt'] = r['cabecera'][0]['totalMesasExt']
            o['totalVotantes'] = r['cabecera'][0]['totalVotantes']
            o['partido'] = partido
            o['cantidad'] = d['cantidad']
            o['nombre'] = d['nombre']
            o['nombreCandidato'] = d['nombreCandidato']
            o['porcentaje'] = d['porcentaje']
            o['Votos afirmativos emitidos'] = r['votos'][0]['cantidad']
            o['Votos Anulados'] = r['votos'][1]['cantidad']
            o['Votos en Blanco'] = r['votos'][2]['cantidad']
            o['Votos impugnados'] = r['votos'][3]['cantidad']
            o['Votos Recurridos'] = r['votos'][4]['cantidad']
            o['Diferencia a determinar en el Escrutinio Definitivo'] = r['votos'][5]['cantidad']
            o['Total de votos'] = r['votos'][6]['cantidad']
            o['Votos Válidos Emitidos'] = r['votos'][7]['cantidad']
            yield o
