"""
Design a exchange system that mimics a stock exchange order system

Class
Order
- LimitOrder
- MarketOrder
- StopMarketOrder
- StopLimitOrder

Order Pool
- Limit Order Pool
- Stop Order Pool

Market:
- Security
- Ask Pool
- Bid Pool
- Best Ask
- Best Bid

Invokation

market = Market("TSLA_US_EQUITY")

order1 = factory.make_limit_order(side='A', quantity=100, price=250.0)
order2 = factory.make_limit_order(side='B', quantity=50, price=251.5)

order1.execute()
order2.execute()

market_order_status = factory.make_market_order(side='B', quantity=150).execute()

order4 = factory.make_stop_market_order(side='A', quantity=100, stop=240)

order4.execute()

"""

from typing import List
from enum import Enum
import heapq
import logging

order_id_count = 0

class OrderSide(Enum):
    ASK = 'ASK'
    BID = 'BID'


class Order:
    def __init__(self, security: str, side: OrderSide, quantity: int):
        self.security = security
        self.side = side
        self.id = order_id_count
        self.quantity = quantity
        self.executed = False
        self.traded = False
        order_id_count += 1

    def __repr__(self):
        return '<#{} {} order for {}>'.format(self.id, self.side, self.security)

    def fill(amount: int):
        logging.info('Order {} filled by {}'.format(self.id, amount))

class MarketOrder(Order):
    def __init__(self, security: str, side: OrderSide, quantity: int):
        super(MarketOrder, self).__init__(security, side, quantity)

    def __repr__(self):
        repr = super(MarketOrder, self).__repr__()
        return repr + ': quantity {}'.format(self.quantity)

class LimitOrder(Order):
    def __init__(self, security: str, side: OrderSide, quantity: int,
                 limit_price: float):
        super(LimitOrder, self).__init__(security, side, quantity




        )
        self.limit_price = limit_price

    def __repr__(self):
        repr = super(limitOrder, self).__repr__()
        return repr + ': quantity {} limit_price {}'.format(self.quantity, self.limit_price)


class StopMixin:
    def convert_order(self):
        raise NotImplementedError

    def trigger_stop(self) -> bool:
        pass

    def process_new_price(self, last_traded_price: float):
        if self.trigger_stop(last_traded_price):
            self.convert_order()
            self.execute()

    def stop_if_greater_equal(self, last_traded_price: float) -> bool:
        if last_traded_price >= self.stop_price:
            return True
        else:
            return False

    def stop_if_less_equal(self, last_traded_price: float) -> bool:
        if last_traded_price <= self.stop_price:
            return True
        else:
            return False

    def set_stop(self, last_traded_price: float):
        if self.side == OrderSide.BID:
            if self.stop_price <= last_traded_price:
                logging.warning(
                    "Current trading price is above stop price, stop bid order will be converted immediately"
                )
            self.trigger_stop = self.stop_if_greater_equal
        if self.side == OrderSide.ASK:
            if self.stop_price >= last_traded_price:
                logging.warning(
                    "Current trading price is below stop price, stop ask order will be converted immediately"
                )
            self.trigger_stop = self.stop_if_less_equal


class StopMarketOrder(MarketOrder, StopMixin):
    def __init__(self, security: str, side: OrderSide, quantity: int,
                 stop_price: float):
        super(StopMarketOrder, self).__init__(security, side, quantity)
        self.stop_price = stop_price

    def convert_order(self):
        pass


class StopLimitOrder(LimitOrder, StopMixin):
    def __init__(self, security: str, side: OrderSide, quantity: int,
                 limit_price: float, stop_price: float):
        super(StopLimitOrder, self).__init__(security, side, quantity,
                                             limit_price)
        self.stop_price = stop_price

    def convert_order(self):
        pass


class Market:
    def __init__(self, security: str):
        self.security = str
        self.asks = []  # sorted by price, low -> high
        self.bids = []  # sorted by price, high -> low
        self.stop_orders = []
        self.last_trading_price = None

    def cascade(self):
        pass

    def best_bid_price(self):
        return self.bid_heap[0].limit_price if self.bid_heap else None

    def best_ask_price(self):
        return self.ask_heap[0].limit_price if self.ask_heap else None

    def execute_order(self, order: Order):
        if isinstance(order, LimitOrder):
            if order.side == OrderSide.ASK:
                for bid in bids:
                    if bid.limit_price >= order.limit_price:
                        logging.info("Matched {} and {}".format(order, bid))
                        fill_amount = min(bid.quantity, order.quantity)
                        bid.fill(fill_amount)
                        order.fill(fill_amount)
                        if bid.quantity == 0:
                            self.bids.pop

        elif isinstance(order, MarketOrder):
            # market order processing
        else:
            pass

