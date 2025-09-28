"""
System Monitor Demo - MTB Observer Pattern.

A practical demonstration of the observer pattern using real system monitoring.
Shows how multiple observers can watch different system metrics and react accordingly.
"""

import asyncio
import time

import psutil
from mtb.core.observer import Observable, Observer
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()


class SystemMetric(Observable):
    """Observable system metric that monitors a specific system value."""

    def __init__(
        self,
        name: str,
        unit: str = "",
        warning_threshold: float = 80.0,
        critical_threshold: float = 90.0,
    ):
        super().__init__()
        self.name = name
        self.unit = unit
        self.current_value = 0.0
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.history = []
        self.status = "normal"  # normal, warning, critical

    def update_value(self, new_value: float):
        """Update the metric value and notify observers."""
        old_value = self.current_value
        self.current_value = new_value
        self.history.append((time.time(), new_value))

        # Keep only last 60 readings for history
        if len(self.history) > 60:
            self.history.pop(0)

        # Determine status
        old_status = self.status
        if new_value >= self.critical_threshold:
            self.status = "critical"
        elif new_value >= self.warning_threshold:
            self.status = "warning"
        else:
            self.status = "normal"

        # Notify observers with comprehensive data
        self.notify("value_changed", old_value, new_value, old_status, self.status)

        # Special notification for status changes
        if old_status != self.status:
            self.notify("status_changed", old_status, self.status, new_value)

    def get_average(self, last_n: int = 10) -> float:
        """Get average of last N readings."""
        if not self.history:
            return 0.0
        recent = self.history[-last_n:] if len(self.history) >= last_n else self.history
        return sum(reading[1] for reading in recent) / len(recent)

    def get_trend(self) -> str:
        """Analyze trend from recent readings."""
        if len(self.history) < 3:
            return "stable"

        recent_values = [reading[1] for reading in self.history[-5:]]
        if len(recent_values) < 3:
            return "stable"

        # Simple trend analysis
        increasing = sum(
            1 for i in range(1, len(recent_values)) if recent_values[i] > recent_values[i - 1]
        )
        decreasing = sum(
            1 for i in range(1, len(recent_values)) if recent_values[i] < recent_values[i - 1]
        )

        if increasing > decreasing + 1:
            return "rising"
        elif decreasing > increasing + 1:
            return "falling"
        else:
            return "stable"


class SystemMonitor:
    """Main system monitor that collects metrics."""

    def __init__(self):
        # Create observable metrics
        self.cpu_usage = SystemMetric("CPU Usage", "%", 70.0, 85.0)
        self.memory_usage = SystemMetric("Memory Usage", "%", 75.0, 90.0)
        self.disk_usage = SystemMetric("Disk Usage", "%", 80.0, 95.0)
        self.cpu_temp = SystemMetric("CPU Temperature", "°C", 70.0, 85.0)

        self.metrics = [self.cpu_usage, self.memory_usage, self.disk_usage, self.cpu_temp]
        self.running = False

    async def collect_metrics(self):
        """Collect system metrics and update observables."""
        while self.running:
            try:
                # CPU Usage
                cpu_percent = psutil.cpu_percent(interval=0.1)
                self.cpu_usage.update_value(cpu_percent)

                # Memory Usage
                memory = psutil.virtual_memory()
                self.memory_usage.update_value(memory.percent)

                # Disk Usage (root partition)
                disk = psutil.disk_usage("/")
                disk_percent = (disk.used / disk.total) * 100
                self.disk_usage.update_value(disk_percent)

                # CPU Temperature (if available)
                # try:
                #     temps = psutil.sensors_temperatures()
                #     if temps:
                #         # Try to get CPU temperature
                #         cpu_temp = None
                #         for name, entries in temps.items():
                #             if "cpu" in name.lower() or "core" in name.lower():
                #                 cpu_temp = entries[0].current
                #                 break

                #         if cpu_temp:
                #             self.cpu_temp.update_value(cpu_temp)
                #         else:
                #             # Fallback: simulate temperature based on CPU usage
                #             simulated_temp = 30 + (cpu_percent * 0.5)
                #             self.cpu_temp.update_value(simulated_temp)
                #     else:
                #         # Simulate temperature if sensors not available
                #         simulated_temp = 30 + (cpu_percent * 0.5)
                #         self.cpu_temp.update_value(simulated_temp)
                # except Exception:
                #     # Fallback simulation
                #     simulated_temp = 30 + (cpu_percent * 0.5)
                #     self.cpu_temp.update_value(simulated_temp)

            except Exception as e:
                console.print(f"[red]Error collecting metrics: {e}[/red]")

            await asyncio.sleep(1)  # Update every second

    def start_monitoring(self):
        """Start the monitoring loop."""
        self.running = True
        return asyncio.create_task(self.collect_metrics())

    def stop_monitoring(self):
        """Stop the monitoring loop."""
        self.running = False


class AlertManager(Observer):
    """Observer that manages system alerts."""

    def __init__(self):
        self.active_alerts = {}
        self.alert_history = []

    def update(self, observable, event_type, *args, **kwargs):
        """Handle metric updates and generate alerts."""
        if event_type == "status_changed":
            old_status, new_status, current_value = args
            metric_name = observable.name

            if new_status in ["warning", "critical"]:
                # Create alert
                severity = "🟡 WARNING" if new_status == "warning" else "🔴 CRITICAL"
                message = f"{severity}: {metric_name} is {current_value:.1f}{observable.unit}"

                self.active_alerts[metric_name] = {
                    "severity": new_status,
                    "message": message,
                    "timestamp": time.time(),
                    "value": current_value,
                }

                self.alert_history.append(
                    {
                        "metric": metric_name,
                        "severity": new_status,
                        "value": current_value,
                        "timestamp": time.time(),
                        "type": "triggered",
                    }
                )

                # console.print(f"[bold red]🚨 ALERT: {message}[/bold red]")

            elif new_status == "normal" and metric_name in self.active_alerts:
                # Clear alert
                del self.active_alerts[metric_name]

                self.alert_history.append(
                    {
                        "metric": metric_name,
                        "severity": "normal",
                        "value": current_value,
                        "timestamp": time.time(),
                        "type": "cleared",
                    }
                )

                console.print(
                    f"[green]✅ CLEARED: {metric_name} back to normal ({current_value:.1f}{observable.unit})[/green]"
                )


class PerformanceAnalyzer(Observer):
    """Observer that analyzes performance trends."""

    def __init__(self):
        self.analysis_count = 0

    def update(self, observable, event_type, *args, **kwargs):
        """Analyze performance trends."""
        if event_type == "value_changed":
            old_value, new_value, old_status, new_status = args

            # Perform analysis every 10 updates to avoid spam
            self.analysis_count += 1
            if self.analysis_count % 10 == 0:
                trend = observable.get_trend()
                avg = observable.get_average()

                if trend == "rising" and avg > observable.warning_threshold * 0.8:
                    console.print(
                        f"[yellow]📊 TREND: {observable.name} is rising (avg: {avg:.1f}{observable.unit}, trend: {trend})[/yellow]"
                    )
                elif trend == "falling" and old_status in ["warning", "critical"]:
                    console.print(
                        f"[green]📉 TREND: {observable.name} is improving (avg: {avg:.1f}{observable.unit}, trend: {trend})[/green]"
                    )


class SystemLogger(Observer):
    """Observer that logs system events to a file."""

    def __init__(self, log_file: str = "system_monitor.log"):
        self.log_file = log_file

    def update(self, observable, event_type, *args, **kwargs):
        """Log system events."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if event_type == "status_changed":
            old_status, new_status, current_value = args
            log_entry = f"{timestamp} | {observable.name} | Status: {old_status} -> {new_status} | Value: {current_value:.2f}{observable.unit}\n"

            with open(self.log_file, "a") as f:
                f.write(log_entry)


def create_status_table(monitor: SystemMonitor) -> Table:
    """Create a rich table showing current system status."""
    table = Table(title="🖥️  System Monitor Dashboard")

    table.add_column("Metric", style="bold")
    table.add_column("Current", justify="right")
    table.add_column("Status", justify="center")
    table.add_column("Trend", justify="center")
    table.add_column("Average", justify="right")

    for metric in monitor.metrics:
        # Status color and emoji
        if metric.status == "critical":
            status_color = "red"
            status_emoji = "🔴"
        elif metric.status == "warning":
            status_color = "yellow"
            status_emoji = "🟡"
        else:
            status_color = "green"
            status_emoji = "🟢"

        # Trend emoji
        trend = metric.get_trend()
        trend_emoji = {"rising": "📈", "falling": "📉", "stable": "➡️"}.get(trend, "➡️")

        table.add_row(
            metric.name,
            f"{metric.current_value:.1f}{metric.unit}",
            f"[{status_color}]{status_emoji} {metric.status.upper()}[/{status_color}]",
            f"{trend_emoji} {trend}",
            f"{metric.get_average():.1f}{metric.unit}",
        )

    return table


async def demo_real_time_monitoring():
    """Demo real-time system monitoring with live updates."""
    # Create system monitor
    monitor = SystemMonitor()

    # Create observers
    alert_manager = AlertManager()
    performance_analyzer = PerformanceAnalyzer()
    logger = SystemLogger()

    # Subscribe observers to all metrics
    for metric in monitor.metrics:
        metric.subscribe(alert_manager)
        metric.subscribe(performance_analyzer)
        metric.subscribe(logger)

    # Start monitoring
    monitor_task = monitor.start_monitoring()

    try:
        # Run for 30 seconds with live updates
        with Live(create_status_table(monitor), refresh_per_second=2) as live:
            for i in range(120):
                live.update(create_status_table(monitor))
                await asyncio.sleep(0.25)

            # for i in range(60):  # 60 seconds
                # await asyncio.sleep(0.5)
                # live.update(create_status_table(monitor))

                # Show active alerts every 10 seconds
                # if i % 20 == 0 and alert_manager.active_alerts:
                #     console.print(
                #         f"\n[bold red]Active Alerts ({len(alert_manager.active_alerts)}):[/bold red]"
                #     )
                #     for alert in alert_manager.active_alerts.values():
                #         console.print(f"  {alert['message']}")
                #     console.print("")

    finally:
        monitor.stop_monitoring()
        await monitor_task

        # Show summary
        console.print("\n[bold green]Monitoring Summary:[/bold green]")
        console.print(
            f"Total alerts triggered: {len([a for a in alert_manager.alert_history if a['type'] == 'triggered'])}"
        )
        console.print(
            f"Alerts cleared: {len([a for a in alert_manager.alert_history if a['type'] == 'cleared'])}"
        )
        console.print(f"Log entries written to: {logger.log_file}")



async def main():
    """Run system monitor demonstrations."""
    console.print("[bold green]🖥️  MTB System Monitor Demo[/bold green]")
    # console.print("Demonstrating the observer pattern with real system monitoring.\n")
    await demo_real_time_monitoring()

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        console.print("\n\n[yellow]Monitoring stopped. Goodbye![/yellow]")

    except asyncio.exceptions.CancelledError:
        pass
