from pathlib import Path
from html import escape
import textwrap

DEST = Path(__file__).resolve().parent
DEST.mkdir(exist_ok=True)
BLUE = ('#1769b8', '#0e4982', '#ffffff')
LIGHT = ('#e9f2fc', '#4b81b5', '#173655')
GRAY = ('#6b7280', '#4b5563', '#ffffff')
AMBER = ('#fff2d6', '#b7791f', '#6b450d')

class Drawing:
    def __init__(self, w, h, title, subtitle):
        self.w, self.h = w, h
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc>', '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#475569"/></marker><marker id="planned" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#b7791f"/></marker></defs>', '<rect width="100%" height="100%" fill="#fff"/>']
        self.text(w/2, 42, title, 27, '#142e49', '700')
        self.text(w/2, 73, subtitle, 15, '#526477')

    def text(self, x, y, value, size=16, color='#334155', weight='400', anchor='middle'):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')

    def multiline(self, x, y, value, width, size=16, color='#334155', weight='400', leading=23):
        lines = textwrap.wrap(value, max(14, int(width/(size*.53))))
        for j, line in enumerate(lines):
            self.text(x, y+j*leading, line, size, color, weight)
        return len(lines)*leading

    def card(self, x, y, w, h, title, tech, desc, palette=BLUE):
        bg, border, color = palette
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="{bg}" stroke="{border}" stroke-width="2"/>')
        used = self.multiline(x+w/2, y+31, title, w-28, 19, color, '700', 24)
        yy = y+31+used+1
        self.text(x+w/2, yy, tech, 12, color)
        self.multiline(x+w/2, yy+29, desc, w-35, 15, color, leading=21)

    def person(self, x, y, w, title, desc):
        cx=x+w/2
        self.parts.append(f'<circle cx="{cx}" cy="{y+35}" r="34" fill="#123f70"/><rect x="{x}" y="{y+79}" width="{w}" height="114" rx="39" fill="#123f70"/>')
        self.text(cx,y+112,title,19,'#ffffff','700')
        self.text(cx,y+133,'[Persona]',12,'#ffffff')
        self.multiline(cx,y+158,desc,w-30,14,'#ffffff',leading=19)

    def db(self, x, y, w, h, title, tech, desc):
        self.parts.append(f'<path d="M{x} {y+25} C{x} {y-5} {x+w} {y-5} {x+w} {y+25} V{y+h-25} C{x+w} {y+h+8} {x} {y+h+8} {x} {y+h-25}Z" fill="#1769b8" stroke="#0e4982" stroke-width="2"/><ellipse cx="{x+w/2}" cy="{y+25}" rx="{w/2}" ry="25" fill="#428ad0" stroke="#0e4982" stroke-width="2"/>')
        title_y, tech_y, desc_y = (62, 85, 110) if h < 150 else (76, 100, 131)
        self.text(x+w/2,y+title_y,title,19,'#ffffff','700')
        self.text(x+w/2,y+tech_y,tech,12,'#ffffff')
        self.multiline(x+w/2,y+desc_y,desc,w-28,14,'#ffffff',leading=20)

    def boundary(self,x,y,w,h,title,subtitle):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#f8fbff" stroke="#8ca4be" stroke-width="2" stroke-dasharray="10 7"/>')
        self.text(x+25,y+33,title,20,'#173655','700','start')
        self.text(x+25,y+58,subtitle,13,'#526477','400','start')

    def line(self,points,label=None,pos=None,planned=False,arrow=True):
        color='#b7791f' if planned else '#475569'
        dash=' stroke-dasharray="8 6"' if planned else ''
        marker=f' marker-end="url(#{"planned" if planned else "arrow"})"' if arrow else ''
        pts=' '.join(f'{x},{y}' for x,y in points)
        self.parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"{dash}{marker}/>')
        if label and pos:
            self.label(*pos,label,color)

    def label(self,x,y,label,color='#475569',size=14):
        w=len(label)*size*.53+14
        self.parts.append(f'<rect x="{x-w/2}" y="{y-size}" width="{w}" height="{size+7}" rx="4" fill="#fff"/>')
        self.text(x,y,label,size,color)

    def save(self,name):
        self.parts.append('</svg>')
        (DEST/name).write_text('\n'.join(self.parts),encoding='utf-8')

# C4 1: one system at the centre, actors above, neighbouring systems below.
d=Drawing(1600,1010,'Canal Marketplace · C4 nivel 1','Contexto del sistema · Inka Athletics · Corte H3 del 17/10/2026')
d.person(675,112,250,'Cliente / Visitante','Explora y utiliza el canal de compra')
d.card(630,390,340,160,'Canal Marketplace','[Sistema de software]','Catálogo, ficha, carrito, favoritos, checkout y consulta de pedidos')
d.line([(800,305),(800,390)],'Usa el canal web',(800,352))
d.line([(800,550),(800,625)],planned=True,arrow=False)
d.line([(195,625),(1435,625)],planned=True,arrow=False)
entries=[(60,'Seguridad y Usuarios','Identidad, credenciales y direcciones','Acceso e identidad',GRAY),(370,'Productos y Ofertas','Catálogo, precios, ofertas y stock','Consulta productos',GRAY),(680,'Ventas y Postventa','Pedidos y comprobantes','Crea / consulta pedido',GRAY),(990,'Despacho y Entrega','Cotización y seguimiento','Consulta envío',GRAY),(1300,'Proveedor de correo','Proveedor pendiente de concretar','Envía notificaciones',AMBER)]
for x,title,desc,label,palette in entries:
    cx=x+135
    d.line([(cx,625),(cx,740)],'Previsto: '+label,(cx,688),True)
    d.card(x,740,270,170,title,'[Sistema externo]',desc,palette)
d.text(800,964,'Azul: sistema propio · Gris: sistema externo · Ámbar / línea discontinua: integración prevista',15)
d.save('c4-01-contexto.svg')

# C4 2: sequential execution units; no line crosses a container.
d=Drawing(1700,1010,'Canal Marketplace · C4 nivel 2','Contenedores de aplicación · Frontend, backend y persistencia propia')
d.boundary(295,160,1360,390,'Canal Marketplace · Grupo 1','React y Next.js pertenecen al repositorio frontend; NestJS tiene su propio repositorio.')
d.person(35,263,205,'Cliente','Navegador web')
d.card(345,300,260,180,'Interfaz web','[Contenedor · React 19]','Páginas y componentes de la experiencia de compra')
d.card(675,300,260,180,'Servidor y fachada','[Contenedor · Next.js 16]','Páginas servidor y proxies /api del canal')
d.card(1005,300,260,180,'API Marketplace','[Contenedor · NestJS 11]','Servicios, validación y proveedores de demo')
d.db(1335,285,260,195,'Base de datos','[Almacén · PostgreSQL]','Datos propios mediante Prisma')
d.line([(240,390),(345,390)],'Usa UI',(292,373))
d.line([(605,390),(675,390)],'Fetch',(640,373))
d.line([(935,390),(1005,390)],'JSON',(970,373))
d.line([(1265,390),(1335,390)],'Prisma',(1300,373))
d.line([(1135,480),(1135,640)],'Contratos reales por verificar',(1135,603),True,False)
d.line([(475,640),(1465,640)],planned=True,arrow=False)
for x,title,desc in [(345,'Seguridad y Usuarios','Identidad y acceso'),(675,'Productos y Ofertas','Catálogo, precios y stock'),(1005,'Ventas y Postventa','Pedido e historial'),(1335,'Despacho y Entrega','Cotización y envío')]:
    d.line([(x+130,640),(x+130,760)],'Previsto',(x+130,707),True)
    d.card(x,760,260,140,title,'[Sistema externo]',desc,GRAY)
d.text(850,961,'Las conexiones de código no acreditan que el despliegue o la integración real estén completos.',15)
d.save('c4-02-contenedores.svg')

# C4 3A: component families in the frontend.
d=Drawing(1600,1080,'Canal Marketplace · C4 nivel 3A','Componentes del frontend · Aplicación Next.js / React')
d.boundary(45,210,1510,625,'Aplicación web Marketplace','Páginas, funcionalidades, estado y fachada de servidor')
d.card(110,335,300,150,'Páginas App Router','[Componente · src/app]','Define rutas y compone la pantalla')
d.card(590,335,340,150,'UI de funcionalidades','[Componente · src/features]','Catálogo, ficha, acceso, carrito, checkout, favoritos y pedidos')
d.card(1110,335,300,150,'Componentes visuales','[Componente · shared/ui]','Campos, botones, estados y elementos del marco visual')
d.card(590,615,340,150,'Estado y servicios','[Componente · Hooks / Context]','Fetch, estados y WishlistProvider')
d.card(1110,615,300,150,'Fachada HTTP','[Componente · /api]','Proxies y validación del transporte al backend')
d.card(110,615,300,150,'Sandbox local','[Componente · MOCK]','Sesión y tokens sintéticos de desarrollo',AMBER)
d.card(1110,915,300,120,'API Marketplace','[Contenedor · NestJS]','Servicios del canal',GRAY)
d.line([(410,410),(590,410)],'Compone',(500,393))
d.line([(930,410),(1110,410)],'Reutiliza',(1020,393))
d.line([(760,485),(760,615)],'Acciones y estado',(760,558))
d.line([(930,690),(1110,690)],'Fetch',(1020,673))
d.line([(1260,765),(1260,915)],'HTTP JSON',(1260,876))
d.line([(1110,725),(1020,725),(1020,798),(260,798),(260,765)],'Solo con demo habilitada',(635,790),True)
d.card(420,115,300,80,'Cliente / Navegador','[Actor externo]','',GRAY)
d.line([(570,195),(570,315),(260,315),(260,335)],'Navegación',(570,295))
d.save('c4-03-componentes-frontend.svg')

# C4 3B: entry, functional services, providers and persistence on separate rows.
d=Drawing(1800,1260,'Canal Marketplace · C4 nivel 3B','Componentes del backend · API NestJS y proveedores de demostración')
d.boundary(45,270,1700,885,'API Marketplace · NestJS','Controladores y servicios por funcionalidad; datos propios separados de los proveedores externos')
d.card(690,110,420,120,'Fachada web','[Contenedor · Next.js /api]','Solicitudes del navegador',GRAY)
d.card(690,375,420,135,'Controladores REST','[Componente · NestJS / DTO]','Catálogo, acceso, carrito, favoritos, checkout y pedidos')
d.card(1300,375,350,135,'Identidad y autorización','[Componente · Guards]','Valida tokens y principal en rutas protegidas')
d.line([(900,230),(900,375)],'HTTP JSON',(900,338))
d.line([(1110,442),(1300,442)],'Rutas protegidas',(1205,424))
d.line([(900,510),(900,585)],'Delega a servicios',(900,562),arrow=False)
d.line([(230,585),(1550,585)],arrow=False)
services=[(90,'Detalle y acceso','ProductDetailService / AuthService','Ficha F-011 y validación F-002 con datos de prueba'),(420,'Carrito','CartService','Ítems y estado de carrito'),(750,'Favoritos','Wishlist services','Guardar, leer y coordinar con carrito'),(1080,'Checkout','CheckoutService / QuotesService','Preparación, resumen e idempotencia'),(1410,'Historial','OrdersService','Proyección de pedidos del titular de prueba')]
for x,title,tech,desc in services:
    d.line([(x+140,585),(x+140,650)])
    d.card(x,650,280,165,title,'[Componente]',desc,LIGHT)
d.line([(750,730),(700,730)])
d.card(135,980,490,135,'Proveedores de demostración','[Componentes · MOCK]','Fixtures, puertos sandbox, MarketplaceGateway y MockHttpAdapter',AMBER)
d.card(1090,980,490,135,'Persistencia propia','[Componente · Prisma / repositorios]','Carrito, favoritos y operación de checkout')
d.db(1320,100,370,130,'PostgreSQL','[Almacén de datos]','Esquema propio')
# Provider connections use an amber lane; persistence uses a separate lower lane.
for cx in [230,890,1220,1550]:
    d.line([(cx,815),(cx,866)],planned=True,arrow=False)
d.line([(230,866),(1550,866)],planned=True,arrow=False)
d.line([(380,866),(380,980)],'Datos de prueba',(380,934),True)
for cx in [560,890,1220]:
    d.line([(cx+16,815),(cx+16,924)],arrow=False)
d.line([(576,924),(1335,924)],arrow=False)
d.line([(1335,924),(1335,980)],'Lee y escribe',(1445,951))
d.line([(1580,1047),(1777,1047),(1777,185),(1690,185)],'Prisma',(1720,675))
d.text(900,1210,'MOCK: respuesta sintética · El esquema no acredita integraciones reales ni un worker de correo operativo.',15)
d.save('c4-04-componentes-backend.svg')

# Architecture overview: preserve the layered view with a stable, readable layout.
d=Drawing(1800,1340,'Arquitectura de la Aplicación · Canal Marketplace','Frontend, backend, persistencia e integración · Inka Athletics · Hito 3')
green=('#e5f4ec','#29754f','#17462f')
d.text(900,118,'Cliente / Visitante · Accede desde el navegador web',17)
d.boundary(60,155,1680,290,'A · Frontend web — Next.js / React','Páginas y componentes, estado de la experiencia y fachada de servidor')
d.card(170,265,400,140,'Interfaz React','Páginas y componentes','Catálogo, ficha, acceso, carrito, favoritos, checkout y pedidos',LIGHT)
d.card(700,265,400,140,'Estado de funcionalidad','Hooks / Context / Fetch','Estado local, solicitudes y WishlistProvider',LIGHT)
d.card(1230,265,400,140,'Fachada de servidor','Next.js · Route Handlers','Proxies /api y controles de transporte',LIGHT)
d.line([(570,335),(700,335)],'Acciones',(635,318))
d.line([(1100,335),(1230,335)],'Fetch',(1165,318))
d.boundary(60,525,1680,415,'B · Backend de aplicación — NestJS','Controladores, servicios, guards, persistencia y proveedores')
d.card(170,635,300,140,'Entrada HTTP','Controladores / DTO','Validación y respuesta de API',green)
d.card(700,635,400,140,'Servicios de aplicación','Módulos por funcionalidad','Producto, carrito, favoritos, checkout e historial',green)
d.card(1230,635,400,140,'Puertos y gateway','Contratos de integración','Traduce contratos y encapsula proveedores',green)
d.card(170,820,300,90,'Identidad y autorización','Guards de rutas protegidas','',green)
d.card(700,820,400,90,'Persistencia','PrismaService / repositorios','',green)
d.line([(1430,405),(1430,483),(585,483),(585,610),(320,610),(320,635)],'HTTP / JSON',(900,476))
d.line([(470,705),(700,705)],'Delega',(585,688))
d.line([(1100,705),(1230,705)],'Consulta',(1165,688))
d.line([(320,775),(320,820)])
d.line([(900,775),(900,820)])
d.db(170,1075,400,165,'PostgreSQL propio','Prisma · seis modelos','Carrito, favoritos y control operativo')
d.card(700,1075,400,165,'Datos de demostración','Fixtures / adaptadores MOCK','Producto, acceso, historial, elegibilidad y checkout',AMBER)
d.card(1230,1075,400,165,'Sistemas externos','Integraciones reales previstas','Seguridad · Productos · Ventas · Despacho',GRAY)
d.line([(900,910),(900,990),(370,990),(370,1075)],'Datos propios',(610,982))
d.line([(1100,740),(1170,740),(1170,1030),(900,1030),(900,1075)],'Respuesta MOCK',(1170,1005),True)
d.line([(1430,775),(1430,1075)],'Contratos por verificar',(1430,1005),True)
d.text(900,1300,'Azul: frontend · Verde: backend · Ámbar: demostración · Gris: sistemas propietarios externos',16)
d.save('arquitectura-general.svg')

print('Generados 5 diagramas SVG en', DEST)
