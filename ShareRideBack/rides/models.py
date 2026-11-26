from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    """Application user, mirrors the ``users`` table in database/schema.sql."""

    DRIVER = 'driver'
    PASSENGER = 'passenger'
    ROLE_CHOICES = [
        (DRIVER, 'Driver'),
        (PASSENGER, 'Passenger'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'{self.name} ({self.email})'


class Trip(models.Model):
    """Trip offered by a driver, mirrors the ``trips`` table."""

    STATUS_ACTIVE = 'active'
    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
    ]

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='trips',
    )
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    trip_date = models.DateField()
    trip_start = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_ACTIVE)

    class Meta:
        db_table = 'trips'
        constraints = [
            models.CheckConstraint(condition=models.Q(price__gte=0), name='trips_price_gte_0'),
            models.CheckConstraint(condition=models.Q(total_seats__gt=0), name='trips_total_seats_gt_0'),
        ]

    def __str__(self):
        return f'{self.from_city} -> {self.to_city} ({self.trip_date})'


class Booking(models.Model):
    """Seats booked on a trip, mirrors the ``bookings`` table."""

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    passenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    seats_booked = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bookings'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(seats_booked__gt=0),
                name='bookings_seats_booked_gt_0',
            ),
        ]

    def __str__(self):
        return f'Booking #{self.pk} for trip #{self.trip_id}'


class Review(models.Model):
    """Review left for a driver after a trip, mirrors the ``reviews`` table."""

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    passenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_written',
    )
    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_received',
    )
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'reviews'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name='reviews_rating_between_1_and_5',
            ),
        ]

    def __str__(self):
        return f'Review #{self.pk} ({self.rating}/5)'
