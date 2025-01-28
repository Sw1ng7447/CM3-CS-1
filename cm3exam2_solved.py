# -*- coding: utf-8 -*-
"""CM3Exam2 - Solved Version"""

class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.current = 0
        self.is_filled = False

    def add(self, value):
        self.buffer[self.current] = value
        self.current = (self.current + 1) % self.size
        if self.current == 0:
            self.is_filled = True

    def get_inorder(self):
        if not self.is_filled:
            return [x for x in self.buffer[:self.current] if x is not None]
        return self.buffer[self.current:] + self.buffer[:self.current]

    def get_all(self):
        return self.get_inorder()

    def is_full(self):
        return self.is_filled

    def current_size(self):
        return self.size if self.is_filled else self.current


class MovingAverageCalculator:
    def __init__(self, window_size):
        self.buffer = RingBuffer(window_size)

    def add_number(self, value):
        self.buffer.add(value)

    def get_average(self):
        values = self.buffer.get_all()
        if not values:
            raise ValueError("No numbers added yet")
        return sum(values) / len(values)


class TradingSystem:
    def __init__(self, history_size=100, short_ma_size=20, long_ma_size=50):
        self.price_history = RingBuffer(history_size)
        self.short_ma = MovingAverageCalculator(short_ma_size)
        self.long_ma = MovingAverageCalculator(long_ma_size)

    def add_price(self, price):
        self.price_history.add(price)
        self.short_ma.add_number(price)
        self.long_ma.add_number(price)

    def get_state(self):
        try:
            return {
                'current_price': self.price_history.get_all()[-1],
                'short_ma': self.short_ma.get_average(),
                'long_ma': self.long_ma.get_average(),
                'price_history': self.price_history.get_all()
            }
        except (IndexError, ValueError):
            return "Insufficient data"

    def get_signal(self):
        try:
            short_avg = self.short_ma.get_average()
            long_avg = self.long_ma.get_average()
            if short_avg > long_avg:
                return "BUY"
            elif short_avg < long_avg:
                return "SELL"
            else:
                return "HOLD"
        except ValueError:
            return "HOLD"


# Testing the implementation
def test_ring_buffer():
    buffer = RingBuffer(3)
    assert buffer.get_all() == [], "New buffer should be empty"

    buffer.add(1)
    assert buffer.get_all() == [1], "Buffer should contain [1]"

    buffer.add(2)
    buffer.add(3)
    assert buffer.get_all() == [1, 2, 3], "Buffer should contain [1, 2, 3]"

    buffer.add(4)
    assert buffer.get_all() == [2, 3, 4], "Buffer should overwrite oldest value"

    print("RingBuffer tests passed!")


def test_moving_average():
    calc = MovingAverageCalculator(3)
    calc.add_number(1)
    assert abs(calc.get_average() - 1.0) < 1e-10

    calc.add_number(2)
    assert abs(calc.get_average() - 1.5) < 1e-10

    calc.add_number(3)
    assert abs(calc.get_average() - 2.0) < 1e-10

    calc.add_number(4)
    assert abs(calc.get_average() - 3.0) < 1e-10

    print("MovingAverageCalculator tests passed!")


def test_trading_system():
    trading = TradingSystem(history_size=5, short_ma_size=3, long_ma_size=4)
    prices = [100, 101, 99, 102, 98, 103]
    expected_signals = ["HOLD", "HOLD", "HOLD", "BUY", "SELL", "BUY"]

    for i, price in enumerate(prices):
        trading.add_price(price)
        assert trading.get_signal() == expected_signals[i], f"Failed at price {price}"

    print("TradingSystem tests passed!")


# Run tests
test_ring_buffer()
test_moving_average()
test_trading_system()
