# API RESTful para gestión de pedidos en NestJS

Esta API permite gestionar pedidos, calcular costos totales con cargos por envío según el estrato socioeconómico y aplicar descuentos automáticos si el monto del pedido supera un umbral definido.

---

## Tecnologías utilizadas

- [NestJS](https://nestjs.com/) 
- [TypeScript](https://www.typescriptlang.org/)
- [Class-validator](https://github.com/typestack/class-validator) 
- [Jest](https://jestjs.io/) 

---

## Instalación del proyecto

### Instalar NestJS CLI 

```bash
npm install -g @nestjs/cli
```

### Clonar el proyecto

```bash
git clone https://github.com/dejahvuuu/prueba.git

cd 04-Endpoint/order-api

npm install

npm run start:dev
```

## Documentación API

POST http://localhost:3000/orders

### Payload ejemplo:

```json
{
  "products": [
    { "name": "Pizza", "price": 25000, "quantity": 2 },
    { "name": "Hamburguesa", "price": 18000, "quantity": 1 }
  ],
  "estrato": 3
}
```

### Respuesta exitosa:

```json
{
  "subtotal": 68000,
  "shippingCost": 10000,
  "discount": 0,
  "total": 78000
}
```

## Pruebas unitarias

```bash
npm run test
```

## Seguridad

En nest.js se puede implementar Guards que protegen las rutas de los endpoint de acceso no autorizado, no lo implemente por facilidad de prueba y ajustandome a los tiempos que tenía.

## Documentación API

Ir a http://localhost:3000/api