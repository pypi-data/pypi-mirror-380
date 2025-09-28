#!/usr/bin/env python3
"""
Example usage of the MTB Observer pattern.

This example demonstrates the improved Observer/Observable pattern with
proper error handling, weak references, and async support.
"""

import asyncio
import time

from mtb.core.observer import FunctionObserver, Observable, Observer, Property
from rich.console import Console

console = Console()


class NewsPublisher(Observable):
    """Example observable that publishes news articles."""

    def __init__(self):
        super().__init__()
        self.articles = []

    def publish_article(self, title: str, content: str):
        """Publish a new article and notify subscribers."""
        article = {"title": title, "content": content, "timestamp": time.time()}
        self.articles.append(article)
        console.print(f"[blue]📰 Publishing:[/blue] {title}")
        self.notify("new_article", article)

    def breaking_news(self, title: str, content: str):
        """Publish breaking news with async notifications."""
        article = {"title": title, "content": content, "timestamp": time.time(), "breaking": True}
        self.articles.append(article)
        console.print(f"[red]🚨 BREAKING NEWS:[/red] {title}")
        return asyncio.create_task(self.notify_async("breaking_news", article))


class NewsSubscriber(Observer):
    """Example observer that receives news updates."""

    def __init__(self, name: str):
        self.name = name
        self.received_articles = []

    def update(self, observable: Observable, event_type: str, *args, **kwargs):
        """Handle news updates."""
        if event_type == "new_article":
            article = args[0]
            self.received_articles.append(article)
            console.print(f"[green]📧 {self.name}:[/green] Received '{article['title']}'")

        elif event_type == "breaking_news":
            article = args[0]
            self.received_articles.append(article)
            console.print(f"[yellow]🚨 {self.name}:[/yellow] URGENT - {article['title']}")


class AsyncNewsSubscriber(Observer):
    """Async observer that simulates processing time."""

    def __init__(self, name: str, delay: float = 0.5):
        self.name = name
        self.delay = delay
        self.processed_count = 0

    async def update(self, observable: Observable, event_type: str, *args, **kwargs):
        """Handle news updates asynchronously."""
        if event_type == "breaking_news":
            article = args[0]
            console.print(f"[cyan]⚙️ {self.name}:[/cyan] Processing '{article['title']}'...")
            await asyncio.sleep(self.delay)  # Simulate processing time
            self.processed_count += 1
            console.print(f"[cyan]✅ {self.name}:[/cyan] Processed article #{self.processed_count}")


def demo_basic_observer_pattern():
    """Demonstrate basic observer pattern usage."""
    console.print("\n[bold blue]Demo: Basic Observer Pattern[/bold blue]")

    # Create publisher and subscribers
    news = NewsPublisher()
    alice = NewsSubscriber("Alice")
    bob = NewsSubscriber("Bob")

    # Subscribe to news
    news.subscribe(alice)
    news.subscribe(bob)

    # Publish some articles
    news.publish_article("Tech Update", "New Python version released!")
    news.publish_article("Weather", "Sunny skies ahead")

    # Show what each subscriber received
    console.print(f"\n[dim]Alice received {len(alice.received_articles)} articles[/dim]")
    console.print(f"[dim]Bob received {len(bob.received_articles)} articles[/dim]")


async def demo_async_observers():
    """Demonstrate async observer notifications."""
    console.print("\n[bold blue]Demo: Async Observer Notifications[/bold blue]")

    news = NewsPublisher()

    # Mix of sync and async subscribers
    charlie = NewsSubscriber("Charlie")
    processor1 = AsyncNewsSubscriber("AI Processor", 0.3)
    processor2 = AsyncNewsSubscriber("News Analyzer", 0.5)

    news.subscribe(charlie)
    news.subscribe(processor1)
    news.subscribe(processor2)

    # Publish breaking news (async notifications)
    console.print("Publishing breaking news with async processing...")
    task = news.breaking_news("Market Crash", "Stock market drops 10%")
    await task

    console.print("[green]All async processing completed![/green]")


def demo_observable_properties():
    """Demonstrate observable properties."""
    console.print("\n[bold blue]Demo: Observable Properties[/bold blue]")

    # Create observable properties
    temperature = Property(20.0)
    status = Property("online")

    # Create observers for property changes
    def temp_monitor(observable, old_val, new_val):
        console.print(f"🌡️ Temperature changed: {old_val}°C → {new_val}°C")
        if new_val > 25:
            console.print("  [red]⚠️ High temperature alert![/red]")

    def status_monitor(observable, old_val, new_val):
        color = "green" if new_val == "online" else "red"
        console.print(f"🔌 Status changed: {old_val} → [{color}]{new_val}[/{color}]")

    # Subscribe using function observers
    temperature.subscribe(FunctionObserver(temp_monitor))
    status.subscribe(FunctionObserver(status_monitor))

    console.print("Simulating property changes...")

    # Change values and see notifications
    temperature.set(22.5)
    temperature.set(28.0)  # Should trigger alert
    status.set("offline")
    status.set("online")

    # Show current values
    console.print(f"\n[dim]Final temperature: {temperature.get()}°C[/dim]")
    console.print(f"[dim]Final status: {status.get()}[/dim]")


def demo_unsubscribe_and_cleanup():
    """Demonstrate unsubscription and automatic cleanup."""
    console.print("\n[bold blue]Demo: Unsubscription & Cleanup[/bold blue]")

    publisher = NewsPublisher()

    # Create subscribers
    subscriber1 = NewsSubscriber("Temp Subscriber")
    subscriber2 = NewsSubscriber("Permanent Subscriber")

    publisher.subscribe(subscriber1)
    publisher.subscribe(subscriber2)

    console.print(f"Active observers: {publisher.observer_count}")

    # Publish article
    publisher.publish_article("Test Article", "Testing subscriptions")

    # Unsubscribe one
    publisher.unsubscribe(subscriber1)
    console.print(f"After unsubscription: {publisher.observer_count} observers")

    # Publish another article
    publisher.publish_article("Second Article", "Only permanent subscriber should get this")

    # Demonstrate automatic cleanup of garbage collected observers
    del subscriber2
    publisher.cleanup()
    console.print(f"After cleanup: {publisher.observer_count} observers")


async def demo_error_handling():
    """Demonstrate error handling in observers."""
    console.print("\n[bold blue]Demo: Error Handling[/bold blue]")

    class BuggyObserver(Observer):
        def update(self, observable, *args, **kwargs):
            raise Exception("Simulated observer error!")

    class WorkingObserver(Observer):
        def update(self, observable, *args, **kwargs):
            console.print("[green]✅ Working observer got the notification[/green]")

    publisher = NewsPublisher()
    buggy = BuggyObserver()
    working = WorkingObserver()

    publisher.subscribe(buggy)
    publisher.subscribe(working)

    console.print("Publishing with buggy observer (errors will be logged)...")
    publisher.publish_article("Error Test", "Testing error handling")

    console.print("[dim]Notice: Errors were caught and logged, other observers still worked[/dim]")


def demo_using_observable_parameter():
    """Demonstrate practical uses of the observable parameter."""
    console.print("\n[bold blue]Demo: Using the Observable Parameter[/bold blue]")

    # Scenario: Smart home system with multiple sensors
    class Sensor(Observable):
        def __init__(self, name: str, room: str):
            super().__init__()
            self.name = name
            self.room = room
            self.value = 0
            self.alert_threshold = None

        def set_alert_threshold(self, threshold):
            self.alert_threshold = threshold

        def update_reading(self, value):
            old_value = self.value
            self.value = value
            self.notify("reading_changed", old_value, value)

    class SmartHomeController(Observer):
        def __init__(self):
            self.actions_taken = []

        def update(self, observable, event_type, old_value, new_value):
            # USE OBSERVABLE: Access the sensor's properties
            sensor_name = observable.name
            room = observable.room
            threshold = observable.alert_threshold

            console.print(f"🏠 {sensor_name} in {room}: {old_value} → {new_value}")

            # USE OBSERVABLE: Make decisions based on which sensor changed
            if threshold and new_value > threshold:
                if observable.name == "Temperature":
                    action = f"Turn on AC in {room}"
                elif observable.name == "Humidity":
                    action = f"Turn on dehumidifier in {room}"
                elif observable.name == "Motion":
                    action = f"Turn on lights in {room}"
                else:
                    action = f"Alert: High {sensor_name} in {room}"

                self.actions_taken.append(action)
                console.print(f"  🚨 [red]ACTION:[/red] {action}")

    # Set up smart home system
    temp_sensor = Sensor("Temperature", "Living Room")
    humidity_sensor = Sensor("Humidity", "Bathroom")
    motion_sensor = Sensor("Motion", "Hallway")

    # Set thresholds
    temp_sensor.set_alert_threshold(25)
    humidity_sensor.set_alert_threshold(70)
    motion_sensor.set_alert_threshold(5)

    # Single controller watches all sensors
    controller = SmartHomeController()
    temp_sensor.subscribe(controller)
    humidity_sensor.subscribe(controller)
    motion_sensor.subscribe(controller)

    console.print("Simulating sensor readings...")
    temp_sensor.update_reading(22)  # Normal
    temp_sensor.update_reading(28)  # Too hot!

    humidity_sensor.update_reading(65)  # Normal
    humidity_sensor.update_reading(75)  # Too humid!

    motion_sensor.update_reading(8)  # Motion detected!

    console.print(f"\n[green]Controller took {len(controller.actions_taken)} actions[/green]")


def demo_observable_chaining():
    """Demonstrate using observable parameter for chaining reactions."""
    console.print("\n[bold blue]Demo: Observable Chaining[/bold blue]")

    class StockPrice(Observable):
        def __init__(self, symbol: str):
            super().__init__()
            self.symbol = symbol
            self.price = 100.0
            self.history = []

        def update_price(self, new_price):
            old_price = self.price
            self.price = new_price
            self.history.append(new_price)
            self.notify("price_changed", old_price, new_price)

        def get_trend(self):
            if len(self.history) < 2:
                return "stable"
            recent = self.history[-3:]
            if all(recent[i] > recent[i-1] for i in range(1, len(recent))):
                return "rising"
            elif all(recent[i] < recent[i-1] for i in range(1, len(recent))):
                return "falling"
            return "volatile"

    class TradingBot(Observer):
        def __init__(self):
            self.portfolio = {}
            self.cash = 10000

        def update(self, observable, event_type, old_price, new_price):
            # USE OBSERVABLE: Get the stock symbol and analyze trend
            symbol = observable.symbol
            trend = observable.get_trend()

            console.print(f"📈 {symbol}: ${old_price:.2f} → ${new_price:.2f} (trend: {trend})")

            # USE OBSERVABLE: Make trading decisions based on the specific stock
            if symbol not in self.portfolio:
                self.portfolio[symbol] = 0

            if trend == "falling" and new_price < old_price * 0.95:
                # Buy on significant dips
                shares_to_buy = min(10, self.cash // new_price)
                if shares_to_buy > 0:
                    self.portfolio[symbol] += shares_to_buy
                    self.cash -= shares_to_buy * new_price
                    console.print(f"  🟢 [green]BUY:[/green] {shares_to_buy} shares of {symbol}")

            elif trend == "rising" and self.portfolio[symbol] > 0:
                # Sell some on rising trend
                shares_to_sell = min(5, self.portfolio[symbol])
                self.portfolio[symbol] -= shares_to_sell
                self.cash += shares_to_sell * new_price
                console.print(f"  🔴 [red]SELL:[/red] {shares_to_sell} shares of {symbol}")

    # Set up trading system
    apple_stock = StockPrice("AAPL")
    google_stock = StockPrice("GOOGL")

    bot = TradingBot()
    apple_stock.subscribe(bot)
    google_stock.subscribe(bot)

    console.print("Simulating market movements...")

    # Simulate price changes
    apple_stock.update_price(105.0)
    apple_stock.update_price(110.0)
    apple_stock.update_price(95.0)   # Big drop - should trigger buy
    apple_stock.update_price(98.0)
    apple_stock.update_price(102.0)  # Rising - should trigger sell

    google_stock.update_price(2800.0)
    google_stock.update_price(2750.0)
    google_stock.update_price(2600.0)  # Big drop - should trigger buy

    console.print(f"\n[dim]Bot portfolio: {bot.portfolio}[/dim]")
    console.print(f"[dim]Cash remaining: ${bot.cash:.2f}[/dim]")


async def main():
    """Run all observer pattern demonstrations."""
    console.print("[bold green]MTB Observer Pattern Demo[/bold green]")
    console.print("This demo shows the improved Observer/Observable pattern.\n")

    demos = [
        ("Basic Observer Pattern", demo_basic_observer_pattern),
        ("Async Observer Notifications", demo_async_observers),
        ("Observable Properties", demo_observable_properties),
        ("Unsubscription & Cleanup", demo_unsubscribe_and_cleanup),
        ("Error Handling", demo_error_handling),
        ("Using Observable Parameter", demo_using_observable_parameter),
        ("Observable Chaining", demo_observable_chaining),
    ]

    for name, demo_func in demos:
        console.print(f"\n[dim]Press Enter to run: {name}[/dim]")
        input()

        if asyncio.iscoroutinefunction(demo_func):
            await demo_func()
        else:
            demo_func()

    console.print("\n[green]All demos completed![/green]")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Demo cancelled. Goodbye![/yellow]")
