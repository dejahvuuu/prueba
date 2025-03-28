import { Test, TestingModule } from '@nestjs/testing';
import { OrderService } from '../order.service';
import { CreateOrderDto } from '../create-order.dto';

describe('OrderService', () => {
  let orderService: OrderService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [OrderService],
    }).compile();

    orderService = module.get<OrderService>(OrderService);
  });

  it('Debe calcular correctamente el total sin descuento', () => {
    const payload: CreateOrderDto = {
      products: [
        { name: 'Pizza', price: 20000, quantity: 2 },
        { name: 'Hamburguesa', price: 15000, quantity: 1 },
      ],
      estrato: 3,
    };

    const result = orderService.calculateOrder(payload);
    expect(result.subtotal).toBe(55000);
    expect(result.shippingCost).toBe(10000);
    expect(result.discount).toBe(0);
    expect(result.total).toBe(65000);
  });

  it('Debe aplicar un descuento si el total supera 100000', () => {
    const payload: CreateOrderDto = {
      products: [
        { name: 'Pizza', price: 40000, quantity: 3 },
        { name: 'Hamburguesa', price: 30000, quantity: 2 },
      ],
      estrato: 5,
    };

    const result = orderService.calculateOrder(payload);
    expect(result.subtotal).toBe(180000);
    expect(result.shippingCost).toBe(20000);
    expect(result.discount).toBe(20000);
    expect(result.total).toBe(180000);
  });

  it('Debe lanzar una excepción si no hay productos', () => {
    const payload: CreateOrderDto = {
      products: [],
      estrato: 2,
    };

    expect(() => orderService.calculateOrder(payload)).toThrow(
      'El pedido debe tener al menos un producto.',
    );
  });
});
