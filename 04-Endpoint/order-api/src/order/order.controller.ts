import { Body, Controller, Post } from '@nestjs/common';
import { ApiTags, ApiResponse, ApiOperation, ApiBody } from '@nestjs/swagger';
import { OrderService } from './order.service';
import { CreateOrderDto } from './create-order.dto';

@ApiTags('orders')
@Controller('orders')
export class OrderController {
  constructor(private readonly orderService: OrderService) {}

  @Post()
  @ApiOperation({ summary: 'Crear un nuevo pedido' })
  @ApiBody({
    description: 'Payload para crear un pedido',
    required: true,
    schema: {
      example: {
        products: [
          { name: 'Pizza', price: 25000, quantity: 2 },
          { name: 'Hamburguesa', price: 18000, quantity: 1 },
        ],
        estrato: 3,
      },
    },
  })
  @ApiResponse({
    status: 201,
    description: 'Pedido creado correctamente',
    schema: {
      example: {
        subtotal: 68000,
        shippingCost: 10000,
        discount: 0,
        total: 78000,
      },
    },
  })  
  @ApiResponse({
    status: 400,
    description: 'Error en la validación del payload',
    schema: {
      example: {
        statusCode: 400,
        message: ['products debe ser una lista de productos válidos'],
        error: 'Bad Request',
      },
    },
  })  
  createOrder(@Body() createOrderDto: CreateOrderDto) {
    return this.orderService.calculateOrder(createOrderDto);
  }
}
