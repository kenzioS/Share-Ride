-- 1. Таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('driver', 'passenger')),
    phone VARCHAR(20)
);

-- 2. Таблица поездок
CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    driver_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    from_city VARCHAR(100) NOT NULL,
    to_city VARCHAR(100) NOT NULL,
    trip_date DATE NOT NULL,
    trip_start TIME NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    total_seats INT NOT NULL CHECK (total_seats > 0),
    status VARCHAR(30) NOT NULL DEFAULT 'active'
);

-- 3. Таблица бронирований
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    trip_id INT NOT NULL REFERENCES trips(id) ON DELETE CASCADE,
    passenger_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    seats_booked INT NOT NULL CHECK (seats_booked > 0),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 4. Таблица отзывов
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    trip_id INT NOT NULL REFERENCES trips(id) ON DELETE CASCADE,
    passenger_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    driver_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT
);