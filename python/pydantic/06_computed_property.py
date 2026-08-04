from pydantic import BaseModel, Field, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    # computer fields are calculated on demand and we use decorators
    # to define computer fields @computed_fields, @property
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(user_id=123, room_id=404, nights=3, rate_per_night=1200)

print(booking.total_amount)
print(
    booking.model_dump()
)  # total amount will show up here as it is marked as property
