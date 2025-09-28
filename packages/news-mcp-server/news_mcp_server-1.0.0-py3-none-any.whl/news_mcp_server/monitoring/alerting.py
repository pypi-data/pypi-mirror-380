"""Alerting system for News MCP Server."""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Callable, Awaitable
from enum import Enum
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

import httpx


logger = logging.getLogger(__name__)


class AlertSeverity(str, Enum):
    """Alert severity levels."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AlertStatus(str, Enum):
    """Alert status."""
    ACTIVE = "active"
    RESOLVED = "resolved"
    ACKNOWLEDGED = "acknowledged"


@dataclass
class Alert:
    """Alert data structure."""
    id: str
    title: str
    description: str
    severity: AlertSeverity
    source: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    status: AlertStatus = AlertStatus.ACTIVE
    metadata: Dict[str, Any] = field(default_factory=dict)
    resolved_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None

    def acknowledge(self) -> None:
        """Mark alert as acknowledged."""
        self.status = AlertStatus.ACKNOWLEDGED
        self.acknowledged_at = datetime.utcnow()

    def resolve(self) -> None:
        """Mark alert as resolved."""
        self.status = AlertStatus.RESOLVED
        self.resolved_at = datetime.utcnow()


class AlertChannel(ABC):
    """Base class for alert channels."""

    def __init__(self, name: str):
        self.name = name
        self.enabled = True

    @abstractmethod
    async def send_alert(self, alert: Alert) -> bool:
        """Send an alert through this channel."""
        pass

    async def test_connection(self) -> bool:
        """Test the alert channel connection."""
        test_alert = Alert(
            id="test",
            title="Test Alert",
            description="This is a test alert",
            severity=AlertSeverity.INFO,
            source="test"
        )
        return await self.send_alert(test_alert)


class LogAlertChannel(AlertChannel):
    """Alert channel that logs alerts."""

    def __init__(self, name: str = "log", log_level: str = "ERROR"):
        super().__init__(name)
        self.log_level = log_level.upper()

    async def send_alert(self, alert: Alert) -> bool:
        """Log the alert."""
        try:
            log_message = (
                f"ALERT [{alert.severity.upper()}] {alert.title}: {alert.description} "
                f"(source: {alert.source}, id: {alert.id})"
            )

            if self.log_level == "INFO":
                logger.info(log_message)
            elif self.log_level == "WARNING":
                logger.warning(log_message)
            elif self.log_level == "ERROR":
                logger.error(log_message)
            elif self.log_level == "CRITICAL":
                logger.critical(log_message)

            return True

        except Exception as e:
            logger.error(f"Failed to log alert: {e}")
            return False


class EmailAlertChannel(AlertChannel):
    """Email alert channel."""

    def __init__(
        self,
        name: str = "email",
        smtp_server: str = "localhost",
        smtp_port: int = 587,
        username: Optional[str] = None,
        password: Optional[str] = None,
        from_email: str = "alerts@yourorg.com",
        to_emails: List[str] = None
    ):
        super().__init__(name)
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.from_email = from_email
        self.to_emails = to_emails or []

    async def send_alert(self, alert: Alert) -> bool:
        """Send alert via email."""
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            if not self.to_emails:
                logger.warning("No email recipients configured")
                return False

            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = ', '.join(self.to_emails)
            msg['Subject'] = f"[{alert.severity.upper()}] {alert.title}"

            # Email body
            body = f"""
Alert Details:
- Title: {alert.title}
- Description: {alert.description}
- Severity: {alert.severity}
- Source: {alert.source}
- Time: {alert.timestamp.isoformat()}
- ID: {alert.id}

Additional Information:
{self._format_metadata(alert.metadata)}
"""

            msg.attach(MIMEText(body, 'plain'))

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.username and self.password:
                    server.starttls()
                    server.login(self.username, self.password)

                server.send_message(msg)

            logger.info(f"Email alert sent: {alert.title}")
            return True

        except Exception as e:
            logger.error(f"Failed to send email alert: {e}")
            return False

    def _format_metadata(self, metadata: Dict[str, Any]) -> str:
        """Format metadata for email."""
        if not metadata:
            return "No additional metadata"

        lines = []
        for key, value in metadata.items():
            lines.append(f"- {key}: {value}")

        return "\n".join(lines)


class SlackAlertChannel(AlertChannel):
    """Slack alert channel."""

    def __init__(self, name: str = "slack", webhook_url: str = "", channel: str = "#alerts"):
        super().__init__(name)
        self.webhook_url = webhook_url
        self.channel = channel

    async def send_alert(self, alert: Alert) -> bool:
        """Send alert to Slack."""
        try:
            if not self.webhook_url:
                logger.warning("Slack webhook URL not configured")
                return False

            # Determine color based on severity
            color_map = {
                AlertSeverity.INFO: "#36a64f",      # green
                AlertSeverity.WARNING: "#ff9500",   # orange
                AlertSeverity.ERROR: "#ff0000",     # red
                AlertSeverity.CRITICAL: "#8B0000"   # dark red
            }

            color = color_map.get(alert.severity, "#808080")

            # Create Slack message
            payload = {
                "channel": self.channel,
                "username": "News MCP Server",
                "icon_emoji": ":warning:",
                "attachments": [
                    {
                        "color": color,
                        "title": f"[{alert.severity.upper()}] {alert.title}",
                        "text": alert.description,
                        "fields": [
                            {
                                "title": "Source",
                                "value": alert.source,
                                "short": True
                            },
                            {
                                "title": "Time",
                                "value": alert.timestamp.strftime("%Y-%m-%d %H:%M:%S UTC"),
                                "short": True
                            },
                            {
                                "title": "Alert ID",
                                "value": alert.id,
                                "short": True
                            }
                        ],
                        "footer": "News MCP Server",
                        "ts": int(alert.timestamp.timestamp())
                    }
                ]
            }

            # Add metadata if present
            if alert.metadata:
                metadata_text = "\n".join([f"• {k}: {v}" for k, v in alert.metadata.items()])
                payload["attachments"][0]["fields"].append({
                    "title": "Additional Info",
                    "value": metadata_text,
                    "short": False
                })

            # Send to Slack
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.webhook_url,
                    json=payload,
                    timeout=10.0
                )
                response.raise_for_status()

            logger.info(f"Slack alert sent: {alert.title}")
            return True

        except Exception as e:
            logger.error(f"Failed to send Slack alert: {e}")
            return False


class WebhookAlertChannel(AlertChannel):
    """Generic webhook alert channel."""

    def __init__(
        self,
        name: str = "webhook",
        url: str = "",
        headers: Optional[Dict[str, str]] = None,
        timeout: float = 10.0
    ):
        super().__init__(name)
        self.url = url
        self.headers = headers or {}
        self.timeout = timeout

    async def send_alert(self, alert: Alert) -> bool:
        """Send alert via webhook."""
        try:
            if not self.url:
                logger.warning("Webhook URL not configured")
                return False

            # Create payload
            payload = {
                "id": alert.id,
                "title": alert.title,
                "description": alert.description,
                "severity": alert.severity.value,
                "source": alert.source,
                "timestamp": alert.timestamp.isoformat(),
                "status": alert.status.value,
                "metadata": alert.metadata
            }

            # Send webhook
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.url,
                    json=payload,
                    headers=self.headers,
                    timeout=self.timeout
                )
                response.raise_for_status()

            logger.info(f"Webhook alert sent: {alert.title}")
            return True

        except Exception as e:
            logger.error(f"Failed to send webhook alert: {e}")
            return False


class AlertRule:
    """Alert rule for triggering alerts based on conditions."""

    def __init__(
        self,
        name: str,
        condition: Callable[[Dict[str, Any]], bool],
        alert_template: Dict[str, Any],
        cooldown_minutes: int = 15
    ):
        self.name = name
        self.condition = condition
        self.alert_template = alert_template
        self.cooldown_minutes = cooldown_minutes
        self.last_triggered: Optional[datetime] = None

    def should_trigger(self, data: Dict[str, Any]) -> bool:
        """Check if alert should be triggered."""
        # Check cooldown
        if self.last_triggered:
            cooldown_end = self.last_triggered + timedelta(minutes=self.cooldown_minutes)
            if datetime.utcnow() < cooldown_end:
                return False

        # Check condition
        return self.condition(data)

    def create_alert(self, data: Dict[str, Any]) -> Alert:
        """Create alert from template and data."""
        self.last_triggered = datetime.utcnow()

        # Format template with data
        alert_data = self.alert_template.copy()
        for key, value in alert_data.items():
            if isinstance(value, str):
                alert_data[key] = value.format(**data)

        return Alert(
            id=f"{self.name}_{int(datetime.utcnow().timestamp())}",
            source=self.name,
            metadata=data,
            **alert_data
        )


class AlertManager:
    """Main alert manager."""

    def __init__(self):
        self.channels: List[AlertChannel] = []
        self.rules: List[AlertRule] = []
        self.active_alerts: Dict[str, Alert] = {}
        self.alert_history: List[Alert] = []
        self.max_history = 1000

    def add_channel(self, channel: AlertChannel) -> None:
        """Add an alert channel."""
        self.channels.append(channel)
        logger.info(f"Added alert channel: {channel.name}")

    def remove_channel(self, name: str) -> bool:
        """Remove an alert channel."""
        for i, channel in enumerate(self.channels):
            if channel.name == name:
                del self.channels[i]
                logger.info(f"Removed alert channel: {name}")
                return True
        return False

    def add_rule(self, rule: AlertRule) -> None:
        """Add an alert rule."""
        self.rules.append(rule)
        logger.info(f"Added alert rule: {rule.name}")

    def remove_rule(self, name: str) -> bool:
        """Remove an alert rule."""
        for i, rule in enumerate(self.rules):
            if rule.name == name:
                del self.rules[i]
                logger.info(f"Removed alert rule: {name}")
                return True
        return False

    async def send_alert(self, alert: Alert) -> bool:
        """Send an alert through all channels."""
        if not self.channels:
            logger.warning("No alert channels configured")
            return False

        success_count = 0
        enabled_channels = [ch for ch in self.channels if ch.enabled]

        for channel in enabled_channels:
            try:
                if await channel.send_alert(alert):
                    success_count += 1
                else:
                    logger.warning(f"Failed to send alert through channel: {channel.name}")

            except Exception as e:
                logger.error(f"Error sending alert through channel {channel.name}: {e}")

        # Store alert
        self.active_alerts[alert.id] = alert
        self.alert_history.append(alert)

        # Limit history size
        if len(self.alert_history) > self.max_history:
            self.alert_history = self.alert_history[-self.max_history:]

        success = success_count > 0
        if success:
            logger.info(f"Alert sent successfully: {alert.title}")
        else:
            logger.error(f"Failed to send alert: {alert.title}")

        return success

    async def check_rules(self, data: Dict[str, Any]) -> List[Alert]:
        """Check all rules and trigger alerts if needed."""
        triggered_alerts = []

        for rule in self.rules:
            try:
                if rule.should_trigger(data):
                    alert = rule.create_alert(data)
                    await self.send_alert(alert)
                    triggered_alerts.append(alert)

            except Exception as e:
                logger.error(f"Error checking rule {rule.name}: {e}")

        return triggered_alerts

    def acknowledge_alert(self, alert_id: str) -> bool:
        """Acknowledge an alert."""
        if alert_id in self.active_alerts:
            self.active_alerts[alert_id].acknowledge()
            logger.info(f"Alert acknowledged: {alert_id}")
            return True
        return False

    def resolve_alert(self, alert_id: str) -> bool:
        """Resolve an alert."""
        if alert_id in self.active_alerts:
            alert = self.active_alerts[alert_id]
            alert.resolve()
            del self.active_alerts[alert_id]
            logger.info(f"Alert resolved: {alert_id}")
            return True
        return False

    def get_active_alerts(self) -> List[Alert]:
        """Get all active alerts."""
        return list(self.active_alerts.values())

    def get_alert_history(self, limit: int = 100) -> List[Alert]:
        """Get alert history."""
        return self.alert_history[-limit:]

    def get_alert_summary(self) -> Dict[str, Any]:
        """Get alert summary."""
        active_by_severity = {}
        for alert in self.active_alerts.values():
            severity = alert.severity.value
            active_by_severity[severity] = active_by_severity.get(severity, 0) + 1

        return {
            "active_alerts": len(self.active_alerts),
            "active_by_severity": active_by_severity,
            "total_channels": len(self.channels),
            "enabled_channels": len([ch for ch in self.channels if ch.enabled]),
            "total_rules": len(self.rules)
        }

    async def test_all_channels(self) -> Dict[str, bool]:
        """Test all alert channels."""
        results = {}

        for channel in self.channels:
            if channel.enabled:
                try:
                    results[channel.name] = await channel.test_connection()
                except Exception as e:
                    logger.error(f"Error testing channel {channel.name}: {e}")
                    results[channel.name] = False
            else:
                results[channel.name] = None  # Disabled

        return results