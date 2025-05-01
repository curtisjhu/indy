import java.util.*;

public class OrderBook {
	// OrderID 
	TreeMap<Double, List<Order>> buyOrders = new TreeMap<>(Collections.reverseOrder());
	TreeMap<Double, List<Order>> sellOrders = new TreeMap<>();

	public OrderBook() {
		// Initialize the order book with empty buy and sell orders

	}

	public void cacheOrders() {

	}

	public void addOrder(Order order) {
		if (order.getSide() == OrderSide.BUY) {
			buyOrders.computeIfAbsent(order.getPrice(), k -> new ArrayList<>()).add(order);
		} else {
			sellOrders.computeIfAbsent(order.getPrice(), k -> new ArrayList<>()).add(order);
		}
	}

	public void removeOrder(Order order) {
		if (order.getSide() == OrderSide.BUY) {
			List<Order> orders = buyOrders.get(order.getPrice());
			if (orders != null) {
				orders.remove(order);
				if (orders.isEmpty()) {
					buyOrders.remove(order.getPrice());
				}
			}
		} else {
			List<Order> orders = sellOrders.get(order.getPrice());
			if (orders != null) {
				orders.remove(order);
				if (orders.isEmpty()) {
					sellOrders.remove(order.getPrice());
				}
			}
		}
	}

	
}