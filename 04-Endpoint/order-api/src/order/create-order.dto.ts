import { IsArray, IsEnum, IsNumber, IsPositive, IsString, Min } from 'class-validator';

enum Estrato {
  E1 = 1,
  E2 = 2,
  E3 = 3,
  E4 = 4,
  E5 = 5,
  E6 = 6,
}

class ProductDto {
  @IsString()
  name: string;

  @IsNumber()
  @IsPositive()
  price: number;

  @IsNumber()
  @IsPositive()
  quantity: number;
}

export class CreateOrderDto {
  @IsArray()
  products: ProductDto[];

  @IsEnum(Estrato)
  estrato: Estrato;
}
