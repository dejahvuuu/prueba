import { Injectable, BadRequestException } from '@nestjs/common';
import { CreateOrderDto } from './create-order.dto';

@Injectable()
export class OrderService {

  private readonly shippingCosts = {
    1: 5000,
    2: 7000,
    3: 10000,
    4: 15000,
    5: 20000,
    6: 25000,
  };

  private readonly discountThreshold = 100000;

  private readonly discountPercentage = 10;

  calculateOrder(createOrderDto: CreateOrderDto): any {
    const { products, estrato } = createOrderDto;

    if (!products || products.length === 0) {
      throw new BadRequestException('El pedido debe tener al menos un producto.');
    }

    let subtotal = 0;
    products.forEach((product) => {
      subtotal += product.price * product.quantity;
    });

    const shippingCost = this.shippingCosts[estrato] || 0;

    const totalBeforeDiscount = subtotal + shippingCost;

    let discount = 0;
    if (totalBeforeDiscount >= this.discountThreshold) {
      discount = (totalBeforeDiscount * this.discountPercentage) / 100;
    }

    const finalTotal = totalBeforeDiscount - discount;

    return {
      subtotal,
      shippingCost,
      discount,
      total: finalTotal,
    };
  }
}
