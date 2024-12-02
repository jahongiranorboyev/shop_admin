from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class Coupon(AbstractBaseModel):
    """
    Model for managing coupons. This includes discounts and promotions.

    Fields:
        - title: Name of the coupon.
        - code: Unique coupon code.
        - start_date: Start date of the coupon's validity.
        - end_date: End date of the coupon's validity.
        - free_shipping: Boolean flag to enable free shipping.
        - quantity: Number of available coupon instances.
        - discount_percent: Discount percentage (from 0% to 100%).
        - status: Status of the coupon (active or inactive).
    """
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    free_shipping = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    discount_percent = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CouponRestriction(AbstractBaseModel):
    """
    Model for managing coupon restrictions. Defines the conditions and limitations
    for applying a coupon.

    Fields:
        - coupon: The coupon associated with the restriction.
        - products: The specific product the coupon applies to.
        - category: The product category the coupon applies to.
        - minimum_spend: Minimum spending amount required to use the coupon.
        - maximum_spend: Maximum spending amount allowed to use the coupon.
    """
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    products = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    category = models.ForeignKey(to='categories.Category', on_delete=models.CASCADE)
    minimum_spend = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    maximum_spend = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )


class CouponUsage(AbstractBaseModel):
    """
    Model for managing coupon usage limits. Tracks usage limitations
    per coupon and per customer.

    Fields:
        - coupon: The coupon associated with the usage limits.
        - per_limited: Total number of times the coupon can be used.
        - per_customer: Maximum number of times a customer can use the coupon.
    """
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    per_limited = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    per_customer = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
