import java.util.*;

public class Order {
	private String id;
	private double price;
	private int quantity;
	private OrderSide side;
	private OrderType type;
	private OrderStatus status;

	public Order(String id, double price, int quantity, OrderSide side, OrderType type) {
		this.id = id;
		this.price = price;
		this.quantity = quantity;
		this.side = side;
		this.type = type;
		this.status = OrderStatus.PENDING;
	}
	public Order(String id, double price, int quantity, OrderSide side) {
		this(id, price, quantity, side, OrderType.MARKET);
	}
	public Order(String id, double price, int quantity, OrderType type) {
		this(id, price, quantity, OrderSide.BUY, type);
	}
	public Order(String id, double price, int quantity) {
		this(id, price, quantity, OrderSide.BUY, OrderType.MARKET);
	}

	public String getId() {
		return id;
	}

	public double getPrice() {
		return price;
	}

	public int getQuantity() {
		return quantity;
	}

	public OrderSide getSide() {
		return side;
	}

	public OrderType getType() {
		return type;
	}

	public OrderStatus getStatus() {
		return status;
	}

	public void setStatus(OrderStatus status) {
		this.status = status;
	}
}